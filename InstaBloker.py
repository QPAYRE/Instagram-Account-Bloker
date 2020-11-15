#!/usr/bin/env python3

import os
import sys
from tkinter import *

class Bloker:
    def __init__(self,win):
        self.label1 = Label(win, text="Nom d'utilisateur")
        self.label2 = Label(win, text="Mot de passe")
        self.label3 = Label(win, text="Bloquage MAX")
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.btn1 = Button(win, text='Fichier liste @')
        self.btn2 = Button(win, text='Run')
        self.btn3 = Button(win, text='Quitter')

        self.label1.place(x=50, y=50)
        self.label2.place(x=50, y=100)
        self.label3.place(x=50, y=150)
        self.t1.place(x=175,y=50)
        self.t2.place(x=175,y=100)
        self.t3.place(x=175,y=150)
        self.btn1.place(x=50,y=200)
        self.btn2.place(x=300,y=250)
        self.btn3.place(x=200,y=250)

        


if __name__ == "__main__":
    window=Tk()
    mywin=Bloker(window)
    window.title('Instagram Bloker')
    window.geometry("400x300+10+10")
    window.mainloop()