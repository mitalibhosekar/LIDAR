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
maxboundary= 500
hit_data = []

def process_data(data):
  global hit_data, maxboundary
  #print(data)
  for i in data:
    if i < maxboundary:
      hit_data.append(forhit)
    else:
      hit_data.append(nothit)
  #print(hit_data)    

#scan_data = [0]*91
scan_data = [0]*360

try:
#  print(lidar.get_info())
  iscans = lidar.iter_scans()
  #print(iscans)
  for scan in iscans:
    for (_, angle, distance) in scan:
      idx = min([359, floor(angle)])
      #print("idx:", idx)
      scan_data[idx] = distance

    process_data(scan_data)  
    #time.sleep(1)
    
except KeyboardInterrupt:
  print('Stopping.')  
else:
  print("scan loop fail: idx="+idx); sys.exit(-1)

lidar.stop()
lidar.disconnect()

#https://github.com/adafruit/Adafruit_CircuitPython_RPLIDAR
     
