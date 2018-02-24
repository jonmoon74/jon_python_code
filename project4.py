import time
import RPi.GPIO as gpio
import random

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)

gpio.output(3,gpio.LOW)
gpio.output(5,gpio.LOW)
gpio.output(7,gpio.LOW)
gpio.output(13,gpio.LOW)
gpio.output(13,gpio.LOW)

time.sleep(1)

list = [3,5,7,11,13]
list2 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

while True:
	light = random.choice(list)
	pause = random.choice(list2)
	gpio.output(light,gpio.HIGH)
	time.sleep(pause)
	gpio.output(light,gpio.LOW)

gpio.cleanup()
