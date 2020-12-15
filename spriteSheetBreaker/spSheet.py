# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:16:42 2020

@author: Sajjad
"""

import PIL
import time
from PIL import Image, ImageTk
print("import successful")

image = PIL.Image.open(r"C:\Users\Sajjad\Desktop\Sprite-sheet.jpg")

width, height = image.size

print (width, height)

widthGap = width/5
heightGap = height/2

import tkinter as tk
master = tk.Tk()
master.title("Sprite Sheet Breaker")

canvas_width = 1000
canvas_height = 600
w = tk.Canvas(master, width=canvas_width, height=canvas_height)
w.pack()


button2 = tk.Button(master, text = "Start...", command = lambda: spriteSheetBreaker(check, i, j, k))
button2.place(x=300, y=85)



tk.mainloop()

'''
im1 = image.crop(((width/5)*2,0,(width/5)*3,height/2))
im1.show()
'''

var_holder={}
i=0
#previousWidth = width/5
j = 0
k = 1
check = 0

def spriteSheetBreaker(check, i, j, k):
    while (check < width):
        previousWidth = int((width//5) * j)
        toNewWidth = int (width//5) * k
        check = toNewWidth
        print("width gap is:{0} and {1}".format(previousWidth, toNewWidth))
        var_holder['my_var_'+str(i)] = image.crop((previousWidth, 0, toNewWidth, heightGap)) 
        j = j + 1
        k = k + 1
        #widthGap = widthGap + widthGap/5
        #var_holder['my_var_'+str(i)].show()
        var_holder['my_var_'+str(i)].save(r"C:\Users\Sajjad\Desktop\breaker{0}.jpg".format(i))
        i=i+1
    
    #timed()

    
    
    
#spriteSheetBreaker(check, i, j, k)    





    
def timed():
    print("begin timer")
    measure1 = time.time()
    measure2 = time.time()
    
    count = 1
    index = 0
    
    while count < 11:
        if measure2 - measure1 >= 2:
            print("two seconds")
            
            img = Image.open(r"C:\Users\Sajjad\Desktop\breaker{0}.jpg".format(index))
            photo = ImageTk.PhotoImage(img)
            newLabel = tk.Label(image=photo)
            newLabel.image = photo
            newLabel.place(500, 200)
            
            measure1 = measure2
            measure2 = time.time()
            count += 1
            index += 1
        else:
            measure2 = time.time()
    
    print("done")










    
