#!/bin/python

#######################
#Author: INFT1004
#Date: 2019-2020
#Task:Manipulate strings,
#Print String, reverse String, Loop through string
#Check boolean from lecture
######################

def myStory(name, age, likes):
   #print strings expecting 3 arguments
   print("My name is " + name + ".")
   print("I am  " + str(age) + " years old.")
   print("I like " + likes + ".")  
  
def printDouble(instring):
   #This funstion prints each character twice
   for x in instring:
     print(x * 2)
      
def printNonLetters(instring):
   #Checks to see if char is a letter
   #if it is not then print it
   letters = "abcdefghijklmnopqrstuvwxyz"
   for char in instring.lower():
     if not char in letters:
       print char

def reverse(instring):
   #Reverses the strings, last is first
   result = ""
   for char in instring:
     result = char + result
   print(result)
  
def indexLoop(instring):
   #This is a loop that will check from 0 index to 
   #length of string and then print them all out in one line
   answer = ""
   for index in range(0, len(instring)):
     answer += instring[index]
   print(answer)
   
   #Now only print each 2nd char in the string
   answer = ""
   for index in range(0, len(instring), 2):
     answer += instring[index]
   print(answer)
  
   #Print the string backwords
   answer = ""
   for index in range(len(instring)-1, -1, -1):
    answer += instring[index]
   print(answer)  

def jumble(sentence):
   #as the function name states we are jumbing the
   #sentence that is sent to the function
   #Odd printed together and then even printed together
   words = sentence.split(" ") #Split on space
   result = ""
   
   #join together all the odd-numbered ones in reverse order
   for count in range(0, len(words), 2):
     result = words[count] + " " + result
	 
   #join together all the even-numbered ones in reverse order
   for count in range(1, len(words), 2):
     result = result + " " + words[count]
   print(result)
  
def checkBoolean():
   #check the following statements
   #from the lecture   
   number1 = 5
   number2 = 7
   if number1 > number2:
      print("number1 is larger")
   if number1 <= number2:
       print("number2 is larger")
