#!/bin/python                                                                                         
    
"""    
movies.py    
    
Basic array play. Gonna list some good movies I enjoy    
"""    
    
movies = ["Reminiscence", "Flashback", "Catch me if you can", "Supercop"]    
    
print(movies[1]) # prints second item    
print(movies[0]) # prints first item    
print(movies[0:1]) # prints first item with original format    
print(movies[0:3]) # prints first 3 items with original format    
print(movies[1:]) # prints only first item    
print(movies[:1]) # prints everything    
print(movies[:4]) # prints everything from last ??    
print(movies[-1]) # prints last item    
print(movies[::-1]) # reverses order    
    
movies.append("Nacho Libre")    
print(movies)    
    
movies.pop() # deletes last item    
movies.pop(0) # deletes first item    
print(movies)    
