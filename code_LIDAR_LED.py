import os
import time
from math import floor
from adafruit_rplidar import RPLidar
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 5

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0
val = 500

def check (scan_data, val):
    for x in scan_data:
        if (x < val):
            print("hit")
            print(x)
            print(scan_data)
            print(hit_data)
            
            while True:
                pixels.fill((255, 0, 0))
                pixels.show()
                #time.sleep(1)

    
         
#def process_data(data):
    
forhit= "Hit"
nothit="not hit"

scan_data = [0]*91
hit_data =  [0]*91
try:
#    print(lidar.get_info())
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([90, floor(angle)])] = distance
        #process_data(scan_data)
            time.sleep(0.5)    
            if(distance < val):
                hit_data[min([90, floor(angle)])] = "hit"
            else:
                hit_data[min([90, floor(angle)])] = "not hit"
            print(hit_data)
        time.sleep(1)    
        #check(scan_data, 500)
        #time.sleep(10)
        
        
    
            #if(check (scan_data, 500)):
                
            #else:
                #print("Not hit")
        
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()




