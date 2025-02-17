from turtle import *
tom = Turtle ()
tom.width(2)
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
        tom.fd(20)
        tom.rt(90)
    tom.end_fill()

#heart
def heart(length,size):
    tom.color("red")
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
    tom.pu()
    tom.rt(90)
    tom.fd(20)
    tom.pd()

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
    tom.pu()
    tom.rt(90)
    tom.fd(20)
    tom.pd()

tom.pu()
tom.fd(200)
tom.pd()
pix('skyblue')

#small heart
j(0,-250)
heart(180,-90)
j(0,195)
heart(60,-30)

j(350,340)
pix('skyblue')

j(-5,200)
pix('black')
j(10,215)
pix('black')
j(25,230)
pix('black')
j(25+10,245)
pix('black')

j(45,260)
pix('black')
j(45,280)
pix('black')
j(45,280)
pix('black')
j(25,300)
pix('black')
j(5,300)
pix('black')
j(5-15,300-15)
pix('black')
j(-25,300)
pix('black')
j(-45,300)
pix('black')
j(-65,280)
pix('black')
j(-65,275)
pix('black')
j(-65,265)
pix('black')
j(-65,255)
pix('black')

j(-55,245)
pix('black')
j(-55+15,245-15)
pix('black')
j(-55+15+15,245-15-15)
pix('black')
#Heart
#tom.color("red")
#tom.begin_fill()
#tom.lt(140)
#tom.fd(180)
#tom.circle(-90,200)
#tom.setheading(60)
#tom.circle(-90,200)
#tom.fd(179)
#tom.end_fill()

#tom.setheading(180)

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