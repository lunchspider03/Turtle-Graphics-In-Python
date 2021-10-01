import turtle


def snowflake(trtl: turtle.Turtle, level, length):
    def bump(length):
        trtl.forward(length/3)
        trtl.left(60)
        #trtl.forward(length/3)
        if level > 1:
            snowflake(trtl, level=level-1, length=length/3)
        trtl.right(120)
        trtl.forward(length/3)
        trtl.left(60)
        trtl.forward(length/3)

    if level == 0:
        for _ in range(3):
            trtl.forward(length)
            trtl.left(120)

    if level > 0:
        for _ in range(3):
            bump(length)
            trtl.right(120)




trtl = turtle.Turtle()
trtl.penup()
trtl.goto(-300, 300)
trtl.pendown()

trtl.fillcolor("orange")


turtle.tracer(False)
trtl.begin_fill()
snowflake(trtl, 5, 800)

turtle.update()
trtl.end_fill()
trtl.screen.mainloop()
