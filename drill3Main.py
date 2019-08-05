

from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.minsize(500,180)
        self.master.maxsize(500,180)
        self.master.title("Check Files")

        guiLoad(self)




def guiLoad(self):

    self.btnBrowse1 = tk.Button(self.master, width=14, height=1, text="Browse...")
    self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(45,0))
    self.btnBrowse2 = tk.Button(self.master, width=14, height=1, text="Browse...")
    self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,0))
    self.btnCheckFiles = tk.Button(self.master, width=14, height=2, text="Check for Files...")
    self.btnCheckFiles.grid(row=2, column=0, padx=(20,0), pady=(10,0))
    self.btnClose = tk.Button(self.master, width=14, height=2, text="Close Program")
    self.btnClose.grid(row=2, column=4, padx=(20,0), pady=(10,0),sticky=E)

    self.txtBrowse1 = tk.Entry(self.master,width=55,text=" ")
    self.txtBrowse1.grid(row=0, column=1, columnspan=4, padx=(10,10), pady=(45,0), sticky=N+E+W)
    self.txtBrowse2 = tk.Entry(self.master,width=55, text=" ")
    self.txtBrowse2.grid(row=1, column=1, columnspan=4, padx=(10,10), pady=(10,0),sticky=N+E+W)
        
    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
