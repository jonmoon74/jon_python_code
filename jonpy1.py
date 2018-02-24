#import modules
import time
import RPi.GPIO as GPIO
import random
import sys

#SetUp GPIO board
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

#set lights to off state
GPIO.output(3,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.output(7,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.HIGH)

time.sleep(1)

#Create lists of random choices
list = [3,5,7,11,13]
list2 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

#Run lights if switch is set
while True:
        if (GPIO.input(12) == True):
                GPIO.output(15,GPIO.LOW)
                light = random.choice(list)
                pause = random.choice(list2)
                GPIO.output(light,GPIO.HIGH)
                time.sleep(pause)
                GPIO.output(light,GPIO.LOW)
        else:
                sys.ext("switch is off")
GPIO.cleanup()
