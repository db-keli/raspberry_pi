import RPi.GPIO as GPIO
from time import sleep

INPIN = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPIN, GPIO.IN)

try:
	while True:
		readVal = GPIO.input(INPIN)
		print(readVal)
		sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
