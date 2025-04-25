import random
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle(shape="turtle")
tim.color("green")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
pensize =5
for num_of_sides in range(3, 10):
    tim.color(random.choice(colours))
    tim.pensize(pensize)

    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        tim.forward(100)
        tim.right(angle)
    pensize+=3

screen.exitonclick()
