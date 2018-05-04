import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
#GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        GPIO.output(18, True)
        sleep(1)
        GPIO.output(18, False)
        sleep(1)
finally:
    GPIO.cleanup()