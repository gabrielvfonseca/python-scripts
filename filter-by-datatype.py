#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'filter-by-datatype.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Filter list according to data types
    List of different values: n (list)
"""
# ---------------------------------------------------------------------------
def filterList(l: list):    
    lw, ln = [], []
    for value in l:
        if (type(value) == int):
            lw.append(value)
        elif (type(value) == str):
            ln.append(value)
    return [lw, ln]