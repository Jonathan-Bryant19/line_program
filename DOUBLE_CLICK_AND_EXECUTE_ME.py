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
# root.geometry("800x600")
root.attributes('-fullscreen', True)

# Sets the background color
root.configure(bg="black")

# NEXT WINDOW heading
row_heading_labels = []
row_heading_labels.append(Label(root, text="PROCEED TO WINDOW", font=("Chalkduster", 100), fg="red", bg="black"))
row_heading_labels[0].pack(pady=(30, 30))

# Create number frames to hold the rows of numbers
number_frames = []
number_frames.append(Frame(root, bg="black"))
number_frames.append(Frame(root, bg="black"))

# Number labels
number_labels = {}
for i in range(1, 12):
    frame = number_frames[0 if i < 7 else 1]
    number_labels[i] = dict()
    number_labels[i]['label'] = Label(frame, text=" %s " % i, font=("SignPainter", 150), borderwidth=2,
                             relief="solid", bg="black", fg="white")
    number_labels[i]['label'].pack(padx=15, side=LEFT)
    number_labels[i]['timer'] = None

# Pack the new number frame under "NEXT WINDOW" label
number_frames[0].pack()

# Add corn row lol
corn_frame = Frame(root, bg="black")
corn_photo = PhotoImage(file="corn_row.png")
corn = Label(corn_frame, image=corn_photo, bg="black")
corn.pack(side=LEFT)
corn_frame.pack(pady=(40, 0))

# Create a Frame to contain "AROUND CORNER" and the arrow image
heading_frame = Frame(root, bg="black")

# AROUND CORNER heading
row_heading_labels.append(Label(heading_frame, text="AROUND CORNER", font=("Chalkduster", 100),fg="orange", bg="black"))
row_heading_labels[1].pack(ipady=30, side=LEFT)

# Add arrow to indicate "AROUND CORNER"
photo = PhotoImage(file="arrow.png")
arrow = Label(heading_frame, image=photo, bg="black")
arrow.pack(side=LEFT)

# Pack the "AROUND CORNER" Frame
heading_frame.pack()

# Pack the new number frame under "NEXT WINDOW" label
number_frames[1].pack()

# Global variables
my_counter = 25  # Sets the counter for how many times a label flashes

# NEXT WINDOW flashing method
row_label_colors = [["red", "white"],["orange", "white"]]
def flash_row_label(row, counter=0):
    row_colors = row_label_colors[row]
    row_heading_labels[row]['fg'] = row_colors[counter % len(row_colors)]

    if counter <= my_counter:
        # set a new timer and save the ID
        root.after(300, flash_row_label, row, counter+1)
    else:
        # Change back to default
        row_heading_labels[row]['fg'] = row_colors[0]


flashing_colors = ["black", "white"]
# Methods to animate the flashing for each number
def flash_number(num, counter=0):    
    number_label = number_labels[num]

    if counter == 0:
        flash_row_label(0 if num < 7 else 1)

    number_label['label']['bg'] = flashing_colors[counter % len(flashing_colors)]
    number_label['label']['fg'] = flashing_colors[(counter + 1) % len(flashing_colors)]


    if counter <= my_counter:
        # set a new timer and save the ID
        number_label['timer'] = root.after(300, flash_number, num, counter+1)

# Key bindings to use keyboard
keymaps = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 10,
    '-': 11
}

for k in keymaps:
    root.bind(k, lambda x: flash_number(keymaps[x.char]))

# GPIO bindings
gpio_mappings = {
	8: 1,
	10: 2,
	12: 3,
	16: 4,
	18: 5,
	22: 6,
	24: 7,
	26: 8,
	11: 9,
	13: 10,
	7: 11
}

# # Setup GPIO functions
GPIO.setwarnings(False) # Ignores warnings
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin, num in gpio_mappings.items():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=lambda x: flash_number(gpio_mappings[x]), bouncetime=300)


# Resize window when 'esc' is pressed
def resize_window(event):
    GPIO.cleanup()
    root.destroy()
root.bind("<Escape>", resize_window)

# Main program loop
root.mainloop()
