from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import sys
import mysql.connector
import os

identifiants__=[]
if(os.path.getsize("../DataLoader/temp.txt")!=0):
    with open('../DataLoader/temp.txt','r') as file:
        myline = file.readlines()
        for line in myline:
            identifiants = list( line.strip().split(None, 2))
            identifiants_=''.join(identifiants)
            identifiants__.append(identifiants_)
    file.close()
    user=identifiants__[0]
    password=identifiants__[1]
    #Connectinng to the DB
    con = mysql.connector.connect(
                user=user, 
                password=password,
                host='127.0.0.1',
                database='DataLoader')
    curseur= con.cursor()

request = "SELECT Nbre_Cas from Regions WHERE NomRegion="+"'"+sys.argv[1]+"'"+""
curseur.execute(request)
Nbre_Cas=curseur.fetchone()
print(Nbre_Cas[0])

fenetre = Tk()
fenetre.title(sys.argv[1])
fenetre.geometry("110x90")

var = StringVar()
lbl = Label(fenetre, textvariable=var)
var.set(""+ sys.argv[1]+"\n Nbre de cas: "+str(Nbre_Cas[0])+"")
lbl.grid(row=0, column=1)
b2=Button(fenetre,text="Détails",command=lambda: rback())
b2.grid(row=1,column=1)
fenetre.mainloop()
