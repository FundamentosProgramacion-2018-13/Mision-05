# Autor: Humberto Carrillo Gómez
# Despliega un menu con funciones para elegir y las ejecuta.

import pygame   # Librería de pygame
import random   # Librería para generar valores aleatorios
import math     # Librería para operaciones matemáticas avanzadas

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
negro =(0, 0, 0)
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


def dibujarCuadradosYCirculos(ventana):
    for x in range (0, 400, 10):
        pygame.draw.rect(ventana, negro, (400 - x, 400 - x, x*2, x*2), 1)
    for y in range (0, 390, 10):
        pygame.draw.circle(ventana, negro, (400,400), y + 10, 1)


def dibujarParabolas(ventana):   # Dibuja una parábola con colores aleatorios
    for parabola in range(0, 400, 10):
        colorRandom = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        pygame.draw.line(ventana, colorRandom, (parabola, 400), (400, 400 + parabola))
        pygame.draw.line(ventana, colorRandom, (800 - parabola, 400), (400, 400 + parabola))
        pygame.draw.line(ventana, colorRandom, (800 - parabola, 400), (400, 400 - parabola))
        pygame.draw.line(ventana, colorRandom, (parabola, 400), (400, 400 - parabola))


def dibujarEspiral(ventana):  # Dibuja un cuadrado con un espiral dentro
    for n in range(0, 400, 10):
        pygame.draw.line(ventana, negro, (400 - n, 400 + n), (400 + 5 + n, 400 + n), 1)
        pygame.draw.line(ventana, negro, (400 - 10 - n, 400 - 10-n), (400 - n - 10, 400 + n + 10), 1)
    for n in range(0, 400, 10):
        pygame.draw.line(ventana, negro, (400 - n - 10, 400 - 10-n), (400 + n + 5, 400 - n - 10), 1)
        pygame.draw.line(ventana, negro, (400 + n + 5, 400 + n), (400 + n + 5, 400 - n - 10), 1)


def dibujarCirculos(ventana): # Dibuja circulos de color negro y con radio de 150.
    radio = 150
    angulo= 30
    for x in range(1, 13):
        pygame.draw.circle(ventana, negro, ((400) + (int(radio * math.cos(math.radians(angulo * x)))),
                                             (400) + (int(radio * math.sin(math.radians(angulo * x))))), radio, 1)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(seleccion):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        if seleccion == 1:
            dibujarCuadradosYCirculos(ventana)
        if seleccion == 2:
            dibujarParabolas(ventana)
        if seleccion == 3:
            dibujarEspiral(ventana)
        if seleccion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def aproximarPi():  # Calcula el valor de Pi en función al número de elementos proporcionado por el usuario

    contador= 0
    terminos= int(input("Teclea el número de terminos: "))
    for numero in range(1,terminos + 1):
        contador = contador + 1/ numero**4
    piAprox= (90*contador)**.25
    print(" El valor aproximado de pi es:", piAprox)


def contarDivisiblesEntre19(): # Calcula cuantos números de tres dígitos son divisibles entre 19
    contador = 0

    for numeros in range(100, 1001):
       if numeros % 19 == 0:
           contador = contador +1
    print("Existen ", contador, "números de 3 dígitos divisibles entre 19")


def imprimirPiramides():    # Calcula e imprime pirámides númericas
    accum = 1
    for numero in range(1, 10):

        print(accum, "*", "8", "+", + numero, "=", accum*8 + numero)
        accum = accum * 10 + numero +1

    print("")

    acumulador = 1
    for numero in range(1, 10):

        print(acumulador, "*", acumulador, "=", acumulador*acumulador )
        acumulador = acumulador * 10 + 1


def enlistarFunciones ():  # Despliega al usuario la lista de funciones y le pide que escoja una
    print("Bienvenido, esta es la lista de funciones ejecutables: ")
    print("1: Dibujar cuadrados y círculos")
    print("2: Dibujar parábolas")
    print("3: Dibujar espiral")
    print("4: Dibujar círculos")
    print("5: Aproximar PI")
    print("6: Contar divisibles entre 19")
    print("7: Imprimir pirámides de números")
    seleccion= int(input("Teclea el numero de la función que quieres ejecutar: "))
    return seleccion


def main():  # Función principal, resuelve el problema
    seleccion = enlistarFunciones()
    while seleccion != 0:
        if seleccion >= 1 and seleccion <= 4:
                dibujar(seleccion)
        if seleccion == 5:
                aproximarPi()
        if seleccion == 6:
                contarDivisiblesEntre19()
        if seleccion == 7:
                imprimirPiramides()
        if seleccion == 0:
            print("Fin del programa")
        print("")
        seleccion = enlistarFunciones()

main() # Llamado a la función principal