import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def mcp3008Setup():
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
	cs = digitalio.DigitalInOut(board.D22)
	mcp = MCP.MCP3008(spi, cs)
	chan_list = []

	chan0 = AnalogIn(mcp, MCP.P0)
	chan1 = AnalogIn(mcp, MCP.P1)
	return chan0, chan1
