# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 00:12:04 2018

@author: steven

This is to introduce some numpy basic props.
"""

import numpy as np
from numpy import pi

def get_details(narr):
    print("narr contents: \n", narr)
    print("narr type: ", type(narr))
    print("ndarray ndim: ", narr.ndim)
    print("ndarray shape: ", narr.shape)
    print("ndarray size: ", narr.size)
    print("ndarray dtype: ", narr.dtype)
    print("ndarray itmesize: ", narr.itemsize)
    print()
    


# some basic examples

get_details(np.array([6, 7, 8]))
get_details(np.array([1.5, 7.2, 8]))
get_details(np.array([(5, 2, 3), (4, 5, 6.2)]))
get_details(np.array([(1, 2), (3, 4)], dtype=complex))
get_details(np.array([[1, 2], [3, 4.5]], dtype=complex))

# some shortcuts

a = np.arange(15)
get_details(a)
get_details(a.reshape(3, 5))

b = np.zeros((3, 4))
get_details(b)

## 3d array
c = np.ones((2,3,4), dtype=np.int16)
get_details(c)

d = np.empty((2,3))
get_details(d)

e = np.linspace(0, 2*pi, 5)  
get_details(e)

f = np.sin(e)
get_details(f)

## more 3d array
g = np.arange(24).reshape(2,3,4)
get_details(g)

## if the array gets too big, use this command to print all
np.set_printoptions(threshold=np.nan)

