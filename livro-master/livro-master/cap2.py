#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:36:01 2020

@author: pedro
"""


def f(x,y,z):
    return (x+y)/z

a = 5;
b =6;
c=7.5
result = f(a,b,c)

a = [1,2,3]
b=a
a.append(4)
b
a

def append_element(some_list,element):
    some_list.append(element)

data = [1,2,3]

append_element (data,4)

data
a = 5
type (a)

a = 'foo'
type (a)
  
 '5'+ 5 
 
 a = 4.5
 b =2
 print ('a is {0}, b is {1}'.format(type(a),type(b)))
 
 a/b
 a=5;
 isinstance(a, float)
 a=5; b=4.5
 isinstance(a,( int,float))
 
 isinstance(b,( int,float))
 a= 'foo'
 getattr(a,'split')
 
 
 def isiterable(obj):
     try:
         iter(obj)
         return True
     except TypeError: # não é interavel
         return False
    
 isiterable ('a string')   
 isiterable ([1,2,3])   
 isiterable (5)   