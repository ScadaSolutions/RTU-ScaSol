
import time
import RPi.GPIO as GPIO

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D22)

mcp = MCP.MCP3008(spi, cs)

chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)

i = 0
while True:
	print("Raw ADC val 1: ", chan0.value)
	print("ADC Vol 1: ", str(chan0.voltage) + "V")
	print()
	print("Raw ADC val 2: ", chan1.value)
	print("ADC Vol 2: ", str(chan1.voltage) + "V")
	print()
	time.sleep(2)

vol = chan0.voltage
print(type(vol))


