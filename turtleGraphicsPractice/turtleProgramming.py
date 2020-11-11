# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:54:58 2020

@author: Sajjad
"""

import turtle
tina = turtle.Turtle()
tina.shape('turtle')

def simpleMoveForward():
    tina.penup()
    tina.forward(20)
    tina.write("Hello there")
    tina.backward(20)
    turtle.done()


def makeSquare():
    tina.forward(30)
    tina.left(90)
    tina.forward(30)
    tina.left(90)
    tina.forward(30)
    tina.left(90)
    tina.forward(30)
    turtle.done()
#makeSquare()
    
def moveUpWithColor():
    tina.left(90)
    tina.forward(20)
    tina.color("Red")
    tina.write("i am red")
    tina.forward(20)
    tina.color("Blue")
    tina.write("i am blue")   
#moveUpWithColor()
    


def gridMovement():
    tina.penup()
    tina.goto(0, 30)
    tina.pendown()
    tina.write("i am at 0, 30")
    tina.penup()
    tina.goto(0, 0)
    tina.pendown()
    tina.write("back at origin")
#gridMovement()
    
def circleFace():
    tina.penup()
    tina.goto(30, -150)
    tina.pendown()
    tina.circle(130)
    tina.penup()
    tina.goto(0, 0)
    tina.pendown()
    tina.circle(20)
    tina.penup()
    tina.goto(0,0)
    tina.pendown()
    tina.circle(10)
    tina.penup()
    tina.goto(50, 0)
    tina.pendown()
    tina.circle(20)
    tina.penup()
    tina.goto(50, 0)
    tina.pendown()
    tina.circle(10)
    tina.penup()
    tina.goto(25, -100)
    tina.pendown()
    tina.circle(35)
    
    
circleFace()








