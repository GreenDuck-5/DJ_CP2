#DJ, 1st, Tkinter GUI Notes


#What is a GUI?
# Graphic User Interface


#What is a widget?
# The window that the user is able to interact with


#How do I set up a basic GUI?
import tkinter as tk

root = tk.Tk()

root.title("Testing")
root.configure(background = "mediumaquamarine")
root.minsize(250, 250)
root.geometry("300x300+100+100")



#How do I make a clickable button?
root.count = 0
def add():
    root.count += 1
    num["text"] = root.count

    
button = tk.Button(root, text = "ADD", command = add)
button.pack()

num = tk.Label(root, text = 0)
num.pack()


#How do you show and hide widgets? 

num = tk.Label(root, text = 0)
num.pack()


root.mainloop()