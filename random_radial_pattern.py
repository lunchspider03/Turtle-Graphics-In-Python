import math
import turtle
import random

screen = turtle.Screen()
screen.setup(width=1920, height=1000)

trtl = turtle.Turtle()
trtl.speed(0)
trtl.hideturtle()
trtl.screen.colormode(255)

def radial_pattern(trtl, n = 3, side_length = 100 , count = 10, x = 0, y = 0):
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()
    for _ in range(count):
        for __ in range(n):
            trtl.forward(side_length)
            trtl.left(360 / n)
        trtl.left(360 / count)


width = trtl.screen.window_width() // 2
height = trtl.screen.window_height() // 2

side_length = random.randint(50, 100)
n = random.randint(3, 10)

inset = math.ceil(math.sqrt(n) * side_length)

trtl.begin_fill()
trtl.fillcolor(random.randint(0, 255), random.randint(0,255), random.randint(0,99))
radial_pattern(trtl=trtl, n = n, side_length = side_length, count= random.randint(3, 100), x = (inset - width), y = (height - inset))
trtl.end_fill()

trtl.begin_fill()
trtl.fillcolor(random.randint(0, 255), random.randint(0,255), random.randint(0,99))
radial_pattern(trtl=trtl, n = n, side_length = side_length, count= random.randint(3, 100), x = (-inset + width), y = (-height + inset))
trtl.end_fill()

trtl.begin_fill()
trtl.fillcolor(random.randint(0, 255), random.randint(0,255), random.randint(0,99))
radial_pattern(trtl=trtl, n = n, side_length = side_length, count= random.randint(3, 100), x = (inset - width), y = (-height + inset))
trtl.end_fill()

trtl.begin_fill()
trtl.fillcolor(random.randint(0, 255), random.randint(0,255), random.randint(0,99))
radial_pattern(trtl=trtl, n = n, side_length = side_length, count= random.randint(3, 100), x = (-inset + width), y = (height - inset))
trtl.end_fill()

trtl.penup()

screen.mainloop()
