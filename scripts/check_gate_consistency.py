#!/usr/bin/env python3
"""Deckt sich die Gate-Liste in CLAUDE.md mit dem, was die Workflows wirklich fahren?

WARUM ES DIESEN GATE GIBT
-------------------------
`## This repository's gates` zitiert die Kommandos beider Workflows und nennt
ihre Zahl. Bis hierher hielt das niemand zusammen. Am 2026-08-21 fiel auf, dass
der zitierte `readme-sync.yml`-Block fuenf Kommandos nannte, waehrend der Job
sieben faehrt: `generate_promotion.py --check` und `generate_showcase_card.py
--check` fehlten. Die Zahl im Fliesstext stand auf acht, richtig waren neun.

Die Abweichung ist unauffaellig, und das ist das Problem: Wer die Liste als
Vorlage nimmt — ein Mensch vor dem Push, ein Agent vor dem Bericht — faehrt
sieben von neun Gates und haelt das fuer vollstaendig. Die CI sagt nichts dazu,
denn die CI liest CLAUDE.md nicht.

BEIDE RICHTUNGEN, UND DIE ZWEITE IST DIE WICHTIGE
--------------------------------------------------
Ein Kommando im Block, das die CI nicht faehrt, ist aergerlich: Man prueft
etwas, das niemanden interessiert. Ein Kommando in der CI, das der Block nicht
nennt, ist gefaehrlich: Man prueft weniger als die CI und erfaehrt es erst im
Pull Request. Genau diese zweite Richtung war der Fall von damals, deshalb
werden beide getrennt gemeldet.

NICHTS GEFUNDEN IST NICHT DASSELBE WIE NICHTS ZU BEANSTANDEN
------------------------------------------------------------
Der Fehlermodus dieses Skripts ist nicht der falsche Alarm, sondern das
Schweigen. Findet die Extraktion ihre Stellen nicht mehr — Abschnitt
umbenannt, Fence entfernt, `run:` auf einen Block-Skalar umgestellt —, dann
vergleicht es zwei fast leere Mengen und meldet zufrieden "einig". Dagegen
stehen zwei Vorkehrungen:

  * Mindestzahlen (`MIN_*`). Kein Sollwert, sondern ein Test der Extraktion
    selbst. Unterschreiten ist ein Befund wie jeder andere.
  * Ein eingebauter Selbsttest bei jedem Lauf (`--kein-selbsttest` schaltet ihn
    ab). Er verbiegt die eingelesenen Texte in drei Richtungen und verlangt,
    dass jede Verbiegung gemeldet wird. Ein Vergleich, der nichts findet,
    beweist nur dann etwas, wenn er beweisbar etwas finden koennte.

HERKUNFT
--------
Portiert aus `swiss-academic-libraries-mcp/scripts/check_gate_consistency.py`,
und zwar als Portierung, nicht als Kopie: Das Original prueft zusaetzlich den
ruff-Pin ueber `pyproject.toml` und `.pre-commit-config.yaml`, den Gate-Scope
und die Quellen-Tabelle der Live-Tests. Nichts davon existiert hier — dieses
Repo ist kein Python-Paket und hat keine Live-Tests. Die beiden Dateien sind
deshalb **nicht** byteweise gleichzuhalten; wer dort etwas aendert, muss hier
nichts nachziehen und umgekehrt.

Uebernommen ist die Idee, nicht der Text: Mindestzahlen als Selbsttest, und
beide Richtungen getrennt melden. Der Vergleich ist hier strenger als dort —
exakte Mengengleichheit statt Teilfolgen-Abgleich —, weil dieser Block die
Kommandos woertlich zitiert und nicht zusammenfasst.

Nur Standardbibliothek. Eine YAML-Abhaengigkeit waere eine weitere Version, die
gepflegt werden muss, und damit ein Beitrag zu dem Problem, gegen das dieses
Skript steht.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CLAUDE_MD = "CLAUDE.md"
WORKFLOWS = (".github/workflows/lint.yml", ".github/workflows/readme-sync.yml")
SCRIPTS = "scripts"
ABSCHNITT = "## This repository's gates"

# Untergrenzen fuer die Extraktion, keine Sollwerte. Bewusst unter dem heutigen
# Stand (je zehn): Ein Gate darf entfernt werden, ohne dass jemand dieses Skript
# anfasst — ein Einbruch der Extraktion faellt trotzdem auf.
MIN_CI_KOMMANDOS = 8
MIN_DOC_GATES = 8

# Was in einem `run:` steht, aber kein Gate ist. Der Install-Schritt gehoert
# nicht in die zitierte Liste: Er richtet die Umgebung ein, er prueft nichts.
SETUP_RE = re.compile(r"^(pip|python -m pip|apt-get|npm|uv) ")

RUN_RE = re.compile(r"^\s+run: (?P<wert>.+)$", re.M)
FENCE_RE = re.compile(r"```bash\n(.*?)```", re.S)

ZAHLWORT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
}


def _wort_zu_zahl(wort: str) -> int | None:
    """Zahlwort oder Ziffer zu einer Zahl.

    Der Fliesstext schreibt Zahlen aus («Ten checks run …»), die Klammer hinter
    dem Scope nennt eine Ziffer («(11 files)»). Beide Formen sind hier
    zugelassen — welche wo steht, entscheidet die Doku, nicht dieses Skript.
    """
    text = wort.strip().lower()
    if text.isdigit():
        return int(text)
    return ZAHLWORT.get(text)


def gate_abschnitt(md: str) -> str:
    """Der Abschnitt ueber die Gates, ohne die folgenden."""
    if ABSCHNITT not in md:
        return ""
    return md.split(ABSCHNITT, 1)[1].split("\n## ", 1)[0]


def doc_gates(md: str) -> list[str]:
    """Jede Kommandozeile aus den Shell-Fences des Gate-Abschnitts."""
    return [
        zeile.strip()
        for block in FENCE_RE.findall(gate_abschnitt(md))
        for zeile in block.strip().splitlines()
        if zeile.strip()
    ]


def ci_kommandos(workflows: dict[str, str]) -> list[str]:
    """Jedes `run:`-Kommando beider Workflows, ohne die Setup-Schritte."""
    kommandos: list[str] = []
    for text in workflows.values():
        for treffer in RUN_RE.finditer(text):
            wert = treffer.group("wert").strip()
            if wert in {"|", ">", "|-", ">-"}:
                # Block-Skalare kommen hier nicht vor. Taeten sie es, wuerde
                # diese Zeile still verschluckt — deshalb ein Befund statt
                # eines Ueberspringens.
                kommandos.append("<Block-Skalar, von diesem Skript nicht gelesen>")
                continue
            if SETUP_RE.match(wert):
                continue
            kommandos.append(wert)
    return kommandos


def _zahl_im_text(abschnitt: str, muster: str) -> tuple[str, int | None]:
    treffer = re.search(muster, abschnitt)
    if not treffer:
        return "", None
    wort = treffer.group(1)
    return wort, _wort_zu_zahl(wort)


def probleme(md: str, workflows: dict[str, str], py_dateien: int) -> list[str]:
    """Alle Abweichungen zwischen Doku, Workflows und Verzeichnis."""
    gefunden: list[str] = []
    doc = doc_gates(md)
    ci = ci_kommandos(workflows)
    abschnitt = gate_abschnitt(md)

    if not abschnitt:
        return [
            f"{CLAUDE_MD}: Der Abschnitt «{ABSCHNITT}» ist nicht auffindbar. Ohne ihn "
            f"vergleicht dieses Skript nichts und waere ab hier still."
        ]

    if len(ci) < MIN_CI_KOMMANDOS:
        gefunden.append(
            f"Workflows: nur {len(ci)} von mindestens {MIN_CI_KOMMANDOS} erwarteten "
            f"Kommandos gelesen. Entweder sind Gates entfallen, oder die Extraktion "
            f"laeuft an einer neuen Schreibweise vorbei — und vergleicht ab dann zu wenig."
        )
    if len(doc) < MIN_DOC_GATES:
        gefunden.append(
            f"{CLAUDE_MD}: nur {len(doc)} von mindestens {MIN_DOC_GATES} erwarteten "
            f"Gate-Zeilen im zitierten Block gefunden. Ein Block, der leerlaeuft, "
            f"behauptet nichts mehr — und faellt genau deshalb sonst nicht auf."
        )

    for kommando in doc:
        if kommando not in ci:
            gefunden.append(
                f"{CLAUDE_MD}: `{kommando}` steht im Block, aber kein `run:` in den "
                f"Workflows lautet so. Wer den Block faehrt, prueft etwas, das die CI "
                f"nicht prueft."
            )
    for kommando in ci:
        if kommando not in doc:
            gefunden.append(
                f"Workflows: `{kommando}` laeuft im Pull Request, der Block in "
                f"{CLAUDE_MD} nennt es nicht. Wer nur die Doku faehrt, prueft weniger "
                f"als die CI und erfaehrt es erst im Pull Request."
            )

    wort, zahl = _zahl_im_text(abschnitt, r"(\w+) checks run on a pull request")
    if zahl is None:
        gefunden.append(
            f"{CLAUDE_MD}: Der Satz «… checks run on a pull request» fehlt oder nennt "
            f"keine lesbare Zahl ({wort!r}). Damit ist die Gesamtzahl unbewacht."
        )
    elif zahl != len(ci):
        gefunden.append(
            f"{CLAUDE_MD}: «{wort} checks run on a pull request», tatsaechlich sind es {len(ci)}."
        )

    generate = [k for k in ci if "generate_" in k]
    wort, zahl = _zahl_im_text(abschnitt, r"The (\w+) `generate_\*\.py --check` gates")
    if zahl is None:
        gefunden.append(
            f"{CLAUDE_MD}: Der Satz «The … `generate_*.py --check` gates» fehlt oder "
            f"nennt keine lesbare Zahl ({wort!r})."
        )
    elif zahl != len(generate):
        gefunden.append(
            f"{CLAUDE_MD}: «The {wort} `generate_*.py --check` gates», tatsaechlich "
            f"sind es {len(generate)}."
        )

    wort, zahl = _zahl_im_text(abschnitt, r"scope is `scripts/` alone \((\w+) files\)")
    if zahl is None:
        gefunden.append(
            f"{CLAUDE_MD}: Die Klammer «(… files)» zum Scope `scripts/` fehlt oder "
            f"nennt keine lesbare Zahl ({wort!r})."
        )
    elif zahl != py_dateien:
        gefunden.append(
            f"{CLAUDE_MD}: Scope `scripts/` mit «({wort} files)», tatsaechlich liegen "
            f"dort {py_dateien} Python-Dateien. ruff meldet dieselbe Zahl."
        )

    return gefunden


def selbsttest(md: str, workflows: dict[str, str], py_dateien: int) -> list[str]:
    """Meldet der Vergleich noch etwas, wenn man ihm etwas zu melden gibt?

    Drei Verbiegungen, je eine pro Zusicherung. Bleibt eine davon unbemerkt,
    ist dieser Gate ab da eine Attrappe — und das ist ein Befund, kein Hinweis.
    """
    fehler: list[str] = []

    doc = doc_gates(md)
    if doc:
        ohne = md.replace(f"{doc[-1]}\n", "", 1)
        if not probleme(ohne, workflows, py_dateien):
            fehler.append(
                f"Selbsttest: Eine aus dem Block entfernte Zeile ({doc[-1]!r}) blieb "
                f"unbemerkt. Die Richtung «CI faehrt es, Doku nennt es nicht» ist blind."
            )

    verbogen = dict(workflows)
    ziel = WORKFLOWS[-1]
    letzte = [m.group(0) for m in RUN_RE.finditer(verbogen[ziel])]
    if letzte:
        verbogen[ziel] = verbogen[ziel].replace(f"{letzte[-1]}\n", "", 1)
        if not probleme(md, verbogen, py_dateien):
            fehler.append(
                "Selbsttest: Ein aus dem Workflow entfernter Schritt blieb unbemerkt. "
                "Die Richtung «Doku nennt es, CI faehrt es nicht» ist blind."
            )

    if not probleme(md, workflows, py_dateien + 1):
        fehler.append("Selbsttest: Eine falsche Dateizahl fuer `scripts/` blieb unbemerkt.")

    return fehler


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--kein-selbsttest",
        action="store_true",
        help="Den eingebauten Selbsttest ueberspringen (nur zum Debuggen).",
    )
    args = parser.parse_args()

    wurzel = Path(__file__).resolve().parent.parent
    md = (wurzel / CLAUDE_MD).read_text(encoding="utf-8")
    workflows = {name: (wurzel / name).read_text(encoding="utf-8") for name in WORKFLOWS}
    py_dateien = len(list((wurzel / SCRIPTS).glob("*.py")))

    gefunden = probleme(md, workflows, py_dateien)
    if not args.kein_selbsttest:
        gefunden += selbsttest(md, workflows, py_dateien)

    if gefunden:
        print("Die Gate-Liste und die Workflows sind auseinandergelaufen:\n", file=sys.stderr)
        for problem in gefunden:
            print(f"  - {problem}\n", file=sys.stderr)
        return 1

    ci = ci_kommandos(workflows)
    print(
        f"Gate-Liste einig mit den Workflows ({len(ci)} Kommandos, "
        f"{py_dateien} Python-Dateien in {SCRIPTS}/); Selbsttest bestanden"
        if not args.kein_selbsttest
        else f"Gate-Liste einig mit den Workflows ({len(ci)} Kommandos); Selbsttest uebersprungen"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
