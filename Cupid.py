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
    tom.fd(15)

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

j(-600,400)
#Blue spark
for count in range(4):
    pix('#4d89b6')
    tom.rt(90)
    tom.fd(15)

j(600,140)
#Blue spark
for count in range(4):
    pix('#4d89b6')
    tom.rt(90)
    tom.fd(15)
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
start_x, start_y = size * 7, size * 12 # Adjustable

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


#Coordinate
size = 15
start_x, start_y = size * -45, size * 10 # Adjustable

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

tom.rt(90)


j(300,160)
blkspark()

j(500,10)
blkspark()

#---------------------------------------------------------------------------------------------------------------------

#Big Heart

j(15,0)

pix('black')
j(30,15)
pix('black')
j(45,30)
pix('black')
j(60,30)
pix('black')
j(75,30)
pix('black')
j(90,30)
pix('black')
j(105,30)
pix('black')
j(120,15)
pix('black')
j(135,15)
pix('black')
j(150,0)
pix('black')
j(150,-15)
pix('black')
j(150,-30)
pix('black')
j(150,-45)
pix('black')
j(150,-60)
pix('black')
j(150,-75)
pix('black')
j(150,-90)
pix('black')
j(135,-105)
pix('black')
j(135,-105-15)
pix('black')
j(135,-105-15-15)
pix('black')
j(135-15,-105-15-15)
pix('black')
j(120-15,-135-15)
pix('black')
j(120-15-15,-135-15-15)
pix('black')
j(120-15-15-15,-135-15-15-15)
pix('black')
j(120-15-15-15-15,-135-15-15-15-15)
pix('black')
j(120-15-15-15-15-15,-135-15-15-15-15-15)
pix('black')
j(120-15-15-15-15-15-15,-135-15-15-15-15-15-15)
pix('black')
j(120-15-15-15-15-15-15-15,-135-15-15-15-15-15-15-15)
pix('black')
j(120-15-15-15-15-15-15-15-15,-135-15-15-15-15-15-15-15-15)
pix('black')
j(0,-255)
pix('black')

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

j(-15,0)  # Mirror along y-axis (negate x-coordinate)
pix('black')
j(-30,15)
pix('black')
j(-45,30)
pix('black')
j(-60,30)
pix('black')
j(-75,30)
pix('black')
j(-90,30)
pix('black')
j(-105,30)
pix('black')
j(-120,15)
pix('black')
j(-135,15)
pix('black')
j(-150,0)
pix('black')
j(-150,-15)
pix('black')
j(-150,-30)
pix('black')
j(-150,-45)
pix('black')
j(-150,-60)
pix('black')
j(-150,-75)
pix('black')
j(-150,-90)
pix('black')
j(-135,-105)
pix('black')
j(-135,-105-15)
pix('black')
j(-135,-105-15-15)
pix('black')
j(-135+15,-105-15-15)  # Adjusted mirrored position
pix('black')
j(-120+15,-135-15)
pix('black')
j(-120+15+15,-135-15-15)
pix('black')
j(-120+15+15+15,-135-15-15-15)
pix('black')
j(-120+15+15+15+15,-135-15-15-15-15)
pix('black')
j(-120+15+15+15+15+15,-135-15-15-15-15-15)
pix('black')
j(-120+15+15+15+15+15+15,-135-15-15-15-15-15-15)
pix('black')
j(-120+15+15+15+15+15+15+15,-135-15-15-15-15-15-15-15)
pix('black')
j(-120+15+15+15+15+15+15+15+15,-135-15-15-15-15-15-15-15-15)
pix('black')

j(0,-15)
pix('black')

#Fill

tom.color('#F74254')
tom.begin_fill()

tom.fd(15)
for count in range(3):
    tom.rt(90)
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
tom.fd(15+15+15+15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(30)
tom.lt(90)
tom.fd(15*7)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(30)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15)
for count in range(7):
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)
    tom.fd(15)
tom.lt(90)
tom.fd(15)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Fill
j(-15,-15)
tom.color('#F74254')
tom.fd(15)
for count in range(3):
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)
    tom.fd(15)
tom.fd(15+15+15+15)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(30)
tom.rt(90)
tom.fd(15*7)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(30)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
for count in range(7):
    tom.rt(90)
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
tom.rt(90)
tom.fd(15)

tom.end_fill()

tom.color('#F74254')
tom.rt(180)
tom.fd(15/2)
tom.lt(90)
tom.width(20)
tom.pu()
tom.fd(5)
tom.pd()
tom.fd(250-25)

tom.width(0)
j(-15,-15)
pix('black')

j(-15,-255)
pix('black')

j(-30,-255+15)
pix('black')

j(0,-255+15)
pix('black')

#detail

j(-15,-255+15)
tom.color('#a50b18')
tom.begin_fill()
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15)
tom.rt(90)
tom.fd(30)
for count in range(7):
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)
    tom.fd(15)
    
tom.lt(90)
tom.fd(30)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15*6)
tom.rt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15*7)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(30)
for count in range(8):
    tom.rt(90)
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
tom.rt(90)
tom.fd(15)

tom.end_fill()


tom.color('#D61A26')
tom.begin_fill()
j(-60+15,-195-15)
tom.rt(180)
tom.fd(45)
for count in range(7):
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)
    tom.fd(15)
tom.lt(90)
tom.fd(30)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15*6)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15*6)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(30)
for count in range(5):
    tom.rt(90)
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)

tom.rt(90)
tom.fd(45+15)
for count in range(5):
    tom.rt(90)
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
tom.rt(90)
tom.fd(45)
for count in range(2):
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)

tom.lt(180)
tom.fd(15*4)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(30)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15)

for count in range(5):
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)
    tom.fd(15)

tom.end_fill()

tom.color('#D61A26')

tom.begin_fill()
j(0-15-15-15-15-15,30)
tom.fd(15)
for count in range(2):
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)
    tom.fd(15)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
for count in range(2):
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
    tom.rt(90)

tom.lt(180)
tom.fd(15)
tom.lt(90)
tom.fd(15)
tom.rt(90)
tom.fd(15)
for count in range(3):
    tom.rt(90)
    tom.fd(15)
    tom.lt(90)
    tom.fd(15)
tom.fd(15)
tom.end_fill()

j(0-15-15-15-15-15,30-15-15)
pix('#FFE1E6')
j(-75-15,0)
pix('#FFE1E6')
j(-75-15-15,0)
pix('#FFE1E6')
j(-75-15-15-15,0)
pix('#FFE1E6')
j(-75-15-15-15-15,0)
pix('#FFE1E6')
j(-75-15-15-15,-15)
pix('#FFE1E6')
j(-75-15-15-15,-15-15)
pix('#FFE1E6')
j(-75-15-15-15+15,-15-15-15)
pix('#FFE1E6')
j(-75-15-15-15+15,-15-15-15-15)
pix('#FFE1E6')
j(-120+15,-60+30)
pix('#FFE1E6')
j(-120+15,-60+30+15)
pix('#FFE1E6')
j(-120+15+15,-60+30+15)
pix('#FFE1E6')
j(-120+15+15+15*8,-60+30+15-30)
pix('#FFE1E6')
j(-120+15+15+15*8+30,-60+30+15-30+15)
pix('#FFE1E6')

j(30,0)
pix('#FFE1E6')
j(30+15,0)
pix('#FFE1E6')
j(30+15+15,0)
pix('#FFE1E6')
j(30+15+15+15,0)
pix('#FFE1E6')
j(30+15+15+15+15,0)
pix('#FFE1E6')
j(30+15+15+15+15+15,0)
pix('#FFE1E6')

j(30+15+15+15+15+15,-15)
pix('#FFE1E6')

for count in range(4):
    pix('#FFE1E6')
    tom.rt(90)

j(300-15,145)
for count in range(10):
    tom.rt(90)
    tom.fd(15)
    for count in range(4):
        pix('#ffc0cb')
        tom.rt(90)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# #Wings

# j(151,0)
# pix('black')
# j(151,15)
# pix('black')
# j(151,30)
# pix('black')
# j(151+15,45)
# pix('black')
# j(151+15+15,45)
# pix('black')
# j(151+15+15+15,45)
# pix('black')
# j(151+15+15+15+15,60)
# pix('black')
# j(151+15+15+15+15+15,60)
# pix('black')
# j(151+15+15+15+15+15+15,60)
# pix('black')
# j(151+15+15+15+15+15+15+15,75)
# pix('black')
# j(151+15+15+15+15+15+15+15+15,75)
# pix('black')
# j(151+15+15+15+15+15+15+15+15+15,75+15)
# pix('black')


# j(287,130-10)
# pix('black')
# j(287,130-10+15)
# pix('black')
# j(287,130-10+15)
# pix('black')
# j(287+15,130-10+15+15)
# pix('black')
# j(287+15,130-10+15+15+15)
# pix('black')
# j(287+15+15,130-10+15+15+15+15)
# pix('black')
# j(332,165)
# pix('black')
# j(332,165-15)
# pix('black')
# j(332,165-15-15)
# pix('black')
# j(332,165-15-15-15)
# pix('black')
# j(332-15,165-15-15-15-15)
# pix('black')
# j(332-15,165-15-15-15-15-15)
# pix('black')
# j(332-15,165-15-15-15-15-15-15)
# pix('black')
# j(332-15,165-15-15-15-15-15-15-15)
# pix('black')
# j(332-15-15,165-15-15-15-15-15-15-15)
# pix('black')
# j(332-15-15,165-15-15-15-15-15-15-15-15)
# pix('black')
# j(332-15-15-15,165-15-15-15-15-15-15-15-15)
# pix('black')
# j(332-15-15-15-15,165-15-15-15-15-15-15-15-15)
# pix('black')

# j(272+15*4,45+30)
# pix('black')
# j(272+15*4+15,45+30-15)
# pix('black')
# j(272+15*4+15,45+30-15-15)
# pix('black')
# j(272+15*4+15-15,45+30-15-15-15)
# pix('black')
# j(272+15*4+15-15-15,45+30-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15,45+30-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15,45+30-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15,45+30-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15,45+30-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15,45+30-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15,45+30-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15,45+30-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15,45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15,45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15-15-15,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15-15-15-16,45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30+15)
# pix('black')

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


# j(-1*(287),130-10)
# pix('black')
# j(-1*(287),130-10+15)
# pix('black')
# j(-1*(287),130-10+15)
# pix('black')
# j(-1*(287)+15,130-10+15+15)
# pix('black')
# j(-1*(287+15),130-10+15+15+15)
# pix('black')
# j(-1*(287+15+15),130-10+15+15+15+15)
# pix('black')
# j(-1*(332),165)
# pix('black')
# j(-1*(332),165-15)
# pix('black')
# j(-1*(332),165-15-15)
# pix('black')
# j(-1*(332),165-15-15-15)
# pix('black')
# j(-1*(332-15),165-15-15-15-15)
# pix('black')
# j(-1*(332-15),165-15-15-15-15-15)
# pix('black')
# j(-1*(332-15),165-15-15-15-15-15-15)
# pix('black')
# j(-1*(332-15),165-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(332-15-15),165-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(332-15-15),165-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(332-15-15-15),165-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(332-15-15-15-15),165-15-15-15-15-15-15-15-15)
# pix('black')

# j(-1*(272+15*4),45+30)
# pix('black')
# j(-1*(272+15*4+15),45+30-15)
# pix('black')
# j(-1*(272+15*4+15),45+30-15-15)
# pix('black')
# j(-1*(272+15*4+15-15),45+30-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15),45+30-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15),45+30-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15),45+30-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15),45+30-15-15-15-15-15)
# pix('black')
# j((-1*272+15*4+15-15-15-15-15+15),45+30-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15),45+30-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15),45+30-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15),45+30-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15),45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15),45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15-15-15),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30)
# pix('black')
# j(-1*(272+15*4+15-15-15-15-15+15+15-15-15-15-15-15-15-15-15-15+15-15-1-15-15-15-16),45+30-15-15-15-15-15-15-15-15-15-15-15-15-15-15+15-30+15)
# pix('black')


tom.hideturtle()
screen.tracer(True)
done()