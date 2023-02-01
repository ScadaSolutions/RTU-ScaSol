import RPi.GPIO as GPIO
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def reqTemp(channel):
	return channel.value, channel.voltage

def calculateTemp(voltage):
	#pin_mV = adc_raw * (3300/1024)
	#temp_C = (pin_mV - 500) / 10
	temp_C = 100*voltage - 50
	temp_F = (temp_C * (9/5)) + 32
	return temp_C, temp_F



