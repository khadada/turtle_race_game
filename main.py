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

print(turtles)
is_end = False
while not is_end:
    for turtle in turtles:
        if turtle.xcor() > 275:
            is_end = True
            if turtle.pencolor() == user_guess:
                print(f'You win: {turtle.pencolor()} is the winner')
            else:
                print(f'You lose: {turtle.pencolor()} is the winner')

        turtle.forward(random.randint(1,7))












































screen.exitonclick()