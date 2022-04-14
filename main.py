from tkinter import Button
import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

button = 4

global lastTime
lastTime = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN)

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

def alert(al):
    global lastTime
    if al == "True" and time.time() - lastTime > 60:
        lastTime = time.time()
        send_email("tyleer253@gmail.com", "Leak Detected", "Leak Detected")
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

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()