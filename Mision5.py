# Autor: Luisa Fernanda Arellano Alvarado A01377974
# Misión 5 (Figuras, ciclos, cadenas)
import math
import pygame
import random

ANCHO = 800  # variable constante
ALTO = 800  # variable constante
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)  # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)  # nada de rojo, ni verde, solo azul


def dibujarCuadradosCirculos(ventana):
    for radio in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, BLANCO, (ANCHO // 2, ALTO // 2), radio, 1)
    for cuadrado in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, BLANCO, (ANCHO // 2 -1, ALTO // 2 -1,1 * 2,1 * 2), 1)


def dibujarDiamante(ventana):
    for x in range(0, ANCHO // 2 + 1, 10):
        colorRandom = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana, colorRandom, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 - x), 1)
        pygame.draw.line(ventana, colorRandom, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x), 1)
        pygame.draw.line(ventana, colorRandom, (ANCHO - x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x), 1)
        pygame.draw.line(ventana, colorRandom, (ANCHO - x, ANCHO // 2), (ANCHO // 2, ALTO // 2 - x), 1)

def dibujarEspiral(ventana):
    for coordenadaX in range(0, 801, 10):
        if (coordenadaX <= 399):
            pygame.draw.line(ventana, BLANCO, (coordenadaX, coordenadaX), (800 - coordenadaX, coordenadaX), 1)
            pygame.draw.line(ventana,BLANCO, (800 - coordenadaX, coordenadaX), (800 - coordenadaX, 800 - coordenadaX),
                             1)
            pygame.draw.line(ventana, BLANCO, (800 - coordenadaX, 800 - coordenadaX),
                             (coordenadaX + 10, 800 - coordenadaX), 1)
            pygame.draw.line(ventana,BLANCO, (coordenadaX + 10, 800 - coordenadaX),
                             (coordenadaX + 10, coordenadaX + 10), 1)

def dibujarCirculos(ventana):
    for angulo in range(0, 360, 30):
        posicionenX = int(math.sin(math.radians(angulo)) * 150)  # En eje  x
        posicionenY = int(math.cos(math.radians(angulo)) * 150)  # En eje  y
        pygame.draw.circle(ventana, BLANCO, ((posicionenX + ANCHO // 2), (posicionenY + ALTO // 2)), 150, 1)

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
'''''
def mostrarSecdos():
    producto = 0
    for incrementos in range(1,9):
        print((producto*10 + 1),"x",(producto*10 + 1),"="((producto*10 + 1)*(producto*10 +1)))

'''''

def main():
        opcion = -1
        while (opcion != 0):
         opcion = int(input('''
            -----------------------------------------------
            Misión 5. Seleccione qué quiere hacer
            1. Dibujar Dibujar cuadros y círculos
            2. Cibujar parábolas
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
                dibujarCuadradosCirculos()
        elif opcion == 2:
                dibujarDiamante()
        elif opcion == 3:
                dibujarEspiral()
        elif opcion == 4:
                dibujarCirculos()
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
