# Importing required libraries 
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import Label
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import statistics as st

# Creating the class of the application
class Application(Tk):
    
    # Defining the __init__ function
    def __init__(self):
        super().__init__()
        
        # Setting the required variables by self  
        self.file_location=""
        self.keyword_location=""
        self.count_of_words=0
        self.count_of_sentences=0
        self.count_of_lines=0
        self.most_frequent_word=""
        self.least_frequent_word=""
        self.count_in_keyword=0
        self.sentences_with_keyword=""
        
        # The symbols that need to be ignored in the input text file are in except_array
        self.except_array=[".",",","?","!",":",";"]

        self.geometry('550x520')
        self.grid()
        
        # File labels 
        self.file_label=Label(self, text = "File Not Chosen ." + self.file_location)
        self.file_label.pack()
        self.keyword_label = Label(self, text = "Keywords File Not Chosen . " + self.keyword_location)
        self.keyword_label.pack()

        #Creating the browse button for choosing the text file in the GUI
        self.browse = tkinter.Button(self,text = "Text File",command = self.set_file_location)
        self.browse.pack()


        #Creating the browse button for choosing the keyword file in the GUI
        self.browse = tkinter.Button(self,text = "Keywords File",fg="brown", command = self.set_keyword_location)
        self.browse.pack()

        #Creating the refresh button in the GUI
        self.refresh = tkinter.Button(self, text="Refresh",fg="green",command=self.refresh_function)
        self.refresh.pack()

        #Labels for all statistics functions used
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
        self.keyword_file = Label(self, text="Number of Sentences with keywords..." + str(self.count_in_keyword))
        self.keyword_file.pack()

        #Creating button which shows extra infomation in the GUI
        self.extra = tkinter.Button(self,text = "Exta Information", command = self.extra_function)
        self.extra.pack()
        
        #Labels for extra information
        self.most_frequents = Label(self, text="")
        self.most_frequents.pack()
        self.least_frequents= Label(self, text="")
        self.least_frequents.pack()

        #Creting Histogram button which displays histogram in the GUI 
        self.histogram = tkinter.Button(self, text="Plot Histogram",fg="red",command=self.plot_function)
        self.histogram.pack()

        #Creating label of string with keyword
        self.keyword_string = Label(self, text="Printing sentences :\n")
        self.keyword_string.pack()

        #Creating the quit button in the GUI 
        self.quit = tkinter.Button(self, text="QUIT", fg="red",command=self.destroy)
        self.quit.pack(side="bottom")

    # Defining the function that sets the main text file location
    def set_file_location(self):
        self.file_location = filedialog.askopenfilename()
        self.file_label.config(text = "File: " + self.file_location)
        self.file_function()
        
    # Defining the function that sets the keyword file location
    def set_keyword_location(self):
        self.keyword_location = filedialog.askopenfilename()
        self.keyword_label.config(text = "Keyword File: " + self.keyword_location)
        self.keyword_function()
        
    # Defining the function which refreshes
    def refresh_function(self):
        if(self.file_location!=""):
            self.file_function()
        if(self.keyword_location!=""):
            self.keyword_function()
        if(self.file_location!=""):
            self.extra_function()
            
    # Defining the function to perform all operations on the text file
    def file_function(self):
        
        # Open and process the text file
        data = open(self.file_location,"r")
        raw_data = data.read()
        words=raw_data.split()
        
        # Create an array word_new_list, containing all required words from the file
        word_new_list=[]
        for i in range(len(words)):
            check=0
            for j in range(len(self.except_array)):
                if words[i]==self.except_array[j]:
                    check=1
            if(check==0):
                word_new_list.append(words[i])
        
        # Count and display the number of words in the file
        self.count_of_words=len(word_new_list)
        self.number_of_words.config(text="Number of Words: " + str(self.count_of_words))
        
        # Count and display the number of sentences in the file
        self.count_of_sentences = raw_data.count('.') + raw_data.count('?') + raw_data.count('!')
        self.number_of_sentences.config(text="Number of Sentences: " + str(self.count_of_sentences))
        
        # Count and display the number of lines in the file
        self.count_of_lines = raw_data.count('\n')
        self.number_of_lines.config(text="Number of Lines: " + str(self.count_of_lines))
        
        # Creating a map to store the words(for finding most and least frequent word)
        map_words=dict()
        word_list=word_new_list
        for i in range(len(word_list)):
            if(map_words.get(word_list[i])==None):
                map_words[word_list[i]]=1
            else:
                map_words[word_list[i]]+=1
                
        # Display the most frequent word in the file using the map 
        self.most_frequent_word=max(map_words,key=map_words.get)
        self.most_frequent.config(text="Most Frequent Word : " + self.most_frequent_word)

        # Display the least frequent word in the file using the map
        self.least_frequent_word=min(map_words,key=map_words.get)
        self.least_frequent.config(text="Least Frequent Word : " + self.least_frequent_word)
        
        
    # Defining the function to perform operations on keyword file
    def keyword_function(self):
        
        # Open and process the file
        data = open(self.file_location,"r")
        raw_data=data.read()
        keyword_data= open(self.keyword_location,"r")
        keyword=keyword_data.read().split()
        
        # Replacing '?'and '!' with '.' and splitting wrt '.' (finding end of sentences)
        raw_data.replace("?",".")
        raw_data.replace("!",".")
        sentences=raw_data.split(".")

        self.sentences_with_keyword=""
        
        # Count the number of sentences with keywords
        self.count_in_keyword=0
        for i in range(len(sentences)):
            check=0
            for j in range(len(keyword)):
                if(sentences[i].count(keyword[j])>0):
                    check=1
            self.sentences_with_keyword+=("\n"+sentences[i])
            self.count_in_keyword+=check
            
        # Display the number of sentences with keywords and also print them..

        self.keyword_string.config(text="Sentences with keywords: \n" + str(self.sentences_with_keyword))

        self.keyword_file.config(text="Number of Sentences with keywords: " + str(self.count_in_keyword))

    # Defining the function to plot the Bar graph
    def plot_function(self):
        
        # Open and process the file
        data = open(self.file_location,"r")
        raw_data=data.read()
        words=raw_data.split()
        
        # Create an array word_new_list, containing all required words from the file
        word_new_list=[]
        for i in range(len(words)):
            check=0
            for j in range(len(self.except_array)):
                if words[i]==self.except_array[j]:
                    check=1
            if(check==0):
                word_new_list.append(words[i])
        
        # Plot the bar graph from the processed data   
        word_uniq,value = np.unique(word_new_list,return_counts=True)
        ticks = range(len(value))
        plt.bar(ticks,value,align='center')
        plt.xticks(ticks,word_uniq)
        plt.title('Histogram for Count of each Word...',fontweight ="bold") 
        plt.xlabel('Words',fontsize=15)
        plt.ylabel('Frequency',fontsize=15)
        plt.show()
        
    # Defining the function that displays extra information 
    def extra_function(self):
        if(self.file_location==""):
            return
        
        # Open and process the file
        data = open(self.file_location,"r")
        raw_data = data.read()
        words=raw_data.split()
        
        # Create an array word_new_list, containing all required words from the file
        word_new_list=[]
        for i in range(len(words)):
            check=0
            for j in range(len(self.except_array)):
                if words[i]==self.except_array[j]:
                    check=1
            if(check==0):
                word_new_list.append(words[i])
        
        # Creating a map to store the words
        map_words=dict()
        word_list=word_new_list
        for i in range(len(word_list)):
            if(map_words.get(word_list[i])==None):
                map_words[word_list[i]]=1
            else:
                map_words[word_list[i]]+=1
        
        # Finding least frequent words 
        temp_map_words=map_words
        map_words=sorted(map_words.items(), key =lambda kv:(kv[1], kv[0]))
        least_frequent_words=""
        x=0 
        for i in range(len(map_words)):
            if x<3:
                least_frequent_words+=(map_words[x][0]+",") 
                x=x+1
            else:
                break  
        least_frequent_words+="etc.."
        
        # Finding most frequent words
        map_words=sorted(temp_map_words.items(), key =lambda kv:(kv[1], kv[0]),reverse=True)
        most_frequent_words=""
        x=0
        for i in range(len(map_words)):
            if x<3:
                most_frequent_words+=(map_words[x][0]+",") 
                x=x+1
            else:
                break  
        most_frequent_words+="etc.."
        
        # Displaying the most and least frequent words
        self.most_frequents.config(text="Other More Frequently Occuring Words : " + most_frequent_words)
        self.least_frequents.config(text="Other Least Frequently Occuring Words :" + least_frequent_words)

# Create and run the application
app = Application()
app.title("Statistics For the File")
app.mainloop()
