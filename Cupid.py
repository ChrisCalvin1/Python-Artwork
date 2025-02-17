from turtle import *
tom = Turtle ()
tom.speed(0)

#background
screen = Screen()
screen.tracer(False)           
screen.bgcolor("pink")

tom.pu()
tom.goto(-400,400)
tom.pd()

tom.pu()
tom.fd(350)
tom.pd()

#Jump
def j(x,y):
    tom.pu()
    tom.goto(x,y)
    tom.pd()


#Pixel
def pix(c):
    tom.color(c)
    tom.begin_fill()
    for count in range(4):
        tom.fd(15)
        tom.rt(90)
    tom.end_fill()

#heart function
def heart(length,size):
    tom.color("#F23B4A")
    tom.begin_fill()
    tom.lt(140)
    tom.fd(length)
    tom.circle(size,200)
    tom.setheading(60)
    tom.circle(size,200)
    tom.fd(length)
    tom.end_fill()
    tom.setheading(0)

#line one
pix("skyblue")
tom.pu()
tom.fd(250)
tom.pd()

#Blue spark
for count in range(4):
    pix('#4d89b6')
    tom.rt(90)

#line 2
tom.pu()
tom.goto(-475,350)
tom.pd()
pix('#4d89b6')

tom.pu()
tom.fd(200)
tom.pd()
pix('#4d89b6')

tom.pu()
tom.fd(200)
tom.pd()
pix('#4d89b6')

#blue spark
for count in range(4):
    pix('#4d89b6')
    tom.rt(90)
    tom.fd(15)

j(350,340)
pix('skyblue')

tom.pu()
tom.fd(200)
tom.pd()
pix('skyblue')

#small heart

#Outline
j(0,200)
pix('black')
j(15,215)
pix('black')
j(30,230)
pix('black')
j(45,245)
pix('black')
j(60,260)
pix('black')
j(60,260+15)
pix('black')
j(60,260+15+15)
pix('black')
j(60,260+15+15+15)
pix('black')

j(60-15+15,260+15+15+15)
pix('black')

j(60-15,290+15+15)
pix('black')
j(60-15-15,290+15+15)
pix('black')
j(60-15-15-15,290+15+15)
pix('black')
j(0,305)
pix('black')

j(-15,320)
pix('black')
j(-30,320)
pix('black')
j(-45,320)
pix('black')
j(-60,305)
pix('black')
j(-60,290)
pix('black')
j(-60,275)
pix('black')
j(-60,260)
pix('black')
j(-45,245)
pix('black')
j(-30,245-15)
pix('black')
j(-15,245-15-15)
pix('black')

#Details
j(45,305)
pix('#D41B25')
j(45,305-15)
pix('#A10B1B')
j(45,305-15-15)
pix('#A10B1B')
j(45,305-15-15-15)
pix('#A10B1B')
j(30,245)
pix('#A10B1B')
j(15,245)
pix('#D41B25')
j(15,230)
pix('#D41B25')
j(0,215)
pix('#D41B25')
j(0,230)
pix('#D41B25')
j(0,245)
pix('#D41B25')
j(-15,230)
pix('#D41B25')
j(-15,245)
pix('#D41B25')
j(-30,245)
pix('#D41B25')
j(-45,245+15)
pix('#D41B25')
j(-45,305)
pix('white')
j(-15,305)
pix('#D41B25')

#fill
j(-45,320-15)
tom.color('#F74254')

tom.pu()
tom.fd(15)
tom.pd()

tom.begin_fill()
tom.fd(15)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(30)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(30)
tom.rt(90)
tom.fd(15*4)
tom.rt(90)
tom.fd(15*5)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15*2)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.end_fill()

j(150,260)
pix('skyblue')
j(450,260)
pix('skyblue')
j(-179,200)
pix('skyblue')

#Big heart
tom.pu()
tom.goto(0,0)
tom.pd()

heart(180,-90)

tom.setheading(180)

#Black_heart_pixels

#def bbox():   
    #tom.width(3)
    #tom.color("black")
    #tom.begin_fill()   
    #for count in range(4):
        #tom.fd(5)
        #tom.rt(90)
    #tom.end_fill()

#for count in range(4):
    #for count in range(7):
        #bbox()
        #tom.lt(90)
        #tom.fd(5)
        #tom.lt(90)
        #tom.fd(5)
        #tom.setheading(0)

tom.hideturtle()
screen.tracer(True)
done()