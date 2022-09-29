#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'calculate-zeros.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate zeros
    a: a (int)
    b: b (int)
    c: c (int)
"""
# ---------------------------------------------------------------------------
def calculateZeros(a: int, b: int, c: int):
    if (a == None or b == None or c == None):
        return "Missing parameters!"
    if (type(a) != int or type(b) != int or type(c) != int): 
        return "Invalid input types!"
    
    x1 = ((-int(b) + int(float((int(b)**2)-4*int(a)*int(c))**0.5)) / 2*int(a))
    x2 = ((-int(b) - int(float((int(b)**2)-4*int(a)*int(c))**0.5)) / 2*int(a))

    if (x1 == x2): return x1 # f(x) can have only one root!
    else: return x1, x2
