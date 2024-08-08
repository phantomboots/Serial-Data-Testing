# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:54:14 2023

@author: Benjamin Snow

"""
This is a small utility code to generated ASCII encoded serial data strings, for use with testing of NDST equipment. Serial port number and baud rate settings can be set to suit, in line 18, below.
The code will generate a comma seperate value string, termianted with <CR><LF>. 

This was intially developped to help configure MicroTronix open caption overlay devices, without the need to have all the relevant sensors configured and working. 

"""

import serial
from time import sleep
import datetime
import random
import string

#Set serial parameters here
with serial.Serial('COM1', 9600, 8, "N", 1) as ser:

#Configure message fields, send forever until keyboard interrupt detected. 
    while True:
        time = datetime.datetime.now()
        time = str(time)
        time = time.split(" ")
        time = str(time[1])
        time = time.split(".")
        time = str(time[0])
        date = str(datetime.date.today())
        lat = str(round(random.uniform(49, 50), 5))
        long = str(round(random.uniform(122, 123), 5))
        dive_id = "A" + str(random.randint(1,95))
        depth = str(round(random.uniform(0, 100), 1))
        heading = str(random.randint(0, 359))
        altitude = str(round(random.uniform(0, 10), 1))
        data = str("$Test," + heading + "," + depth + "," + altitude + "," + dive_id + "," + date + 
        "," + time + "," + lat + "," + long + "," + "END" + "\r\n")
      
#Encode the data as an ASCII string, and send it out of the serial port. 

        bytes_val = ser.write(data.encode('ascii'))
        print(data)

#Change this value if you want to send faster or slower.
        sleep(1)
