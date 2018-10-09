# encoding: UTF-8
# Autor: Oscar Macias Rodríguez, A01376398
# Descripción: Funciones que dibujan en pygame o que calculan valores.


# Importar librerías
import pygame
import random
from math import *


# Tamaño de la pantalla
ANCHO = 800
ALTO = 800


# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


# Dibuja círculos y rectángulos cada 10 px.
def dibujarCuadrosyCirculos(ventana):
    for x in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), x, 1)
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x, 2 * x, 2 * x), 1)


# Dibuja del punto más pequeño de un eje al más grande del otro para todos los cuadrantes.
def dibujarCuadrantes1(ventana):
    for x in range(0, 408, 10):
        colores = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana, colores, (x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))  # Parte superior izquierda
        pygame.draw.line(ventana, colores, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x)) # Parte superior derecha
        pygame.draw.line(ventana, colores, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x)) # Parte inferior derecha
        pygame.draw.line(ventana, colores, (x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))  # Parte inferior izquierda


# Avanza aumentando 5 pixles en sus coordenadas (x o y), tomando en cuenta el punto anterior. Formando una espiral.
def dibujarEspiral(ventana):
    for x in range(0, 401, 10):
        pygame.draw.line(ventana, NEGRO, (400 - x, 400 + x), (405 + x, 400 + x), 1)  # Dibuja hacia abajo
        pygame.draw.line(ventana, NEGRO, (405 + x, 400 + x), (405 + x, 390 - x), 1)  # Dibuja hacia la derecha
        pygame.draw.line(ventana, NEGRO, (405 + x, 390 - x), (390 - x, 390 - x), 1)  # Dibuja hacia arriba
        pygame.draw.line(ventana, NEGRO, (390 - x, 390 - x), (390 - x, 410 + x), 1)  # Dibuja hacia la izquierda


# Dibuja 12 círculos utilizando trigonometría.
def dibujarCirculos12(ventana):
    for n in range(12):
        pygame.draw.circle(ventana, NEGRO, (400 + int(150 * cos(radians(-30 * (n + 1)))), 400 + int(150 * sin(radians(-30 * (n + 1))))), 150, 1)


# Dibuja la función de dibujarCuadrosyCírculos.
def dibujarCuadrosYCirculos():
    # Inicializa el motor de pygame
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.display.set_caption("Mision 5. Cuadros y círculos")  # Nombra la ventana

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Colorea la ventana

        dibujarCuadrosyCirculos(ventana)  # Llama a la función

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Dibuja la función de dibujarCuadrantes1.
def dibujarCuadrantes():
    # Inicializa el motor de pygame
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.display.set_caption("Mision 5. Parábolas")  # Nombra la ventana

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Colorea la ventana

        dibujarCuadrantes1(ventana)  # Llama a la función

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Dibuja la función de dibujarEspiral.
def dibujarSnake():
    # Inicializa el motor de pygame
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.display.set_caption("Mision 5. Espiral")  # Nombra la ventana

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Colorea la ventana

        dibujarEspiral(ventana)  # Llama la función

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Dibuja la función de dibujarCírculos12.
def dibujarCirculos():
    # Inicializa el motor de pygame
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.display.set_caption("Mision 5. Círculos")  # Nombra la ventana

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Colorea la ventana

        dibujarCirculos12(ventana)  # Llama la función

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Calcula y regresa una aproximación al valor de PI utilizando una serie numérica.
def aproximarPI(terminos):
    suma = 0

    for denominador in range(1, terminos+1):
        suma += 1/denominador**4

    despeje = (90*suma)**0.25
    return despeje


# Calcula y regresa cuántos números de tres dígitos son divisibles entre 19.
def calcularDivisibles():
    i = 0
    count = 0
    ultimo = []
    for numeros in range(100, 1000):
        if numeros % 19 == 0:
            count += 1
            ultimo.append(count)

        i = i + 1
    return len(ultimo)


# Calcula e imprime pirámides numéricas utilizando base 10.
def calcularPiramidesDeNumeros():
    variable = 0
    variable1 = 0
    variable2 = 0

    for factor1 in range(0, 9):
        base1 = 10**factor1
        variable1 = variable1 + base1
        variable2 += variable1
        piramide2 = variable2 * 8 + (factor1 + 1)
        print(variable2, "* 8 +", factor1+1, "=", piramide2)

    print()

    for factor in range(0, 9):
        base = 10 ** factor
        variable = variable + base
        piramide1 = variable * variable
        print(variable, "*", variable, "=", piramide1)


# Despliega un menú de opciones preguntándole al usuario que desea realizar.
def main():
    opcion = 1
    while opcion != 0:
        print("""
        Misión 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar círculos
        5. Aproximar PI
        6. Contar divisibles entre 19
        7. Imprimir pirámides de números
        0. Salir
        """)

        opcion = int(input("¿Qué desea hacer?"))
        if opcion == 1:
           dibujarCuadrosYCirculos()
        if opcion == 2:
            dibujarCuadrantes()
        if opcion == 3:
            dibujarSnake()
        if opcion == 4:
            dibujarCirculos()
        if opcion == 5:
            terminos = int(input("Número de términos: "))
            valorPI = aproximarPI(terminos)
            print("PI = ", valorPI)
        if opcion == 6:
            divisible = calcularDivisibles()
            print("La cantidad de números de 3 dígitos divisibles entre 19 son: ", divisible)
        if opcion == 7:
            calcularPiramidesDeNumeros()
        if opcion == 0:
            exit("Has salido")
        else:
            main()


main()