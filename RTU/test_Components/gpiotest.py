import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if GPIO.input(35) == True:
		GPIO.output(37, False)
		#time.sleep(0.5)
	else:
		#time.sleep(0.5)
		GPIO.output(37, True)
GPIO.cleanup()
