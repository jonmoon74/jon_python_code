import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

GPIO.output(13,GPIO.HIGH)

while True:
	if (GPIO.input(12)==True):
		GPIO.output(13,GPIO.LOW)
GPIO.cleanup()
