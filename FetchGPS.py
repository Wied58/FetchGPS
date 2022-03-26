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

    GPSLat = 0.0
    GPSLong = 0.0
    GPSTime = "00:00:00"
    GPSAlt = 000
    GPSMode = 0

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

        #print("System Time: ", CurrTimestamp)
        #print ("Lat: ", GPSLat)
        #print ("Long: ", GPSLong)
        #print ("GPS Time: ", GPSTime)
        #print ("Altitude: ", GPSAlt)
        #print ("GPSMode: ",GPSMode)
        #print ()

        if GPSMode == 3:
          break
    x += 1
    if x == 48:
        print("Giving up on GPS - We must be in the basement")
        break
    time.sleep(0.8)

with open('/home/pi/Tools/FetchGPS/FetchGPS.log', "w") as fout:

        fout.write (f"System Time: {CurrTimestamp}\n")
        fout.write (f"Lat: {GPSLat}\n")
        fout.write (f"Long: {GPSLong}\n")
        fout.write (f"GPS Time: {GPSTime}\n")
        fout.write (f"Altitude: {GPSAlt}\n")
        fout.write (f"GPSMode: {GPSMode}\n")
   
