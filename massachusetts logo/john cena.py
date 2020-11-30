# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:15:33 2020

@author: Sajjad
"""

import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.speed(0)

def first():
    tina.left(20)
    tina.forward(100)
    tina.left(70)
    tina.forward(50)
    tina.left(104)
    tina.forward(100)
    tina.left(-28)
    tina.forward(100)
    tina.left(104)
    tina.forward(50)
    tina.left(71)
    tina.forward(105)
    tina.penup()
    tina.goto(10, -30)
    tina.left(10)
    tina.pendown()
    
def right():
    tina.pendown()
    tina.left(-95)
    tina.forward(100)
    tina.left(60)
    tina.forward(60)
    tina.left(120)
    tina.forward(100)
    tina.left(-40)
    tina.forward(100)
    tina.left(100)
    tina.forward(50)
    tina.left(75)
    tina.forward(100)
    tina.penup()
    tina.goto(-40, -30)
    tina.pendown()

def left():
    tina.left(290)
    tina.forward(100)
    tina.left(60)
    tina.forward(60)
    tina.left(120)
    tina.forward(100)
    tina.left(-40)
    tina.forward(100)
    tina.left(100)
    tina.forward(50)
    tina.left(75)
    tina.forward(100)

    
first()

tina.left(30)
tina.forward(100)
tina.penup()
tina.back(100)
tina.pendown()
tina.left(249)
tina.forward(100)
tina.left(60)
tina.fd(60)
tina.left(120)
tina.fd(90)
tina.left(295)
tina.fd(90)
tina.left(115)
tina.forward(60)    
tina.penup()
tina.goto(-10, -30)
tina.pendown()

tina.left(130)
tina.forward(100)
tina.penup()
tina.back(100)
tina.pendown()
tina.left(249)
tina.forward(100)
tina.left(60)
tina.fd(60)
tina.left(120)
tina.fd(90)
tina.left(291)
tina.fd(90)
tina.left(115)
tina.forward(60) 
    
    

turtle.done()
