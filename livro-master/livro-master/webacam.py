#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:13:15 2020

@author: pedro
"""


import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("nao é possivel abrir webcam")
while True:
     ret, frame = cap.read()
     frame = cv2.resize(frame,None,fx=0.5,
                        interpolation = cv2.INTER_AREA)
     cv2.imshow('input',frame)
     c = cv2.waitKey(1)
     if c == 27:
         break
cap.release()
cv2.destroyAllWindows()