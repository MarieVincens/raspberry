import RPi.GPIO as GPIO
import time

class Led:

    def __init__(self, GPIO_number):
        self.GPIO_number = GPIO_number
        GPIO.setup(GPIO_number, GPIO.OUT)

    def on(self):
        GPIO.output(self.GPIO_number, GPIO.HIGH)

    def off(self):
        GPIO.output(self.GPIO_number, GPIO.LOW)

    @classmethod
    def initialisation(cls):
        #Utilisation d'une norme de nommage pour les broches
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    @classmethod
    def clean(cls):
        GPIO.cleanup()

Led.initialisation()

redLed= Led(16)
blueLed= Led(14)

redLed.on()
time.sleep(1)
redLed.off()
blueLed.on()
time.sleep(5)
blueLed.off()

Led.clean