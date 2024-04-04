# Pony Clicking Game

import turtle

wn = turtle.Screen()
wn.title("CLICK THE PONY")
wn.bgcolor("white")

wn.register_shape("MustangLogo.gif")

pony = turtle.Turtle()
pony.shape("MustangLogo.gif")
pony.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0,400)
pen.write(f"Clicks: {clicks}", align="center", font=("Bauhaus 93", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks {clicks}", align="center", font=("Bauhaus 93", 32, "normal"))

pony.onclick(clicked)

wn.mainloop()