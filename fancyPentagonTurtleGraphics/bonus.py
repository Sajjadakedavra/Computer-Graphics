# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:48:39 2020

@author: Sajjad
"""

import turtle
tina = turtle.Turtle()
tina.shape('turtle')
window = turtle.Screen()

tina.speed(0)



def pentagon(angle):
    for i in range(5):
       tina.forward(100) #Assuming the side of a pentagon is 100 units
       tina.right(angle) #72

def penta():
    for i in range(17):
        if (i == 10):
            tina.left(80)
        else:
            tina.left(100)
        tina.forward(90)
        tina.left(300)
        tina.forward(90)
        tina.left(300)
        tina.forward(90)
        tina.left(300)
        tina.forward(90)
        tina.left(300)
        tina.forward(90)
        tina.left(300)
        tina.forward(90)
        
       


penta()

i=0
j=0
k=l=m=n=0
'''
for i in range(5):
    tina.left(72)
    tina.forward(100)
    
tina.penup()
tina.goto(130,95)
tina.pendown()
for j in range(5):
    tina.right(72)
    tina.forward(100)
    
tina.penup()
tina.goto(120,0)
tina.pendown()
for k in range(5):
    tina.right(72)
    tina.forward(100)
'''

'''
tina.speed(0)
    
for i in range(5):
    tina.left(70)
    tina.forward(100)
tina.left(18.8)
for i in range(5):
    tina.left(70)
    tina.forward(100)
tina.left(28.8)
for i in range(5):
    tina.left(70)
    tina.forward(100)
    
 '''   
    

window.exitonclick()
turtle.done()



















