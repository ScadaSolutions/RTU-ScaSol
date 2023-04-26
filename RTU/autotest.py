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
relayOff(relay_output)

#commands:
#	chpos "" - change servo position
#	relay on - relay on
#	relay off - relay off
#	pull n - pull data last n rows

data_ls = [["Servo Angle", "Temp C", "temp F", "Rkr Switch", "Relay"]]

print("Beginning test function...\n")
time.sleep(.5)
print("Moving servo to 0 degrees...")
time.sleep(.25)
setAngle(0, servo_pin, pwm)
servo_adc, servo_v = reqPos(channel_1)
angle_servo = round(calculateAngle(servo_v), 2)
print("Angle is :",angle_servo)
time.sleep(.25)

print("Moving servo to 90 degrees...")
time.sleep(.25)
setAngle(90, servo_pin, pwm)
servo_adc, servo_v = reqPos(channel_1)
angle_servo = round(calculateAngle(servo_v), 2)
print("Angle is :",angle_servo)
time.sleep(.25)

print("Moving servo to 180 degrees...")
time.sleep(.25)
setAngle(180, servo_pin, pwm)
servo_adc, servo_v = reqPos(channel_1)
angle_servo = round(calculateAngle(servo_v), 2)
print("Angle is :",angle_servo)
time.sleep(.25)

print("Servo test complete!\n")
print("Beginning relay test...")
time.sleep(.5)

relayOn(relay_output)
time.sleep(.5)
print("Relay Status: ",relayStat(relay_input))
time.sleep(1.5)
relayOff(relay_output)
time.sleep(.5)
print("Relay Status: ",relayStat(relay_input))
time.sleep(1.5)

print("Relay Test complete!\n")
print("Beginning thermistor test...")
time.sleep(0.5)

for i in range(5):
	therm_adc, therm_vol = reqTemp(channel_0)
	temp_C, temp_F = calculateTemp(therm_vol)
	print("Temparature (C):", temp_C)
	time.sleep(0.25)
print("NOTE: Thermistor may be hotter than ambient due to pi CPU heat.")
time.sleep(2)

print("Thermistor Test done!\n")
print("Beginning switch input test...")
time.sleep(.5)
print("Initial condition is:")

if int(swStat(rocker_sw_pin)) == 1:
	print("Relay On")
else:
	print("Relay Off")

print("Toggle switch manually now...")
time.sleep(5)

if int(swStat(rocker_sw_pin)) == 1:
        print("Switch is On")
else:
        print("Switch is Off")


print("Rocker switch test is done!")

print("Test done!")
GPIO.cleanup()
