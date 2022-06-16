import tkinter as tk

class reverseString:

    define __init__(self, root):
        self.root = root
        self.root.title("Reverse Inputted String")
        self.root.geometry("500x500+0+0)

        mainFrame = Frame(self.root)
        mainFrame.grid()
        tops = Frame(mainFrame, bd=20, width=450)
        
        
        self.label = tk.Label(window, text="Insert String: ", font=("",15))
        self.label.grid(column=0, row=0)

""" ^ is borrowed from: https://www.youtube.com/watch?v=CUNsfaNWpcs
  
# Attempt II
    window = tk.Tk()
    
    window.title("reverseString app")
    window.geometry('500x500')
    
    label = tk.Label(window, text="Insert String: ", font=("",15))
    label.grid(column=0, row=0)
    
    self.text = text(window, width=10)
    text.grid(column=2,row=0)
    
    def run():
        return text[::-1]
    
        string = reverse(text)

    button = tk.Button(window, text="Enter", bg="black", fg="white", command=run)
    button.grid(column=4, row=0)
    
    window.mainloop()

# Attempt I
window = tk.Tk(
    label = tk.Label(
    text="Welcome to my app o.o",
    foreground="black",
    background="white",
    width=100,
    height=100,
)

button = tk.Button(
    text="Insert value",
    foreground="blue",
    background="green",
    width=25,
    height=5,
)

window.mainloop()

^ these are my awful attempts"""
