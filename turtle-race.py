import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightgreen')

andy = turtle.Turtle()
tess = turtle.Turtle()
andy.color('red')
tess.color('blue')
andy.shape('turtle')
tess.shape('turtle')

andy.up()
tess.up()
andy.goto(-200, 20)
tess.goto(-200, -20)
movA = movT = -200

for i in range(50):
	move_andy = random.randrange(1, 20)
	move_tess = random.randrange(1, 20)
	movA = movA + move_andy 
	movT = movT + move_tess
	andy.goto(movA, 20)
	tess.goto(movT, -20)

wn.exitonclick()