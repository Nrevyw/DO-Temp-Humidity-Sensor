import time
import os
import sys
import csv
import datetime as dt
import serial
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import logging.config

root = Tk()
root.geometry('1200x700+200+100')
root.title('Temperature/Humidity Sensor')
root.state('zoomed')
root.config(background='#fafafa')



## Define functions

def animate(i,xar,yar):
    global loglocation
    data = arduino.readline()
    decoded_values = str(data[0:len(data)].decode("utf-8"))
    list_values = decoded_values.split('x')
    for item in list_values:
        list_in_floats.append(float(item))

    # IF DIFFERENT UNIT REQUIRED, (0=C,1=K,2=F)
    yvalue = list_in_floats[0]

    yar.append(yvalue)
    xar.append(dt.datetime.now().strftime('%H:%M:%S'))
    xvalue = xar[-1]
    xar = xar[-20:]
    yar = yar[-20:]
    ax1.clear()
    ax1.plot(xar, yar)


    if record == True:
        # EDIT PATH OF FILE
        path_to_script = os.path.dirname(os.path.abspath("__file__"))
        my_filename = os.path.join(path_to_script, r"templog.csv")
        if loglocation==True:
            print('Log found at '+my_filename)
            loglocation = False
        with open(my_filename, "a") as log:
            log.write("{0},{1}\n".format(xvalue,yvalue))


    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    plt.xlabel('Time (HH:MM:SS)')

    list_in_floats.clear()
    list_values.clear()


def switch():
    global record
    if record==False:
        record = True
        on_button.config(text = 'Recording, click to Stop Log')

    else:
        record = False
        on_button.config(text = 'Start Log')


## Main Code

record = False
loglocation = True

on_button = Button(master = root,command = switch,text = 'Start Log')
on_button.pack()

xar = []
yar = []

style.use('ggplot')
fig = plt.figure(figsize=(14, 4.5), dpi=100)
ax1 = fig.add_subplot(1, 1, 1)
line, = ax1.plot(xar, yar, 'r', marker='o')

# EDIT PORT NUMBER AND BAUD RATE
arduino = serial.Serial('COM3', 9600)

list_values = []
list_in_floats = []
plotcanvas = FigureCanvasTkAgg(fig, root)
plotcanvas.get_tk_widget().pack()
ani = animation.FuncAnimation(fig, animate, fargs=(xar, yar), interval=30000)       # ABLE TO CHANGE SAMPLING RATE

root.mainloop()