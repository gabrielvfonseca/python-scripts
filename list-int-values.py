#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'list-int-values.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Sort list of int values
    List of numbers: n (list)
"""
# ---------------------------------------------------------------------------
def sortList(n: list):
    if (n == None):
        return "Missing parameter!"
    if (type(n) != list): 
        return "Invalid input type!"

    for index in range(len(n)):
        for i in range((index + 1), len(n)):
            if (n[index] > n[i]):
                n[index], n[i] = n[i], n[index]
    return n
