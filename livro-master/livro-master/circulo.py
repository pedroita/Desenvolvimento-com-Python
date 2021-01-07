# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:43:27 2020

@author: Enterprise
"""


import turtle
t= turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
a=0
b=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
    t.hideturtle()
turtle.done()