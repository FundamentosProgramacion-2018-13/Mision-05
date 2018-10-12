# encoding: UTF-8
# Autor: Irma Gómez Carmona
# Menú que permite elegir entre 7 opciones, 4 son dibujos 

import math
import random
import pygame   # Librería de pygame

# Dimensiones de la pantalla

ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO  = (  0,   0,   0)


# Funciones para cada opción


def dibujarCuadradosYCirculos(ventana): #el radio de los circulos se incrementan de 10 en 10 y los lados del cuadrado son el doble del tamaño que el anterior
    delta=10
    for cu in range (10,ALTO//2+10,delta):
       pygame.draw.rect(ventana,NEGRO, (ANCHO//2-cu, ALTO//2-cu, 2*cu, 2*cu),1)
    for ci in range (10,ALTO//2+10,delta):
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),ci,1)


def dibujarParabolas(ventana):

    for y in range (0,ALTO//2,10): #composición de rombos que se alargan en x y disminuyen en y para diseñar parábolas
        ALEATORIO1=random.randint(0,255)
        ALEATORIO2 = random.randint(0, 255)
        ALEATORIO3 = random.randint(0, 255)
        ColorAleatorio=(ALEATORIO1,ALEATORIO2,ALEATORIO3)
        pygame.draw.lines(ventana, ColorAleatorio, True, [(ANCHO//2, y), (ANCHO//2+y, ALTO//2), (ANCHO//2, ALTO-y),(ANCHO//2-y,ALTO//2)], 1)


def dibujarCirculos(ventana): #el angulo aumenta de 30 y 30 y mediante los oomponentes x, y se designa el centro de los circulos
    angulo=0
    radio=150
    for circulo in range (12):
        x=int(radio*math.cos(angulo*math.pi/180))
        y=int(radio*math.sin(angulo*math.pi/180))
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2+x,ALTO//2+y),radio,1)
        angulo +=30



def calcularDivisiblesEntre19(): #números de tres digitos que son exactamente divisibles (residuo=0) entre 19
    sum=0
    for num in range(100,1001):
        if num%19==0:
            sum=sum+1
    return sum


def calcularAproximacionPI(parametro): #calcular aproximación de Pi, el máximos denominador lo teclea el usuario
    sum=0
    for num in range (1,parametro+1):
       sum+= 1/num**4
    aprox=(sum*90)**0.25
    return aprox


def hacerSecuencia1(): #el factor uno es un acumulador de factor1*10+factor3
    factor1=0
    factor2=8
    for factor3 in range (1,10):
        factor1 = factor1 * 10 + factor3
        multiplicacion= factor1*factor2+factor3
        print("%d * %d + %d = %d" %(factor1,factor2,factor3,multiplicacion))


def hacerSecuencia2(): #factor se obtiene mediante la cumulación del mismo valor *10 +1
    factor=1
    for num in range(9):
        multiplicacion=factor*factor
        print("%d * %d = %d" %(factor,factor,multiplicacion))
        factor=factor*10+1


def dibujarEspiral(ventana): #la segunda coordenada de una linea es la primera de la siguiente linea que forma la espiral
    for linea in range(0, ANCHO + 1, 10):
        if linea <= 399:
            pygame.draw.line(ventana, NEGRO, (linea, linea), (ANCHO - linea, linea), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - linea, linea), (ANCHO - linea, ANCHO - linea), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - linea, ANCHO - linea), (linea + 10, 800 - linea), 1)
            pygame.draw.line(ventana, NEGRO, (linea + 10, 800 - linea), (linea + 10, linea + 10), 1)


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

        if opcion==1:
            dibujarCuadradosYCirculos(ventana)
        elif opcion==2:
            dibujarParabolas(ventana)
        elif opcion==3:
            dibujarEspiral(ventana)
        elif opcion==4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    opcion=1
    while opcion != 0:
        print("Misión 5. Seleccione que quiere hacer ")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar parábolas")
        print("3. Dibujar espiral")
        print("4. Dibujar círculos")
        print("5. Aproximar PI")
        print("6. Contar divisibles entre 19 ")
        print("7. Imprimir pirámides de números")
        print("0. Salir")
        opcion = int(input("¿Qué desea hacer?"))
        if opcion>=1 and opcion<=4:
            dibujar(opcion)
        elif opcion==5:
            parametro=int(input("Valor del último divisor: "))
            total=calcularAproximacionPI(parametro)
            print("PI: ", total)
            print("")
        elif opcion==6:
            numeros=calcularDivisiblesEntre19()
            print("Números de tres cifras divisibles entre 19: ", numeros)
            print("")
        elif opcion==7:
            hacerSecuencia1()
            print("")
            hacerSecuencia2()
            print("")
        elif opcion<0 or opcion>7:
            print("---Opción no válida, vuelva a intentarlo---")
            print("")
    print("*** Programa terminado :) ***")



# Llamas a la función principal
main()