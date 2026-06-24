import turtle as t
import random

screen = t.Screen()
screen.bgcolor("black")

t.speed(0)
t.hideturtle()
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

leaf_colors = ["#00ff7f", "#32cd32", "#7fff00", "#adff2f"]

flower_colors = ["#ff69b4", "#ff1493", "#ffd700", "#ffffff"]

def tree(length):

    if length < 12:
        t.color(random.choice(leaf_colors))
        t.dot(random.randint(8, 16))

        if random.random() < 0.25:
            t.color(random.choice(flower_colors))
            t.dot(random.randint(4, 8))

        return

    t.color("#8B4513")
    t.pensize(length / 10)
    t.forward(length)

    angle = random.randint(18, 35)

    t.left(angle)
    tree(length * random.uniform(0.68, 0.80))

    t.right(angle * 2)
    tree(length * random.uniform(0.68, 0.80))

    t.left(angle)
    t.backward(length)

tree(120)
t.done()