# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:09:39 2020

@author: Sajjad
"""


import turtle
tina = turtle.Turtle()
tina.shape('turtle')

def nameIni():
    tina.speed(0)
    tina.penup()
    tina.goto(20, 20)
    tina.pendown()
    tina.goto(0, 20)
    tina.goto(0, 0)
    tina.goto(20, 0)
    tina.goto(20, -20)
    tina.goto(0, -20)
    
    
    tina.penup()
    
    tina.goto(40, 0)
    tina.pendown()
    tina.goto(40, 20)
    tina.goto(60, 20)
    tina.goto(60, 0)
    tina.goto(40, 0)
    tina.goto(40, -20)
    tina.goto(40, 0)
    tina.right(45)
    tina.forward(30)
    
    tina.penup()
    tina.hideturtle()
    
    
    turtle.done()
    
nameIni()