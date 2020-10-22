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
        self.keyword_location=""
        self.count_of_words=0
        self.count_of_sentences=0
        self.count_of_lines=0
        self.most_frequent_word=""
        self.least_frequent_word=""
        self.count_in_keyword=0

        self.except_array=[".",",","?","!",":",";"]

        self.geometry('400x300')
        self.grid()

        self.file_label=Label(self, text = "File Not Chosen ." + self.file_location)
        self.file_label.pack()

        #Code for making browse button for choosing file
        self.browse = tkinter.Button(self,text = "Text File",command = self.set_file_location)
        self.browse.pack()

        #Labels for statistics function
        self.number_of_words = Label(self, text="Number of Words: " + str(self.count_of_words))
        self.number_of_words.pack()
        self.number_of_sentences = Label(self, text="Number of Sentences: " + str(self.count_of_sentences))
        self.number_of_sentences.pack()
        self.number_of_lines = Label(self, text="Number of Lines: " + str(self.count_of_lines))
        self.number_of_lines.pack()
        self.most_frequent = Label(self, text="Most Frequent Word ...." + (self.most_frequent_word))
        self.most_frequent.pack()
        self.least_frequent = Label(self, text="Least Frequent Word ...." + (self.least_frequent_word))
        self.least_frequent.pack()

        #Quit button 
        self.quit = tkinter.Button(self, text="QUIT", fg="red",command=self.destroy)
        self.quit.pack(side="bottom")


    def set_file_location(self):
        self.file_location = filedialog.askopenfilename()
        self.file_label.config(text = "File: " + self.file_location)
        self.file_function()

    def file_function(self):
        data = open(self.file_location,"r")
        raw_data = data.read()
        words=raw_data.split()
        word_new_list=[]
        for i in range(len(words)):
            check=0
            for j in range(len(self.except_array)):
                if words[i]==self.except_array[j]:
                    check=1
            if(check==0):
                word_new_list.append(words[i])
        self.count_of_words=len(word_new_list)
        self.number_of_words.config(text="Number of Words: " + str(self.count_of_words))

        self.count_of_sentences = raw_data.count('.') + raw_data.count('?') + raw_data.count('!')
        self.number_of_sentences.config(text="Number of Sentences: " + str(self.count_of_sentences))

        self.count_of_lines = raw_data.count('\n')
        self.number_of_lines.config(text="Number of Lines: " + str(self.count_of_lines))

        map_words=dict()
        word_list=word_new_list
        for i in range(len(word_list)):
            if(map_words.get(word_list[i])==None):
                map_words[word_list[i]]=0
            else:
                map_words[word_list[i]]+=1
        self.most_frequent_word=max(map_words,key=map_words.get)
        self.most_frequent.config(text="Most Frequent Word : " + self.most_frequent_word)


        self.least_frequent_word=min(map_words,key=map_words.get)
        self.least_frequent.config(text="Least Frequent Word : " + self.least_frequent_word)


app = Application()
app.title("Statistics For the File")
app.mainloop()
