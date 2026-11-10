import turtle as t
import random

logo = t.Turtle()

logo.shape("circle")
logo.up()
logo.speed(100)

box = t.Turtle()
box.shape("square")
box.width(10)
box.teleport(-310,-310)
for x in range(4):
    box.forward(620)
    box.left(90)
box.hideturtle()

logo_angle = 100

while True:
    logo.setheading(logo_angle)
    logo.forward(1)
    if logo.ycor() >= 300:
        logo_angle = random.randint(180, 360)
    if logo.ycor() <= -300:
        logo_angle = random.randint(1, 180)
    if logo.xcor() >= 300:
        logo_angle = random.randint(90, 270)
    if logo.xcor() <= -300:
        logo_angle = random.randint(270, 450)




