from time import sleep
import RPi.GPIO as gpio

DELAY = .1
INPIN = 40
OUTPIN = 38

gpio.setmode(gpio.BOARD)
gpio.setup(OUTPIN, gpio.OUT)
gpio.setup(INPIN, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
	while True:
		readVal = gpio.input(INPIN)
		print(readVal)
		while readVal == 1:
			gpio.output(OUTPIN, 1)
		if readVal == 0:
			gpio.output(OUTPIN,1)
		sleep(DELAY)

except KeyboardInterrupt:
	gpio.cleanup()
	print('\nGPIO ready to go')
