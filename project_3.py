from time import sleep
import RPi.GPIO as gpio

DELAY = 0.1
INPIN = 40
OUTPIN = 38

gpio.setmode(gpio.BOARD)
gpio.setup(INPIN, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(OUTPIN, gpio.OUT)

LEDstate = 0
buttonState = 1
oldButtonState = 1
try:
    while True:
        buttonState = gpio.input(INPIN)
        print(buttonState)
        if buttonState == 1 and oldButtonState == 0:
            LEDstate = not LEDstate
            gpio.output(OUTPIN, LEDstate)
        oldButtonState = buttonState 
except KeyboardInterrupt:
    gpio.cleanup()

 