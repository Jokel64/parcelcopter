import logging
import RPi.GPIO as GPIO
import time

class DistSensor:
    def __init__(self, porta, portb):
        self.porta = porta
        self.portb = portb

    #Pins zuweisen
    GPIO.setmode(GPIO.BCM)
    GPIO_TRIGGER = porta
    GPIO_ECHO = portb


    #Richtung der GPIO-Pins festlegen (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    def dist(self):
        # setze Trigger auf HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        startZeit = time.time()
        stopZeit = time.time()

        # speichere Startzeit
        while GPIO.input(GPIO_ECHO) == 0:
            startZeit = time.time()

        # speichere Ankunftszeit
        while GPIO.input(GPIO_ECHO) == 1:
            stopZeit = time.time()

        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = stopZeit - startZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz = (TimeElapsed * 34300) / 2

        return distanz

