import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import Label
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import statistics as st

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.file_location=""

        self.except_array=[".",",","?","!",":",";"]

        self.geometry('400x300')
        self.grid()

        self.file_label=Label(self, text = "File Not Chosen ." + self.file_location)
        self.file_label.pack()

        #Code for making browse button for choosing file
        self.browse = tkinter.Button(self,text = "Text File",command = self.set_file_location)
        self.browse.pack()

        #Quit button 
        self.quit = tkinter.Button(self, text="QUIT", fg="red",command=self.destroy)
        self.quit.pack(side="bottom")


    def set_file_location(self):
        self.file_location = filedialog.askopenfilename()
        self.file_label.config(text = "File: " + self.file_location)


app = Application()
app.title("Statistics For the File")
app.mainloop()