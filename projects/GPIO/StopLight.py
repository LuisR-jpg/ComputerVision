import RPi.GPIO as GPIO
import time


def setupPins(pins):
    for p in pins:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pins[p], GPIO.OUT)
def reset(pins, pin = None, isBlink = False): # Resets the pins and turns one on if provided
    waitTime = 1
    for p in pins:
        value = False
        if p == pin: value = True
        GPIO.output(pins[p], value)
    if isBlink: time.sleep(waitTime / 3)
    else: time.sleep(waitTime)

pins = {'green': 3, 'yellow': 5, 'green': 7}
setupPins(pins)
while True:
    reset(pins, 'green')
    for i in range(3):
        if i % 2: reset(pins, isBlink = True)
        else: reset(pins, 'green', True)
    reset(pins, 'yellow')
    reset(pins, 'red')
    