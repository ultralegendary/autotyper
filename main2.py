import threading
import time
from pynput import keyboard

Controller = keyboard.Controller()
typing = False
typing_thread = None
stop_typing_event = threading.Event()

def start_typing():
    print("Start typing...")
    while not stop_typing_event.is_set():
        words_to_type = "Ihackedyou"

        for char in words_to_type:
            Controller.type(char)
            time.sleep(0.1)

def on_key_press(key):
    global typing, typing_thread, stop_typing_event

    if key == keyboard.Key.space:
        if typing:
            typing = False
            print("Stop typing...")
            stop_typing_event.set()
            typing_thread.join()
            stop_typing_event.clear()
        else:
            typing = True
            stop_typing_event.clear()
            typing_thread = threading.Thread(target=start_typing)
            typing_thread.start()

def main():
    print("Auto Clicker activated. Press space to start/stop typing.")

    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    while True:
        time.sleep(0.1)

if __name__ == '__main__':
    main()
