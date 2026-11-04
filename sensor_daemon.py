"""
Soluma sensor_daemon.py - pause aware, privacy preserving
Only emits labels, no raw data. 100% local.
"""
import time, json, pathlib
from datetime import datetime

try:
    from pynput import mouse, keyboard  # noqa: F401  (optional, see below)
    HAS_PYNPUT = True
except ImportError:
    HAS_PYNPUT = False

STATE_FILE = pathlib.Path("sensor_context.json")
IDLE_RESET_MINUTES = 3      # no activity for this long -> counter goes back to 0
TICK_SECONDS = 5

deep_work_minutes = 0.0
last_activity = time.monotonic()
pause_hint = "none"


def register_activity():
    """Called on any real input event: resets the deep-work counter."""
    global deep_work_minutes, last_activity, pause_hint
    now = time.monotonic()
    if now - last_activity > IDLE_RESET_MINUTES * 60:
        deep_work_minutes = 0.0
        pause_hint = "none"
    last_activity = now


def update_pause_hint():
    global pause_hint
    if deep_work_minutes < 50:
        pause_hint = "none"
    elif deep_work_minutes < 60:
        pause_hint = "suggest_pause"
    else:
        pause_hint = "pause_needed"


def write_context():
    data = {
        "timestamp": datetime.now().isoformat(),
        "state": "deep_work" if deep_work_minutes > 2 else "active",
        "deep_work_minutes": round(deep_work_minutes, 1),
        "pause_hint": pause_hint,
        "network": "unknown",
        "motion": "still",
        "focus_score": round(max(0.0, 1.0 - deep_work_minutes / 120), 3),
        "frustration": "low",
        "activity_source": "pynput" if HAS_PYNPUT else "none",
    }
    STATE_FILE.write_text(json.dumps(data, indent=2))


def start_listeners():
    """Only if pynput is installed. Labels only - no keys, no positions, nothing stored."""
    if not HAS_PYNPUT:
        return []
    from pynput import mouse as m, keyboard as k

    def on_event(*_args, **_kwargs):
        register_activity()

    listeners = [m.Listener(on_move=on_event, on_click=on_event, on_scroll=on_event),
                 k.Listener(on_press=on_event)]
    for listener in listeners:
        listener.daemon = True
        listener.start()
    return listeners


if __name__ == "__main__":
    print("Soluma sensor daemon - pause aware - labels only")
    print(f"Activity source: {'pynput' if HAS_PYNPUT else 'none (idle timer only)'}")
    print(f"Writing sensor_context.json every {TICK_SECONDS}s, Ctrl+C to stop")

    listeners = start_listeners()
    try:
        while True:
            # Without pynput we can only count wall-clock time in the session.
            if not HAS_PYNPUT:
                deep_work_minutes += TICK_SECONDS / 60
            else:
                register_activity_if_active = time.monotonic() - last_activity
                if register_activity_if_active < IDLE_RESET_MINUTES * 60:
                    deep_work_minutes += TICK_SECONDS / 60
                elif deep_work_minutes > 0:
                    deep_work_minutes = 0.0

            update_pause_hint()

            if pause_hint == "suggest_pause":
                print(f"\n🧘 {int(deep_work_minutes)} Min deep_work - Zeit fuer kurze Pause? -> suggest_pause")
            elif pause_hint == "pause_needed":
                print(f"\n🌿 Pause empfohlen - {int(deep_work_minutes)} Min -> pause_needed")

            write_context()
            time.sleep(TICK_SECONDS)
    except KeyboardInterrupt:
        for listener in listeners:
            listener.stop()
        print("\nSensor daemon stopped.")
