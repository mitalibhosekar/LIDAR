# https://stackoverflow.com/questions/54524225/keyboard-input-over-ssh-to-the-raspberry-pi3-with-pynput-function-in-python

import keyboard
import time

#declaring it global so that it can be modified from function
global releaseListening
keepListening = True

def key_press(key):
  global keepListening
  print(key.name)
  #if escape is pressed make listening false and exit 
  #if key.name == "esc":
  if key.name == " ":
    print("foo")
    keepListening = False

keyboard.on_press(key_press)

while keepListening :
  time.sleep(1)

### end ###
