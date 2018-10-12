# Autor: Ithan Alexis Pérez Sánchez, A01377717
# Descripción: Mision 5 todas las funciones mostradas en un menu

# El codigo empieza después de esta linea

import random
import pygame

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

def dibujarCuadricula(ventana):
    for y in range(0, 410, 10):
        Random = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana, Random, (y, ALTO // 2), (ANCHO // 2, ALTO // 2 - y))
        pygame.draw.line(ventana, Random, (y, ALTO // 2), (ANCHO // 2, ALTO // 2 + y))
        pygame.draw.line(ventana, Random, (ALTO // 2, y), (ANCHO // 2 + y, ALTO // 2))
        pygame.draw.line(ventana, Random, (ANCHO - y, ANCHO // 2), (ANCHO // 2, ALTO // 2 + y))

def dibujarCirculosyCuadrados(ventana):
    for radio in range (10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2 , ALTO//2), radio, 1)
    for rect in range (10, ALTO//2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO//2-rect, ALTO//2-rect, 2*rect, 2*rect), 1)


def dibujarCirculos(ventana):
    for y in range(10, ANCHO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + 129), (ALTO // 2 - 75)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + 75), (ALTO // 2 - 129)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2), (ALTO // 2 - 150)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 75), (ALTO // 2 - 129)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 129), (ALTO // 2 - 75)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 150), (ALTO // 2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 129), ALTO // 2 + 75), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 75), (ALTO // 2 + 129)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2), (ALTO // 2 + 150)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + 75), (ALTO // 2 + 129)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + 129), (ALTO // 2 + 75)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + 150), ALTO // 2), 150, 1)


def dibujarCuadradoLineas(ventana):
    pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 10, ALTO // 2 - 10), (ANCHO // 2 + 10, ALTO // 2))
    pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 10, ALTO // 2), (ANCHO // 2 + 5, ALTO // 2))

    for y in range(0, ANCHO // 2, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - y, ALTO // 2 - y), (ANCHO // 2 + y, ALTO // 2 - y))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - y, ALTO // 2 - y), (ANCHO // 2 - y, ALTO // 2 + y))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - y, ALTO // 2 + y), ((ANCHO // 2 + 10) + y, ALTO // 2 + y))
        pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 + 10) + y, (ALTO // 2 - 10) - y), ((ANCHO // 2 + 10) + y, ALTO // 2 + y))

def dibujar1():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False


    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
        ventana.fill(BLANCO)

        dibujarCirculosyCuadrados(ventana)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()  # termina pygame

def dibujar2():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False


    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
        ventana.fill(BLANCO)

        dibujarCuadricula(ventana)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()  # termina pygame

def dibujar3():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False


    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
        ventana.fill(BLANCO)

        dibujarCuadradoLineas(ventana)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()  # termina pygame


def dibujar():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False


    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
        ventana.fill(BLANCO)

        dibujarCirculos(ventana)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()  # termina pygame


def Piramide2():
    suma = 0
    suma2 = 8
    for y in range(1, 10):
        suma = (suma * 10) + y
        print(suma, "*", suma2, "+", y, "=", suma2 * suma + y)


def Piramide():
    suma = 0
    for y in range(1, 10):
        suma = suma * 10 + 1
        print(suma, "*", suma, "=", suma * suma)


def aproximarValorPI(Terminos):
    suma = 0
    for denominador in range(1, Terminos + 1):
        suma += 1 / denominador ** 4
    return (90 * suma) ** 0.25


def Divisibles19():
    contador = 0
    for y in range(100, 1000):
        if y % 19 == 0:
            contador += 1
    return contador

def menu():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    Usuario = int(input("Escoge el número que desees saber: "))
    return Usuario


def main():
    Usuario = menu()
    while Usuario != 0:
        if Usuario == 1:
            dibujar1()
            Usuario = menu()

        elif Usuario == 2:
            dibujar2()
            Usuario = menu()

        elif Usuario == 3:
            dibujar3()
            Usuario = menu()

        elif Usuario == 4:
            dibujar()
            Usuario = menu()

        elif Usuario == 5:
            Terminos = int(input("Ingresa los terminos que desee: "))
            AproximaciónPi = aproximarValorPI(Terminos)
            print("PI = ", AproximaciónPi)
            Usuario = menu()

        elif Usuario == 6:
            print(Divisibles19())
            Usuario = menu()

        elif Usuario == 7:
            Piramide2()
            Piramide()
            Usuario = menu()

    print("Bye-Bye")


main()