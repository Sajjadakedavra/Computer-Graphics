# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:27:58 2020

@author: Sajjad
"""

import turtle
tina = turtle.Turtle()
tina.shape('turtle')


def routineOne():
    i = 0
    j = 100
    for i in range(16):
        if (i % 4 == 0):
            j = j - 20
            
        tina.forward(j)
        tina.left(90)
        tina.forward(j)
        tina.left(90)
        tina.forward(j)
        tina.left(90)
        tina.forward(j)
        tina.left(90)
    turtle.done()



def routineTwo():
    tina.speed(0)
    i = 0
    j = 100
    
    for i in range(15):
        if (i % 2 == 0):
            j = j - 10
    
        tina.forward(j)
        tina.left(90)
        #tina.forward(j)
        #tina.left(90)
        #tina.forward(j)
    tina.hideturtle()
    turtle.done()
    
    
def routineThree():
    i = 0
    j = 0
    #tina.speed(0)
    
    tina.forward(50)
    tina.left(120)
    tina.forward(100)
    tina.left(120)
    tina.fd(100)
    tina.left(120)
    tina.fd(50)
    
    tina.left(120)
    tina.fd(50)
    
    tina.left(-120)
    tina.fd(50)
    tina.left(-120)
    tina.fd(50)
    
 
    tina.hideturtle()
    turtle.done()
    
    
def first(firstAngle):
    tina.left(firstAngle) #120
    tina.forward(50)
    tina.right(60)
    tina.fd(50)
    tina.right(120)
    tina.fd(50)
    tina.left(-60)
    tina.fd(50)
    
def routineFour():
    tina.speed(0)
    first(120)
    first(120)
    first(-240)
    
    turtle.done()
    
routineFour()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    