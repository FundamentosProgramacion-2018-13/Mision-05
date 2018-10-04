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

    run = True

    reloj = pygame.time

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                main()

    pygame.display.update()


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

    run = True

    reloj = pygame.time

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                main()

    pygame.display.update()


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

        run = True

        reloj = pygame.time

        # Lógica de pygame que básicamente es la función main pero en tiempo real
        while run:
            reloj.tick(4)  # Para salvar al planeta

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    main()

        pygame.display.update()


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

    run = True

    reloj = pygame.time

    # Lógica de pygame que básicamente es la función main pero en tiempo real
    while run:
        reloj.tick(4)  # Para salvar al planeta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                main()

    pygame.display.update()


# Usando fórmula dada por el profesor, se aproxima al valor de PI
def calcularPi():
    maximo = int(input("Valor del último divisor: "))
    total = 0.
    for n in range(1, maximo+1):
        total = total + (1/n ** 4)
    print("El valor calculado de Pi es: %f" % ((90 * total) ** .25))


# Comprueba si son divisibles entre 19 a todos los números de 3 dígitos con un contador
def comprobarNumerosDeTresDigitos():
    numeroQueEs = 0
    for n in range(100, 1000):
        if n % 19 == 0:
            numeroQueEs = numeroQueEs + 1
    print("La cántidad de enteros divisibles entre 3 conformados por 3 dígitos es: %d" % numeroQueEs)


# Aunque usted no lo crea, hace las pirámides de números
def hacerPiramidesDeNumeros():
    ultimoValor = 0
    for i in range(9):
        print("%d * 8 + %d = %d" % (ultimoValor*10+i+1, i+1, ((ultimoValor*10)+i+1)*8+i+1))
        ultimoValor = ultimoValor * 10 + i + 1

    ultimoValor = 0
    for n in range(9):
        print("%d * %d = %d" % (ultimoValor * 10 + 1, ultimoValor * 10 + 1, (ultimoValor * 10 + 1)**2))
        ultimoValor = ultimoValor * 10 + 1


def main():
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
            calcularPi()
        if instruccion == 6:
            comprobarNumerosDeTresDigitos()
        if instruccion == 7:
            hacerPiramidesDeNumeros()
        if instruccion == 0:
            pass
        else:
            main()


main()

"""# Toma inputs del teclado y llama función pertinente
    keys = pygame.key.get_pressed()

    if keys[pygame.K_0]:
        run = False

    if keys[pygame.K_1]:
        win.fill(blanco)
        dibujarA()

    if keys[pygame.K_2]:
        win.fill(blanco)
        dibujarB()

    if keys[pygame.K_3]:
        win.fill(blanco)
        dibujarC()

    if keys[pygame.K_4]:
        win.fill(blanco)
        dibujarD()

    if keys[pygame.K_5]:
        win.fill(blanco)
        calcularPi()

    if keys[pygame.K_6]:
        win.fill(blanco)
        comprobarNumerosDeTresDigitos()

    if keys[pygame.K_7]:
        win.fill(blanco)
        hacerPiramidesDeNumeros()

    if keys[pygame.K_8]:
        modoPeda = True

    pygame.font.init()
    myfont = pygame.font.SysFont('Helvetica', 20, True)
    textsurface = myfont.render("Mision 5: Seleccione que quiere hacer:", False, darColorATexto(modoPeda))
    textsurface1 = myfont.render("1. Dibujar cuadrados y circulos ", False, darColorATexto(modoPeda))
    textsurface2 = myfont.render("2. Dibujar parabolas", False, darColorATexto(modoPeda))
    textsurface3 = myfont.render("3. Dibujar Espiral", False, darColorATexto(modoPeda))
    textsurface4 = myfont.render("4. Dibujar circulos", False, darColorATexto(modoPeda))
    textsurface5 = myfont.render("5. Aproximar PI", False, darColorATexto(modoPeda))
    textsurface6 = myfont.render("6. Contar divisibles entre 19", False, darColorATexto(modoPeda))
    textsurface7 = myfont.render("7. Imprimir piramides de numeros", False, darColorATexto(modoPeda))
    textsurface10 = myfont.render("8. Sorpresa para que me de mis 100hp", False, darColorATexto(modoPeda))
    textsurface8 = myfont.render("0. Salir", False, darColorATexto(modoPeda))
    textsurface9 = myfont.render("-Que desea hacer?", False, darColorATexto(modoPeda))

    win.blit(textsurface, (0, 0))
    win.blit(textsurface1, (0, 20))
    win.blit(textsurface2, (0, 40))
    win.blit(textsurface3, (0, 60))
    win.blit(textsurface4, (0, 80))
    win.blit(textsurface5, (0, 100))
    win.blit(textsurface6, (0, 120))
    win.blit(textsurface7, (0, 140))
    win.blit(textsurface10, (0, 160))
    win.blit(textsurface8, (0, 180))
    win.blit(textsurface9, (0, 200))"""