#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'trapeze-area.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate trapeze Area
    Small Base value: sb (int)
    Bigger Base value: bb (int)
    Height: h (int)
"""
# ---------------------------------------------------------------------------
def trapezeArea(sb: int, bb:int, h: int):
    if (sb == None or bb == None or h == None):
        return "Data values missing!"
    if (type(sb) != int or type(bb) != int or type(h) != int): 
        return "Invalid data type!"
    
    return (((bb + sb)*h)/2)