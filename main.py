from ast import Return
from pdb import Restart
from tkinter import Button
from xmlrpc.client import Server
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

Sensor1 = [4, "Sensor1", False, 0]
Sensor2 = [17, "Sensor2", False, 0]
Sensor3 = [27, "Sensor3", False, 0]
Sensor4 = [22, "Sensor4", False, 0]
Sensor5 = [5, "Sensor5", False, 0]
Sensor6 = [6, "Sensor6", False, 0]
Sensor7 = [13, "Sensor7", False, 0]
Sensor8 = [19, "Sensor8", False, 0]
Sensor9 = [26, "Sensor9", False, 0]
Sensor10 = [18, "Sensor10", False, 0]
Sensor11 = [23, "Sensor11", False, 0]
Sensor12 = [24, "Sensor12", False, 0]
Sensor13 = [25, "Sensor13", False, 0]
Sensor14 = [12, "Sensor14", False, 0]
Sensor15 = [16, "Sensor15", False, 0]
Sensor16 = [20, "Sensor16", False, 0]
Sensor17 = [21, "Sensor17", False, 0]

global lastTime
lastTime = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Sensor1[0], GPIO.IN)
    GPIO.setup(Sensor2[0], GPIO.IN)
    GPIO.setup(Sensor3[0], GPIO.IN)
    GPIO.setup(Sensor4[0], GPIO.IN)
    GPIO.setup(Sensor5[0], GPIO.IN)
    GPIO.setup(Sensor6[0], GPIO.IN)
    GPIO.setup(Sensor7[0], GPIO.IN)
    GPIO.setup(Sensor8[0], GPIO.IN)
    GPIO.setup(Sensor9[0], GPIO.IN)
    GPIO.setup(Sensor10[0], GPIO.IN)
    GPIO.setup(Sensor11[0], GPIO.IN)
    GPIO.setup(Sensor12[0], GPIO.IN)
    GPIO.setup(Sensor13[0], GPIO.IN)
    GPIO.setup(Sensor14[0], GPIO.IN)
    GPIO.setup(Sensor15[0], GPIO.IN)
    GPIO.setup(Sensor16[0], GPIO.IN)
    GPIO.setup(Sensor17[0], GPIO.IN)

def send_email(too, sub="test", mm="test"):
    SMTP_SERVER = "smtp.mail.yahoo.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "leak_detection@yahoo.com" #leak_detection@yahoo.com @att.net Soccer0127=
    SMTP_PASSWORD = "qyfivnxtrequzavv" # qyfivnxtrequzavv
    EMAIL_FROM = "leak_detection@yahoo.com"
    EMAIL_TO = too
    EMAIL_SUBJECT = sub
    co_msg = mm
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

def alert(sensor):
    if time.time() - sensor[3] > 60 and sensor[2] == False:
        print("Sending email")
        send_email("tyleer253@gmail.com", "Leak Detected", f"Leak Detected on sensor {sensor[1]}")
        return True, time.time()
    return False, sensor[3]
    
    """
    elif sensor[2] == True and time.time() - lastTime > 60:
        print("Sensor is no longer detecting a leak, reset")
        sensor[2] = False
    elif sensor[2] == True:
        print("Leak was already detected")
    elif time.time() - lastTime < 60:
        print("Leak was detected within the last minute")
    else:
        print("Something went wrong")"""

def ResetPins():
    global lastTime
    if GPIO.input(Sensor1[0]) == GPIO.LOW:
        Sensor1[2] = False
    if GPIO.input(Sensor2[0]) == GPIO.LOW:
        Sensor2[2] = False
    if GPIO.input(Sensor3[0]) == GPIO.LOW:
        Sensor3[2] = False
    if GPIO.input(Sensor4[0]) == GPIO.LOW:
        Sensor4[2] = False
    if GPIO.input(Sensor5[0]) == GPIO.LOW:
        Sensor5[2] = False
    if GPIO.input(Sensor6[0]) == GPIO.LOW:
        Sensor6[2] = False
    if GPIO.input(Sensor7[0]) == GPIO.LOW:
        Sensor7[2] = False
    if GPIO.input(Sensor8[0]) == GPIO.LOW:
        Sensor8[2] = False
    if GPIO.input(Sensor9[0]) == GPIO.LOW:
        Sensor9[2] = False
    if GPIO.input(Sensor10[0]) == GPIO.LOW:
        Sensor10[2] = False
    if GPIO.input(Sensor11[0]) == GPIO.LOW:
        Sensor11[2] = False
    if GPIO.input(Sensor12[0]) == GPIO.LOW:
        Sensor12[2] = False
    if GPIO.input(Sensor13[0]) == GPIO.LOW:
        Sensor13[2] = False
    if GPIO.input(Sensor14[0]) == GPIO.LOW:
        Sensor14[2] = False
    if GPIO.input(Sensor15[0]) == GPIO.LOW:
        Sensor15[2] = False
    if GPIO.input(Sensor16[0]) == GPIO.LOW:
        Sensor16[2] = False
    if GPIO.input(Sensor17[0]) == GPIO.LOW:
        Sensor17[2] = False



def loop():
    while True:
        if GPIO.input(Sensor1[0]) == GPIO.HIGH:
            print("Alerting on Sensor1")
            Sensor1[2], Sensor1[3] = alert(Sensor1)
        #else:
            #print("No leak detected on Sensor1")
        if GPIO.input(Sensor2[0]) == GPIO.HIGH:
            print("Alerting on Sensor2")
            Sensor2[2], Sensor2[3] = alert(Sensor2)
        #else:
         #   print("No leak detected on Sensor2")
        if GPIO.input(Sensor3[0]) == GPIO.HIGH:
            print("Alerting on Sensor3")
            Sensor3[2], Sensor3[3] = alert(Sensor3)
        #else:
         #   print("No leak detected on Sensor3")
        if GPIO.input(Sensor4[0]) == GPIO.HIGH:
            print("Alerting on Sensor4")
            Sensor4[2], Sensor4[3] = alert(Sensor4)
        #else:
         #   print("No leak detected on Sensor4")
        if GPIO.input(Sensor5[0]) == GPIO.HIGH:
            print("Alerting on Sensor5")
            Sensor5[2], Sensor5[3] = alert(Sensor5)
        #else:
         #   print("No leak detected on Sensor5")
        if GPIO.input(Sensor6[0]) == GPIO.HIGH:
            print("Alerting on Sensor6")
            Sensor6[2], Sensor6[3] = alert(Sensor6)
        #else:
         #   print("No leak detected on Sensor6")
        if GPIO.input(Sensor7[0]) == GPIO.HIGH:
            print("Alerting on Sensor7")
            Sensor7[2], Sensor7[3] = alert(Sensor7)
        #else:
         #   print("No leak detected on Sensor7")
        if GPIO.input(Sensor8[0]) == GPIO.HIGH:
            print("Alerting on Sensor8")
            Sensor8[2], Sensor8[3] = alert(Sensor8)
        #else:
         #   print("No leak detected on Sensor8")
        if GPIO.input(Sensor9[0]) == GPIO.HIGH:
            print("Alerting on Sensor9")
            Sensor9[2], Sensor9[3] = alert(Sensor9)
        #else:
         #   print("No leak detected on Sensor9")
        if GPIO.input(Sensor10[0]) == GPIO.HIGH:
            print("Alerting on Sensor10")
            Sensor10[2], Sensor10[3] = alert(Sensor10)
        #else:
         #   print("No leak detected on Sensor10")
        if GPIO.input(Sensor11[0]) == GPIO.HIGH:
            print("Alerting on Sensor11")
            Sensor11[2], Sensor11[3] = alert(Sensor11)
        #else:
         #   print("No leak detected on Sensor11")
        if GPIO.input(Sensor12[0]) == GPIO.HIGH:
            print("Alerting on Sensor12")
            Sensor12[2], Sensor12[3] = alert(Sensor12)
        #else:
         #   print("No leak detected on Sensor12")
        if GPIO.input(Sensor13[0]) == GPIO.HIGH:
            print("Alerting on Sensor13")
            Sensor13[2], Sensor13[3] = alert(Sensor13)
        #else:
         #   print("No leak detected on Sensor13")
        if GPIO.input(Sensor14[0]) == GPIO.HIGH:
            print("Alerting on Sensor14")
            Sensor14[2], Sensor14[3] = alert(Sensor14)
        #else:
         #   print("No leak detected on Sensor14")
        if GPIO.input(Sensor15[0]) == GPIO.HIGH:
            print("Alerting on Sensor15")
            Sensor15[2], Sensor15[3] = alert(Sensor15)
        #else:
         #   print("No leak detected on Sensor15")
        if GPIO.input(Sensor16[0]) == GPIO.HIGH:
            print("Alerting on Sensor16")
            Sensor16[2], Sensor16[3] = alert(Sensor16)
        #else:
         #   print("No leak detected on Sensor16")
        if GPIO.input(Sensor17[0]) == GPIO.HIGH:
            print("Alerting on Sensor17")
            Sensor17[2], Sensor17[3] = alert(Sensor17)
        #else:
         #   print("No leak detected on Sensor17")

        ResetPins()
        
        time.sleep(0.05)
        

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()