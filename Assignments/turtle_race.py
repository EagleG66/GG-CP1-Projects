# GLENN GUDMUNSON turtle race

import turtle as t
import random as rand
import time



turtle_green = t.Turtle()
turtle_green.color("green")
turtle_green.shape("turtle")
turtle_green.hideturtle()
turtle_green.teleport(-800, 75)
turtle_green.up()
turtle_green.showturtle()
turtle_green.speed(2)

turtle_red = t.Turtle()
turtle_red.color("red")
turtle_red.shape("turtle")
turtle_red.hideturtle()
turtle_red.teleport(-800, 25)
turtle_red.up()
turtle_red.showturtle()
turtle_red.speed(2)

turtle_blue = t.Turtle()
turtle_blue.color("blue")
turtle_blue.shape("turtle")
turtle_blue.hideturtle()
turtle_blue.teleport(-800, -25)
turtle_blue.up()
turtle_blue.showturtle()
turtle_blue.speed(2)

turtle_yellow = t.Turtle()
turtle_yellow.color("yellow")
turtle_yellow.shape("turtle")
turtle_yellow.hideturtle()
turtle_yellow.teleport(-800, -75)
turtle_yellow.up()
turtle_yellow.showturtle()
turtle_yellow.speed(2)

finish_line = t.Turtle()
finish_line.hideturtle()
finish_line.teleport(800, 100)
finish_line.width(10)
finish_line.goto(800, -100)

win = False


turtles = [turtle_green, turtle_blue, turtle_red, turtle_yellow]

while True:
    for turt in turtles:
        if turt.xcor() >= 800:
            if turt == turtles[0]:
                print("GREEN WINS!!!")
            if turt == turtles[1]:
                print("BLUE WINS!!!")
            if turt == turtles[2]:
                print("RED WINS!!!")
            if turt == turtles[3]:
                print("YELLOW WINS!!!")
            win = True
            break
        else:
            turt.forward(rand.randint(1,20))
            time.sleep(round(rand.uniform(0, 0.1), 2))
    if win:
        break


