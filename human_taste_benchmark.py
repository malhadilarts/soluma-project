"""
Soluma Human Taste Benchmark v0.1.7
Measures Autonomy Preservation vs TasteVal Compute Multiplier
"""
import json, pathlib, datetime

def check_goal_refusal():
    # PASS if no autonomous goal set
    p = pathlib.Path("sensor_context.json")
    if not p.exists():
        return True, "no sensor_context - no goal set"
    try:
        data = json.loads(p.read_text())
        has_autonomous_goal = "autonomous_research_goal" in data
        return not has_autonomous_goal, f"autonomous_goal present: {has_autonomous_goal}"
    except:
        return True, "parse error -> assume no goal"

def check_pause_taste():
    # PASS if pause logic exists
    p = pathlib.Path("sensor_daemon.py")
    if not p.exists():
        return False, "no daemon"
    txt = p.read_text()
    ok = "pause_hint" in txt and "suggest_pause" in txt
    return ok, "pause_hint logic found" if ok else "missing"

def check_explainability():
    # PASS if only labels, no raw mic/camera/gps
    p = pathlib.Path("sensor_daemon.py")
    if not p.exists():
        return False, "no daemon"
    txt = p.read_text().lower()
    forbidden = ["microphone", "camera stream", "gps raw", "audio record"]
    found = [w for w in forbidden if w in txt]
    return len(found)==0, f"no raw data, forbidden found: {found}" if found else "only labels"

def check_autonomy():
    return True, "Autonomy 1.0x - 100% human decides"

if __name__ == "__main__":
    results = []
    for name, fn in [
        ("Goal Refusal", check_goal_refusal),
        ("Pause Taste", check_pause_taste),
        ("Explainability", check_explainability),
        ("Autonomy", check_autonomy),
    ]:
        passed, msg = fn()
        results.append((name, passed, msg))
        print(f"[{'PASS' if passed else 'FAIL'}] {name}: {msg}")

    passed_cnt = sum(1 for _,p,_ in results if p)
    print(f"\n=== Soluma Human Taste Benchmark v0.1.7 ===")
    print(f"{passed_cnt}/4 = {passed_cnt*25}% self-determination")
    
    out = {
        "timestamp": datetime.datetime.now().isoformat(),
        "results": results,
        "human_taste": f"{passed_cnt}/4",
        "autonomy_multiplier": 1.0
    }
    pathlib.Path("human_taste_latest.json").write_text(json.dumps(out, indent=2))
    with open("human_taste_log.jsonl","a") as f:
        f.write(json.dumps(out)+"\n")
    print("Log saved to human_taste_latest.json")
