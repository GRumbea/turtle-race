from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
is_race_on = False
x = -230
y = -100
for turtle in turtles:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(turtle)
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 35

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You lost! The {winning_color} turtle is the winner! ")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()
