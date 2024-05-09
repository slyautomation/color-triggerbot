import ctypes
import winsound
import random
import time
import cv2
import keyboard
import numpy as np
import serial
from mss import mss
monitor = {"top": 400, "left": 850, "width": 250, "height":200}
sct = mss()

# ====== CHANGE THESE ======
port = 'COM12'
color_to_use = 'red'
# ==========================

if color_to_use == 'purple':
    lpoint = [135, 35, 20]
    upoint = [155, 255, 255]
    
if color_to_use == 'yellow':
    lpoint = [22, 46, 255]
    upoint = [38, 255, 255]

if color_to_use == 'red':
    lpoint = [0, 95, 95]
    upoint = [4, 235, 255]

timeBeginPeriod = ctypes.windll.winmm.timeBeginPeriod #new
timeBeginPeriod(1) #new

baudrate = 1152000
pt= (110,138)
arduino = serial.Serial(port=port, baudrate=baudrate, timeout=.1)

print("Pistol: OFF")
print("Script: ON")
print("Trigger Bot: ON")

lower = np.array(lpoint, dtype="uint8")
upper = np.array(upoint, dtype="uint8")
kernel = np.ones((4, 3), np.uint8)


def play_beep(frequency, duration):
    winsound.Beep(frequency, duration)

def triggerMain():
    global pistol, auto
    while True:
        #start_time = time.time()
        if keyboard.is_pressed('F1'):
            pistol = True
            print("Pistol: ON")
            play_beep(1000, 250)
        if keyboard.is_pressed('F2'):
            pistol = False
            auto = True
            print("AutoRifle: ON")
            play_beep(1000, 250)
            time.sleep(0.1)
            play_beep(1200, 250)
        if keyboard.is_pressed('F3'):
            pistol = False
            auto = False
            print("Triggerbot Off")
            play_beep(1000, 250)
            time.sleep(0.1)
            play_beep(800, 250)
        image = sct_screenshot()
        try:
            roi_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(roi_hsv, lower, upper)
            dilated = cv2.dilate(mask, kernel, iterations=3)
            contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            #cv2.drawContours(image, contours, -1, (255, 0, 0), 1)
            trigger = -1.0
            for c in contours:
                trigger = cv2.pointPolygonTest(c, pt, False)
                if trigger > 0:
                    #end_time = time.time()
                    #print("MAND: ", end_time - start_time)
                    arduino_click()
                    return
        except:
            pass
        #cv2.imshow("images", image)
        #cv2.waitKey(5)

def arduino_click():
    global arduino, pistol, deagle, auto
    if pistol or auto:
        arduino.write('left'.encode())
    if pistol:
        c = random.uniform(0.35, 0.40)
        time.sleep(c)
    if auto:
        c = random.uniform(0.19, 0.23)
        time.sleep(c)
def sct_screenshot():
    global sct
    try:
        img = np.array(sct.grab(monitor))
        return img
    except:
        sct = mss()
while True:
    triggerMain()
