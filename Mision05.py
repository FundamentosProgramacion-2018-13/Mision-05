# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Funciones que dibujan distintas cosas usando Pygame

# Importar librerías necesarias
import pygame
import random
from math import *


# Colores
blanco = (248, 248, 248)
negro = (38, 38, 38)


# Función que regresa tres valores del 0 al 255 para usarlos como colores aleatorios
def colorAleatorio():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Clase de Vector2D porque no sabía que Pygame tenía una y pues así lo hice
class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Dibuja Círculos y Rectángulos cada 10 px
def dibujarA():
    # Ajustes iniciales de PyGame
    pygame.init()

    Ancho = 800
    Alto = 800

    win = pygame.display.set_mode((Ancho, Alto))

    pygame.display.set_caption("Mision 5")

    win.fill(blanco)

    for n in range(80):
        pygame.draw.rect(win, negro, ((400-(n+1)*5), 400-(n+1)*5, (n+1)*10, (n+1)*10), 1)

    for n in range(40):
        pygame.draw.circle(win, negro, (400, 400), (n+1) * 10, 1)

    pygame.display.update()

    run = True

    reloj = pygame.time.Clock()

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


# Dibuja del punto más grande de un eje al más pequeño del otro para todos los cuadrantes
def dibujarB():
    # Ajustes iniciales de PyGame
    pygame.init()

    Ancho = 800
    Alto = 800

    win = pygame.display.set_mode((Ancho, Alto))

    pygame.display.set_caption("Mision 5")

    win.fill(blanco)

    for n in range(40):
        n = (n+1)*10
        pygame.draw.line(win, colorAleatorio(), (400 - n, 400), (400, n), 1)
        pygame.draw.line(win, colorAleatorio(), (400 + n, 400), (400, n), 1)
        pygame.draw.line(win, colorAleatorio(), (400 - n, 400), (400, 800 - n), 1)
        pygame.draw.line(win, colorAleatorio(), (400 + n, 400), (400, 800 - n), 1)

    pygame.display.update()

    run = True

    reloj = pygame.time.Clock()

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                main()


# Toma del punto anterior y avanza 2.5 más que la línea pasada perpendicularmente girando 90 grados
def dibujarC():
    # Ajustes iniciales de PyGame
    pygame.init()

    Ancho = 800
    Alto = 800

    win = pygame.display.set_mode((Ancho, Alto))

    pygame.display.set_caption("Mision 5")

    win.fill(blanco)

    puntoInicio = Vector2D(400, 400)
    i = 1
    for n in range(320):
        n = n + 1
        largo = n * 2.5

        if i > 4:
            i = 1

        if i == 1:
            puntoFinal = Vector2D(puntoInicio.x + largo, puntoInicio.y)
            pygame.draw.line(win, negro, (puntoInicio.x, puntoInicio.y), (puntoFinal.x, puntoFinal.y), 1)
            puntoInicio = puntoFinal

        if i == 2:
            puntoFinal = Vector2D(puntoInicio.x, puntoInicio.y - largo)
            pygame.draw.line(win, negro, (puntoInicio.x, puntoInicio.y), (puntoFinal.x, puntoFinal.y), 1)
            puntoInicio = puntoFinal

        if i == 3:
            puntoFinal = Vector2D(puntoInicio.x - largo, puntoInicio.y)
            pygame.draw.line(win, negro, (puntoInicio.x, puntoInicio.y), (puntoFinal.x, puntoFinal.y), 1)
            puntoInicio = puntoFinal

        if i == 4:
            puntoFinal = Vector2D(puntoInicio.x, puntoInicio.y + largo)
            pygame.draw.line(win, negro, (puntoInicio.x, puntoInicio.y), (puntoFinal.x, puntoFinal.y), 1)
            puntoInicio = puntoFinal

        i = i + 1

    pygame.display.update()

    run = True

    reloj = pygame.time.Clock()

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


# En las aristas de un dodecágono de radio 150, dibuja 12 círculos
def dibujarD():
    # Ajustes iniciales de PyGame
    pygame.init()

    Ancho = 800
    Alto = 800

    win = pygame.display.set_mode((Ancho, Alto))

    pygame.display.set_caption("Mision 5")

    win.fill(blanco)

    for n in range(12):
        pygame.draw.circle(win, negro, (400 + int(150*cos(radians(-30*(n+1)))), 400 + int(150*sin(radians(-30*(n+1))))), 150, 1)

    pygame.display.update()

    run = True

    reloj = pygame.time.Clock()

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


# Usando fórmula dada por el profesor, se aproxima al valor de PI
def calcularPi(maximo):
    total = 0.
    for n in range(1, maximo+1):
        total = total + (1/n ** 4)
    return total


# Comprueba si son divisibles entre 19 a todos los números de 3 dígitos con un contador
def comprobarNumerosDeTresDigitos():
    numeroQueEs = 0
    for n in range(100, 1000):
        if n % 19 == 0:
            numeroQueEs = numeroQueEs + 1
    return numeroQueEs


# Aunque usted no lo crea, hace las pirámides de números
def hacerPiramidesDeNumeros():
    ultimoValor = 0
    for i in range(9):
        print("%d * 8 + %d = %d" % (ultimoValor*10+i+1, i+1, ((ultimoValor*10)+i+1)*8+i+1))
        ultimoValor = ultimoValor * 10 + i + 1
    print("""""")
    ultimoValor = 0
    for n in range(9):
        print("%d * %d = %d" % (ultimoValor * 10 + 1, ultimoValor * 10 + 1, (ultimoValor * 10 + 1)**2))
        ultimoValor = ultimoValor * 10 + 1


def leerOpcionMenu():
    instruccion = int(input("""
Mision 5: Seleccione que quiere hacer:
1. Dibujar cuadrados y circulos
2. Dibujar parabolas
3. Dibujar Espiral
4. Dibujar circulos
5. Aproximar PI
6. Contar divisibles entre 19
7. Imprimir piramides de numeros
0. Salir
¿Que desea hacer?
- """))

    return instruccion


def main():
    instruccion = leerOpcionMenu()

    while instruccion != 0:
        if instruccion <= 4:
            if instruccion == 1:
                dibujarA()
            if instruccion == 2:
                dibujarB()
            if instruccion == 3:
                dibujarC()
            if instruccion == 4:
                dibujarD()
        else:
            if instruccion == 5:
                maximo = int(input("Valor del último divisor: "))
                print("El valor calculado de Pi es: %f" % ((90 * calcularPi(maximo)) ** .25))
            if instruccion == 6:
                print("La cántidad de enteros divisibles entre 3 conformados por 3 dígitos es: %d" % comprobarNumerosDeTresDigitos())
            if instruccion == 7:
                hacerPiramidesDeNumeros()
            else:
                print("Error en la entrada, intente de nuevo")
        instruccion = leerOpcionMenu()

    print("Termina programa")


main()
