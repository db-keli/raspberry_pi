from time import sleep
import RPi.GPIO as gpio

DELAY = 0.1
INPIN = 40
OUTPIN = 38

gpio.setmode(gpio.BOARD)
gpio.setup(INPIN, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    pass
except KeyboardInterrupt:
    gpio.cleanup()

