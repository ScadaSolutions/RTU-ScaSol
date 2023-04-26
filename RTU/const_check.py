import RPi.GPIO as GPIO
import json
import time
from rocker.rocker_functions import *
from relay.relay_functions import *

with open("config_pin.json", "r") as configFile:
        pinout = json.load(configFile)
        configFile.close()

rocker_sw_pin = pinout.get("rocker_sw_pin")
relay_input = pinout.get("relay_pin_in")
relay_output = pinout.get("relay_pin_out")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

rockerSetup(rocker_sw_pin)
relaySetup(relay_input, relay_output)

cmd_check = False

while True:

	with open("output.txt", "r") as cmd_file:
		cmd = cmd_file.read()
		cmd_file.close()

	if cmd == "exit":
		break

	elif cmd == "relay on":
		cmd_check = True
	elif cmd == "relay off":
		cmd_check = False

	if not cmd_check:

		if swStat(rocker_sw_pin) == True:
			relayOn(relay_output)
		elif swStat(rocker_sw_pin) == False:
			relayOff(relay_output)
	time.sleep(1)

GPIO.cleanup()
