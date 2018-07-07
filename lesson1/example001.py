# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 09:52:17 2018

"""
def solution():
    result = []
    for i in range(1000, 2001):
        if (i % 5 == 0) and (i % 3 != 0):
            result.append(str(i))
    print(",".join(result))

solution()
            