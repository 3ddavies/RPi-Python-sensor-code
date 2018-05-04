import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    #GPIO.output(18, True)
    while True:    
        curli = GPIO.input(17)
        print(curli)
        
        if (curli == 0):
            GPIO.output(18, False)
            sleep(0.2)
        else:
            GPIO.output(18, True)
            sleep(0.2)
        
finally:
    GPIO.cleanup()