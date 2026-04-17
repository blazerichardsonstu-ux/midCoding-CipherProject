import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(12):
    for j in range(5):
        t.forward(23)
        t.right(10)
    t.right(7)

turtle.done()
