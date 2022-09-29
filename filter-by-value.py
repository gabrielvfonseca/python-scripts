#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'filter-by-value.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Filter list according to value
    List of values: n (list)
    Filter value: f (non-defined)
"""
# ---------------------------------------------------------------------------
def filterListByValue(l: list, f):
    if (l == None or f == None):
        return "Missing parameter!"
    if (type(l) != list): 
        return "Invalid input type!"
    
    for value in l:
        if (value == f):
            return True
        else: return False