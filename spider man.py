from turtle import *
import math
tom = Turtle ()
tom.color("black")
tom.width(5)
tom.speed(0)

#background
screen = Screen()           
screen.bgcolor("pink")


tom.pu()
tom.goto(0,-100)
tom.pd()

tom.circle(200)

#centre
tom.pu()
tom.goto(-10,123)
tom.pd()

tom.speed(5)
num_points = 10
radius = 200
# 
# for count in range(10):

def line (l):

    tom.fd(15)
    a,b=tom.position()
    tom.rt(360/10)
    tom.fd(l)

    # Optional, this just marks each edge point with a dot
    tom.goto(a,b)

x = 200
for count in range(10):
    line(x)
done()