import FetchGPS


#this is the string we have to create to set time
#18 MAR 2022 10:49:25

#2022-03-18T01:26:38.000Z

print (f"FetchGPS.GPSTime = {FetchGPS.GPSTime}") 
print (f"FetchGPS.GPSTime.year = {FetchGPS.GPSTime[0:4]}") 
print (f"FetchGPS.GPSTime.month = {FetchGPS.GPSTime[5:7]}") 
print (f"FetchGPS.GPSTime.day = {FetchGPS.GPSTime[8:10]}") 
print (f"FetchGPS.GPSTime.min = {FetchGPS.GPSTime[11:13]}") 
print (f"FetchGPS.GPSTime.sec = {FetchGPS.GPSTime[14:16]}") 
print (f"FetchGPS.GPSLat = {FetchGPS.GPSLat}") 
print (f"FetchGPS.GPSLong = {FetchGPS.GPSLong}")
print (f"FetchGPS.GPSAlt = {FetchGPS.GPSAlt}")
print (f"FetchGPS.GPSMode = {FetchGPS.GPSMode}")




