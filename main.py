from tkinter import Button
import RPi.GPIO as GPIO
import time

button = 4

global lastTime
lastTime = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN)

def alert(al):
    global lastTime
    if al == "True" and time.time() - lastTime > 60:
        lastTime = time.time()
        print("Alert!")
    else:
        if al == "True":
            print("Alert already sent per lastTime")
        else:
            print("No alert at all")

def loop():
    alertboo = False
    while True:
        if GPIO.input(button) == GPIO.HIGH:
            alertboo = True
            print("Alert set to True")
        else:
            alertboo = False
            print("Alert set to False")
        
        time.sleep(5)

        alert(str(alertboo))

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