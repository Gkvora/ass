# -*- coding: utf-8 -*-
"""
Created on Wed May 25 07:08:42 2022

@author: A
"""
import numpy as np
A=np.array([1,2,3,4,5,6,7,8,9])
B=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
C=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(A)
print(B)
print(C)
print(A.ndim)
print(B.ndim)
print(C.ndim)
print(A.size)
print(B.size)
print(B.shape)
print(C.size)
print(A[0::2])
print(B[0][1])
print(B[0::,1:5:])