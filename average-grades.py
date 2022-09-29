#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'average-grades.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate Grades Averge
    grade1: n1 (int)
    grade2: n2 (int) 
    grade3: n3 (int) 
"""
# ---------------------------------------------------------------------------
def averageGrades(n1: int, n2: int, n3: int):
    if (n1 == None or n2 == None or n3 == None):
        return "Data values missing!"
    if (type(n1) != int or type(n2) != int or type(n3) != int): 
        return "Invalid data type!"
    return (n1 + n2 + n3) / 3 # (n1 + n2 + n3) / 3