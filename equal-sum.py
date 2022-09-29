#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'equal-sum.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" number + number = other number
    Value 1: n1 (int)
    Value 2: n2 (int)
    Value 3: n3 (int)
"""
# ---------------------------------------------------------------------------
def checkValues(n1: int, n2: int, n3: int):
    if (n1 == None or n2 == None or n3 == None):
        return "Data values missing!"
    elif (type(n1) != int or type(n2) != int or type(n3) != int): 
        return "Invalid numbers!"
    else:
        if ((n1 + n2) == n3): return True
        else: return False
