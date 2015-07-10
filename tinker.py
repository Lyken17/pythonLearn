#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import os
import math
import datetime,time

master = Tk()

w = Canvas(master, width=800, height=600)
w.pack()

x = 10

#start = time.time()

string = "release"

def change():
	global x
	global string
	#global start
	#start = time.time()
	#end = start
	w.coords(i, 200, 200, 200 + 50 * math.cos(math.radians(x)),200 + 50 * math.sin(math.radians(x)))
	x += 10
	string = "P"
	print x
	c.flash()

	#print start

def release():
    w.delete(i)

b = Button(master, text="change",command=change)
b.pack()

c = Button(master, text=string,command=release)
c.pack()


i = w.create_line(0, 0, 0, 0)
w.create_text(100,100,text="Hello World")

 # change coordinates
w.itemconfig(i, fill="blue") # change color
#w.coords()
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

#w.create_rectangle(100, 50, 300, 150, fill="#FFF")

mainloop()
