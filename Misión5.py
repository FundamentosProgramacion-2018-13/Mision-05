# encoding: UTF-8
# Autor de versión usada de pygame (programa base): Roberto Martínez Román
# Programa que sirve para desplegar opciones a un usuario, ya sean dibujos o calculos
# Autor programas Javier Alexandro Vargas Sánchez A01377718

import math

import random

import pygame

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def leerOpcionMenu():  # Despliega las opciones de actividades al usuario para que escoja una
    print("Misión 5. Seleccione qué quiere hacer")
    print("1. Dibujar cuadros y círculos ")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def dibujarCircYCuadr():  # Despliega el primer dibujo de unos círculos y cuadros

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        x = ANCHO // 2
        y = ALTO // 2

        for circulo in range(10, x, 10):
            pygame.draw.circle(ventana, NEGRO, (x, y), (circulo + 1), 1)

        for cuad in range(10, x, 10):
            pygame.draw.rect(ventana, NEGRO, (x - cuad, y - cuad, cuad * 2, cuad * 2), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def dibujarEstrella():  # Despliega el segundo dibujo de una estrella a partir de parabolas en los cuadrantes del plano cartesiano

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for posicion in range(0, 400, 10):
            RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            # El randomizador lo usamos 3 veces por el rgb

            pygame.draw.line(ventana, RANDOM, (posicion, 400), (400, 400 - posicion), 1)
            pygame.draw.line(ventana, RANDOM, (800 - posicion, 400), (400, 400 - posicion), 1)
            pygame.draw.line(ventana, RANDOM, (posicion, 400), (400, 400 + posicion), 1)
            pygame.draw.line(ventana, RANDOM, (800 - posicion, 400), (400, 400 + posicion), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def dibujarEspiralCuadrado():  # Despliega el tercer dibujo de un espiral, existe un aumento de 5 unidades entre linea y linea
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        x = ANCHO // 2
        y = ALTO // 2

        for linea in range(5, 760, 20):
            pygame.draw.line(ventana, NEGRO, (x, y), (x + linea, y), 1)  # "x" avanza horizontalmente
            x = x + linea
            pygame.draw.line(ventana, NEGRO, (x, y), (x, y - (linea + 5)), 1)  # "y" sube y se mantiene x
            y = y - (linea + 5)
            pygame.draw.line(ventana, NEGRO, (x, y), (x - (linea + 10), y), 1)  # la "y" se mantiene y retrocedemos en x
            x = x - (
                        linea + 10)  # Asumimos que el aumento que existe entre la primera y segunda linea es el doble, pues
            # si medimos, se nota el aumento
            pygame.draw.line(ventana, NEGRO, (x, y), (x, y + (linea + 15)), 1)  # "x" se mantiene y bajamos en y
            y = y + (linea + 15)
        pygame.draw.line(ventana, NEGRO, (x, y), (x + (linea + 20), y), 1)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Funcion que dibuja un mandala a partir de 12 círculos con un radio compratido de 150
def dibujarMandala():
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        radioPorCirculo = 150

        for circulo in range(12):
            circulo += 1

            xCor = (int(150 * math.cos(math.radians(30 * circulo))) + ANCHO // 2)
            yCor = (int(150 * math.sin(math.radians(30 * circulo))) + ALTO // 2)
            pygame.draw.circle(ventana, NEGRO, (xCor, yCor), radioPorCirculo, 1)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Función que sirve para aproximar Pi recibiendo unos términos que el usuario da, este ejercicio fue hecho en clase
def aproximarPI():
    terminos = int(input("Número de términos: "))
    suma = 0
    for n in range(1, terminos + 1):
        suma += (1 / n ** 4)  # suma = suma + 1/n/ **4

    ap = (suma * 90) ** 0.25
    print("PI = ", ap)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def hallarNoDeMultiplos():  # Esta función sirve para encontar el número de múltiplos de 19  entre 100 y 999
    contador = 0

    for numeros in range(100, 1000):

        if numeros % 19 == 0:
            contador = contador + 1

    print("Dentro de los números de 3 dígitos(de 100 a 999),", contador, "son multiplos de 19")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def crearPiramides():  # Esta función crea 2 pirámides de números a partir de operaciones aritméticas

    resultado = 0
    numero = 0

    for piramide in range(1, 10, 1):
        resultado = resultado * 10 + piramide
        calculo = resultado * 8 + piramide
        print(resultado, "* 8 +", piramide, "=", calculo)

    print()

    for escalera in range(1, 10, 1):
        cantidad = (numero * 10) + 1
        cantidadElevadaAlC = ((numero * 10) + 1) ** 2

        print(cantidad, "*", cantidad, "=", cantidadElevadaAlC)

        numero = (numero * 10) + 1


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main():  # Función principal: Contiene todas las funciones o actividades, dependiendo de la tecla oprimida sera la actividad que se despliegue en pantalla
    opcion = leerOpcionMenu()
    if opcion == 1:
        dibujarCircYCuadr()
    elif opcion == 2:
        dibujarEstrella()
    elif opcion == 3:
        dibujarEspiralCuadrado()
    elif opcion == 4:
        dibujarMandala()
    elif opcion == 5:
        aproximarPI()
    elif opcion == 6:
        hallarNoDeMultiplos()
    elif opcion == 7:
        crearPiramides()
    elif opcion == 0:
        print("Termina programa")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# LLamada a la función principal
main()




