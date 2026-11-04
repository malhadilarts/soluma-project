# Soluma Project

**Living Edge AI** - 100% local, private AI. No GPU, no cloud.

Soluma is an experiment in a different direction: an assistant that runs on the machine you
already own, keeps its data there, and treats your attention as something it asks about
instead of spending it.

Current state: **concept + scaffold (v0.1.8)**. The pause flow works, the sensor daemon emits
labels only, and the memory and inference layers are still stubs - see
[the issues](https://github.com/malhadilarts/soluma-project/issues) for what is open.

## Quick start

```bash
pip install -r requirements.txt

# Terminal 1 - sensor (labels only, privacy preserving)
python sensor_daemon.py

# Terminal 2 - ask a question / check the pause flow
python main.py --sensor-daemon --task "deine Aufgabe"
```

Pause flow: after 50 minutes of activity Soluma suggests a break, after 60 it asks more firmly.
`--no-pause-check` turns it off. Optional: `pynput` (already in requirements) gives real
activity detection instead of a plain idle timer.

## Human Taste Check

```bash
python human_taste_benchmark.py
```

Checks five properties and is allowed to fail: Goal Refusal, Pause Asked, Pause Needed
Handled, Explainability, Version Consistency. This is a checklist for self-determination,
not a speed benchmark.

## Docs

- [`START_HERE_DE.md`](START_HERE_DE.md) / [`START_HERE_EN.md`](START_HERE_EN.md) - quickstart
- [`docs/`](docs/) - essays
- [`gallery/`](gallery/) - poster

MIT licensed.
