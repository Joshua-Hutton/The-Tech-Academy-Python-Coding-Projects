
from tkinter import *
import tkinter as tk

import drill5Main
import drill5Functions

def guiLoad(self):

    self.txtBrowse1 = Text(self.master,width=40,height=1)
    self.txtBrowse1.grid(row=0, column=1, columnspan=4, padx=(10,10), pady=(45,0), sticky=N+E+W)
    self.txtBrowse2 = Text(self.master,width=40, height=1)
    self.txtBrowse2.grid(row=1, column=1, columnspan=4, padx=(10,10), pady=(10,0),sticky=N+E+W)

    self.btnBrowse1 = tk.Button(self.master, width=14, height=1, text="Browse...", command = lambda: drill5Functions.getFilePath(self, self.txtBrowse1))
    self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(45,0))
    self.btnBrowse2 = tk.Button(self.master, width=14, height=1, text="Browse...", command = lambda: drill5Functions.getFilePath(self, self.txtBrowse2))
    self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,0))
    self.btnCheckFiles = tk.Button(self.master, width=14, height=2, text="Check for Files...", command = lambda: drill5Functions.getFileNames(self,self.txtBrowse1.get("1.0",'end-1c'),self.txtBrowse2.get("1.0",'end-1c')))
    self.btnCheckFiles.grid(row=2, column=0, padx=(20,0), pady=(10,0))
    self.btnClose = tk.Button(self.master, width=14, height=2, text="Close Program", command = lambda: drill5Functions.close(self))
    self.btnClose.grid(row=2, column=4, padx=(20,0), pady=(10,0),sticky=E)

   



if __name__ == "__main__":
    pass
