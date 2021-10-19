from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'green', 'orange', 'yellow', 'blue', 'purple']
y_shift = 0
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=100 - y_shift)
    all_turtles.append(new_turtle)
    y_shift += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle wins!")
            else:
                print(f"You've lost! The {winning_color} turtle wins!")
            is_race_on = False
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()