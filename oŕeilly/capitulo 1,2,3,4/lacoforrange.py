#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:47:10 2020

@author: pedro
"""


for i in range(4):
    for j in range(4):
        if j>i:
            break
        print((i,j))