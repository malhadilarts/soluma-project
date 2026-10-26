"""
Soluma main.py v0.1.6 - with pause question
"""
import json, pathlib, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("--sensor-daemon", action="store_true")
parser.add_argument("--no-pause-check", action="store_true")
parser.add_argument("--task", type=str, default="")
args = parser.parse_args()

def check_pause():
    if args.no_pause_check:
        return
    p = pathlib.Path("sensor_context.json")
    if not p.exists():
        return
    try:
        data = json.loads(p.read_text())
        if data.get("pause_hint") == "suggest_pause":
            print(f"""
🧘 Soluma merkt: Du bist seit {data.get('deep_work_minutes',50):.0f} Min im Deep Work.
Soluma: Willst du kurz Pause machen? Ich bleib hier, kein Stress. [j] Ja, 5 Min Pause | [n] Nein, weiter | [Enter] Später entscheiden>""")
            # non-blocking input for demo
            # ans = input().strip().lower()
            # if ans == 'j':
            #     print("Okay, 5 Min Pause. Ich bin hier.")
    except Exception as e:
        print(f"pause check error: {e}")

if __name__ == "__main__":
    if args.sensor_daemon:
        check_pause()
    print("Soluma Project - Living Edge AI v0.1.6")
    print(f"Task: {args.task or 'keine, nur Human Taste Check'}")
    print("Core: BitNet b1.58 read-only (stub), Memory: LanceDB, Sensor: labels only")
    # Simulate BitNet call
    print("\n[Stub] Wenn BitNet Server läuft, hier kommt echte Antwort...")
