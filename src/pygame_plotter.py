import pygame as pg

WIDTH, HEIGHT = 0, 0
STEP = 0
NAME = ''
WIN = None

def to(x, y): # translate origin
    return x + WIDTH // 2 - STEP//2, -y + HEIGHT // 2 + STEP//2


def draw_pixel(x, y, color=(0, 255, 0)):
    x = x * STEP
    y = y * STEP
    x, y = to(x, y)
    pg.draw.rect(WIN, color, (x, y-STEP, STEP, STEP))


def draw_graph():
    rows = HEIGHT // STEP
    for i in range(-rows//2, rows//2 + rows):
        pg.draw.line(WIN, (255, 255, 255), to(-WIDTH//2, i*STEP), to(WIDTH//2 + STEP, i*STEP), 1)

    cols = WIDTH // STEP
    for i in range(-cols//2, cols//2 + cols):
        pg.draw.line(WIN, (255, 255, 255), to(i*STEP, -HEIGHT//2), to(i*STEP, HEIGHT//2+STEP), 1)

    # pg.draw.line(WIN, (255, 0, 0), to(-WIDTH // 2, 0), to(WIDTH // 2 + STEP, 0), 1)
    # pg.draw.line(WIN, (255, 0, 0), to(0, -HEIGHT // 2), to(0, HEIGHT // 2 + STEP), 1)


def cb():
    draw_pixel(0, 0)
    draw_pixel(1, 1)


def show(call, args, width=500, height=500, step=20, name='PyGame Ploter'):
    global WIN
    global WIDTH
    global HEIGHT
    global STEP

    WIDTH = width
    HEIGHT = height
    STEP = step

    WIN = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(name)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # draw_graph()
        call(*args)
        pg.display.flip()


if __name__ == '__main__':
    show(cb, (), 500, 600, 20)