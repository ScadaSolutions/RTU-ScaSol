from gpiozero import Servo
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

servo = GPIO.PWM(3, 50)
servo.start(0)
time.sleep(2)

def setAngle(angle):
	duty = angle/ 18 + 2
	GPIO.output(3, True)
	servo.ChangeDutyCycle(duty)
	time.sleep(1.5)
	GPIO.output(3, False)
	servo.ChangeDutyCycle(0)

angle = 0
setAngle(0)

while angle <= 180:
	print("Setting servo to angle:", angle)
	setAngle(angle)
	time.sleep(2)
	angle += 15

servo.stop()
GPIO.cleanup()
