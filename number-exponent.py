#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'number-exponent.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Exp
    Number: n (int)
    Exp: e (int)
"""
# ---------------------------------------------------------------------------
def exp(n: int, e: int):
    if (n == None or e == None):
        return "Data values missing!"
    if (type(n) != int or type(e) != int): 
        return "Invalid numbers!"
    return (n**e)
    
