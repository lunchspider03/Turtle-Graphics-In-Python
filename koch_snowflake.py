import sys
import turtle

def snowflake(trtl: turtle.Turtle, level, length):
    def bump(trtl, length, bumpLevel):
        if bumpLevel == 0:
            trtl.forward(length/3)
            trtl.left(60)
            trtl.forward(length/3)
            trtl.right(120)
            trtl.forward(length/3)
            trtl.left(60)
            trtl.forward(length/3)

        elif bumpLevel > 0:
            bump(trtl, length/3, bumpLevel= bumpLevel - 1)
            trtl.left(60)
            bump(trtl, length/3, bumpLevel = bumpLevel - 1)
            trtl.right(120)
            bump(trtl, length/3, bumpLevel = bumpLevel - 1)
            trtl.left(60)
            bump(trtl, length/3, bumpLevel = bumpLevel - 1)
        else:
            trtl.forward(length)

    for _ in range(3):
        bump(trtl, length, level - 1)
        trtl.right(120)

trtl = turtle.Turtle()

turtle.tracer(False)

screen_width, screen_height = trtl.screen.screensize()
trtl.penup()
inset = int(sys.argv[-2]) + 10 * int(sys.argv[-2])
trtl.goto(-screen_width + inset, screen_height - inset)
trtl.pendown()

trtl.hideturtle()

trtl.screen.colormode(255)
trtl.fillcolor(160, 227, 246)
trtl.begin_fill()

snowflake(trtl, int(sys.argv[-2]), int(sys.argv[-1]))
trtl.end_fill()

turtle.update()

trtl.screen.mainloop()
