import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, False)

while True:
	print("LED ON")
	GPIO.output(40, True)
	time.sleep(1)
	print("LED OFF")
	GPIO.output(40, False)
	time.sleep(1)

GPIO.output(38, False)
GPIO.cleanup()
