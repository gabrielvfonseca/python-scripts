#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'lists-percentage.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Calculate lists percentage
    Number of students: nullStudents (int)
    Null votes: nullVotes (int)
    Votes for each list [X, Z, K]: lists (list)
"""
# ---------------------------------------------------------------------------
def listPercentage(nullStudents: int, nullVotes: int):
    if (nullStudents == None or nullVotes == None):
        return "Data values missing!"
    if (type(nullStudents) != int or type(nullVotes) != int): 
        return "Invalid data type!"

    lists = [
        int(input('Votes for list X: ')),
        int(input('Votes for list Z: ')),
        int(input('Votes for list K: ')),
    ]

    for index in range(3):
        print(f'Lista {"X" if index==0 else "Z" if index==1 else "K"}: {((lists[index] / (nullStudents - nullVotes)) * 100)}%')