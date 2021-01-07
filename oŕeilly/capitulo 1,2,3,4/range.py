#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:25:36 2020

@author: pedro
"""


range (10)
list (range(10))
list (range(0,20,2))
list (range(5,0,-1))
seq= [1,2,3,4]

for i in range (len(seq)):
    val = seq[i]
    
sum = 0
for i in range (100000):
    if i % 3 == 0 or i%5 ==0:
        sum+=i
        
value = true-expr if condition else false-expr