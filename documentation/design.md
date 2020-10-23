## Introduction
    
1. ### Project Overview

    `File-Inspector` is a Graphical User Interface Driven Tool/Application that can be used to obtain statistical data about the words and the sentences of an ASCII file which will be provided by the user as input. The Statistical Data include the number of sentences, number of words, number of newlines, most and least frequently occurring word. The tool can also plot a histogram denoting the frequency of the words in the file.
    
    The user can provide another file containing a list of keywords and `File-Inspector` can show all the occurrences of the sentences in the input file containing those keywords.

2. ### Scope of the document
    
    This document describes the implementation details of the File Inspector Tool. It will also serve as a User Manual since it explains User Interface, buttons, and associated operations they can perform using this tool.

3. ### Environment
    
    The project is completely based on the python programming language.

## Design Overview

1. <h3 id="desc">Description of Problem</h3>

    The tool is expected to provide an option for the user to navigate and choose any ASCII file on his system and allow him to obtain statistical data about the words and the sentences of the same.

    The statistical information to be generated includes -

    * Number of words
    * Number of sentences
    * Number of newlines
    * Histogram for word frequency
    * Most frequently occurring words
    * Least frequently occurring words

    The tool should also provide a button to navigate and select another file containing a list of keywords. The tool should show all the occurrences of the sentences in the input file containing those keywords.

    **Important Consideration**

    The user should be able to dynamically change the file, i.e. the user may update the file, save it and close the editor. The tool must provide an option to fetch the new statistical data.
    

2. **Decomposition Description**

    ![piysuh](https://user-images.githubusercontent.com/43112419/97027559-8665a800-1578-11eb-87aa-33d9f192f992.png)


3. **Technologies and Dependencies**

    The project solely uses `Python` language for scripting.

    It uses several libraries in its aid for development. Some of them include:

    * tkinter: A standard GUI library for the Python programming language, which permits to create of the GUI application. We have used this library to design our tool and also to obtain its various controls, such as buttons, labels, and text boxes.

    * statistics: A Python library for calculating mathematical statistics of numeric(Real-valued) data, such as mean, standard deviation, variance, mode, etc.

    * matplotlib: A plotting library for the Python programming language. We have used this library to plot the histogram for word-frequency.

    * NumPy: A Python library that provides efficient operations, especially with arrays. We have used this library to store the list of words and find a unique set of elements from them.


## User Interface

![rsz_1whatsapp_image_2020-10-22_at_103004_pm](https://user-images.githubusercontent.com/43112419/97032278-30483300-157f-11eb-9e9a-1150a038b024.jpg)


![rsz_whatsapp_image_2020-10-22_at_103004_pm](https://user-images.githubusercontent.com/43112419/97032207-11e23780-157f-11eb-90bf-89254597bc6a.jpg)


## References

[1] [Tkinter Official Documentation](https://docs.python.org/3/library/tkinter.html)
<br>
[2] [Guide to GUI Programming](https://realpython.com/python-gui-tkinter/)
<br>
[3] [Tutorial to write Design Document](https://www.sampletemplates.com/business-templates/design-document.html)
<br>
[4] [Padmanabhan Sir Data Adder](https://github.com/padmanrajan/DataAdder)
<br>
[5] [Padmanabhan Sir Data Adder-Wiki](https://github.com/padmanrajan/DataAdder/wiki)
<br>
[6] [Github Wiki Pages Offical Documentation](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/about-wikis)
<br>