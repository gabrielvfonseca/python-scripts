#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'number-sequencie.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Number Sequencies
    Start interval: x (int)
    End interval: y (int)
"""
# ---------------------------------------------------------------------------
def interSequencies(x: int, y: int):
    if (x == None or y == None):
        return "Data values missing!"
    if (type(x) != int or type(y) != int): 
        return "Invalid numbers!"
    if (x < y):
        return (y-x)
