import json
import time
import RPi.GPIO as GPIO
import os
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from servo.servo_functions import *
from rocker.rocker_functions import *
from relay.relay_functions import *
from thermistor.thermistor_functions import *
from mcp3008.mcp_config import mcp3008Setup


with open("config_pin.json", "r") as configFile:
    pinout = json.load(configFile)
    configFile.close()

servo_pin = pinout.get("servo_pin")
rocker_sw_pin = pinout.get("rocker_sw_pin")
relay_input = pinout.get("relay_pin_in")
relay_output = pinout.get("relay_pin_out")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pwm = servoSetup(servo_pin)
#setAngle(-20, servo_pin, pwm)
channel_0, channel_1 = mcp3008Setup()
rockerSetup(rocker_sw_pin)
relaySetup(relay_input, relay_output)


#commands:
#	chpos "" - change servo position
#	reqpos - request servo position
#	relay on - relay on
#	relay off - relay off
#	swstat - switch status


while True:
	cmd = input("RTU>")
	cmd = cmd.split()
	if cmd[0] == "chpos":
		try:
			setAngle(int(cmd[1]), servo_pin, pwm)
		except ValueError:
			print("\nInvalid Servo CMD\n")
	elif cmd[0] == "reqpos":
		adc_servo, vol_servo = reqPos(channel_0)
		print("\n1. ADC Value.........:  {}".format(adc_servo))
		print("2. Voltage Reading...: {0:.3f} V".format(vol_servo))
		print()
		print(" - Feedback Angle....:   {:.3f}\n".format(calculateAngle(vol_servo)))

	elif cmd[0] == "relay":
		if cmd[1] == "on":
			if swStat(rocker_sw_pin) == False:
				relayOn(relay_output)
			else:
				print("Relay On by local switch.")
		elif cmd[1] == "off":
			if swStat(rocker_sw_pin) == False:
				relayOff(relay_output)
			else:
				print("Relay On by local switch.")
		else:
			print("Invalid Relay CMD")
			pass
	elif cmd[0] == "swstat":
		print("Rocker Switch Status: ", swStat(rocker_sw_pin))
	elif cmd[0] == "temp":
		adc_tmp36, vol_tmp36 = reqTemp(channel_1)
		temp_C, temp_F = calculateTemp(vol_tmp36)
		print("Current Temp in C: {:.2f}C\n".format(temp_C))
		print("Current Temp in F: {:.2f}F\n".format(temp_F))
	elif cmd[0] == "exit":
		print("Exiting...")
		break
	else:
		print("Invalid CMD")
		pass
GPIO.cleanup()
