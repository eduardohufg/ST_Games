from random import randrange
from turtle import *

from freegames import square, vector

# Lista de colores diferentes (excepto el rojo)
colors = ['green', 'blue', 'yellow', 'purple', 'orange']

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambiar la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Devuelve True si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mover la serpiente un segmento hacia adelante."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Serpiente:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:

        color_index = randrange(len(colors))
        square(body.x, body.y, 9, colors[color_index])

        if(randrange(0,500) > 490):
            if(food.x > 190 or food.x < -200 or food.y > 190 or food.y < -200):
                pass
            else:
                food.x = food.x + 10
                food.y = food.y + 10
        if(randrange(0,500) <10):
            if(food.x > 190 or food.x < -200 or food.y > 190 or food.y < -200):
                pass
            else:
                food.x = food.x - 10
                food.y -= 10

    # Seleccionar un color aleatorio para la comida
    food_color = colors[randrange(len(colors))]
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
