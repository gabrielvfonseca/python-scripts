#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'average-fuel.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate Fuel Averge
    Distance: km (int)
    Liters: l (int)
"""
# ---------------------------------------------------------------------------
def averageFuel(d: int, l: int):
    if (d == None or l == None):
        return "Data values missing!"
    if (type(d) != int or type(l) != int): 
        return "Invalid data type!"

    return ((l / d) * 100)
