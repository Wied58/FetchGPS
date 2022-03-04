import os
import sys
import time
import smbus
import subprocess

from datetime import datetime

from gps import *

# Delay start by 15 seconds
time.sleep(1)



gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

x = 0

while True:

    GPSLat = "0.0"
    GPSLong = "0.0"
    GPSTime = "00:00:00"
    GPSAlt = "000"

# Get timestamp
    CurrTimestamp = datetime.now()
    #print(f"CurrTimestamp = {CurrTimestamp}")
    report = gpsd.next()
    #print(report['class'])
    #print(x)

    if report['class'] == 'TPV':
        GPSLat = getattr(report,'lat',0.0)
        GPSLong = getattr(report,'lon',0.0)
        GPSTime = getattr(report,'time','')
        GPSAlt = getattr(report,'alt','nan')
        GPSMode = getattr(report,'mode','nan')

        #print("Timestamp: ", CurrTimestamp)
        #print ("Lat: ", GPSLat)
        #print ("Long: ", GPSLong)
        #print ("GPS Time: ", GPSTime)
        #print ("Altitude: ", GPSAlt)
        #print ("GPSMode: ",GPSMode)
        #print ()

        if GPSMode == 3:
          break
    x += 1
    time.sleep(0.8)


