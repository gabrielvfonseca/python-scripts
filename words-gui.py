#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Gabriel Fonseca
# Created Date: 22/09/2022
# File Name   : 'words-gui.py'
# Version = '0.0'
# ---------------------------------------------------------------------------
""" Graphic User Interface (GUI) """
# ---------------------------------------------------------------------------
import tkinter as tk
# ---------------------------------------------------------------------------
def GUI():
    def display():
        print(inp.get())
        area.insert(0, inp.get())

    w = tk.Tk()
    w.title("Python GUI window")
    w.geometry("500x300")

    title = tk.Label(w, text="Python Simple GUI", font=("Helvetica", 18, "bold"))
    txt = tk.Label(w, text="Insert text:", font=("Helvetica", 10, "normal"))

    inp = tk.Entry(w, bd=2)
    area = tk.Entry(w, bd=2)

    title.place(x=20, y=20)
    txt.place(x=20, y=80)

    inp.place(x=100, y=80, width=280, height=25)
    area.place(x=20, y=120, width=360, height=100)

    qbtn = tk.Button(w, text='Cancel', command=w.quit)
    sbtn = tk.Button(w, text='OK', command=display)
    qbtn.place(x=60, y=250)
    sbtn.place(x=20, y=250)

    w.mainloop()
