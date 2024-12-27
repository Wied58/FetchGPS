# a simple test to check if gps id being read. 
# reads serial port and prints data
# 
import serial

import time


# if this fails, rebot, could add try except 


port = "/dev/serial0"
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)


gps_time_out = 0
while  gps_time_out < 35:
   time.sleep(1.0)
   data = ser.readline().decode('utf_8') 
   print (data)



