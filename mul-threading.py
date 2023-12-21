import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def first():
    GPIO.output(18, 1)
    time.sleep(1)
    GPIO.output(18, 0)
    time.sleep(1)
    

def second():
    GPIO.output(16, 1)
    time.sleep(1)
    GPIO.output(16, 0)
    time.sleep(1)

t1 = threading.Thread(target=first)
t2 = threading.Thread(target=second)

threads = [t1, t2]

for i in threads:
    i.start()
for i in threads:
    i.join()   
    

GPIO.cleanup()