import RPi.GPIO as GPIO
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D22)
mcp = MCP.MCP3008(spi, cs)

chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)

while True:
	print(f"Channel 0:")
	print(f"ADC:     {chan0.value}")
	print(f"Voltage: {chan0.voltage}")
	print("---------------------------------")
	print(f"Channel 1:")
	print(f"ADC:     {chan1.value}")
	print(f"Voltage: {chan1.voltage}")
	print("=================================")
	time.sleep(3)


