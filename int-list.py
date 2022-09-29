#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'ex19.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Create list of int values
    How many items will the list have: nItems (int)
    List: l (list)
"""
# ---------------------------------------------------------------------------
def createIntList(nItems: int):
    if (nItems == None):
        return "Strings missing!"
    if (type(nItems) != int):
        return "Invalid input types!"
    
    l = []
    for index in range(nItems):
        l.append(int(input(f'Value {(index + 1)}: ')))
    return l
