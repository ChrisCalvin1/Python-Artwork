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

#------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------

#Red Spark


#pix('black')
#j(-125+15,145-15)
#pix('black')
#j(-125+15+15,145-15-15)
#pix('black')
#tom.rt(270)
#j(-125+15+15,145-15-15-15)
#pix('black')
#tom.fd(15)
#pix('black')
#j(-95,145-15-15-15-15-15-15)

#-------------------------------------------------------------------------------------------------------------------------------------
def move_to(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()

# Pixel function
def pix(c):
    tom.color(c)
    tom.begin_fill()
    for _ in range(4):
        tom.fd(15)
        tom.rt(90)
    tom.end_fill()

#Coordinate
size = 15
start_x, start_y = size * -9, size * 11 # Adjustable

# Pixel pattern (1=black, 2=#F74254, 3=dark red #A10B1B)
pattern = [
    [0, 0, 1, 0, 0],
    [0, 1, 2, 1, 0],
    [1, 2, 1, 3, 1],
    [0, 1, 3, 1, 0],
    [0, 0, 1, 0, 0]
]

# Draw the pattern using the pix function
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        color = None
        if pattern[row][col] == 1:
            color = "black"
        elif pattern[row][col] == 2:
            color = "#F74254"
        elif pattern[row][col] == 3:
            color = "#A10B1B"
        
        if color:
            move_to(start_x + col * size, start_y - row * size) # type: ignore
            pix(color)

#------------------------------------------------------------------------------------------------------------------------

#Coordinate
size = 15
start_x, start_y = size * 7, size * 8 # Adjustable

# Pixel pattern (1=black, 2=#F74254, 3=dark red #A10B1B)
pattern = [
    [0, 0, 1, 0, 0],
    [0, 1, 2, 1, 0],
    [1, 2, 1, 3, 1],
    [0, 1, 3, 1, 0],
    [0, 0, 1, 0, 0]
]

# Draw the pattern using the pix function
for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        color = None
        if pattern[row][col] == 1:
            color = "black"
        elif pattern[row][col] == 2:
            color = "#F74254"
        elif pattern[row][col] == 3:
            color = "#A10B1B"
        
        if color:
            move_to(start_x + col * size, start_y - row * size) # type: ignore
            pix(color)

#----------------------------------------------------------------------------------------------------------------------

#Black spark
def blkspark():
    for count in range(4):
        pix('black')
        tom.rt(90)
        tom.fd(15)
    tom.rt(90)
    pix('#F74254')

j(-10,80)
blkspark()

j(300,160)
blkspark()

#---------------------------------------------------------------------------------------------------------------------
#Big Heart


tom.hideturtle()
screen.tracer(True)
done()