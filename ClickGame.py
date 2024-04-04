# Pony Clicking Game

import turtle

wn = turtle.screen()
wn.title("CLICK THE PONY")
wn.bgcolor("white")

wn.register_shape("c:\Users\eholzer2\Documents\03Einsatzstelle_CAE_VV_IT_FoE\PythonExercises\MustangLogo.png")

pony = turtle.Turtle()
pony.shape("c:\Users\eholzer2\Documents\03Einsatzstelle_CAE_VV_IT_FoE\PythonExercises\MustangLogo.png")
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