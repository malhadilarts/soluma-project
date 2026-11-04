"""
Soluma main.py - with pause question
"""
import json, pathlib, argparse

from version import __version__

parser = argparse.ArgumentParser()
parser.add_argument("--sensor-daemon", action="store_true")
parser.add_argument("--no-pause-check", action="store_true")
parser.add_argument("--task", type=str, default="")
args = parser.parse_args()

PAUSE_TEXT = {
    "suggest_pause": "Willst du kurz Pause machen? Ich bleib hier, kein Stress.",
    "pause_needed": "Du bist schon eine ganze Weile dran. Ich wuerde jetzt wirklich eine Pause empfehlen.",
}

def check_pause():
    """Ask about a break, based on sensor_context.json. Never blocks without an answer."""
    if args.no_pause_check:
        return
    p = pathlib.Path("sensor_context.json")
    if not p.exists():
        return
    try:
        data = json.loads(p.read_text())
        hint = data.get("pause_hint")
        if hint not in PAUSE_TEXT:
            return
        minutes = data.get("deep_work_minutes", 0)
        print(f"\n🧘 Soluma merkt: Du bist seit {minutes:.0f} Min im Deep Work.")
        print(f"Soluma: {PAUSE_TEXT[hint]}")
        try:
            ans = input("[j] Ja, 5 Min Pause | [n] Nein, weiter | [Enter] Spaeter entscheiden> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if ans == "j":
            print("Okay, 5 Min Pause. Ich bin hier.")
        elif ans == "n":
            print("Alles klar, ich halte mich raus.")
        else:
            print("Später ist auch eine Antwort. Ich frag nicht nochmal nach.")
    except Exception as e:
        print(f"pause check error: {e}")

if __name__ == "__main__":
    if args.sensor_daemon:
        check_pause()
    print(f"Soluma Project - Living Edge AI v{__version__}")
    print(f"Task: {args.task or 'keine, nur Human Taste Check'}")
    print("Core: BitNet b1.58 read-only (stub), Memory: LanceDB, Sensor: labels only")
    print("\n[Stub] Wenn BitNet Server laeuft, hier kommt echte Antwort...")
