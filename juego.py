import pygame
import random
import math

ANCHO = 800
ALTO = 800

BLANCO = (245, 245, 245)
NEGRO = (20, 20, 20)


def dibujarCuadradosCirculos():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for delta in range(1, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - delta, ALTO // 2 - delta, delta * 2, delta * 2), 1)
        for radio in range(1, ANCHO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarParabolaDeColores():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for delta in range(0, ALTO // 2 + 1, 10):
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 + delta, ALTO // 2), (ANCHO // 2, ALTO - delta), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 + delta, ALTO // 2), (ANCHO // 2, 0 + delta), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 - delta, ALTO // 2), (ANCHO // 2, ALTO - delta), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 - delta, ALTO // 2), (ANCHO // 2, 0 + delta), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarEspiral():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for delta in range(0, ALTO // 2, 10):
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 5 + delta, ALTO // 2 + 5 + delta),
                                 (ANCHO // 2 + 5 + delta, ALTO // 2 - 5 - delta))
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 5 - delta, ALTO // 2 - 5 + delta),
                                 (ANCHO // 2 - 5 + delta, ALTO // 2 - 5 + delta))
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 5 - delta, ALTO // 2 - 5 + delta),
                                 (ANCHO // 2 - 5 - delta, ALTO // 2 - 5 - delta))
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 5 - delta, ALTO // 2 - 5 - delta),
                                 (ANCHO // 2 + 5 + delta, ALTO // 2 - 5 - delta))

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarDoceCirculos():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for angulo in range(0, 360, 30):
            pygame.draw.circle(ventana, NEGRO, (int(ANCHO // 2 + 150 * math.sin(math.radians(angulo))), int(ALTO // 2 + 150 * math.cos(math.radians(angulo)))), 150, 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def aproximarPi():
    terminos = int(input("¿Cuántos términos quieres sumar? "))
    suma = 0
    for denominador in range(1, terminos):
        suma = 1/denominador**4 + suma
    pi = (suma*90)**.25
    print("pi = ", pi)


def calcularDivisibles():
    contador = 0
    for numero in range(100, 1000):
        if numero % 19 == 0:
            contador += 1
        else:
            pass
    print("Hay %d números de tres dígitos divisibles entre 19" % contador)


def multiplicarPiramides():
    suma = 0
    for n in range(1, 10):
        suma = (suma*10) + n
        print(suma, "* 8 + %d = " % n, suma * 8 + n)

    contador = 0
    suma = 0
    for x in range(9):
        suma = (suma*10) + 1
        print("%d * %d =" % (suma, suma), suma**2)
        contador += 1


def leerOpcion():
    print("""Misión 5. Seleccione qué quiere hacer.
    1. Dibujar cuadros y círculos
    2. Dibujar parábolas
    3. Dibujar espiral
    4. Dibujar círculos
    5. Aproximar PI
    6. Contar divisibles entre 19
    7. Imprimir pirámides de números
    0. Salir""")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion


def main():
    opcion = leerOpcion()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadradosCirculos()
        elif opcion == 2:
            dibujarParabolaDeColores()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarDoceCirculos()
        elif opcion == 5:
            aproximarPi()
        elif opcion == 6:
            calcularDivisibles()
        elif opcion == 7:
            multiplicarPiramides()
        opcion = leerOpcion()
    print("¡Hasta la próxima!")


main()
