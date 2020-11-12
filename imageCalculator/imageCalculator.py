# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:26:33 2020

@author: Sajjad
"""

from PIL import Image, ImageTk
import sys
import skimage.io
import skimage.viewer
import numpy as np


def imgTry1():
    im = Image.open(r'C:\Users\Sajjad\Desktop\tree.jpg')
    im2 = Image.open(r'C:\Users\Sajjad\Desktop\mountains.jpg')
    im = im.convert('RGB')
    im2 = im.convert('RGB')
    r, g, b = im.split()
    rr, gg, bb = im2.split()
    r = r.point(lambda i: i * 1.5)
    out = Image.merge('RGB', (r, g, b))
    out.show()
    
    

def imgTry2():
    img = skimage.io.imread(r'C:\Users\Sajjad\Desktop\tree.jpg')
    viewer = skimage.viewer.ImageViewer(img)
    viewer.show()
    img[img < 128] = 0
    viewer = skimage.viewer.ImageViewer(img)
    viewer.view()
    
    
def pixelCreation():
    import numpy as np
    width=1 
    height=1
    array = np.zeros([height, width, 3], dtype=np.uint8)
    array[:,:] = [255,128,0]
    img = Image.fromarray(array)
    img.save(r'C:\Users\Sajjad\Desktop\savedImg.jpg')
    print("image saved!")
    


















fileLocation1 = ""
fileLocation2 = ""
selectedOp = ""

    
    
def imageDivide(array, array2):
    array3 = np.ceil(np.divide(array, array2, out=np.zeros_like(array), where = array2!=0))
    newArray = np.array(array3, np.uint8)
    return newArray

def imageAdd(array, array2):
    array3 = np.add(array, array2)
    newArray = np.array(array3, np.uint8)
    return newArray

def imageSubtract(array, array2):
    array3 = np.subtract(array, array2)
    newArray = np.array(array3, np.uint8)
    return newArray

def imageMultiply(array, array2):
    array3 = np.multiply(array, array2)
    newArray = np.array(array3, np.uint8)
    return newArray
    

def imgArrayShape():
    
    img = Image.open(r'C:\Users\Sajjad\Desktop\tree.jpg')
    #img = Image.open(fileLocation1)
    array = np.array(img, dtype=np.float64)
    
    #array = array.transpose(2,0,1).reshape(3,-1)
    print(array.shape)
    print(array[:10,:10])      
    
    print("----------------------------")
    
    img2 = Image.open(r'C:\Users\Sajjad\Desktop\mountains.jpg')
    #img2 = Image.open(fileLocation2)
    array2 = np.array(img2, dtype=np.float64)
    print(array2.shape)
    print(array2[:10,:10])
    
    print("----------------------------")
    
    #array3 = np.ceil(np.divide(array, array2, out=np.zeros_like(array), where = array2!=0))
    #newArray = np.array(array3, np.uint8)
    
    #newArray = imageMultiply(array, array2)
    selectedOp = tkvar.get()
    print("performing opeartion: ", selectedOp)
    
    if (selectedOp == "Add"):
        newArray = imageAdd(array, array2)
    elif (selectedOp == "Subtract"):
        newArray = imageSubtract(array, array2)
    elif (selectedOp == "Multiply"):
        newArray = imageMultiply(array, array2)
    elif (selectedOp == "Divide"):
        newArray = imageDivide(array, array2)
        
    print(newArray.shape)
    print(newArray[:10,:10])
    
    img = Image.fromarray(newArray)
    img.save(r"C:\Users\Sajjad\Desktop\cgecking10.jpg")

#imgArrayShape()



def browse1(master):
    from tkinter import filedialog
    print("hello browse")
    master.filename = filedialog.askopenfilename(initialdir="C:/Users/Sajjad/Desktop", title="Select image", filetypes=(("all files", "*.*"), ("png files", "*.png"), ("JPEG files", "*.jpg")))
    fileLocation1 = master.filename
    print(fileLocation1)
    labelfl1 = tk.Label(master, text = fileLocation1)
    labelfl1.place(x=400, y=40)
    img = Image.open(fileLocation1)
    photo = ImageTk.PhotoImage(img.resize((190,108)))
    newlabel = tk.Label(image=photo)
    newlabel.image = photo
    newlabel.place(x=700, y=10)
    #return fileLocation1

def browse2(master):
    from tkinter import filedialog
    print("hello browse")
    master.filename = filedialog.askopenfilename(initialdir="C:/Users/Sajjad/Desktop", title="Select image", filetypes=(("all files", "*.*"), ("png files", "*.png"), ("JPEG files", "*.jpg")))
    fileLocation2 = master.filename
    print(fileLocation2)
    labelfl2 = tk.Label(master, text = fileLocation2)
    labelfl2.place(x=400, y=250)
    img = Image.open(fileLocation2)
    photo = ImageTk.PhotoImage(img.resize((190,108)))
    newlabel = tk.Label(image=photo)
    newlabel.image = photo
    newlabel.place(x=700, y=150)
    #return fileLocation2






#def createGui():
import tkinter as tk
master = tk.Tk()

canvas_width = 1000
canvas_height = 600
w = tk.Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

label = tk.Label(master, text = "Select two images")
label.place(x=10, y=10)

label1 = tk.Label(master, text = "Enter path or browse")
label1.place(x=10, y=40)
entry1 = tk.Entry(master, width=25)
entry1.place(x=130, y=40)
button1 = tk.Button(master, text = "Browse...", command = lambda: browse1(master))
button1.place(x=300, y=35)

label2 = tk.Label(master, text = "Enter path or browse")
label2.place(x=10, y=90)
entry2 = tk.Entry(master, width=25)
entry2.place(x=130, y=90)
button2 = tk.Button(master, text = "Browse...", command = lambda: browse2(master))
button2.place(x=300, y=85)

label3 = tk.Label(master, text = "Select an opeartion to be performed on the images")
label3.place(x=10, y=150)

tkvar = tk.StringVar(master)
choices = {'Add', 'Subtract', 'Multiply', 'Divide'}
tkvar.set('Add')
popupMenu = tk.OptionMenu(master, tkvar, *choices)
popupMenu.place(x=320, y=145)



selectedOp = tkvar.get()
performOpButton = tk.Button(master, text = "Perform Operation", command = lambda: imgArrayShape())
performOpButton.place(x=320, y=190)



tk.mainloop()

#createGui()







#https://stackoverflow.com/questions/32838802/numpy-with-python-convert-3d-array-to-2d
#https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/
#https://datacarpentry.org/image-processing/aio/index.html
#https://homepages.inf.ed.ac.uk/rbf/HIPR2/pixmult.htm
#https://stackoverflow.com/questions/26248654/how-to-return-0-with-divide-by-zero
#https://stackoverflow.com/questions/48948308/cant-use-on-numpy-array










