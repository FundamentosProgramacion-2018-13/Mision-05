# Autor: Luisa Fernanda Arellano Alvarado A01377974
# Misión 5 (Figuras, ciclos, cadenas)
import pygame

import random

import math

ANCHO = 800  # variable constante
ALTO = 800  # variable constante
# Colores
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
ROSA = (255,20,147)


def dibujarCuadradosCirculos(ventana):
    for radio in range(10, ALTO//2, 10):
            pygame.draw.circle(ventana, AZUL, (ANCHO//2, ALTO//2), radio, 1)
    for cuadrado in range(10, ALTO//2, 10):
            pygame.draw.rect(ventana, ROJO, ((ANCHO//2 - cuadrado), (ALTO//2 - cuadrado), cuadrado * 2, cuadrado * 2 ), 1)

def dibujarDiamante(ventana):

    for linea in range(40):
        linea = (linea+1)*10
        pygame.draw.line(ventana, VERDE_BANDERA, (400 - linea, 400), (400, linea), 1)
        pygame.draw.line(ventana, AZUL, (400 + linea, 400), (400, linea), 1)
        pygame.draw.line(ventana, ROJO, (400 - linea, 400), (400, 800 - linea), 1)
        pygame.draw.line(ventana, ROSA, (400 + linea, 400), (400, 800 - linea), 1)

def dibujarEspiral(ventana):
    for coordenadaX in range(0, 801, 10):
        if (coordenadaX <= 399):
            pygame.draw.line(ventana,BLANCO,(coordenadaX, coordenadaX),(800-coordenadaX, coordenadaX), 1)
            pygame.draw.line(ventana, BLANCO, (800-coordenadaX,coordenadaX), (800-coordenadaX, 800-coordenadaX), 1)
            pygame.draw.line(ventana, BLANCO, (800-coordenadaX, 800-coordenadaX), (coordenadaX+10,800-coordenadaX), 1)
            pygame.draw.line(ventana, BLANCO, (coordenadaX+10,800-coordenadaX), (coordenadaX + 10, coordenadaX+10), 1)

def dibujarCirculos(ventana):
    for angulo in range(0, 360, 30):
        posicionX = int(math.sin(math.radians(angulo)) * 150)
        posicionY = int(math.cos(math.radians(angulo)) * 150)
        pygame.draw.circle(ventana, ROJO, ((posicionX + ANCHO//2), (posicionY + ALTO //2)), 1)


def dibujar(opcion):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
                ventana.fill(BLANCO)
            if opcion == 1:
             dibujarCuadradosCirculos(ventana)
            elif opcion == 2:
             dibujarDiamante(ventana)
            elif opcion == 3:
             dibujarEspiral(ventana)
            elif opcion == 4:
             dibujarCirculos(ventana)

             pygame.display.flip()
             reloj.tick(40)
             pygame.quit()


def AproximarValorPI(terminos):
    suma= 0 #acumulador
    for denominador in range(1,terminos +1):
        suma += 1/denominador**4
    return (90*suma)**0.25

def esMultiplo(numero):
    if numero % 19 == 0:
        return True
        False

def mostrarSecUno():
    numero = 0 #acumulador
    for factor in range(1,9):
        print((numero*10+factor+1),"x",8,"+",factor+1,"=",((numero*10+factor+1)*8+(factor+1)))
        numero = numero*10+factor+1

    print("                                                                                                   ")

    producto = 0
    for incrementos in range(1, 9):
        print((producto * 10 + 1), "x", (producto * 10 + 1), "=",((producto * 10 + 1) * (producto * 10 + 1)))
        producto = producto*10 + 1


def main():
    opcion = -1
    while (opcion != 0):
        opcion = int(input('''
        -----------------------------------------------
        Misión 5. Seleccione qué quiere hacer
        1. Dibujar Dibujar cuadro y círculo
        2. Dibujar parábolas
        3. Dibujar espiral
        4. Dibujar círculos
        5. Aproximar PI
        6. Contar divisibles entre 19
        7. Imprimir pirámides de números
        0. Salir
        -----------------------------------------------
        ¿Qué desea hacer?
         '''))
        if opcion == 1:
            dibujar(opcion)
        elif opcion == 2:
            dibujar(opcion)
        elif opcion == 3:
            dibujar(opcion)
        elif opcion == 4:
            dibujar(opcion)
        elif opcion == 5:
            terminos = int(input("teclea cuantos terminos quieres:"))
            aproximaciónPI = AproximarValorPI(terminos)
            print("PI =", aproximaciónPI)
        elif opcion == 6:
            Numero = 0  # Contador
            for numero in range(100, 1000):  # Los números van de 100 a 999
                if esMultiplo(numero):
                    print("%03d es" % (numero), end="")
                    print(" Multiplo de 19")
                    Numero += 1
                    print("Hay: %d multiplos de 19 con 3 digitos" % (Numero))
        elif opcion == 7:
            mostrarSecUno()
        elif opcion == 0:
            print("Adios!! :)")


main()