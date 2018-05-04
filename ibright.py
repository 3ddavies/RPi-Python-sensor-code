import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
br = 0
pl = GPIO.PWM(18, 500)
pl.start(0)
try:
    while True:
        insta = GPIO.input(16)
        if (insta == False):
            br+=1
            print(br)
            pl.ChangeDutyCycle(br*10)
            sleep(0.2)
finally:
    GPIO.cleanup()