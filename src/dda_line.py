import pygame_plotter as pgp


def dda_line(x1, y1, x2, y2, color=(0, 255, 0)):
    dx = x2 - x1
    dy = y2 - y1

    step = abs(dy)
    if abs(dx) > abs(dy):
        step = abs(dx)

    xn = dx / step
    yn = dy / step

    for i in range(1, step + 1):
        pgp.draw_pixel(x1, y1, color)
        x1 = round(x1 + xn)
        y1 = round(y1 + yn)


def draw():
    pgp.draw_graph()
    dda_line(0, 0, 0, 10, (211, 245, 22))
    dda_line(20, 0, 0, 0, (100, 150, 230))
    dda_line(-12, -10, 0, 0, (0, 0, 255))
    dda_line(2, 5, 1, 1, (255, 0, 255))


pgp.show(draw, (), 800, 400, 15, 'DDA Line')
