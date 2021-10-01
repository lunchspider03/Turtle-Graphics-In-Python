import turtle

def main():
    trtl = turtle.Turtle()
    trtl.hideturtle()
    trtl.screen.colormode(255)
    trtl.pencolor(0, 0, 255)
    trtl.pensize(2)
    trtl.speed(0)
    
    fractal_level = int(input("Enter The Fractal Level You Want To Get :\t"))
    trtl_position_x, trtl_position_y = 0, 150

    if fractal_level > 8:
        print("fractal_level is greater than 8 wait while computing it")
        turtle.tracer(False)

    draw_fractal(trtl, fractal_level, trtl_position_x, -trtl_position_y, trtl_position_x, trtl_position_y)
    if fractal_level > 8:
        turtle.update()
    draw_fractal(trtl, fractal_level, trtl_position_x, trtl_position_y, trtl_position_x, -trtl_position_y)
    
    if fractal_level > 8:
        turtle.update()

    trtl.screen.mainloop()

def draw_fractal(trtl, fractal_level, x1=0, y1=0, x2=0, y2=0):
    if fractal_level == 0:
        draw_line(trtl, x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        draw_fractal(trtl=trtl, fractal_level= (fractal_level - 1), x1=x1, y1= y1, x2= xm, y2= ym)
        draw_fractal(trtl=trtl, fractal_level= (fractal_level - 1), x1=xm, y1= ym, x2= x2, y2= y2)


def draw_line(trtl, x1, y1, x2, y2):
    trtl.penup()
    trtl.goto(x1, y1)
    trtl.pendown()
    trtl.goto(x2, y2)


if __name__ == "__main__":
    main()

