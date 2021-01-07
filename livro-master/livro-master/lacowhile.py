#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:00:13 2020

@author: pedro
"""


x=256
total = 0
while x>0:
    if total > 500:
        break
    total +=x
    x=x // 2