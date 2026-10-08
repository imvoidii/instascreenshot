import os
import subprocess
import time

# Define where you want to save the screenshots
SAVE_DIRECTORY = os.path.expanduser("~/Pictures/Screenshots")
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

# Generate a unique filename using the current timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = f"Screenshot_{timestamp}.png"
filepath = os.path.join(SAVE_DIRECTORY, filename)

try:
    # Native KDE screenshot utility
    subprocess.run(["spectacle", "-b", "-n", "-o", filepath], check=True)
    print(f"Screenshot saved to: {filepath}")
except Exception as e:
    print(f"Error taking screenshot: {e}")
