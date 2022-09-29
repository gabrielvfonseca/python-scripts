#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'endless-list.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Create an endless list
    List: l (list)
    New input: i (non-defined)
"""
# ---------------------------------------------------------------------------
def endlessList():
    print("""\033[93m
        Enter how many values you want. If you want to stop type enter 'stop'.
        \033[0m""")

    l = []
    while True:
        i = input("Value: ")
        if (i == "stop"): break
        else: l.append(i)

    return l