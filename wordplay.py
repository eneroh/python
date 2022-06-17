fWord = input("Enter first word: ")
sWord = input("Enter second word: ")
choice = input("Select (c)oncat, (s)wap, (r)everse: ")

def reverse (string):
    return string[::-1]

if choice == "c":
    print(fWord + " " + sWord)

elif choice == "s":
    print(sWord + " " + fWord)

elif choice == "r":
    print(reverse(fWord + " " + sWord))

else:
    print("Incorrect entry, please try again")
