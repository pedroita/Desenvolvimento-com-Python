# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:39:41 2020

@author: Pedro Italo
"""

arr = np.arange(10)

arr
Out[46]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[5]
Out[47]: 5

array([5
,6,7])
Traceback (most recent call last):

  File "<ipython-input-48-13720f567d9f>", line 1, in <module>
    array([5

NameError: name 'array' is not defined


arr[5:8]
Out[49]: array([5, 6, 7])

arr[5:8]=12

arr_s=arr[5:8]

arr_s[1]=12345

arr_s[:]=64

arr[5:8].copy()
Out[54]: array([64, 64, 64])

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[2]
Out[56]: array([7, 8, 9])

arr2d[0][2]
Out[57]: 3

arr2d[0,2]
Out[58]: 3