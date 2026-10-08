import os
import subprocess
import time
import keyboard

TRIGGER_KEY = "print screen" # change this to whatever key you feel fits

SAVE_DIRECTORY = os.path.expanduser("~/Pictures/Screenshots")

os.makedirs(SAVE_DIRECTORY, exist_ok=True)

def take_screenshot():
    print ("Capturing Screen..")

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:

        subprocess.run(["spectacle", "-b", "-n", "-o", filepath], check=True)
        print(f"Screenshot saved to: {filepath}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")


def main():
    print(f"Press [{TRIGGER_KEY}] To take a screenshot. Press [esc] to exit.")

    keyboard.add_hotkey(TRIGGER_KEY, take_screenshot)

    keyboard.wait("esc")

if__name__=="__main__":
    main()
