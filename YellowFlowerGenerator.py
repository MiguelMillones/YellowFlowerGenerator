import turtle

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Configurar el lápiz
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)

def petalo():
    pen.color("orange")
    pen.fillcolor("yellow")
    pen.right(90)
    pen.begin_fill()
    pen.circle(100, 90)
    pen.left(90)
    pen.circle(100, 90)
    pen.end_fill()

def petalos():
    # Ubicación del inicio del trazo
    pen.up()              # Levantar el lápiz
    pen.setpos(0,100)     # Mover lápiz a las coordenadas x,y
    pen.down()            # Baja el lápiz
    for _ in range(8):
        petalo()
        pen.forward(45)
        pen.left(45)
    pen.left(22.5)
    for _ in range(8):
        petalo()
        pen.forward(45)
        pen.left(45)

def tallo():
    pen.up()              # Levantar el lápiz
    pen.setpos(0,-250)     # Mover lápiz a las coordenadas x,y
    pen.down()            # Baja el lápiz
    pen.color("black")
    pen.fillcolor("green")
    pen.begin_fill()
    pen.left(45)
    pen.forward(25.45)
    pen.left(45)
    pen.forward(357)
    pen.left(90)
    pen.forward(18)
    pen.left(90)
    pen.forward(375)
    pen.end_fill()

def centro():
    pen.up()              # Levantar el lápiz
    pen.setpos(-50,100)     # Mover lápiz a las coordenadas x,y
    pen.down()            # Baja el lápiz
    pen.color("black")
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    print(pen.position())

# Dibujar el tallo
tallo()
# Dibujar los pétalos de la flor
petalos()
# Dibujar el centro de la flor
centro()


# Ocultar el lápiz y cerrar la ventana haciendo clic en ella
pen.hideturtle()
screen.exitonclick()
