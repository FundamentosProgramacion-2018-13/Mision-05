#Autor: Víctor Manuel Rodríguez Loyola
#Muestra al usuario un menú donde podrá ejecutar diversas funciones que realizan diferentes acciones.

import pygame
import math
import random

ANCHO = 800
ALTO = 800

#COLORES USADOS PARA LA MISIÓN
def generarColorAleatorio(): #GENERA UN COLOR AL AZAR EN EL FORMATO RGB
    color= random.randint(0,255), random.randint(0,255), random.randint(0,255)
    return color

BLANCO = (255, 255, 255)
NEGRO = (0,0,0)


def dibujarCuadrosYCirculos(): #HACE UN PATRÓN DE CUADRADOS Y DE CÍRCULOS AUMENTANDO SU TAMAÑO
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        for l in range(1, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - l, ALTO // 2 - l, l * 2, l * 2), 1)
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), l, 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarParabolas(): #DIBUJA UNA SERIE DE LÍNEAS AUMENTANDO SU TAMAÑO Y CAMBIANDO EL COLOR DE LAS MISMAS AL AZAR
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        for linea in range(-1, 41):
            linea = (linea + 1) * 10
            pygame.draw.line(ventana, generarColorAleatorio(), (ANCHO // 2 - linea, ALTO // 2), (ANCHO // 2, linea), 1)
            pygame.draw.line(ventana, generarColorAleatorio(), (ANCHO // 2 + linea, ALTO // 2), (ANCHO // 2, linea), 1)
            pygame.draw.line(ventana, generarColorAleatorio(), (ANCHO // 2 - linea, ALTO // 2),
                             (ANCHO // 2, ALTO - linea), 1)
            pygame.draw.line(ventana, generarColorAleatorio(), (ANCHO // 2 + linea, ALTO // 2),
                             (ANCHO // 2, ALTO - linea), 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarEspiral(): #DIBUJA UN ESPIRAL CON VARIAS LÍNEAS QUE DISMINUYEN SU TAMAÑO
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        for coorx in range(10, ANCHO, 10):
            if coorx < ANCHO // 2:
                pygame.draw.line(ventana, NEGRO, (ANCHO - coorx, ANCHO - coorx), (coorx, ANCHO - coorx), 1)
                pygame.draw.line(ventana, NEGRO, (coorx, ANCHO - coorx), (coorx, coorx), 1)
            if coorx > ANCHO // 2:
                pygame.draw.line(ventana, NEGRO, (ANCHO - coorx, ANCHO - coorx), (coorx - 10, ANCHO - coorx), 1)
                pygame.draw.line(ventana, NEGRO, (coorx - 10, ANCHO - coorx), (coorx - 10, coorx - 10), 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarCirculos(): #DIBUJA 12 CÍRCULOS ENTRELAZADOS. SE UTILIZÓ EL CÍRCULO TRIGONOMÉTRICO
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
        for angulos in range(0, 361, 30):
            radianes = math.radians(angulos)
            pygame.draw.circle(ventana, NEGRO, (x + int(150 * math.cos(radianes)), y - int(150 * math.sin(radianes))),
                               150, 1)

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
def aproximarValorPI(terminos): #HACE UNA APROXIMACIÓN AL VALOR DE PI DE ACUERDO AL NÚMERO DE TÉRMINOS INGRESADOS
    suma =0 #Acumulador
    for denominador in range(1,terminos+1):
        suma += 1/denominador**4

    resultado= (suma*90)**0.25
    return resultado


def calcularTerminosDivisibles(): #CALCULA EL NÚMERO DE TÉRMINOS DIVISIBLES ENTRE 19.
    terminos= 0
    for divisibles in range (1,1000):
        terminos += divisibles%19==0
    return terminos

def ImprimirOperaciones(): #CALCULA E IMPRIME PIRÁMIDES FORMADAS POR DIFERENTES PATRONES DE OPERACIONES.
    cifras = 0
    for suma in range(1, 10):
        cifras = cifras * 10 + suma
        resultado = cifras *8+suma
        print(cifras, "*8 +",suma, "=", resultado)

    digitos=0
    for multiplicacion in range(1,10):
        digitos= digitos*10+1
        resultado= digitos**2
        print(digitos,"*",digitos,"=",resultado)


def leerOpcion(): #MUESTRA UN MENÚ AL USUARIO DONDE ÉSTE PUEDE ELEDIR LA FUNCIÓN QUE DESEA EJECUTAR
    print("Misión 5. Seleccione qué quiere hacer: ")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion


def main():
    opcion = leerOpcion()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosYCirculos()
        elif opcion == 2:
            dibujarParabolas()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
         terminos=int(input("Teclea cuántos términos quieres: "))
         aproximacionPI= aproximarValorPI(terminos)
         print("PI= ", aproximacionPI)
        elif opcion == 6:
            print("%d terminos son divisibles entre 19" % (calcularTerminosDivisibles()))
        elif opcion == 7:
            ImprimirOperaciones()
        opcion = leerOpcion()
    print("¡Vuelve pronto!")


main()