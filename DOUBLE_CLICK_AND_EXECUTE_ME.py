#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:42:37 2020

@author: jonathanbryant 
"""

from tkinter import *
from PIL import ImageTk, Image
import RPi.GPIO as GPIO

# Create window and give it a title
root = Tk()
root.title("Dell'Osso Line Program")

# Set window size
#root.geometry("1920x1080")
root.attributes('-fullscreen', True)

# Sets the background color
root.configure(bg="black")

# NEXT WINDOW heading
label_heading = Label(root, text="PROCEED TO WINDOW", font=("Chalkduster", 100),
                      fg="red", bg="black") 

# Timer for NEXT WINDOW
label_heading.timer = ' '

# Pack label_heading
label_heading.pack(pady=(30, 30))

# Create a Frame to contain the numbers 1 through 6
number_frame = Frame(root, bg="black")

# Number 1 through 6
nmbr_1 = Label(number_frame, text =" 1 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_1.pack(padx=15, side=LEFT)
nmbr_2 = Label(number_frame, text =" 2 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_2.pack(padx=15, side=LEFT)
nmbr_3 = Label(number_frame, text =" 3 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_3.pack(padx=15, side=LEFT)
nmbr_4 = Label(number_frame, text =" 4 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_4.pack(padx=15, side=LEFT)
nmbr_5 = Label(number_frame, text =" 5 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_5.pack(padx=15, side=LEFT)
nmbr_6 = Label(number_frame, text =" 6 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_6.pack(padx=15, side=LEFT)

# Pack the new number frame under "NEXT WINDOW" label
number_frame.pack()

# Add corn row lol
corn_frame = Frame(root, bg="black")
corn_photo = PhotoImage(file="corn_row.png")
corn = Label(corn_frame, image=corn_photo, bg="black")
corn.pack(side=LEFT)
corn_frame.pack(pady=(40,0))

# Create a Frame to contain "AROUND CORNER" and the arrow image
heading_frame = Frame(root, bg="black")

# AROUND CORNER heading
label_heading2 = Label(heading_frame, text="AROUND CORNER", font=("Chalkduster", 100),
                      fg="orange", bg="black")
label_heading2.pack(ipady=30, side=LEFT)

# Timer for AROUND CORNER
label_heading2.timer = ' '

# Add arrow to indicate "AROUND CORNER"
photo = PhotoImage(file="arrow.png")
arrow = Label(heading_frame, image=photo, bg="black")
arrow.pack(side=LEFT)

# Pack the "AROUND CORNER" Frame
heading_frame.pack()

# Create a Frame to contain the numbers 7 through 11
number_frame2 = Frame(root, bg="black")

# Number 7 through 11
nmbr_7 = Label(number_frame2, text =" 7 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_7.pack(padx=15, side=LEFT)
nmbr_8 = Label(number_frame2, text =" 8 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_8.pack(padx=15, side=LEFT)
nmbr_9 = Label(number_frame2, text =" 9 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_9.pack(padx=15, side=LEFT)
nmbr_10 = Label(number_frame2, text =" 10 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_10.pack(padx=15, side=LEFT)
nmbr_11 = Label(number_frame2, text =" 11 ", font=("SignPainter", 150), borderwidth=2,
               relief="solid", bg="black", fg="black")
nmbr_11.pack(padx=15, side=LEFT)

# Pack the new number frame under "NEXT WINDOW" label
number_frame2.pack()

# Create timers so that current functions cancel when a new one is called
nmbr_1.timer = ' '
nmbr_2.timer = ' '
nmbr_3.timer = ' '
nmbr_4.timer = ' '
nmbr_5.timer = ' '
nmbr_6.timer = ' '
nmbr_7.timer = ' '
nmbr_8.timer = ' '
nmbr_9.timer = ' '
nmbr_10.timer = ' '
nmbr_11.timer = ' '

# Global variables
my_counter = 25 # Sets the counter for how many times a label flashes

# NEXT WINDOW flashing method
def next_window_flash(event, h1counter=0):
    if (label_heading['fg'] == "red"):
            label_heading['fg'] ="white"
    elif (label_heading['fg'] == "white"):
        label_heading['fg'] = "red"
    if h1counter < int(my_counter): # How many times it will flash
        root.after_cancel(label_heading.timer) # cancel any currently running timers
        label_heading.timer = root.after(300, next_window_flash, event, h1counter+1)  # set a new timer and save the ID
    elif h1counter >= int(my_counter): # How many times it will flash
        label_heading['bg'] ="black"
        label_heading['fg'] ="red"

def around_corner_flash(event, h2counter=0):
    if (label_heading2['fg'] == "orange"):
        label_heading2['fg'] ="white"
    elif (label_heading2['fg'] == "white"):
        label_heading2['fg'] = "orange"
    if h2counter < int(my_counter): # How many times it will flash
        root.after_cancel(label_heading2.timer) # cancel any currently running timers
        label_heading2.timer = root.after(300, around_corner_flash, event, h2counter+1)  # set a new timer and save the ID
    elif h2counter >= int(my_counter): # How many times it will flash
        label_heading2['bg'] ="black"
        label_heading2['fg'] ="orange"

# Methods to animate the flashing for each number
def flash_once1(event, counter=0):
    if (counter == 0):
        next_window_flash(event)
    if (nmbr_1['bg'] == "white"):
        nmbr_1['bg'] ="black"
        nmbr_1['fg'] ="white"
    elif (nmbr_1['bg'] == "black"):
        nmbr_1['bg'] = "white"
        nmbr_1['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_1.timer) # cancel any currently running timers
        nmbr_1.timer = root.after(300, flash_once1, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_1['bg'] ="black"
        nmbr_1['fg'] ="black"
#root.bind("1", flash_once1)

def flash_once2(event, counter=0):
    if (counter == 0):
        next_window_flash(event)
    if (nmbr_2['bg'] == "white"):
        nmbr_2['bg'] ="black"
        nmbr_2['fg'] ="white"
    elif (nmbr_2['bg'] == "black"):
        nmbr_2['bg'] = "white"
        nmbr_2['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_2.timer) # cancel any currently running timers
        nmbr_2.timer = root.after(300, flash_once2, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_2['bg'] ="black"
        nmbr_2['fg'] ="black"
root.bind("2", flash_once2)

def flash_once3(event, counter=0):
    if (counter == 0):
        next_window_flash(event)
    if (nmbr_3['bg'] == "white"):
        nmbr_3['bg'] ="black"
        nmbr_3['fg'] ="white"
    elif (nmbr_3['bg'] == "black"):
        nmbr_3['bg'] = "white"
        nmbr_3['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_3.timer) # cancel any currently running timers
        nmbr_3.timer = root.after(300, flash_once3, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_3['bg'] ="black"
        nmbr_3['fg'] ="black"
root.bind("3", flash_once3)

def flash_once4(event, counter=0):
    if (counter == 0):
        next_window_flash(event)
    if (nmbr_4['bg'] == "white"):
        nmbr_4['bg'] ="black"
        nmbr_4['fg'] ="white"
    elif (nmbr_1['bg'] == "black"):
        nmbr_4['bg'] = "white"
        nmbr_4['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_4.timer) # cancel any currently running timers
        nmbr_4.timer = root.after(300, flash_once4, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_4['bg'] ="black"
        nmbr_4['fg'] ="black"
root.bind("4", flash_once4)

def flash_once5(event, counter=0):
    if (counter == 0):
        next_window_flash(event)
    if (nmbr_5['bg'] == "white"):
        nmbr_5['bg'] ="black"
        nmbr_5['fg'] ="white"
    elif (nmbr_5['bg'] == "black"):
        nmbr_5['bg'] = "white"
        nmbr_5['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_5.timer) # cancel any currently running timers
        nmbr_5.timer = root.after(300, flash_once5, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_5['bg'] ="black"
        nmbr_5['fg'] ="black"
root.bind("5", flash_once5)

def flash_once6(event, counter=0):
    if (counter == 0):
        next_window_flash(event)
    if (nmbr_6['bg'] == "white"):
        nmbr_6['bg'] ="black"
        nmbr_6['fg'] ="white"
    elif (nmbr_6['bg'] == "black"):
        nmbr_6['bg'] = "white"
        nmbr_6['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_6.timer) # cancel any currently running timers
        nmbr_6.timer = root.after(300, flash_once6, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_6['bg'] ="black"
        nmbr_6['fg'] ="black"
root.bind("6", flash_once6)

def flash_once7(event, counter=0):
    if (counter == 0):
        around_corner_flash(event)
    if (nmbr_7['bg'] == "white"):
        nmbr_7['bg'] ="black"
        nmbr_7['fg'] ="white"
    elif (nmbr_7['bg'] == "black"):
        nmbr_7['bg'] = "white"
        nmbr_7['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_7.timer) # cancel any currently running timers
        nmbr_7.timer = root.after(300, flash_once7, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_7['bg'] ="black"
        nmbr_7['fg'] ="black"
root.bind("7", flash_once7)

def flash_once8(event, counter=0):
    if (counter == 0):
        around_corner_flash(event)
    if (nmbr_8['bg'] == "white"):
        nmbr_8['bg'] ="black"
        nmbr_8['fg'] ="white"
    elif (nmbr_8['bg'] == "black"):
        nmbr_8['bg'] = "white"
        nmbr_8['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_8.timer) # cancel any currently running timers
        nmbr_8.timer = root.after(300, flash_once8, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_8['bg'] ="black"
        nmbr_8['fg'] ="black"
root.bind("8", flash_once8)

def flash_once9(event, counter=0):
    if (counter == 0):
        around_corner_flash(event)
    if (nmbr_9['bg'] == "white"):
        nmbr_9['bg'] ="black"
        nmbr_9['fg'] ="white"
    elif (nmbr_9['bg'] == "black"):
        nmbr_9['bg'] = "white"
        nmbr_9['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_9.timer) # cancel any currently running timers
        nmbr_9.timer = root.after(300, flash_once9, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_9['bg'] ="black"
        nmbr_9['fg'] ="black"
root.bind("9", flash_once9)

def flash_once10(event, counter=0):
    if (counter == 0):
        around_corner_flash(event)
    if (nmbr_10['bg'] == "white"):
        nmbr_10['bg'] ="black"
        nmbr_10['fg'] ="white"
    elif (nmbr_7['bg'] == "black"):
        nmbr_10['bg'] = "white"
        nmbr_10['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_10.timer) # cancel any currently running timers
        nmbr_10.timer = root.after(300, flash_once10, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_10['bg'] ="black"
        nmbr_10['fg'] ="black"
root.bind("+", flash_once10)

def flash_once11(event, counter=0):
    if (counter == 0):
        around_corner_flash(event)
    if (nmbr_11['bg'] == "white"):
        nmbr_11['bg'] ="black"
        nmbr_11['fg'] ="white"
    elif (nmbr_7['bg'] == "black"):
        nmbr_11['bg'] = "white"
        nmbr_11['fg'] = "black"
    if counter < int(my_counter): # How many times it will flash
        root.after_cancel(nmbr_11.timer) # cancel any currently running timers
        nmbr_11.timer = root.after(300, flash_once11, event, counter+1)  # set a new timer and save the ID
    elif counter >= int(my_counter): # How many times it will flash
        nmbr_11['bg'] ="black"
        nmbr_11['fg'] ="black"
root.bind("-", flash_once11)

# Setup GPIO functions
GPIO.setwarnings(False) # Ignores warnings
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# GPIO for "1"
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 as input and set initial value to low (off)   
GPIO.add_event_detect(8,GPIO.RISING, callback=flash_once1)

# GPIO for "2"
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(10,GPIO.RISING, callback=flash_once2)

# GPIO for "3"
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(12,GPIO.RISING, callback=flash_once3)

# GPIO for "4"
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(16,GPIO.RISING, callback=flash_once4)

# GPIO for "5"
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(18,GPIO.RISING, callback=flash_once5)

# GPIO for "6"
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(22,GPIO.RISING, callback=flash_once6)

# GPIO for "7"
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(24,GPIO.RISING, callback=flash_once7)

# GPIO for "8"
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(26,GPIO.RISING, callback=flash_once8)

# GPIO for "9"
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(11,GPIO.RISING, callback=flash_once9)

# GPIO for "10"
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(13,GPIO.RISING, callback=flash_once10)

# GPIO for "11"
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
GPIO.add_event_detect(7,GPIO.RISING, callback=flash_once11)




# Resize window when 'esc' is pressed
def resize_window(event):
    GPIO.cleanup()
    root.destroy()
root.bind("<Escape>", resize_window)

# Main program loop
root.mainloop()

