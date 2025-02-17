from turtle import *

tom = Turtle ()
tom.color("white")
tom.width(5)
tom.speed(5)

#background
screen = Screen()           
screen.bgcolor("pink")


tom.pu()
tom.goto(0,0)
tom.pd()

tom.fd(200)
tom.bk(400)
tom.rt(90)
tom.fd(100)
tom.lt(90)
tom.fd(400)
done()