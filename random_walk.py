import turtle as t
import random

tim = t.Turtle(shape="turtle")

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",]
directions = [0, 90, 180, 270]


while True:
    tim.speed("fastest")

    tim.color(random.choice(colours))
    tim.pensize(10)
    tim.forward(random.randint(1,100))
    tim.setheading(random.choice(directions))
