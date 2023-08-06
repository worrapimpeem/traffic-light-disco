# Import the required libraries
from tkinter.constants import END, LEFT
from tkinter import TOP, X, Button, Label, ttk
import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk


win = Tk()

win.geometry("500x350")
win.configure(background='#EEEEEE')


def discoo_show():
    if running == 1:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)

        GPIO.output(21, 0)
        GPIO.output(20, 1)
        GPIO.output(16, 1)
        time.sleep(1)

        GPIO.output(21, 1)
        GPIO.output(20, 0)
        GPIO.output(16, 1)
        time.sleep(1)

        GPIO.output(21, 1)
        GPIO.output(20, 1)
        GPIO.output(16, 0)
        time.sleep(1)
        GPIO.cleanup()

    win.after(1000, discoo_show)


def stop_show():
    if running == 3:
        GPIO.cleanup()

    win.after(1000, stop_show)


def sloww_show():
    if running == 2:
        GPIO.setmode(GPIO.BCM)

    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

    pwm = GPIO.PWM(21, 100)   # Initialize PWM on pwmPin 100Hz frequency
    pwm1 = GPIO.PWM(20, 100)
    pwm2 = GPIO.PWM(16, 100)

    dc1 = 0                               # set dc variable to 0 for 0%
    dc2 = 0
    dc3 = 0
    pwm.start(dc1)
    pwm1.start(dc2)
    pwm2.start(dc3)
    # Loop until Ctl C is pressed to stop.
    for dc in range(0, 101, 1):    # Loop 0 to 100 stepping dc by 5 each loop
        pwm.ChangeDutyCycle(dc)
        pwm1.ChangeDutyCycle(dc)
        pwm2.ChangeDutyCycle(dc)
        # wait .05 seconds at current LED brightness
        time.sleep(0.05)
    print(dc)
    for dc in range(95, 0, -1):    # Loop 95 to 5 stepping dc down by 5 each loop
        pwm.ChangeDutyCycle(dc)
        pwm1.ChangeDutyCycle(dc)
        pwm2.ChangeDutyCycle(dc)
        # wait .05 seconds at current LED brightness
        time.sleep(0.05)
    print(dc)
    GPIO.cleanup()

    win.after(1000, sloww_show)


# Define a function to discoo the loop
def on_discoo():
    global running
    running = 1
    if running == 1:
        discoo_show()

# Define a function to slow the loop


def on_slow():
    global running
    running = 2
    if running == 2:
        sloww_show()

# Define a function to stop the loop


def on_stop():
    global running
    running = 3
    if running == 3:
        stop_show()


canvas = Canvas(win, bg="#A0C3D2", width=600, height=60)
canvas.create_text(
    180, 40, text="Click to open disco or slow light", font=('', 13))
canvas.pack()

discoo = ttk.Button(win, text="discoo", command=on_discoo)
discoo.pack(padx=10, pady=30)

c_slow = ttk.Button(win, text="slow", command=on_slow)
c_slow.pack(padx=10, pady=32)

stop = ttk.Button(win, text="Stop", command=on_stop)
stop.pack(padx=10, pady=34)

win.mainloop()
