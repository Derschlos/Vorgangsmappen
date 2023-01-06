# -*- coding: utf-8 -*-


#pyinstaller *****.py -D -w --collect-all tkinterdnd2 --noconfirm


import tkinter as tk
import time
import os
import json
from tkinter import messagebox
import Models
from tkinterdnd2 import DND_FILES, TkinterDnD
from ProcessFolderEditPageData import ProcessFolderEditPage
from Page2Data import Page2
import re
import sqlite3
from PyInstaller.utils.hooks import collect_data_files, eval_statement
datas = collect_data_files('tkinterdnd2')

def setupDB():
    db = 'Database.db'
    if os.path.isfile(db):
        return
    con = sqlite3.connect(db)
    cur = con.cursor()
    Table1Create = """CREATE TABLE "ProcessFolder" (
	"idNum" INTEGER NOT NULL UNIQUE,
	"sourceNr" TEXT NOT NULL,
	"title" TEXT NOT NULL,
	"year" TEXT NOT NULL,
	"dokDat" TEXT NOT NULL,
	"user" TEXT,
	"status" TEXT,
	"folder" TEXT,
	"register" TEXT,
	PRIMARY KEY("idNum" AUTOINCREMENT)
        )"""
##    Table2Create= """CREATE TABLE "TableName2" (
##	"id"	INTEGER NOT NULL UNIQUE,
##	"text"	TEXT NOT NULL,
##	PRIMARY KEY("id" AUTOINCREMENT)
##        )"""
    cur.execute(Table1Create)
##    cur.execute(Tabel2Create)
    return

class basedesk:
    def __init__(self,root, configVars):
        self.root = root
        self.configVars  = configVars
##        self.root.config()
        self.root.title('Base page')
        self.root.geometry('370x200')
        self.baseContainer = tk.Frame(self.root)
        self.baseContainer.pack(side = "top", fill = "both", expand = True)
        self.baseContainer.grid_rowconfigure(0, weight = 1)
        self.baseContainer.grid_columnconfigure(0, weight = 1)
        self.lastFrame =''

        self.frames = {}
        for f in (ProcessFolderEditPage,Page2,):
            frame = f(self.baseContainer, self)
            self.frames[frame.pageName] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.showFrame('ProcessFolderEditPage')
        self.setLastFrame('ProcessFolderEditPage')

    def showFrame(self,frameName):
        frame= self.frames[frameName]
        frame.tkraise()
        frame.onRaise()

    def updateFrame(self, frameName,*args):
        try:
            self.frames[frameName].update(*args)
        except:
            pass

    def setLastFrame(self, frameName):
        self.lastFrame = frameName

    def returnToPrev(self, savedChanges, pageName):
        if savedChanges == False:
            message = messagebox.askyesnocancel(message = 'Do you want to save any changes?')
            if message == None:
                return
            elif message == True:
                self.frames[pageName].saveChanges()
            else:
                self.savedChanges = True        
        self.showFrame(self.lastFrame)







if __name__ == '__main__':
    setupDB()
    configFile= 'Config.txt'
    configString = '''{"Username": "David Leon Schmidt",
                "baseColor" : "lightsalmon",
                "ProcessFolderEditPageColor" : "lightsalmon",
                "ProcessFolderEditPageDimensions" : "475x450",
                "page2Color": "lightsalmon",
                "page2Dimensions" : "430x200"
                }'''
    if os.path.isfile(configFile):
        with open(configFile, 'r') as f:
            configString = f.read()
    else:
        with open(configFile, 'w') as f:
            f.write(configString)
    configString= json.loads(configString)
    root= TkinterDnD.Tk()
    basedesk(root, configString)
    root.mainloop()


        
