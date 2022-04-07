import os
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
maxboundery= 500
hit_data = []

def process_data(data):
    print(data)
    for i in data:
        if i < maxboundery:
            hit_data.append(forhit)
        else:
            hit_data.append(nothit)
    print(hit_data)        

scan_data = [0]*91

try:
#    print(lidar.get_info())
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([90, floor(angle)])] = distance
        #process_data(scan_data)    
        time.sleep(1)
        
            

except KeyboardInterrupt:
    print('Stopping.')    
lidar.stop()
lidar.disconnect()



#https://github.com/adafruit/Adafruit_CircuitPython_RPLIDAR
         