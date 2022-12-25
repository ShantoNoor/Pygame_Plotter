import pygame_plotter as pgp


def line(x1, y1, x2, y2, color=(0, 255, 0)):
    d = x1 - x2
    m = y1 - y2
    c = None

    if d == 0:
        m = float('inf')
    else:
        m = m / d
        c = y1 - m * x1

    if m <= 1:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        while x1 <= x2:
            pgp.draw_pixel(x1, y1, color)
            x1 += 1
            y1 = round(m * x1 + c)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        while y1 <= y2:
            pgp.draw_pixel(x1, y1, color)
            y1 += 1
            if m != float('inf'):
                x1 = round((y1 - c) / m)


def draw():
    pgp.draw_graph()
    line(0, 0, 0, 10, (211, 245, 22))
    line(20, 0, 0, 0, (100, 150, 230))
    line(-12, -10, 0, 0, (0, 0, 255))
    line(2, 5, 1, 1, (255, 0, 255))


pgp.show(draw, (), 800, 400, 15, 'Line')
