#!/usr/bin/env python3

import os
import sys
from tkinter import *
from tkinter import filedialog, messagebox

class Bloker:
    def __init__(self,win):
        self.root = win
        self.data = dict()
        self.label1 = Label(win, text="Nom d'utilisateur")
        self.label2 = Label(win, text="Mot de passe")
        self.label3 = Label(win, text="Bloquage MAX")
        self.t1 = Entry()
        self.t2 = Entry(show="*")
        self.t3 = Entry()
        self.btn1 = Button(win, text='Fichier liste @', command=self.findFile)
        self.btn2 = Button(win, text='Run', command=self.run)
        self.btn3 = Button(win, text='Quitter', command=self.quit)

        self.label1.place(x=50, y=50)
        self.label2.place(x=50, y=100)
        self.label3.place(x=50, y=150)
        self.t1.place(x=175,y=50)
        self.t2.place(x=175,y=100)
        self.t3.place(x=175,y=150)
        self.btn1.place(x=50,y=200)
        self.btn2.place(x=300,y=250)
        self.btn3.place(x=200,y=250)

    def findFile(self):
        filename = filedialog.askopenfilename(initialdir="/",title="Choisi un fichier",filetypes=(("pdf files","*.pdf"),("all files","*.*")))
        self.label4 = Label(self.root, text="")
        self.label4.place(x=150,y=200)
        self.label4.configure(text=filename)
        self.data["file"] = filename

    def run(self):
        if self.data["file"] == '':
            messagebox.showwarning(title='File missing', message='Vous devez choisir un fichier de list @ au format PDF')
        elif self.t1.get() == '':
            messagebox.showwarning(title='Username missing', message='Vous devez renseigner votre username instagram (@)')
        elif self.t2.get() == '':
            messagebox.showwarning(title='Password missing', message='Vous devez renseigner votre mot de passe instagram')
        elif self.t3.get() == '':
            messagebox.showwarning(title='NB Bloker missing', message='Vous devez renseigner le nombre de compte à bloquer')
        elif self.t3.get().isnumeric() != True:
            messagebox.showerror(title='NB Bloker error', message='Vous devez entrer uniquement des chiffres pour le nombre de bloquage')
        else:
            print("ok")
    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    window=Tk()
    mywin=Bloker(window)
    window.title('Instagram Bloker')
    window.geometry("400x300+10+10")
    window.mainloop()