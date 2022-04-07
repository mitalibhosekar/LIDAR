import os
from math import floor
import math
from adafruit_rplidar import RPLidar


# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

def process_data(data):
    print(data)
    x_axis = []
    for i in range(len(data)):
        x = data[i]*math.sin((i/360)*math.pi)
        x_axis.append(x)
    print("aha")
    print(x_axis)
    return x_axis
        

scan_data = [0]*91

try:
#    print(lidar.get_info())
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([90, floor(angle)])] = distance
        process_data(scan_data)

except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()
         