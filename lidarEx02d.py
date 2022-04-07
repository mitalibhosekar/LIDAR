from rpi_ws281x import *
import time

# LED strip configuration:
LED_COUNT      = 10      # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()


import os, sys
import time
from math import floor
from adafruit_rplidar import RPLidar

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0
forhit= "Hit"
nothit="not hit"
maxboundary= 1500
hit_data = []

def process_data(data):
  global hit_data, maxboundary
  #print(data)
  for i in range(len(data)):
    if data[i] < maxboundary:
      #hit_data.append(forhit)
        print("Its a hit")
        print(i)
        print(data[i])
        for x in range(0,LED_COUNT):
            strip.setPixelColor(x,Color(255,0,0))
            strip.show()
            #time.sleep(0.001)
            strip.setPixelColor(x,Color(0,0,0))
            strip.show()
            #time.sleep(0.001)
    else:
      #hit_data.append(nothit)
        print("Its a not hit")
        print(i)
        print(data[i])
  #print(hit_data)    

scan_data = [0]*91
#scan_data = [0]*360

try:
#  print(lidar.get_info())
  iscans = lidar.iter_scans()
  #print(iscans)
  for scan in iscans:
    for (_, angle, distance) in scan:
      idx = min([90, floor(angle)])
      #print("idx:", idx)
      scan_data[idx] = distance

    process_data(scan_data)  
    #time.sleep(0.5)
    
except KeyboardInterrupt:
  print('Stopping.')  
else:
  print("scan loop fail: idx="+idx); sys.exit(-1)

lidar.stop()
lidar.disconnect()

#https://github.com/adafruit/Adafruit_CircuitPython_RPLIDAR
     
