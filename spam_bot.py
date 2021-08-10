from pynput.keyboard import Key,Controller
import time
Keyboard = Controller()
time.sleep(2)
while True:
    for letter in "Spam Text":
        Keyboard.press(letter) 
        Keyboard.release(letter)
    Keyboard.press(Key.enter) 
    Keyboard.release(Key.enter)   