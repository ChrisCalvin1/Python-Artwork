from turtle import *

tom = Turtle()
tom.color('white')
screen = Screen()
screen.bgcolor("black")
tom.speed(1000)
tom.pu()
tom.goto(0,0)
tom.pd()

for count in range(10):
    tom.rt(360/10)
    for count in range(10):
        tom.fd(100)
        tom.rt(360/10)
        

tom.pu()
tom.goto(5,0)
tom.pd()

for count in range(10):
    tom.rt(360/10)
    for count in range(10):
        tom.fd(100)
        tom.rt(360/10)

tom.pu()
tom.goto(10,0)
tom.pd()

for count in range(10):
    tom.rt(360/10)
    for count in range(10):
        tom.fd(100)
        tom.rt(360/10)

tom.pu()
tom.goto(15,0)
tom.pd()

for count in range(10):
    tom.rt(360/10)
    for count in range(10):
        tom.fd(100)
        tom.rt(360/10)

tom.pu()
tom.fd(350)
tom.pd()

def p():
    for count in range(5):
        tom.rt(120)
        for count in range(5):
            tom.fd(10)
            tom.rt(360/6)
            tom.fd(10)
            tom.rt(360/6)
tom.p
