#!/usr/bin/env python3

import os
import sys
import csv
import time

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tkinter import *
from tkinter import filedialog, messagebox

import docx

class Bloker:
    def __init__(self,win):
        self.root = win
        self.data = dict()
        self.data["file"] = ''

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
        filename = filedialog.askopenfilename(initialdir="/",title="Choisi un fichier",filetypes=(("word files","*.docx"),("all files","*.*")))
        self.label4 = Label(self.root, text="")
        self.label4.place(x=180,y=203)
        tmp = filename.split('/')
        i = len(tmp)
        self.label4.configure(text=tmp[i-1])
        self.data["file"] = filename

    def run(self):
        if self.data["file"] == '':
            messagebox.showwarning(title='File missing', message='Vous devez choisir un fichier de list @ au format docx')
        elif self.t1.get() == '':
            messagebox.showwarning(title='Username missing', message='Vous devez renseigner votre username instagram (@)')
        elif self.t2.get() == '':
            messagebox.showwarning(title='Password missing', message='Vous devez renseigner votre mot de passe instagram')
        elif self.t3.get() == '':
            messagebox.showwarning(title='NB Bloker missing', message='Vous devez renseigner le nombre de compte à bloquer')
        elif self.t3.get().isnumeric() != True:
            messagebox.showerror(title='NB Bloker error', message='Vous devez entrer uniquement des chiffres pour le nombre de bloquage')
        else:
            self.data['user'] = self.t1.get()
            self.data['password'] = self.t2.get()
            self.data['nbBlok'] = self.t3.get()
            if bot(self.data) == 'OK':
                messagebox.showinfo(title='Instagram Bloker', message='Done :)')

    def quit(self):
        self.root.destroy()

def getInstagramAccountsToBlock(file):
    try:
        doc = docx.Document(file)
        accounts = list()
        for para in doc.paragraphs:
            tmp = para.text.replace("https://www.instagram.com/",'')
            accounts.append(tmp[:-1])
    except Exception as e:
        print(e)
        pass
    try:
        results = []
        with open('blocked.csv') as inputfile:
            for row in csv.reader(inputfile):
                for elem in row:
                    results.append(elem)
    except Exception as e:
        print(e)
        pass
    try:
        accounts = [item for item in accounts if item not in results]
    except Exception as e:
        print(e)
    return accounts, results

def bot(data):
    accounts, results = getInstagramAccountsToBlock(data['file'])
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("https://instagram.com/")
    try:
        driver.find_element_by_css_selector('.bIiDR').click()
    except:
        pass
    """ Connexion instagram account """
    try:
        instaAccount = driver.find_element_by_name("username")
        instaPassword = driver.find_element_by_name("password")
        instaAccount.send_keys(data['user'])
        instaPassword.send_keys(data['password'])
        time.sleep(1)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
    except:
        pass
    try:
        ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
    except:
        pass
    """ Loop bloker account """
    try:
        accountsBlocked = []
        i=1
        for account in accounts:
            if i <= int(data['nbBlok']):
                driver.get("https://www.instagram.com/"+account)  
                driver.find_element_by_css_selector('.wpO6b').click()
                time.sleep(2)
                driver.find_element_by_css_selector(".mt3GC:only-child .aOOlW:first-child").click()
                time.sleep(2)
                driver.find_element_by_css_selector(".bIiDR").click()
                time.sleep(2)
                accountsBlocked.append(account)
            else:
                break
            i=i+1
    except Exception as e:
        print(e)
        pass
    try:
        for elem in results:
            accountsBlocked.append(elem)
        with open("blocked.csv","w") as f:
            wr = csv.writer(f,delimiter=",")
            wr.writerow(accountsBlocked)
    except Exception as e:
        print(e)
        pass
    driver.close()
    return('OK')


if __name__ == "__main__":
    window=Tk()
    mywin=Bloker(window)
    window.title('Instagram Bloker')
    window.geometry("400x300+10+10")
    window.mainloop()