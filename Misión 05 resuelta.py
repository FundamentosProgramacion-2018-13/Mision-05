# Autor: Alberto Contreras Torres
# Multiusos

import pygame   # Librería de pygame
import math
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
MORADO= (200,100,255)
NEGRO= (0,0,0)


#Crea un color
def crearColor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCuadradoYCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for x in range(0, 801, 10):
            pygame.draw.rect(ventana, NEGRO,(400-x,400-x,x*2,x*2), 1)
            if(x == 0):
                pygame.draw.circle(ventana, NEGRO, (400, 400), 1, 1)

            if(x <= 401 and x != 0):
                pygame.draw.circle(ventana,NEGRO, (400, 400), x, 1)
            pygame.display.flip()
            reloj.tick(1)
    pygame.quit()


#Estructura de dibujo   800 lineas con 10 pixeles
def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for x in range(0, 801, 10):
            if(x <=400):
                pygame.draw.line(ventana, crearColor(),(x,400),(400,400-x), 1)
                pygame.draw.line(ventana, crearColor(), (800-x, 400), (400, 400 - x), 1)

                pygame.draw.line(ventana, crearColor(), (x, 400), (400, 400 + x), 1)
                pygame.draw.line(ventana, crearColor(), (800 - x, 400), (400, 400 + x), 1)
            pygame.display.flip()
            reloj.tick(1)
    pygame.quit()


def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for x in range(0, 801, 10):
            if (x <= 399):
                pygame.draw.line(ventana,NEGRO,(x,x),(800-x,x), 1)
                pygame.draw.line(ventana, NEGRO, (800-x,x), (800-x, 800 - x), 1)

                pygame.draw.line(ventana, NEGRO, (800-x, 800 - x), (x+10,800-x), 1)
                pygame.draw.line(ventana, NEGRO, (x+10,800-x), (x + 10, x+10), 1)
            pygame.display.flip()
            reloj.tick(1)
    pygame.quit()


def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        for angulo in range (0,360,30):
            x = int(math.cos(math.radians(angulo))*150)
            y = int(math.sin(math.radians(angulo))*150)

            pygame.draw.circle(ventana,NEGRO,(x+400,y+400),150,1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


def aproximarPI(terminos):
    suma = 0 #ACUMULADOR
    for n in range (1, terminos+1):
        suma += (1/n**4)            #Suma = suma + 1/n**4

    aproximacionPI= (suma*90)**.25
    return aproximacionPI

def calcularDivisiblesEn19():
    acumulador = 0
    for numerosPorDividir in range (100,1000):
        resultado= numerosPorDividir % 19
        if resultado == 0:
            acumulador = acumulador + 1
    return acumulador

def crearPiramides():
    aumento = 0
    for variable in range(9):
        print((aumento*10+variable+1),"*",8,"+",variable+1,"=",((aumento*10+variable+1)*8+(variable+1)))
        aumento=aumento*10+variable+1



    aumento2 = 0
    for variable in range(9):
        print((aumento2*10+1),"*",(aumento2*10+1),"=",((aumento2*10+1)*(aumento2*10+1)))
        aumento2= aumento2*10+1




    pygame.quit()  # termina pygame

def leerOpcionMenu():
  print("Menú principal")
  print("1. Dibujar cuadros y círculos ")
  print("2. Dibujar parábolas ")
  print("3. Dibujar espiral")
  print("4. Dibujar círculos ")
  print("5. Aproximar PI ")
  print("6. Contar divisibles entre 19 ")
  print("7. Imprimir pirámides de números ")
  print("0. Salir")
  opcion = int(input("Teclea tu opción: "))
  return opcion

# Función principal, aquí resuelves el problema
def main():
    opcion= leerOpcionMenu()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    while opcion!= 0:
        if opcion == 1:
            dibujarCuadradoYCirculos()
        elif opcion == 2:
            dibujarParabolas()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            terminos = int(input("Número de términos: "))
            valorPI = aproximarPI(terminos)
            print("PI =", valorPI)
        elif opcion == 6:
            divisibles =calcularDivisiblesEn19()
            print("Existen %d números de 3 digitos que son divisibles entre 19" % (divisibles))
        elif opcion == 7:
            crearPiramides()
        else:
            print("Error, ingrese una opción disponible")
        opcion= leerOpcionMenu()
    print("Termina programa")

# Llamas a la función principal
main()