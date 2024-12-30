# Turtle-Race game gui

import random
import turtle as t

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']


screen = t.Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet:", prompt=f"Which Turtle will win the race ({color_list})?")

instance_list = []
for color in color_list:
    variable = color + "_turtle"
    variable = t.Turtle(shape="turtle")
    variable.color(color)
    instance_list.append(variable)

x_coordinate = -245
y_coordinate = -220

for instance in instance_list:
    y_coordinate += 60
    instance.penup()
    instance.goto(x_coordinate, y_coordinate)



is_race_on = True
while is_race_on:
    for instance in instance_list:
        instance.speed(50)
        if instance.xcor() > 230:
            is_race_on = False
            winning_color = instance.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} turtle won the race!!!")
            else:
                print(f"You lost! {winning_color} turtle won the race!!!")


        instance.forward(random.randint(0,100))



screen.exitonclick()

