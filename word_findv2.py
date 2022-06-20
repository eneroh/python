#!/bin/python

"""
text_find.py

File and Text Manipulation

This script is to find text in a specific file. GUI involved. User input for word find function.

It is missing 2 features, displaying lines where the word appears and highlight functionality for word on line. Need to add when I gain more knowledge. Expect a text_findv2.py shortly. Think this may involve dict?
"""

import tkinter as tk
from tkinter import filedialog

file = filedialog.askopenfilename()

def colored(r, g, b, string):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, string)

if(not file):
    print("No file selected")
    exit()
else:
    fileOpen = open(file).read().lower()
    #print(fileOpen)

string = input("Enter word you want to find: ")

for line in fileOpen.splitlines():
    if string in line:
        print(line + colored(255, 0, 0, string))

def findText(string):
    #print(string.count in fileOpen.read().lower())
    #print(stringCount)
    return string.lower() in fileOpen

if(not string):
    print("Please enter a string")

else:
    findText(string)

def result():
    if(findText(string) == True):
        print("Your word appears in the document!")
        stringCount = fileOpen.count(string)
        print("Your word appears " + str(stringCount) + " times.")
    else:
        print("Your word doesn't appear in the document! Try again?")

result()

# Attempt #3
"""
import easygui

string = input("Enter word you would like to find: ")
file = easygui.fileopenbox()

file.textbox(str)
print()

#print(string.lower in file.read().lower())
"""


# Attempt #2
"""
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

folder_path = filedialog.askpath()
"""
# Attempt #1
"""def word_lookup(string):
    string = input("Enter word to locate: ")

print(word_lookup(string.lower in open_file.lower(path)))

def open_file(path):
    subprocess.run(["xdg-open", path])

open_file(".")
"""
