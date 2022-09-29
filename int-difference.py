#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'int-difference.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate difference between two int values
    Value1: v1 (int)
    Value2: v2 (int) 
"""
# ---------------------------------------------------------------------------
def intDifference(v1: int, v2: int):
    if (v1 == None or v2 == None):
        return "Data values missing!"
    if (type(v1) != int or type(v2) != int): 
        return "Invalid data type!"

    if (v1 > v2): return (v1 - v2)
    else: return (v2 - v1)