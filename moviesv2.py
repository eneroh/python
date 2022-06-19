#!/bin/python                                                                                         
    
"""    
moviesv2.py    
    
Me adding extra functionality to movies.py app    
    
Specifically, input functionality to have a more inviting, intuitive user experience.    
    
"""    
    
fMovie = input("Please enter your first favourite movie: ")    
sMovie = input("Please enter your second favourite movie: ")    
tMovie = input("Please enter your third favourite movie: ")    
    
list = [fMovie, sMovie, tMovie]    
    
def movies(list):    
    return list     
    
print(movies(list))    
print(movies(list[0]))
