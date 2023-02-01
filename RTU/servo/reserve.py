import RPi.GPIO as GPIO
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


def servoSetup(pin):
	GPIO.setup(pin, GPIO.OUT)
	servo  = GPIO.PWM(pin, 50)
	servo.start(0)

	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
	cs = digitalio.DigitalInOut(board.D22)
	mcp = MCP.MCP3008(spi, cs)
	cha0 = AnalogIn(mcp, MCP.P0)

	time.sleep(0.5)
	return servo, cha0

def setAngle(angle, pin, servo):
	duty = angle / 18 + 2
	GPIO.output(pin, True)
	servo.ChangeDutyCycle(duty)
	time.sleep(2)
	GPIO.output(pin, False)
	servo.ChangeDutyCycle(0)

def reqPos(channel):
	return channel.value, channel.voltage

def calculateAngle(voltage):
	high_voltage = 2.456
	min_voltage = 0.416
	max_angle = 181
	slope = (high_voltage - min_voltage) / (max_angle)
	feedback_angle = (voltage - min_voltage) / slope
	return feedback_angle
