#DJ, 1st, Fractal Pattern Generator
import turtle as t
import time 


def recursion_num():
#Get how many times they want to nest the fractal 
    recursions = t.textinput("Recursions Num", "How many recusions (1-7)?").strip().lower()

    while True:
        #use try and except to check if it is an integer

        try:
            recursions = int(recursions)
            return recursions

        except:
            recursions = t.textinput("Recursions Num", "How many recusions (1-7)?").strip().lower()

recursions = recursion_num()

def t_color():
    #get them to enter a color
    color = t.textinput("Turtle Color", "What Color?").strip().lower()

#A while loop that checks if it is possible to set the turtle to that color using try and except and if not asks them again
    while True:

        try:
            t.color(color)
            break

        except:
            color = t.textinput("Turtle Color", "What Color?").strip().lower()


def s_color():
    #Setup the screen 
    screen = t.Screen()
    background = t.textinput("BG Input","What Color?").strip().lower()
    while True:

        try:
            screen.bgcolor(background)
            break

        except:
            background = t.textinput("BG Input","What Color?").strip().lower()
    screen.setup(1000,1000)



def main(recursions):

    t_color()
    s_color()

    #hide the turtle
    t.hideturtle()

    #increase speed, making it near instant
    t.tracer(0, 0)
    base = -350
    #define a function that uses turtle to display the fractal inside of itself repeating that many times 
    def fractal(number, startx, starty, size):

        #create a base case
        if number == 0: 
            return
        #set the turtle to a position
        t.teleport(startx, starty)
        #draw a triangle
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        
        #return something that calls this function in returning it
        fractal(number - 1, startx, starty, size / 2)
        fractal(number - 1, startx + size / 2, starty, size / 2)
        fractal(number - 1, startx + size / 4, starty + size * 0.436, size / 2)
    fractal(recursions, base, base, 500)
    t.update()
    t.done()

main(recursions)