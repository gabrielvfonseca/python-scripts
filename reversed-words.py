#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'reversed-words.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Reverse Words
    Word 1: s1 (str)
    Word 2: s2 (str)
"""
# ---------------------------------------------------------------------------
def checkReverse(s1: str, s2: str):
    if (s1 == None or s2 == None):
        return "Strings missing!"
    if (type(s1) != str or type(s2) != str): 
        return "Invalid input types!"

    string = ''
    for i in s1:
        string = i + string
    if (string == s2): return True
    else: return False    
