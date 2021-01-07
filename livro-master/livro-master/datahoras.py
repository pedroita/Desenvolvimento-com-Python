#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:15:40 2020

@author: pedro
"""


from datetime import datetime,date,time

dt = datetime(2020,6,22,11,25,25)
dt.day
dt.minute
dt.date()
dt.time()
dt.strftime('%m/%d/%y %H:%M')