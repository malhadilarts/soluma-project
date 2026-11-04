# Soluma Project - START HERE DE v0.1.8

## 10-Minuten Start auf deinem Laptop - kein Neukauf, kein Vor-Ort nötig

Du brauchst nur: deinen vorhandenen Laptop (8-16 GB reicht), Ubuntu/Windows, Python 3.10+

### Teil 1: Startklar machen
```bash
git clone https://github.com/malhadilarts/soluma-project.git
cd soluma-project
pip install -r requirements.txt
```

### Teil 2: 2 Terminals - läuft 100% lokal, offline

Terminal 1 - Sensor (nur Labels, privat):
```bash
python sensor_daemon.py
```
Schreibt alle 5 Sek `sensor_context.json` mit `pause_hint`
(`none` / `suggest_pause` / `pause_needed`).

Terminal 2 - Fragen stellen + Pause-Check:
```bash
python main.py --sensor-daemon --task "deine Aufgabe"
```

Nach 50 Min deep_work:
```
🧘 Soluma merkt: Du bist seit 50 Min im Deep Work.
Soluma: Willst du kurz Pause machen? Ich bleib hier, kein Stress.
[j] Ja, 5 Min Pause | [n] Nein, weiter | [Enter] Später entscheiden>
```
Kein Zwang. Mit `--no-pause-check` abschaltbar.

### Teil 3: Human Taste Check
```bash
python human_taste_benchmark.py
```
Prüft fünf Eigenschaften: Goal Refusal, Pause Asked, Pause Needed Handled,
Explainability, Version Consistency. Darf auch durchfallen - es ist eine Checkliste
für Selbstbestimmung, kein Geschwindigkeitsvergleich.

### Was ist neu in v0.1.8:
- Pause-Frage wird wirklich gestellt und gelesen (nicht mehr nur gedruckt)
- `pause_needed` wird behandelt, nicht nur `suggest_pause`
- Sensor-Daemon erkennt echte Aktivität über `pynput` und setzt den Zähler zurück
- Version an einer Stelle (`version.py`)
- Doppelte Dateien entfernt, `README.md` und `.gitignore` ergänzt
- Human Taste Check statt selbstbestätigendem "Benchmark"

### Was noch fehlt:
- `ingest_codebase.py` (Memory befüllen) - siehe Issue
- echte BitNet-Inferenz (aktuell Stub)

### Sichern gegen Chat-Verlust:
GitHub ist dein Autosave. Nach jeder Änderung:
```bash
git add . && git commit -m "autosave" && git push
```

Viel Spaß - High-tech prognostiziert, wir bauen.
