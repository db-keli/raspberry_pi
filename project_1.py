import RPi.GPIO as GPIO
import time

PIN11 = 11
PIN13 = 13
PIN15 = 15
PIN16 = 16
PIN18 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

for i in range(20):
    print(f"This is iteration {i}")
    GPIO.output(18, 1)
    time.sleep(1)
    GPIO.output(18, 0)
    time.sleep(1)

GPIO.cleanup()