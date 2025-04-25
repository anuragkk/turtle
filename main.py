from turtle import Turtle, Screen

screen = Screen()
tim = Turtle(shape="turtle")
tim.color("green")

for num_of_sides in range(3, 10):

    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        tim.forward(100)
        tim.right(angle)

screen.exitonclick()
