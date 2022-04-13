from tkinter import Button
import RPi.GPIO as GPIO
import time

button = 4

global lastTime
lastTime = time.time()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN)

def alert(al):
    if al == "True" and time.time() - lastTime > 60:
        print("Alert!")
    else:
        if al == "True":
            print("Alert already sent per lastTime")
        else:
            print("No alert at all")

def loop():
    alert = False
    while True:
        if GPIO.input(button) == GPIO.HIGH:
            alert = True
            print("Alert set to True")
        else:
            alert = False
            print("Alert set to False")
        
        time.sleep(5)

        alert(str(alert))

        """
        if GPIO.input(button) == GPIO.HIGH:
            print("Button pressed")
        else:
            print("Button released")
        time.sleep(0.2)"""

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()