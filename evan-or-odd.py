#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'evan-or-odd.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Check Evan or Odd numbers
    Number: n (int)
"""
# ---------------------------------------------------------------------------
def checkEvanOdd(n: int):
    if (n == None):
        print("Data value missing!")
    elif (type(n) != int): 
        print("Invalid number!")
    else:
        if (not(n % 2)):
            return True
        else: return False
