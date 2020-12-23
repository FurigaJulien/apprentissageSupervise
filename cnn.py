import tensorflow as tf 
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
from PIL import ImageGrab
import cv2 as cv


model = tf.keras.models.load_model('C:/Users/julie/Desktop/Microsoft/Apprentissage supervisé/model/noew')

lastx, lasty = 0, 0
 
def xy(event):
    "Takes the coordinates of the mouse when you click the mouse"
    global lastx, lasty
    lastx, lasty = event.x, event.y
 
 
def addLine(event):
    """Creates a line when you drag the mouse
    from the point where you clicked the mouse to where the mouse is now"""
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y),width=15,capstyle='round')
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y
 
def save():
    x=root.winfo_rootx()+canvas.winfo_x()
    y=root.winfo_rooty()+canvas.winfo_y()
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    return ImageGrab.grab((x, y, x1, y1))
    
def guess():

    im=np.array(save())
    im=cv.resize(im,(28,28))
    im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    im = cv.bitwise_not(im)
    im=im.astype('float')/255
    y=model.predict_classes(im.reshape(1,28,28,1))
    label.config(text=str(y[0]))



    
   


def reset():
    canvas.delete('all')
     

    
root = tk.Tk()
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = tk.Canvas(root,bg='white')
canvas.pack()
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
tk.Button(root,text='Reset',command=reset).pack()
tk.Button(root,text="Deviner le chiffre",command=guess).pack()
label=tk.Label(root)
label.pack()
 


 
root.mainloop()