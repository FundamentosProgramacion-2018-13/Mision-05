#Autor: Alan Diaz Carrera
#Un programa que puede dibujar, calcular Pi, calcular piramide de numeros y la canditdad de numeros divisiles enre 19
#dependiendo de lo que quiera el usuario

import pygame
import random
import math
from math import *

ANCHO=800
ALTO=800
BLANCO=(255,255,255)
NEGRO=(0,0,0)
BLANCO=(255,255,255)

def cuadradoCirculo():
    y2 = 800
    y1 = 0
    x1 = 0
    x2 = 800
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    ventana.fill(BLANCO)
    for r in range(10,400,10):
        pygame.draw.circle(ventana,NEGRO,(400,400),r,1)

    for x in range(0, 400, 10):
        pygame.draw.line(ventana, NEGRO, (x, y1), (x, (y2)))
        y2 = y2 - 10
        y1 = y1 + 10
    for x in range(400, 800, 10):
        pygame.draw.line(ventana, NEGRO, (x, y1), (x, y2))
        y2 = y2 - 10
        y1 = y1 + 10
    for y in range(0, 400, 10):
        pygame.draw.line(ventana, NEGRO, (x1, y), (x2, y))
        x1 = x1 + 10
        x2 = x2 - 10
    for y in range(400, 800, 10):
        pygame.draw.line(ventana, NEGRO, (x1, y), (x2, y))
        x1 = x1 + 10
        x2 = x2 - 10
    termina = False
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
        pygame.display.flip()
    pygame.display.flip()

def cuadrados():
    y2 = 790
    y1 = 10
    x1 = 10
    x2 = 790
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    ventana.fill(BLANCO)
    for y in range(790,400,-10):
        pygame.draw.line(ventana,NEGRO,(x2,y),(x1,y))
        x2=x2-10
        x1=x1+10
    for y in range(400,0,-10):
        pygame.draw.line(ventana,NEGRO,(x2,y),(x1-10,y))
        x2=x2-10
        x1=x1+10
    for x in range(10,390,10):
        pygame.draw.line(ventana,NEGRO,(x,y1),(x,y2))
        y1=y1+10
        y2=y2-10
    for x in range(390,790,10):
        pygame.draw.line(ventana,NEGRO,(x,y1),(x,y2-10))
        y1=y1+10
        y2=y2-10
    termina = False
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
        pygame.display.flip()
    pygame.display.flip()

def parabla():
    y2 = 400
    y1 = 790
    x1 = 10
    x2 = 400
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    ventana.fill(BLANCO)
    for y in range(400,800,10):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana,color,(x2,y),(x1,y2))
        x1=x1+10
    for y in range(0,400,10):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana,color,(x2,y),(x1,y2))
        x1=x1+10
    for x in range(400,800,10):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana,color,(x,y2),(x2,y1))
        y1=y1-10
    for x in range(0,400,10):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana,color,(x,y2),(x2,y1))
        y1=y1-10
    termina = False
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
        pygame.display.flip()
    pygame.display.flip()

def circulos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    ventana.fill(BLANCO)
    a=0
    for c in range(12):
        pygame.draw.circle(ventana,NEGRO,(400+int(150*math.cos(radians(-30*(c+1)))),(400+int(150*math.sin(radians(-30*(c+1)))))),150,1)
    termina = False
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
        pygame.display.flip()
    pygame.display.flip()

def aproximarPI(terminos):
    suma = 0
    for denominador in range(1,terminos+1):
        suma += 1/denominador**2
    return (6*suma)**0.5
def pi():
    terminos=int(input("Teclea cuantos terminos quieres: "))
    aproximacionPI = aproximarPI(terminos)
    print("PI=",aproximacionPI)

def division():
    cantidad=0
    for x in range(100,1000):
        if x%19==0:
            cantidad=cantidad+1
    print(cantidad)

def piramidesNumericas():
    numero1 = 0
    numero2=0
    for dato in range(1,10):
        numero1=(numero1*10)+dato
        valor = (numero1*8)+dato
        print(numero1,"* 8 +",dato,"=",valor)

    for dato in range(1,10):
        numero2=(numero2*10)+1
        valor=numero2*numero2
        print(numero2,"*",numero2,"=",valor)

def main():
    u = -1
    while u != 0:
        print("""1.Dibujar cuadros y circulos
2. Dibujar parabolas
3. Dibujar espiral
4. Dibujar circulos
5. Aproximar PI
6. Contar divisibles entre 19
7. Imprimir piramides de numeros
0. Salir""")
        u = int(input("¿Que desea hacer?"))
        if u == 1:
            cuadradoCirculo()
        elif u == 2:
            parabola()
        elif u==3:
            cuadrados()
        elif u==4:
            circulos()
        elif u==5:
            pi()
        elif u==6:
            division()
        elif u==7:
            piramidesNumericas()

    if u==0:
        exit("Has salido del programa")
    else:
        print("Numero no permitido")
        main()

main()