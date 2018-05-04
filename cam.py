from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
x = 0
camera = PiCamera()
try:
    #GPIO.output(18, True)
    while True:    
        curli = GPIO.input(17)
        print(curli)
        
        if (curli == 0):
            camera.capture('/home/pi/Desktop/image'+str(x)+'.jpg')
            x += 1
            sleep(0.2)
        else:
            sleep(0.2)
        
finally:
    GPIO.cleanup()
