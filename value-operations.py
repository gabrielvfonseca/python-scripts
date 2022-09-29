#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'valueOperations.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Operations:
    Value 1: v1 (int)
    Value 2: v2 (int)
    Value 3: v3 (int)
"""
# ---------------------------------------------------------------------------
def operations(v1: int, v2: int, v3: int):
    if (v1 == None or v2 == None or v3 == None):
        return "Data values missing!"
    if (type(v1) != int or type(v2) != int or type(v3) != int): 
        return "Invalid data type!"

    if ((v1 > v2) and (v2 > v3)): 
        b, s = v1, v3
    elif ((v1 < v2) and (v2 < v3)):
        b, s = v3, v1
    elif ((v1 < v2) and (v1 < v3)):
        b, s = v2, v1
    elif ((v3 < v2) and (v3 < v1)):
        b, s = v2, v3
    else: b, s = v1, v3

    # average, sum, multiply, smaller, bigger
    return [((v1 + v2 + v3) / 3), (v1 + v2 + v3), (v1 * v2 * v3), s, b]