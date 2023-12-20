import RPi.GPIO as GPIO
import time


PIN11 = 11
PIN13 = 13
PIN15 = 15
PIN16 = 16
PIN18 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN11, GPIO.OUT)
GPIO.setup(PIN13, GPIO.OUT)
GPIO.setup(PIN15, GPIO.OUT)
GPIO.setup(PIN16, GPIO.OUT)
GPIO.setup(PIN18, GPIO.OUT)

while True:
    GPIO.output(PIN18, 1)
    time.sleep(1)
    GPIO.output(PIN18, 0)
    time.sleep(1)
    GPIO.output(PIN16, 1)
    time.sleep(1)
    GPIO.output(PIN16, 0)
    time.sleep(1)
    GPIO.output(PIN18, 1)
    GPIO.output(PIN16, 1)
    time.sleep(3)
    GPIO.output(PIN18, 0)
    GPIO.output(PIN16, 0)
    time.sleep(1)
    break

GPIO.cleanup()