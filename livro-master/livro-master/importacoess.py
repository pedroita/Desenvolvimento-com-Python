#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 08:51:24 2020

@author: pedro
"""


import some_module
result = some_module.f(5)
pi = some_module.PI

from some_module import f,g, PI
result = g(5,PI)
re= f(9)
print (result)
print (re)

import  some_module as zezinho
from some_module import PI as pi ,  g as gaf
r1 = zezinho.f(pi)
r2 = gaf(6,pi) 