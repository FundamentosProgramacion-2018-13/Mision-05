# encoding: UTF-8
# Autor: Oscar Alejandro Torres Maya, A01377686
# Muestra un menú y el usuario selecciona los dibujos o programas que quiera ver. Hasta que se salga.

import pygame        # Librería de pygame
import random        # Librería para importar números random
from math import *   # Librería para importar funciones matemáticas

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # COLOR BLANCO
NEGRO = (0,0,0)           # COLOR NEGRO


def dibujarCuadrosCirculos(ventana):
    for n in range (0, 400, 10):
        pygame.draw.rect(ventana,NEGRO,(400-n, 400-n, n*2, n*2),1)
    for n in range (0, 390, 10):
        pygame.draw.circle(ventana,NEGRO,(400,400),n+10,1)


def dibujarRombo(ventana):
    for rombo in range(0,400,10):
        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (400, rombo), (400 + rombo, 400), 1)
        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (rombo, 400), (400, 400 - rombo), 1)
        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (rombo, 400), (400, 400 + rombo), 1)
        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (400, 800 - rombo), (400 + rombo, 400), 1)


def dibujarCaracol(ventana):
    for caracol in range(0, 400, 10):
        pygame.draw.line(ventana, NEGRO, (405 + caracol, 390 - caracol), (390 - caracol, 390 - caracol), 1)
        pygame.draw.line(ventana, NEGRO, (400 - caracol, 400 + caracol), (405 + caracol, 400 + caracol), 1)
        pygame.draw.line(ventana, NEGRO, (405 + caracol, 400 + caracol), (405 + caracol, 390 - caracol), 1)
        pygame.draw.line(ventana, NEGRO, (390 - caracol, 410 + caracol), (390 - caracol, 390 - caracol), 1)


def dibujarCirculos(ventana):
    for n in range(12):
        pygame.draw.circle(ventana, NEGRO,(400 + int(150 * cos(radians(-30 * (n + 1)))), 400 + int(150 * sin(radians(-30 * (n + 1))))),150, 1)

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(opcion):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        if opcion == 1:
            dibujarCuadrosCirculos(ventana)
        elif opcion == 2:
            dibujarRombo(ventana)
        elif opcion == 3:
            dibujarCaracol(ventana)
        elif opcion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # Termina pygame


def aproximarPI(terminos):
    suma = 0    #ACUMULADOR
    for n in range (1,terminos+1):
        suma += (1/n**4)    #+= SIRVE PARA SUMAR Y APARTE ASIGNAR 1 VALOR
    aproximacion = (suma*90)**(1/4)
    return aproximacion


def indentificarNumerosDivisibles():
    divisibles = 0
    for n in range(100,1000):
        if n%19 == 0:
            divisibles = divisibles+1
    return divisibles


def calcularOperaciones():
    serie1 = 0
    serie2 = 0

    for numero in range(1,10):
        serie1 = serie1 * 10 + numero
        resultado = serie1 * 8 + numero
        print(serie1, " * 8 + ", numero, " = ", resultado)
    print("")
    for n in range(1,10):
        unos = serie2 * 10 + 1
        restultado = unos * unos
        print(unos, "*", unos, "=", restultado)
        serie2 = unos


# Función principal, aquí resuelves el problema
def main():
    opcion = 1
    while opcion != 0:
        print('''''
Misión 5. Seleccione qué quiere hacer. 
1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar espiral
4. Dibujar círculos
5. Aproximar PI
6. Contar divisibles entre 19 
7. Imprimir pirámides de números 
0. Salir''')

        opcion = int(input("¿Qué deseas hacer? "))
        print("")
        if opcion > 0 and opcion < 5:
            dibujar(opcion)
        elif opcion == 5:
            terminos = int(input("Número de términos: "))
            valorPI = aproximarPI(terminos)
            print("Aproximacion de PI =", valorPI)
        elif opcion == 6:
            numerosDivisibles = indentificarNumerosDivisibles()
            print("Hay", numerosDivisibles, "números divisibles entre 19 en el intervalo de (100,999)")
        elif opcion == 7:
            calcularOperaciones()
        elif opcion == 0:
            print("Saliste del programa. ¡Hasta luego!")
            break

# Llamas a la función principal
main()