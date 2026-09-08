"""
DOUGLAS STUDIO - GitHub Edition
Made by Douglas | Nakuru, Kenya | No Ads, No Premium
One code, many tasks: Music + Robot Line Follower + Box Stacker + Traffic Light
Runs in GitHub Actions without typing
"""

import time
from datetime import datetime

def play_music():
    print("\n🎵 === MUSIC PLAYER ===")
    song = [("C",0.3), ("D",0.3), ("E",0.3), ("G",0.6)]
    for note, d in song:
        print(f"  Playing {note} - beep")
        time.sleep(d)
    print("  Music done - Made by Douglas")

def traffic_light():
    print("\n🚦 === TRAFFIC LIGHT (Njoro Interchange) ===")
    for color in ["RED - STOP 3s", "GREEN - GO 3s", "YELLOW - WAIT 1s"]:
        print(f"  {color}")
        time.sleep(0.5)

def robot_line_follower():
    print("\n🤖 === ROBOT LINE FOLLOWER - State Machine ===")
    states = [
        ("FOLLOW BLACK", "Sensor: BLACK -> moving..."),
        ("WHITE DETECTED", "⚪ White found! Search YELLOW"),
        ("SEARCH YELLOW", "🔍 Turning... YELLOW found!"),
        ("GO BACK BLACK", "↩️ Back on BLACK line"),
        ("WAIT 20s", "⏰ Staying 20s on BLACK (3s demo)"),
        ("SEARCH RED", "🔍 Searching RED... RED found!"),
        ("MISSION COMPLETE", "🔴 RED found! Made by Douglas")
    ]
    for name, msg in states:
        print(f"  [{name}] {msg}")
        time.sleep(0.5)
    print("  Robot stopped - Pillar safe!")

def box_stacker():
    print("\n📦 === BOX STACKER - No Breaking Pillar ===")
    tower = []
    boxes = [10, 8, 5, 7, 3] # kg
    
    def can_place(new_w):
        if not tower: return True
        return new_w <= tower[-1]
    
    for w in boxes:
        print(f"  Trying {w}kg on tower {tower}")
        if can_place(w):
            tower.append(w)
            print(f"  ✅ Placed! Tower: {tower}")
        else:
            print(f"  ❌ Refused {w}kg > top {tower[-1]}kg - Would fall!")
        time.sleep(0.3)
    print(f"  Final pillar (bottom->top): {tower} - Standing!")

def main():
    print(f"=== DOUGLAS STUDIO v1.0 ===")
    print(f"Author: Douglas | Nakuru, KE")
    print(f"Time: {datetime.now()}")
    print(f"GitHub: Running in cloud - No Ads, No Premium")
    print("="*40)
    
    traffic_light()
    play_music()
    robot_line_follower()
    box_stacker()
    
    print("\n" + "="*40)
    print("✅ ALL SYSTEMS PASSED - Ready for real hardware!")
    print("Next: Arduino + IR sensors + TCS3200 color sensor")

if __name__ == "__main__":
    main()
