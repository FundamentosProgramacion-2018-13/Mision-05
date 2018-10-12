# encoding: UTF-8
# Autor: Luis Jonathan Rosas Ramos
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame
import random
import math
# ancho y alto de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)

#Generar lus cuadrados y los circulos a partir del centro
def dibujarCuadrosYCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False
    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(BLANCO)
        for x in range(1, 400, 10):
            pygame.draw.circle(ventana, NEGRO, (400, 400), x, 1)
        for y in range(1, 800, 10):
            pygame.draw.rect(ventana, NEGRO, ((400 - (y // 2)), (400 - (y / 2)), y, y), 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()

# dibujar rectas con colores aleatorios
def dibujarEstrella():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False
    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(BLANCO)
        for x in range(0, 800 // 2 + 1, 10):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.line(ventana, color, (x, 800 // 2), (800 // 2, 800 // 2 - x), 1)
            pygame.draw.line(ventana, color, (x, 800 // 2), (800 // 2, 800 // 2 + x), 1)
            pygame.draw.line(ventana, color, (800 - x, 800 // 2), (800 // 2, 800 // 2 + x), 1)
            pygame.draw.line(ventana, color, (800 - x, 800 // 2), (800 // 2, 800 // 2 - x), 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

# Dibujar una linea que vaya disminuyendo su tamaño
def dibujarLaberinto():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False
    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(BLANCO)
        x = 0
        y = 790
        for z in range(1, 100):
            if x < 390:
                x = x + 10
                pygame.draw.line(ventana, NEGRO, [y, y], [x, y], 1)
                pygame.draw.line(ventana, NEGRO, [x, y], [x, x], 1)
                y = y - 10
                pygame.draw.line(ventana, NEGRO, [x, x], [y, x], 1)
                pygame.draw.line(ventana, NEGRO, [y, x], [y, y], 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()

#Dibujar los doce círculos
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False
    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        ventana.fill(BLANCO)
        radio = 150
        for x in range(1, 13, 1):
            pygame.draw.circle(ventana, NEGRO, (800 // 2 + int(radio * math.cos(math.radians(30 * x))),
                                               800 // 2 + int(radio * math.sin(math.radians(30 * x)))), radio, 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()

# calcular numeros divisbles de 19 entre 100 y 1000
def calcularDivisible ():
    contador = 0
    for x in range(0, 1000):
        if x > 100 and x % 19 == 0:
            contador = contador + 1
    print("El numero 19 es divisble ", contador, "en 3 terminos")

# Calcular el numero pi con la aproximacion de un dato
def calcularPi():
    dato = int(input("Numero de términos: "))
    resultado = 0
    for x in range(1, dato+1):
        resultado = resultado + (1/(x*x*x*x))
    pi = (resultado*90)**0.25
    print ("El resultado de Pi es: ", pi)

# Generar las piramides de numeros
def imprimirPiramides():
    contador = 0
    for x in range(1, 10):
        contador = contador * 10 + x
        operacion = contador * 8 + x
        print(contador, "x 8 ", "+",x, " = ", operacion)
    print("")
    numero = 1
    for x in range(1, 10):
        multiplicacion = numero * numero
        print(numero, "x",numero, multiplicacion)
        numero = numero * 10 + 1

# Mostrar el menu y las opciones a tomar
def calcularMenu():
    print("Mision 5. Selecciona que quieres hacer: ")
    print("1. Dibujar cuadros y círculas ")
    print("2. Dibujar Parabolas ")
    print("3. Dibujar Esperiales ")
    print("4. Dibujar Circulos ")
    print("5. Aproximar ")
    print("6. Contar diviible entre 19 ")
    print("7. Imprimir pirámidas de números ")
    print("0. Salir")
    lectura = int(input("¿Qué desea hacer? "))
    return lectura
# funcion principal
def main():
    datoMenu = calcularMenu()
    while datoMenu != 0:
        if datoMenu == 1:
            dibujarCuadrosYCirculos()
        elif datoMenu == 2:
            dibujarEstrella()
        elif datoMenu == 3:
            dibujarLaberinto()
        elif datoMenu == 4:
            dibujarCirculos()
        elif datoMenu == 5:
            calcularPi()
        elif datoMenu == 6:
            calcularDivisible()
        elif datoMenu == 7:
            imprimirPiramides()
        datoMenu = calcularMenu()
    print("El programa ha terminado")
# llama a la función principal
main()