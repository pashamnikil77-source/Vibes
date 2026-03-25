# ---------------------------------------------------------
# REPO: /user/sweetness-detector-v3
# COMMIT: "Fixed bug where cuteness caused system crash"
# AUTHOR: [Your Name]
# ---------------------------------------------------------

import time
import sys

def stream_text(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def main():
    NAME = "NAME_HERE" # <--- Put her name here
    
    print(f"\033[94m[GIT] Fetching remote data for subject: {NAME}...\033[0m")
    time.sleep(1.5)
    
    print("\n[ANALYSIS START]")
    print("-" * 35)
    
    # Fake terminal logs
    logs = [
        "Checking database for 'cute'...",
        "Searching for 'sweetest personality'...",
        "Scanning for 'kindest soul'...",
        "MATCH FOUND: " + NAME
    ]
    
    for log in logs:
        print(f" > {log}")
        time.sleep(0.8)

    print("-" * 35)
    print("\n\033[92m[MATCH CONFIRMED]\033[0m")
    stream_text(f"Subject {NAME} is officially 10/10.", 0.08)
    stream_text("Warning: High probability of melting this terminal.", 0.06)
    
    # The "Cool" Cat
    print("\n      |\__/,|   (`\ ")
    print("    _.|o o  |_   ) )")
    print("---(((---(((-----------------")
    print(f"   (This is {NAME} in code form)")
    
    time.sleep(2)

    # THE CRITICAL ERROR / SELF DESTRUCT
    print("\n\033[91m[CRITICAL ERROR]: SYSTEM OVERHEAT\033[0m")
    print("REASON: TARGET IS TOO SWEET FOR LOCAL HARDWARE")
    
    for i in range(3, 0, -1):
        print(f"DETONATING IN {i}...", end="\r")
        time.sleep(1)

    print("\n\nBOOM. 💥")
    print("Terminal Offline. Mission Accomplished.")

if __name__ == "__main__":
    main()
