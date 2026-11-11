import turtle as t
import random

box = t.Turtle()
box.shape("square")
box.width(10)
box.teleport(-315,-315)
for x in range(4):
    box.forward(630)
    box.left(90)
box.hideturtle()

def bouncyThing(shape):
    logo = t.Turtle()
    logo.shape(shape)
    logo.up()
    logo.speed(100)
    logo_angle = random.randint(1,360)

    while True:
        logo.setheading(logo_angle)
        logo.forward(3)
        if logo.ycor() >= 300:
            logo_angle = random.randint(180, 360)
        if logo.ycor() <= -300:
            logo_angle = random.randint(1, 180)
        if logo.xcor() >= 300:
            logo_angle = random.randint(90, 270)
        if logo.xcor() <= -300:
            logo_angle = random.randint(270, 450)


bouncyThing("turtle")



