from turtle import Turtle, Screen
import random
screen = Screen()
user_guess = screen.textinput(title="Khaled Melizi", prompt="Make a guess which turtle win? type the color:").lower()
colors = ['red', 'green', 'crimson', 'blue', 'purple']
screen.setup(600, 450)
space_between = 40
turtles = []
for clr in colors:
    player = Turtle('turtle')
    player.penup()
    player.color(clr)
    player.goto(-250, space_between - 200)
    space_between += 80
    turtles.append(player)
start = False
if user_guess:
    if user_guess in colors:
        start = True
    else:
        print("restart the game because you didn't enter color value")
while start:
    for turtle in turtles:
        if turtle.xcor() > 275:
            start = False
            if turtle.pencolor() == user_guess:
                print(f'You win: the {turtle.pencolor()} turtle is the winner')
            else:
                print(f'You lose: the {turtle.pencolor()} turtle is the winner')

        turtle.forward(random.randint(1,10))












































screen.exitonclick()