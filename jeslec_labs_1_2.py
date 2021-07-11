def hello():
  print "Hello World"
  
def pickAndShow():
  myFile = pickAFile()
  myPict = makePicture(myFile)
  show(myPict)
  
def sillyString():
  print("""We are using triple quotes. Why?
Notice the different lines.
And we cant ignore the use of apostrophes.
  
Because we can do this.""")

def madlib():
  name = "Mark"
  pet = "Baxter"
  verb = "ate"
  snack = "Krispy Kreme Doughnuts"
  line1 = "Once upon a time, "+name+" was walking"
  line2 = " with "+pet+", a trained dragon. "
  line3 = "Suddenly, "+pet+" stopped and announced,"
  line4 = "'I have a desperate need for "+snack+"'. "
  line5 = name+" complained. 'Where I am going to get that?' "
  line6 = "Then "+name+" found a wizard's wand. "
  line7 = "With a wave of the wand, "
  line8 = pet+" got "+snack+". "
  line9 = "Perhaps surprisingly, "+pet+" "+verb+" the "+snack+"."
  print(line1+line2+line3+line4)
  print(line5+line6+line7+line8+line9)
  
# pg 71

def madlib2():
  name = "Ty"
  pet = "Fluffy"
  verb = "rolled on"
  snack = "a seven-layer wedding cake."
  line1 = "Once upon a time, "+name+" was walking"
  line2 = " with "+pet+", a trained dragon. "
  line3 = "Suddenly, "+pet+" stopped and announced,"
  line4 = "'I have desperate need for "+snack+"' "
  line5 = name+" complained. 'Where I am going to get that?' "
  line6 = "Then "+name+" found a wizard's wand. "
  line7 = "With a wave of the wand, "
  line8 = pet+ " got "+snack+" "
  line9 = "Perhaps surprisingly, "+pet+" "+verb+" the "+snack+""
  print(line1+line2+line3+line4)
  print(line5+line6+line7+line8+line9)
  

  
def mathWithStrings():
  myString = "My name is Ingo Montoya. "
  myThreat = "You killed my father. Prepare to die."
  print(myString + myThreat) # String concatenation
  print(myString * 6)