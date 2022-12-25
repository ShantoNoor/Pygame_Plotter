import pygame_plotter as pgp


def bresenhams_line(x1, y1, x2, y2, color=(0, 255, 0)):
    dx = x2 - x1
    dy = y2 - y1
    p0 = 2 * dy - dx

    m = 1
    if dx != 0:
        m = dy / dx

    p = p0

    if m < 1:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        while x1 <= x2:
            pgp.draw_pixel(x1, y1, color)

            x1 += 1
            if p < 0:
                p = p0 + 2 * dy
            else:
                y1 += 1
                p = p0 + 2 * dy - 2 * dx
    else:
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        while y1 <= y2:
            pgp.draw_pixel(x1, y1, color)

            y1 += 1
            if p < 0:
                p = p0 + 2 * dx
            else:
                x1 += 1
                p = p0 + 2 * dx - + 2 * dy


def draw():
    pgp.draw_graph()
    bresenhams_line(0, 0, 0, 10, (211, 245, 22))
    bresenhams_line(20, 0, 0, 0, (100, 150, 230))
    bresenhams_line(-12, -10, 0, 0, (0, 0, 255))
    bresenhams_line(2, 5, 1, 1, (255, 0, 255))


pgp.show(draw, (), 800, 400, 15, "Bresenham's Line")
