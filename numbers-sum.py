#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'numbers-sum.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate sum of numbers
    Values: t (tuple)
"""
# ---------------------------------------------------------------------------
def sum(v: tuple):
    if (v == None):
        return "Data values missing!"
    if (type(v) != tuple): 
        return "Invalid data type!"

    if (v[0] == v[1]): 
        return (v[0] + 3)
    elif (v[1] == v[2]): 
        return (v[0] + v[1])
    elif (v[0] == v[2]):
        return (v[0] + v[1])
    else: return (v[0] + v[1] + v[2])