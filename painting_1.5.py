# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# # rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# print(colors)
# # for color in colors:
# #     r = color.rgb.r
# #     g=color.rgb.g
# #     b=color.rgb.b
# #     rgb_colors.append((r,g,b))
# # print(rgb_colors)
#
# rgb_colors=[(color.rgb.r,color.rgb.g,color.rgb.b) for color in colors]
# print(rgb_colors)
import random
from turtle import Turtle, Screen

rgb_colors = [(202, 164, 110), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("white")
tim.hideturtle()
dot_size = 20
spacing = 40
tim.penup()
tim.speed("fastest")

# Move to starting position
tim.setheading(225)  # 225 degrees to move diagonally left-down
tim.forward(300)
tim.setheading(0)  # Face to the right

rows = 10
columns = 10

for row in range(rows):
    for col in range(columns):
        color = random.choice(rgb_colors)
        tim.dot(dot_size, color)
        tim.forward(spacing)

    # Go back to start of the row
    tim.backward(spacing * columns)  # Return to the start of the row
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)

screen.exitonclick()
