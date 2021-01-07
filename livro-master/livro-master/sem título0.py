# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:03:50 2020

@author: Enterprise
"""


import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colurs  in ['red','blue','cyan','green','yellow',
                    'white']:
        turtle.color(colurs)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()