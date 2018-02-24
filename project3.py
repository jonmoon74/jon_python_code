import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)

gpio.output(3,gpio.HIGH)
gpio.output(5,gpio.LOW)
gpio.output(7,gpio.LOW)

time.sleep(5)

gpio.output(5,gpio.HIGH)

time.sleep(2)

gpio.output(3,gpio.LOW)
gpio.output(5,gpio.LOW)
gpio.output(7,gpio.HIGH)

time.sleep(5)

gpio.output(5,gpio.HIGH)
gpio.output(7,gpio.LOW)

time.sleep(2)

gpio.output(5,gpio.LOW)
gpio.output(3,gpio.HIGH)

time.sleep(5)

gpio.output(3,gpio.LOW)

gpio.cleanup()
