import pygame_plotter as pgp

def cbb(m, c):
    pgp.put_pixel(10, 10)
    pgp.put_pixel(5, 3, (255, 0, 0))
    pgp.put_pixel(-20, 3)
    print(m, c)


pgp.show(cbb, (3, 2), 800, 400, 15, 'Line')