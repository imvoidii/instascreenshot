import os
import subprocess
import time
from pynput import keyboard

# Define the key that will trigger the screenshot
# For numbers, use keyboard.KeyCode.from_char('1')
# For special keys, use things like keyboard.Key.print_screen or keyboard.Key.f9
TRIGGER_KEY = "1"

# Define where you want to save the screenshots
SAVE_DIRECTORY = os.path.expanduser("~/Pictures/Screenshots")
os.makedirs(SAVE_DIRECTORY, exist_ok=True)


def take_screenshot():
    print("Capturing Screen...")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"Screenshot_{timestamp}.png"
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        # Running as normal user allows spectacle to talk to the KDE desktop environment properly
        subprocess.run(["spectacle", "-b", "-n", "-o", filepath], check=True)
        print(f"Screenshot saved to: {filepath}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")


def on_press(key):
    try:
        # Check if the pressed alphanumeric key matches our trigger
        if key.char == TRIGGER_KEY:
            take_screenshot()
    except AttributeError:
        # Handle special keys (like Esc)
        if key == keyboard.Key.esc:
            print("Exiting script.")
            return False  # Returning False stops the listener loop


def main():
    print(f"Press [{TRIGGER_KEY}] to take a screenshot. Press [esc] to exit.")

    # Start listening to global keyboard events as a normal user
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
