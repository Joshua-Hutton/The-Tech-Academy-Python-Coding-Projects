

import os
import datetime
import sqlite3
from tkinter import * #<-- I can not get this to work every time I try to use a function I have needed to import that library on its own 
import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
import shutil

import drill5Main
import drill5Gui


def getFilePath(self, txt):
    var = tk.filedialog.askdirectory()
    txt.insert(INSERT,var)
    

def close(self):
    if messagebox.askokcancel("End Program", "Would you like to end the program"):
        self.master.destroy()
        os.close(0)



###############################################
   #"CHECK FOR FILES ..." BUTTON OPERATIONS#
###############################################

#drill 1
        
def getFileNames(self, txt1, txt2):

    dirPath = str(txt1)
    newTxt2 = str(txt2)
    print(dirPath)
    print(newTxt2)
    files = os.listdir(dirPath)

    findTxt(files,dirPath,newTxt2)


def findTxt(files,dirPath,txt2):
    lst = []
    for file in files:
        if file.split(".")[1] == "txt":
            lst.append(file)

    mkFilePath(lst,dirPath,txt2)   
    


def mkFilePath(files,dirPath,txt2):
    filePaths1 = []
    filePaths2 = []
    for file in files:
        filePaths1.append(os.path.join(dirPath,file))

    for file in files:
        filePaths2.append(os.path.join(txt2,file))
        
    moveFiles(filePaths1,filePaths2,files)

def moveFiles(filePaths1,filePaths2,files):
    i = 0
    for file in files:
        shutil.move(filePaths1[i],filePaths2[i])
        i = i+1
    printFiles(filePaths1,filePaths2,files)
        
    

def printFiles(filePaths1,filePaths2,files):
    datetimeList = []
    i = 0 
    for file in files:        
        print(file + ": " + datetime.datetime.fromtimestamp(os.path.getmtime(filePaths2[i])).strftime('%c'))
        datetimeList.append(datetime.datetime.fromtimestamp(os.path.getmtime(filePaths2[i])).strftime('%c'))                   
        i = i + 1

    dbInput(files,datetimeList)

#drill 2



def dbInput(files,datetimeList):
   
    conn = sqlite3.connect('drill5.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS file_tbl( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, file_col TEXT, dateTime_col TEXT )")
        conn.commit()
        
        for i , j in zip(files,datetimeList):
            cur.execute("INSERT INTO file_tbl(file_col, dateTime_col) VALUES(?,?)", (i,j))
           

        conn.commit()
           
    conn.close()

 

if __name__ == "__main__":
    pass
