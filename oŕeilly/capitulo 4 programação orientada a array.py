# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:29:37 2020

@author: Pedro Italo
"""
##programação orientada a array
import numpy as np
pontos = np.arange(-5,5,0.01)

xs,ys = np.meshgrid(pontos, pontos)
z=np.sqrt(xs**2+ys**2)

import matplotlib.pyplot as plt

plt.imshow(z,cmap=plt.cm.Blues),plt.colorbar()
plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of valeus")
#logica condicional como aperaçoes de array
xarr = np.array([1.1,1.2,1.3,1.4,1.5])

yarr = np.array([2.1,2.2,2.3,2.4,2.5])

cond = np.array([True,False,True,True,False])

result  = [(x if c else y)
           for x,y,c in zip(xarr,yarr,cond)]

result = np.where(cond,xarr,yarr)
  
arr = np.random.rand(4,4)
np.where(arr>0,2,arr)

#metodos matematicos

arr = np.random.randn(5,4)
arr.mean()#media
np.mean(arr)
arr.sum()
arr.mean(axis=1)
arr.sum(axis=0)