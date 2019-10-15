import RPi.GPIO as GPIO
import time
from threading import Thread

class Led:

    def __init__(self, GPIO_number):
        self.GPIO_number = GPIO_number
        GPIO.setup(GPIO_number, GPIO.OUT)

    def on(self):
        GPIO.output(self.GPIO_number, GPIO.HIGH)

    def off(self):
        GPIO.output(self.GPIO_number, GPIO.LOW)

    def blink(self, numBlink, sleepTime):
        i=0
        while i<numBlink:
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            i += 1

    def asyncBlink(self, numBlink, sleepTime):
        thread = Thread(target=self.blink, args=(numBlink, sleepTime))
        thread.start()
        return thread

    @classmethod
    def initialisation(cls):
        #Utilisation d'une norme de nommage pour les broches
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @classmethod
    def clean(cls):
        GPIO.cleanup()

'''Led.initialisation()

redLed= Led(16)
blueLed= Led(14)
redThread =  redLed.asyncBlink(10, 0.25)
blueThread =  blueLed.asyncBlink(10, 0.25)


redLed.on()
time.sleep(1)
redLed.off()
blueLed.on()
time.sleep(1)
blueLed.off()

Led.clean()

blueThread.join()
redThread.join()

Led.clean()'''