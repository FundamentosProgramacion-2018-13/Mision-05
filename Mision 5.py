#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que dibuja figuras, aproxima PI, calcula y regresa los números divisibles entre 19 e imprime pirámides de números.


import pygame
import random
import math


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


#Función que imprime el menú, lee y regresa la opción que quiere el usuario.
def leerSeleccionMenu():
    print("""Misión 5. Seleccione qué quiere hacer.
1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar espiral
4. Dibujar círculos
5. Aproximar PI
6. Contar divisibles entre 19
7. Imprimir pirámides de números
0. Salir""")
    seleccion = int(input("¿Qué desea hacer? "))
    return seleccion


#Función que traza cuadrados y círculos.
def dibujarCuadrosYCirculos(ventana):
    for delta in range(0, ALTO//2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO//2 - delta, ALTO//2 - delta, 2 * delta, 2 * delta), 1)
    for radio in range(10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO// 2, ALTO // 2), radio, 1)


#Función que dibuja parabolas con líneas de colores aleatorios.
def dibujarParabolas(ventana):
    for cambioCoordenada in range(0, ALTO//2 + 1, 10):
        randomColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana, randomColor, (cambioCoordenada, ALTO//2), (ANCHO//2, ALTO//2-cambioCoordenada))
        pygame.draw.line(ventana, randomColor, (ANCHO-cambioCoordenada, ALTO//2), (ANCHO//2, ALTO//2-cambioCoordenada))
        pygame.draw.line(ventana, randomColor, (cambioCoordenada, ALTO//2), (ANCHO//2,ALTO//2+cambioCoordenada))
        pygame.draw.line(ventana, randomColor, (ANCHO-cambioCoordenada, ALTO//2), (ANCHO//2, ALTO//2+cambioCoordenada))


#Función que dibuja un espiral
def dibujarEspiral(ventana):
    for x in range(0, ALTO//2, 10):
        pygame.draw.line(ventana, NEGRO, (ALTO//2 - x, ALTO//2 - x), (ALTO//2 - x, ALTO//2 + x))
        pygame.draw.line(ventana, NEGRO, (ALTO//2 - x, ALTO//2 + x), (ALTO//2 + x + 5, ALTO//2 + x))

    for y in range(0, ALTO//2 - 10, 10):
        pygame.draw.line(ventana, NEGRO, (ALTO//2 - y - 10, ALTO//2 - y -10), (ALTO//2 + y + 5, ALTO//2 - y - 10))
        pygame.draw.line(ventana, NEGRO, (ALTO//2 + y + 5, ALTO//2 - y - 10), (ALTO//2 + y + 5, ALTO//2 + y))


#Función que dibuja 12 círculos
def dibujarCirculos(ventana):
    for angulo in range(0, 331, 30):
        anguloRadianes = angulo * math.pi / 180
        pygame.draw.circle(ventana, NEGRO, (int(math.cos(anguloRadianes) * 150 + ANCHO//2), int(math.sin(anguloRadianes) * 150 + ALTO//2)), 150, 1)


#Función que dibuja con Pygame las figuras que el usuario desea, dependiendo de la selección que hizo en el menú.
def dibujarFiguras(seleccion):
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:  # Ciclo principal
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        # Dibujar
        if seleccion == 1:
            dibujarCuadrosYCirculos(ventana)

        elif seleccion == 2:
            dibujarParabolas(ventana)

        elif seleccion == 3:
            dibujarEspiral(ventana)

        elif seleccion == 4:
            dibujarCirculos(ventana)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


#Función que aproxima PI, dependiendo los términos que el usuario desee.
def aproximarPI(terminos):
    suma = 0

    for denominador in range(1, terminos+1):
        suma += 1/denominador**4

    return (suma * 90) ** 0.25


#Función que calcula los divisibles de 19 que sean de 3 dígitos, regresa el número de divisibles.
def contarDivisibles():
    numeroDeDivisibles = 0

    for divisible in range(100,1000):
        if divisible%19==0:
            numeroDeDivisibles += 1

    return numeroDeDivisibles


#Función que calcula e imprime pirámides de números
def imprimirPiramides():
    numeroInicial1= 0
    sumaNumeroInicial1 = 0
    numeroInicial2 = 0
    multiplicador = 8

    for coeficientePiramide1 in range(0,9):
        base1 = 10**coeficientePiramide1
        numeroInicial1 = numeroInicial1 + base1
        sumaNumeroInicial1 += numeroInicial1
        piramide1 = sumaNumeroInicial1 * multiplicador + (coeficientePiramide1 + 1)
        print(sumaNumeroInicial1, "*", multiplicador, "+", (coeficientePiramide1 + 1), "=", piramide1)

    print()

    for coeficientePiramide2 in range(0,9):
        base2 = 10**coeficientePiramide2
        numeroInicial2 = numeroInicial2 + base2
        piramide2 = numeroInicial2 * numeroInicial2

        print(numeroInicial2, "*", numeroInicial2, "=", piramide2)


#Función principal. Lee e imprime datos.
def main():

    seleccion = leerSeleccionMenu()

    while not seleccion == 0:

        #seleccion = int(input("¿Qué desea hacer? "))

        if seleccion == 1 or seleccion == 2 or seleccion == 3 or seleccion == 4:
            dibujarFiguras(seleccion)
            print()

        if seleccion == 5:
            print()
            terminos = int(input("Teclea cuantos términos quieres "))
            PI = aproximarPI(terminos)
            print("PI =", PI)
            print()

        if seleccion == 6:
            print()
            numeroDeDivisibles = contarDivisibles()
            print("Hay %d números de 3 digitos que son divisibles entre 19." % (numeroDeDivisibles))
            print()

        if seleccion == 7:
            imprimirPiramides()
            print()

        seleccion = leerSeleccionMenu()
    print("Termina programa")


#Llamar a la función principal
main()