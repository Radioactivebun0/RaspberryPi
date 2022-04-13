from tkinter import Button
import RPi.GPIO as GPIO
import time

button = 40

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(button, GPIO.IN)

def loop():
    while True:
        if GPIO.input(button) == GPIO.HIGH:
            print("Button pressed")
        else:
            print("No button pressed")
        time.sleep(0.2)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()