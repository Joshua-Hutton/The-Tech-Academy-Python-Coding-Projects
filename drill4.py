

from tkinter import *
import tkinter as tk
import tkinter.filedialog

class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        self.master = master

        self.master.minsize(500,200)
        self.master.title("Drill 4")

        self.btn = tk.Button(self.master, width = 10, height= 1, text="Find File",command = lambda: self.getFilePath())
        self.btn.grid(row=0,column=0,padx=(10,0),pady=(40,0))
        self.txt = Text(self.master,height=1,width=45)
        self.txt.grid(row=0,column=1,padx=(5,0),pady=(40,0))
        

    def getFilePath(self):
        var = tk.filedialog.askdirectory()
        self.txt.insert(INSERT,var)
        
    



if __name__== "__main__":
    root =tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
