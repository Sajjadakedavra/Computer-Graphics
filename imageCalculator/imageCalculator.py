# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:26:33 2020

@author: Sajjad
"""

from PIL import Image 
import sys
import skimage.io
import skimage.viewer

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
    
    
def imgArrayShape():
    import numpy as np
    img = Image.open(r'C:\Users\Sajjad\Desktop\tree.jpg')
    array = np.array(img)
    #array = array.transpose(2,0,1).reshape(3,-1)
    print(array.shape)
    print(array[:3,:3])      
    #array[:200,:400] = [255, 128, 0]
    print("----------------------------")
    img2 = Image.open(r'C:\Users\Sajjad\Desktop\mountains.jpg')
    array2 = np.array(img2)
    
    array3 = np.add(array, array2) #add, multiply, subtract, divide
    print(array3[:3,:3])
    
    img = Image.fromarray(array3)
    img.save(r"C:\Users\Sajjad\Desktop\cgecking.jpg")

imgArrayShape()
    





#https://stackoverflow.com/questions/32838802/numpy-with-python-convert-3d-array-to-2d
#https://www.pythoninformer.com/python-libraries/numpy/numpy-and-images/
#https://datacarpentry.org/image-processing/aio/index.html
#https://homepages.inf.ed.ac.uk/rbf/HIPR2/pixmult.htm











