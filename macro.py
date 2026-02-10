import threading
import time
from pynput import keyboard

TOGGLE_KEY = keyboard.Key.f8
MACRO_KEYS = ['2', '3', '4']
DELAY = 0.2

macro_active = False
stop_event = threading.Event()


def macro_loop():
    from pynput import keyboard 
    kb = keyboard.Controller()
    print("[Macro] Loop started")

    while not stop_event.is_set():
        for k in MACRO_KEYS:
            if stop_event.is_set():
                break
            kb.press(k)
            kb.release(k)
            time.sleep(DELAY)

    print("[Macro] Loop stopped")


def toggle_macro():
    global macro_active

    if macro_active:
        stop_event.set()
        macro_active = False
        print("[Macro] OFF")
    else:
        stop_event.clear()
        threading.Thread(target=macro_loop, daemon=True).start()
        macro_active = True
        print("[Macro] ON")


def on_press(key):
    if key == TOGGLE_KEY:
        toggle_macro()


print("F8 ile macro aç/kapat")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
