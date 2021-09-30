import turtle
import random

trtl = turtle.Turtle()
trtl.speed(0)
trtl.hideturtle()
trtl.screen.colormode(255)

def radial_pattern(trtl, n = 3, side_length = 100 , count = 10):
    trtl.pendown()
    for _ in range(count):
        for __ in range(n):
            trtl.forward(side_length)
            trtl.left(360 / n)
        trtl.left(360 / count)


trtl.begin_fill()
trtl.fillcolor(random.randint(0, 255), random.randint(0,255), random.randint(0,255))
radial_pattern(trtl=trtl, n = random.randint(3, 10), side_length = random.randint(150, 300), count= random.randint(3, 100))
trtl.end_fill()

turtle.mainloop()
