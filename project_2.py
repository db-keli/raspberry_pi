import RPi.GPIO as GPIO
from time import sleep

PIN = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

try:
    while True:
        readVal = GPIO.input(PIN)
        
        if readVal == 1:
            print("LED is on")
        else:
            print("LED is off")
             
        
    
    
except KeyboardInterrupt:
    GPIO.cleanup()
