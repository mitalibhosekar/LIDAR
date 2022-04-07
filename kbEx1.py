# https://stackoverflow.com/questions/54524225/keyboard-input-over-ssh-to-the-raspberry-pi3-with-pynput-function-in-python

import keyboard
import time

#declaring it global so that it can be modified from function

keepListening = True

def key_press(key):
  print(key.name)
  if key.name == ".":
    print("foo")

keyboard.on_press(key_press)

while keepListening :
  time.sleep(1)

### end ###
