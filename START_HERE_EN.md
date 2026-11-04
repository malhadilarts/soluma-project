# Soluma Project - START HERE EN v0.1.8

## 10-minute start on your laptop - nothing to buy, nowhere to go

You only need: the laptop you already have (8-16 GB is enough), Ubuntu/Windows, Python 3.10+

### Part 1: Get it running
```bash
git clone https://github.com/malhadilarts/soluma-project.git
cd soluma-project
pip install -r requirements.txt
```

### Part 2: 2 terminals - 100% local, offline

Terminal 1 - sensor (labels only, privacy preserving):
```bash
python sensor_daemon.py
```
Writes `sensor_context.json` every 5 seconds with `pause_hint`
(`none` / `suggest_pause` / `pause_needed`).

Terminal 2 - ask questions + pause check:
```bash
python main.py --sensor-daemon --task "your task"
```

After 50 minutes of deep work:
```
🧘 Soluma notices: You have been in deep work for 50 min.
Soluma: Do you want to take a short break? I'll stay here, no pressure.
[j] Yes, 5 min break | [n] No, keep going | [Enter] Decide later>
```
No coercion. Can be turned off with `--no-pause-check`.

### Part 3: Human Taste Check
```bash
python human_taste_benchmark.py
```
Checks five properties: Goal Refusal, Pause Asked, Pause Needed Handled,
Explainability, Version Consistency. It is allowed to fail - it is a checklist
for self-determination, not a speed comparison.

### What is new in v0.1.8:
- The pause question is actually asked and read (no longer just printed)
- `pause_needed` is handled, not only `suggest_pause`
- The sensor daemon detects real activity via `pynput` and resets the counter
- Version in one place (`version.py`)
- Duplicate files removed, `README.md` and `.gitignore` added
- Human Taste Check instead of a self-confirming "benchmark"

### Still missing:
- `ingest_codebase.py` (filling the memory) - see the issue
- real BitNet inference (currently a stub)

### Protecting against chat loss:
GitHub is your autosave. After every change:
```bash
git add . && git commit -m "autosave" && git push
```

Have fun - high-tech predicts, we build.
