#!/usr/bin/env python

#Licensed under the MIT licence 
#To end the Programme use "C+Ctrl" at the same time. 

#pretty obvious, but you'll want these dependencies to be installed for this script to work

# This imports the Raspberry Pi's GPIO library but as GPIO so we don't need to be repeating it.
import RPi.GPIO as GPIO

#This is used to sleep the code a the end.
import time

#Requests is the ONE that is need to be installed with "sudo apt-get install python-requests" this lets us to grab and interpret PHP
import requests

import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])
	
#Uncomment this is you don't want to get the GPIO warning. This is useful if you changing things around constantly and are ending the code.
#GPIO.setwarnings(False)

DEBUG = 1

#this defines the pins for each ONE
ONE = 23
TWO = 24
THREE = 25

#sets the mode for the pin out
GPIO.setmode(GPIO.BCM)

#defines if the pins are inputs or out puts
GPIO.setup(ONE, GPIO.OUT)
GPIO.setup(TWO, GPIO.OUT)
GPIO.setup(THREE, GPIO.OUT)


#replace the http://YourWebsite.com/test.php with where your test.php is located.
response = requests.get('http://yourwebsite.com/text.php')

#replace the http://YourWebsite.com/test.php with where your test.php is located.
while response.text != 'exit':
    response = requests.get('http://yourwebsite.com/text.php')

#This says ONE is the first digit TWO is the second and THREE is the last 
    colrs = response.text
    one = colrs[0]
    two = colrs[1]
    three = colrs[2]

    cls()

    if response.text == 'exit':
        print (colrs)
    else:
        print ("one" + one + ", "),
        print ("two" + two + ", "),
        print ("three" + three)
        print

# This says if the number is 1 then the the light is on else if it is 0 the light is off.
    if one == '1':
        GPIO.output(ONE,True)
    else:
        GPIO.output(ONE,False)
		
    if two  == '1':
        GPIO.output(TWO,True)
    else:
        GPIO.output(TWO,False)
		
    if three  == '1':
        GPIO.output(THREE,True)
    else:
        GPIO.output(THREE,False)
		

#This can be removed but this time is to stop the web server from being overloaded with requests.
    time.sleep(0.15)
