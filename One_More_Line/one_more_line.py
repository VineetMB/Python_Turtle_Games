import turtle
from random import randint
import time


# initialize the screen for turtle graphics
screen = turtle.Screen()
screen.setup(700, 900)
screen.title("One More Line")
# screen.bgcolor('black')
# screen.tracer(0, 0)

Player_main = turtle.Turtle()
Player_main.width(5)
Player_main.color("cyan")
Player_main.pu()
Player_main.left(90)
Player_main.goto(0,-450)
Player_main.pd()

Player_left = turtle.Turtle()
Player_left.width(5)
Player_left.color("white")
Player_left.pu()
Player_left.left(90)
Player_left.goto(-10,-450)
Player_left.pd()

Player_right = turtle.Turtle()
Player_right.width(5)
Player_right.color("yellow")
Player_right.pu()
Player_right.left(90)
Player_right.goto(10,-450)
Player_right.pd()

Player_main.fd(10)
Player_left.fd(10)
Player_right.fd(10)

screen.update()

points_list = []
for _ in range(4):
    for _ in range(4):
        points = turtle.Turtle()
        # points.ht()
        points.pu()
        points.speed(0)
        points.goto(1000,1000)
        points.color('black')
        points.seth(270)
        points.goto(randint(-250, 250), randint(900, 1100))
        points.st()
        points.pd()
        points_list.append(points)

    for _ in range(2):
        for points in points_list:
            points.fd(200)
            # screen.update()
            time.sleep(0.5)
            print('done')
    



turtle.mainloop()