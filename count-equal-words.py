#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'count-equal-words.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Count equal words inside list
    List of words: w (list)
"""
# ---------------------------------------------------------------------------
def countEqualWords(w: list):
    if (w == None):
        return "Missing parameter!"
    if (type(w) != list): 
        return "Invalid input type!"

    if (len(w) != len(set(w))):
        return True
    else: return False
