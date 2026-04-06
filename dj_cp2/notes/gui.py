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
label = tk.Label(root, text = "This is currently working!", font = ("Times New Roman", 14))
label.config(fg = "black")
label.config(background = "mediumaquamarine")
label.pack()


#How do I make a clickable button?
root.count = 0
def add():
    root.count += 1
    tk.Label(root, text = root.count).pack()
    
button = tk.Button(root, text = "ADD", command = add)
button.pack()



#How do you show and hide widgets? 




root.mainloop()