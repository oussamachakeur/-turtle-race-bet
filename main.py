import random
from turtle import Turtle , Screen

screen= Screen()
screen.setup(width=500 , height=400)
user_bet =screen.textinput(title=" make a bet" , prompt="choose a color")

turtle_color = ['red' , 'purple','pink','blue']
y_position=[50 , 70 , 30 ,10]
all_turtle=[]

for index in range(0,4):
    new_turtle= Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(turtle_color[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[index])
    all_turtle.append(new_turtle)

if user_bet:
    turtle_on =True
while turtle_on :

    for turtle in all_turtle:
        if turtle.xcor()>=230:
            turtle_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you won! , {winner} won the race")
            else :
                print(f"you lost! , {winner} won the race")
        rand_distance = random.randint(0,5)
        turtle.forward(rand_distance)










screen.exitonclick()
