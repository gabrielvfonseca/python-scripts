#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'evan-interval.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate number interval of evan numbers
    Start interval: start (int)
    End interval: end (int) 
"""
# ---------------------------------------------------------------------------
def evanInterval(start: int, end: int):
    if (start == None or end == None):
        return "Data values missing!"
    if (type(start) != int or type(end) != int): 
        return "Invalid data type!"
    l = []
    for v in range(start, (end + 1)): 
        if v % 2 == 0: 
            l.append(v)
    return l