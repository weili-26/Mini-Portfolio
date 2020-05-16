

import turtle as t


def rec(length, width, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for i in range(1,3):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed(50)
t.getscreen().bgcolor('dodger blue')
t.goto(-100,-150)
rec(50,20,'blue')
t.goto(-20,-150)
rec(50,20,'blue')
t.goto(-20,-50)
rec(15,100,'grey')
t.goto(-65,-50)
rec(15,100,'grey')
t.goto(-85,100)
rec(100,150,'red')
t.goto(-150,70)
rec(65,15,'grey')
t.goto(-150,110)
rec(15,40,'grey')
t.goto(15,70)
rec(65,15,'grey')
t.goto(70,115)
rec(15,60,'grey')
t.goto(-50,120)
rec(35,20,'grey')
t.goto(-155,130)

rec(30,25,'green')
t.goto(-145,130)
rec(10,15,t.bgcolor())
t.goto(65,130)
rec(30,25,'green')
t.goto(72,130)
rec(15,10,t.bgcolor())

t.goto(-75,170)
rec(80,50,'red')
t.goto(-60,160)
rec(50,10,'white')
t.goto(-60,160)
rec(5,5,'black')
t.goto(-25,155)
rec(5,5,'black')
t.goto(-55,135)
t.right(5)
rec(40,5,'black')






t.hideturtle()

t.done()
