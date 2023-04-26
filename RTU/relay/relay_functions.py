import RPi.GPIO as GPIO


def relaySetup(in_pin, out_pin):
	GPIO.setup(out_pin, GPIO.OUT)
	GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(out_pin, False)


def relayOn(out_pin):
	GPIO.output(out_pin, True)


def relayOff(out_pin):
	GPIO.output(out_pin, False)


def relayStat(in_pin):
	if GPIO.input(in_pin) == True:
		return True
	else:
		return False
