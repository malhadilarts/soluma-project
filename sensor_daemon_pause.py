"""
Soluma sensor_daemon.py v0.1.6 - pause aware, privacy preserving
Only emits labels, no raw data. 100% local.
"""
import time, json, pathlib, psutil
from datetime import datetime

try:
    from pynput import mouse, keyboard
    HAS_PYNPUT=True
except:
    HAS_PYNPUT=False

STATE_FILE = pathlib.Path("sensor_context.json")
deep_work_minutes = 0
last_activity = datetime.now()
pause_hint = "none"

def write_context():
    data = {
        "timestamp": datetime.now().isoformat(),
        "state": "deep_work" if deep_work_minutes>2 else "active",
        "deep_work_minutes": deep_work_minutes,
        "pause_hint": pause_hint,
        "network": "unknown",
        "motion": "still",
        "focus_score": max(0.0, 1.0 - deep_work_minutes/120),
        "frustration": "low"
    }
    STATE_FILE.write_text(json.dumps(data, indent=2))

if __name__ == "__main__":
    print("Soluma sensor daemon - pause aware - labels only")
    print("Writing sensor_context.json every 5s, Ctrl+C to stop")
    while True:
        # simple simulation: increase deep_work
        deep_work_minutes += 5/60  # per 5 sec loop
        if deep_work_minutes < 50:
            pause_hint = "none"
        elif deep_work_minutes < 60:
            pause_hint = "suggest_pause"
            print(f"\n🧘 {int(deep_work_minutes)} Min deep_work - Zeit für kurze Pause? -> suggest_pause")
        else:
            pause_hint = "pause_needed"
            print(f"\n🌿 Pause empfohlen - {int(deep_work_minutes)} Min")

        write_context()
        time.sleep(5)
