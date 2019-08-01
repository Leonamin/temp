#-*- coding: utf-8 -*-
# Importing Libraries

import RPi.GPIO as GPIO
import time
from Tkinter import *
import tkFont
import cv2                  # opencv 카메라 제어
import threading            # 멀티 스레딩
from PIL import Image, ImageTk

# Libraries Imported successfully

# Raspberry Pi 3 Pin Settings

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # We are accessing GPIOs according to their physical location
pins = [14,15,17,4,23,24,27,22]

GPIO.setup(pins, GPIO.OUT) # We have set our LED pin mode to output
GPIO.output(pins, GPIO.HIGH) # When it will start then LED will be OFF

# Raspberry Pi 3 Pin Settings

# tkinter GUI basic settings

Gui = Tk()
Gui.title("PROJECT AVATAR V.1")
Gui.config(background= "#1E1E1E")
Gui.minsize(800,400)
Font1 = tkFont.Font(family = 'Helvetica', size = 24, weight = 'bold')

# tkinter simple GUI created

# image Label setting

# Flag variables creating
killCamFlag = 0
camFlag = 1

# Funtion for Buttons started here

'''
for pin in pins :
 #setting the GPIO to HIGH or 1 or true
 GPIO.output(pin,  GPIO.HIGH)
 #wait 0,5 second
 time.sleep(0.5)
 #setting the GPIO to LOW or 0 or false
 GPIO.output(pin,  GPIO.LOW)
 #wait 0,5 second
 time.sleep(0.5)

 #Checking if the current relay is running and printing it 
 if not GPIO.input(pin) : 
  print("Pin "+str(pin)+" is working" )
'''  

def UP():
    GPIO.output(14, GPIO.LOW) # UP button pressed 
    Text2 = Label(Gui,text='     UP     ', font = Font1, bg = '#1E1E1E', fg='white', padx = 0)
    Text2.grid(row=0,column=1)
    time.sleep(0.5)
    GPIO.output(14, GPIO.HIGH)


def DOWN():
    GPIO.output(15, GPIO.LOW) # DOWN button pressed 
    Text2 = Label(Gui,text='  DOWN  ', font = Font1, bg = '#1E1E1E', fg='white', padx = 0)
    Text2.grid(row=0,column=1)
    time.sleep(0.5)
    GPIO.output(15, GPIO.HIGH)

def STOP():
    GPIO.output(17, GPIO.LOW) # STOP button pressed 
    Text2 = Label(Gui,text='  STOP  ', font = Font1, bg = '#1E1E1E', fg='white', padx = 0)
    Text2.grid(row=0,column=1)
    time.sleep(0.5)
    GPIO.output(17, GPIO.HIGH)

def DOOR():
    GPIO.output(27, GPIO.LOW)
    Text2 = Label(Gui,text='Sensor OFF', font = Font1, bg = '#1E1E1E', fg='white', padx = 0)
    Text2.grid(row=0,column=1)

def DOOR2():
    GPIO.output(27, GPIO.HIGH)
    Text2 = Label(Gui,text='Sensor ON', font = Font1, bg = '#1E1E1E', fg='white', padx = 0)
    Text2.grid(row=0,column=1)

def REBOOT():
    GPIO.output(4, GPIO.LOW) # Reboot button pressed 
    Text2 = Label(Gui,text='  REBOOT  ', font = Font1, bg = '#1E1E1E', fg='white', padx = 0)
    Text2.grid(row=0,column=1)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)

def QUIT():
    print("Exit Button pressed")
    GPIO.cleanup()
    Gui.quit()

def CAMINIT():
    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)
    pass

def CAMMERA():
    if camFlag:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        imgLbl.imgtk = imgtk
        imgLbl.configure(image=imgtk)
    else:
        pass
    Gui.after(100, CAMMERA)

def CAMONOFF():
    camFlag ^= 1
    if camFlag:
        CamToggleBtn.configure(text="Off")
    else:
        CamToggleBtn.configure(text="On")
    pass

# Funtion for Buttons ended here

Text1 = Label(Gui,text='STATUS:', font = Font1, fg='#FFFFFF', bg = '#1E1E1E', padx = 20, pady = 30)
Text1.grid(row=0,column=0)

Text2 = Label(Gui,text='', font = Font1, fg='#FFFFFF', bg = '#1E1E1E', padx = 0)
Text2.grid(row=0,column=1)

Button1 = Button(Gui, text='UP', font = Font1, command = UP, bg='bisque2', height = 1, width = 10)
Button1.grid(row=1,column=0)

Button2 = Button(Gui, text='DOWN', font = Font1, command = DOWN, bg='bisque2', height = 1, width = 10)
Button2.grid(row=2,column=0)

Button3 = Button(Gui, text='STOP', font = Font1, command = STOP, bg='bisque2', height = 1, width = 10)
Button3.grid(row=3,column=0)

Button4 = Button(Gui, text='REBOOT', font = Font1, command = REBOOT, bg='bisque2', height = 1, width = 10)
Button4.grid(row=4,column=0)

Button5 = Button(Gui, text='DOORclosed', font = Font1, command = DOOR, bg='bisque2', height = 1, width = 10)
Button5.grid(row=5,column=0)

Button6 = Button(Gui, text='DOORon', font = Font1, command = DOOR2, bg='bisque2', height = 1, width = 10)
Button6.grid(row=5,column=1)

Button7 = Button(Gui, text='QUIT', font = Font1, command = QUIT, bg='bisque2', height = 1, width = 10)
Button7.grid(row=6,column=0)

Text3 = Label(Gui,text='PROJECT AVATAR', font = Font1, bg = '#1E1E1E', fg='#FFFFFF', padx = 5, pady = 10)
Text3.grid(row=7,columnspan=5)


imgLbl = Label(Gui, text="Img")
imgLbl.grid(row = 0, column= 1)

CamToggleBtn = Button(Gui, text='On', font = Font1, command = CAMONOFF, bg='bisque2', height = 1, width = 10)
CamToggleBtn.grid(row=6, column=1)

CAMINIT()
CAMMERA()
Gui.mainloop()