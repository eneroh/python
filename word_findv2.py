#!/bin/python

"""
text_find.py

File and Text Manipulation

This script is to find text in a specific file. GUI involved. User input for word find function.

The script has been completed in its entirety. The final .replace on line 32 was a suggestion from a distant friend.
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
        print(line.replace(string,colored(255, 0, 0,string)))

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
