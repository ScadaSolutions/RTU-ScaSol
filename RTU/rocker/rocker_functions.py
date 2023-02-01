import RPi.GPIO as GPIO

def rockerSetup(pin):
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def swStat(pin):
	if GPIO.input(pin) == True:
		return True
	else:
		return False
