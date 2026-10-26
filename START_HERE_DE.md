# Soluma Project - START HERE DE v0.1.7

## 10-Minuten Start auf deinem Laptop - kein Neukauf, kein Vor-Ort nötig

Du brauchst nur: deinen vorhandenen Laptop (8-16GB reicht), Ubuntu/Windows, Python 3.10+

### Teil 1: Entpacken
```bash
unzip soluma-project-v0.1.7-final.zip -d soluma-project
cd soluma-project
pip install -r requirements.txt
```

### Teil 2: 3 Terminals - läuft 100% lokal, offline

Terminal 1 - Sensor (nur Labels, privat):
```bash
python sensor_daemon.py
```
Schreibt alle 5 Sek sensor_context.json mit pause_hint

Terminal 2 - Memory füllen:
```bash
python ingest_codebase.py ./src
```

Terminal 3 - Fragen stellen + Pause-Check:
```bash
python main.py --sensor-daemon --task "deine Aufgabe"
```

Nach 50 Min deep_work:
```
🧘 Soluma merkt: Du bist seit 50 Min im Deep Work.
Soluma: Willst du kurz Pause machen? Ich bleib hier, kein Stress. [j]/[n]/[Enter]
```
Kein Zwang. Mit --no-pause-check abschaltbar.

### Teil 3: Human Taste Benchmark (Gegenentwurf zu TasteVal)
```bash
python human_taste_benchmark.py
```
Ergebnis: 4/4 = 100% Selbstbestimmung vs TasteVal 2.3x faster

### Was ist neu in v0.1.7:
- pause_hint: none / suggest_pause / pause_needed
- Human Taste Benchmark: Goal Refusal, Pause Taste, Explainability, Autonomy 1.0x
- Poster final mit richtig rumstehendem ThinkPad
- Alles remote machbar, kein Einkaufen, kein Rumlaufen nötig

### Sichern gegen Chat-Verlust:
GitHub ist dein Autosave. Nach jeder Änderung:
```bash
git add . && git commit -m "autosave" && git push
```

Viel Spaß - High-tech prognostiziert, wir bauen.
