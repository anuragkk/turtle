import random
from turtle import Turtle, Screen

screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which color you choose")
y_positions = [210, 170, 130, 70, 30, -30]
screen.setup(500, 500)
all_turtles = []
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

for color, y_position in zip(colours, y_positions):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)


is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Move each turtle forward by a random amount
        turtle.forward(random.randint(0, 10))

        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")

# Exit on click
screen.exitonclick()
