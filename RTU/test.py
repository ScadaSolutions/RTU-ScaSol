import socket
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
from prettytable import PrettyTable


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
#	relay on - relay on
#	relay off - relay off
#	pull n - pull data last n rows

data_ls = [["Servo Angle", "Temp C", "temp F", "Rkr Switch", "Relay"]]

while True:

	cmd = input("RTU~$ ")
	if cmd == "":
		pass
	elif cmd =="exit":
		print("\nExiting RTU files and programs...")
		time.sleep(1)
		print("Done!")
		break

	elif cmd=="help" or cmd=="h":
		print("""Commands:
			chpos # - change servo position to # degrees
			relay on/off - turns relay on/off
			pull # - pull data, where # is the last # rows (# is an optional parameter)""")
	else:
		cmd = cmd.split()
		if cmd[0] == "chpos":
			try:
				setAngle(int(cmd[1]), servo_pin, pwm)
			except ValueError:
				print("[!] Invalid Servo CMD")
		elif cmd[0] == "relay":
			if cmd[1] == "on":
				relayOn(relay_output)
			elif cmd[1] == "off":
				relayOff(relay_output)
			else:
				print("[!] Invalid Relay CMD")

		elif cmd[0] == "pull":
			if len(cmd) == 1:
				print()
				table = PrettyTable(data_ls[0])
				for data in data_ls[1:]:
					table.add_row(data)
				print(table)
				print()
			else:
				try:
					n = int(cmd[1])
					new_data = data_ls[-n-1:]
					table = PrettyTable(data_ls[0])
					for data in new_data[1:]:
						table.add_row(data)
					print()
					print(table)
					print()
				except ValueError:
					print("\nCMD: 'pull n' -> where n is an integer.\n")
		else:
			print("\nInvalid CMD [!]\n")

	servo_adc, servo_vol = reqPos(channel_1)
	angle_servo = round(calculateAngle(servo_vol), 2)

	therm_adc, therm_vol = reqTemp(channel_0)
	temp_C, temp_F = calculateTemp(therm_vol)

	rocker_sw = int(swStat(rocker_sw_pin))

	relay = int(relayStat(relay_input))

	ls = [angle_servo, round(temp_C, 2), round(temp_F, 2), rocker_sw, relay]
	data_ls.append(ls)

	data = ",".join(str(comp) for comp in ls)


GPIO.cleanup()
