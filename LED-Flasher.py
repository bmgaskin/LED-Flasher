# LED Flasher                 
# Version: 1.0                            
# Date: 07-DEC-2020                   
# Programmer: Billy Gaskin
#
# Notes: Raspberry Pi 4 with breadboard configured with 4 LEDs: Red, Yellow, Green and Blue.
#
#        Red LED = GPIO port 18 to Red LED Anode
#                  220 Ohm resister from Ground to Red LED Cathode
#
#        Yellow LED = GPIO port 23 to Yellow LED Anode
#                  220 Ohm resister from Ground to Yellow LED Cathode
#
#        Green LED = GPIO port 24 to Green LED Anode
#                  220 Ohm resister from Ground to Green LED Cathode
#
#        Blue LED = GPIO port 25 to Blue LED Anode
#                  220 Ohm resister from Ground to Blue LED Cathode
#
# References:  CanaKit Raspberry Pi Ultimate Kit -- www.canakit.com
#              Starter Kit for Raspberry Pi -- www.freeNove.com
#

import RPi.GPIO as GPIO
import time
import random

red_port=18
yellow_port=23
green_port=24
blue_port=25
on=True
off=False

GPIO.setwarnings(off)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_port,GPIO.OUT)
GPIO.setup(yellow_port,GPIO.OUT)
GPIO.setup(green_port,GPIO.OUT)
GPIO.setup(blue_port,GPIO.OUT)

print("\n","*\n","* LED Flasher - Random Duration, All LEDs\n *")
for i in range (1,10):
    delay_time=random.uniform(0.01,1.0)
    print("\n",i,":","{0:.2f}".format(delay_time), "-", end=" ")
    for x in range(1,6):
        print(x,end=" ")
        GPIO.output(red_port,on)
        GPIO.output(yellow_port,on)
        GPIO.output(green_port,on)
        GPIO.output(blue_port,on)
        time.sleep(delay_time)
        GPIO.output(red_port,off)
        GPIO.output(yellow_port,off)
        GPIO.output(green_port,off)
        GPIO.output(blue_port,off)
        time.sleep(delay_time)

print("\n\n","*\n","* LED Flasher - Fixed Duration, Random Pattern\n *")
for i in range (1,100):
    delay_time=0.07
    print("\n",i,":","{0:.2f}".format(delay_time), "-", end=" ")
    Red_LED_state = random.randint(0,1)
    Yellow_LED_state = random.randint(0,1)
    Green_LED_state = random.randint(0,1)
    Blue_LED_state = random.randint(0,1)
    print("Red LED=",Red_LED_state,"Yellow LED=",Yellow_LED_state,"Green LED=",Green_LED_state,"Blue LED=",Blue_LED_state, "[",Red_LED_state,Yellow_LED_state,Green_LED_state,Blue_LED_state,"]",end=" ")
    GPIO.output(red_port,Red_LED_state)
    GPIO.output(yellow_port,Yellow_LED_state)
    GPIO.output(green_port,Green_LED_state)
    GPIO.output(blue_port,Blue_LED_state)
    time.sleep(delay_time)
    GPIO.output(red_port,off)
    GPIO.output(yellow_port,off)
    GPIO.output(green_port,off)
    GPIO.output(blue_port,off)
    time.sleep(delay_time)
