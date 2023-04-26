import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	print("Pin status: ", GPIO.input(40))
GPIO.cleanup()
