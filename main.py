import turtle
import random

window = turtle.Screen()
window.tracer(0)
window.title('Pacman By farrius')
window.bgcolor('black')
window.setup(1920, 1080)

pacman = turtle.Turtle()
pacman.speed(0)
pacman.penup()
pacman.color('yellow')
pacman.shape('circle')
pacman.direction = 'stop'

foods =[]
for food in range(40):
    food=turtle.Turtle()
    food.speed(0)
    food.penup()
    food.color('orange')
    food.shape('triangle')
    food.shapesize(stretch_wid=0.4, stretch_len=0.4)
    x=random.randint(-280,280)
    y=random.randint(-280,280)
    food.setposition(x,y)
    foods.append(food)



def movement():
    if pacman.direction == 'up':
        y = pacman.ycor()
        y += .1
        pacman.sety(y)

    if pacman.direction == 'down':
        y = pacman.ycor()
        y -= .1
        pacman.sety(y)

    if pacman.direction == 'left':
        x = pacman.xcor()
        x -= .1
        pacman.setx(x)

    if pacman.direction == 'right':
        x = pacman.xcor()
        x += .1
        pacman.setx(x)


def moveUp():
    pacman.direction = 'up'


def moveDown():
    pacman.direction = 'down'


def moveLeft():
    pacman.direction = 'left'


def moveRight():
    pacman.direction = 'right'


window.listen()
window.onkeypress(moveUp, 'Up')
window.onkeypress(moveDown, 'Down')
window.onkeypress(moveLeft, 'Left')
window.onkeypress(moveRight, 'Right')

while True:
    window.update()

    for food in foods:
        if pacman.distance(food) < 10:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x,y)

    movement()
