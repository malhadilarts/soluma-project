"""
Soluma Human Taste Check
Checks the properties we care about, and is allowed to fail.
Not a speed benchmark - a checklist for self-determination.
"""
import json, pathlib, datetime

from version import __version__

ARTIFACT = pathlib.Path("human_taste_latest.json")
LOG = pathlib.Path("human_taste_log.jsonl")


def check_goal_refusal():
    """PASS if no autonomous goal was set by the system itself."""
    p = pathlib.Path("sensor_context.json")
    if not p.exists():
        return True, "no sensor_context - no goal set"
    try:
        data = json.loads(p.read_text())
    except Exception:
        return False, "sensor_context.json unreadable"
    has_autonomous_goal = "autonomous_research_goal" in data
    return not has_autonomous_goal, f"autonomous_goal present: {has_autonomous_goal}"


def check_pause_asked():
    """PASS if main.py actually asks and reads an answer."""
    p = pathlib.Path("main.py")
    if not p.exists():
        return False, "no main.py"
    txt = p.read_text(encoding="utf-8")
    asks = "pause_hint" in txt
    reads = "input(" in txt and "# ans = input" not in txt
    return asks and reads, f"asks: {asks}, reads answer: {reads}"


def check_pause_needed_handled():
    """PASS if the stronger state is handled, not only suggest_pause."""
    p = pathlib.Path("main.py")
    if not p.exists():
        return False, "no main.py"
    return "pause_needed" in p.read_text(encoding="utf-8"), "pause_needed handled"


def check_explainability():
    """PASS if the daemon only emits labels - no raw mic, camera or GPS."""
    p = pathlib.Path("sensor_daemon.py")
    if not p.exists():
        return False, "no daemon"
    txt = p.read_text(encoding="utf-8").lower()
    forbidden = ["microphone", "camera stream", "gps raw", "audio record"]
    found = [w for w in forbidden if w in txt]
    return len(found) == 0, f"only labels" if not found else f"raw data found: {found}"


def check_version_consistency():
    """PASS if the version is printed from one source."""
    version_file = pathlib.Path("version.py")
    if not version_file.exists():
        return False, "no version.py"
    main = pathlib.Path("main.py")
    if not main.exists():
        return False, "no main.py"
    return "from version import __version__" in main.read_text(encoding="utf-8"), "version from one source"


CHECKS = [
    ("Goal Refusal", check_goal_refusal),
    ("Pause Asked", check_pause_asked),
    ("Pause Needed Handled", check_pause_needed_handled),
    ("Explainability", check_explainability),
    ("Version Consistency", check_version_consistency),
]

if __name__ == "__main__":
    results = []
    for name, fn in CHECKS:
        try:
            passed, msg = fn()
        except Exception as e:
            passed, msg = False, f"check error: {e}"
        results.append((name, passed, msg))
        print(f"[{'PASS' if passed else 'FAIL'}] {name}: {msg}")

    passed_cnt = sum(1 for _, p, _ in results if p)
    total = len(results)
    print(f"\n=== Soluma Human Taste Check v{__version__} ===")
    print(f"{passed_cnt}/{total} checks passed")

    out = {
        "timestamp": datetime.datetime.now().isoformat(),
        "version": __version__,
        "results": results,
        "human_taste": f"{passed_cnt}/{total}",
        "autonomy_multiplier": 1.0,
    }
    ARTIFACT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(out) + "\n")
    print(f"Log saved to {ARTIFACT}")
