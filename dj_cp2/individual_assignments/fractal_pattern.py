#DJ, 1st, Fractal Pattern Generator

import turtle

turtle.shape("turtle")

color = input("What color do you want your fractal in? ")

while True:
    try:
        turtle.color(color)
        break
    except:
        color = input("What color do you want your fractal in? ")

recursions = int(input("How many recursions do you want to do (1-5)? "))

while True:
    try:
        recursions = int(recursions)
        if 0 < recursions < 6:
            break
        recursions = int(input("How many recursions do you want to do (1-5)? "))
    except:
        recursions = int(input("How many recursions do you want to do (1-5)? "))

screen = turtle.Screen()
screen.tracer(0)

turtle.teleport(-125, -100)
turtle.setheading(60)
length = 200

turtle.pendown()

for x in range(recursions):
    for y in range(3 ** (x + 1)):
        turtle.forward(length)
        turtle.right(120)

screen.update()
screen.mainloop()