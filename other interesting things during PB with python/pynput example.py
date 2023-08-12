from pynput.keyboard import Key, Controller, Listener
import time

kb = Controller()
def pressed(e):
    print("pressed")
def released(e):
    print("released")

with Listener(on_press=pressed,on_release=released,) as listener:
    listener.join()

