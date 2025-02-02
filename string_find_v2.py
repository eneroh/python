#!/bin/python

"""
string_find_v2.py

File and Text Manipulation

This script is to find text in a specific file. GUI involved. User input for word find function.

The script has been completed in its entirety. The final .replace on line 32 was a suggestion from a distant friend.

Suggestion from senior developers suggest using fstrins instead of normal strings

Pending update
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
        print(line.replace(string,colored(255, 0, 0,string))) # change with f string

def findText(string):
    #print(string.count in fileOpen.read().lower())
    #print(stringCount)
    return string.lower() in fileOpen

if(not string):
    print("Please enter a string")

else:
    findText(string)

def result():
    if(findText(string)):
        print("Your word appears in the document!")
        stringCount = fileOpen.count(string)
        print("Your word appears " + str(stringCount) + " times.") # change with f string
    else:
        print("Your word doesn't appear in the document! Try again?")

result()
