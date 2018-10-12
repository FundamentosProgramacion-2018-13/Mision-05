# Autor: Damián Iván García Ravelo
# Muestra distintas opciones que el usuario decida ver entre distintos dibujos y operaciones matemáticas

import pygame   # Librería de pygame

from random import  randint #Libreria random, importa enteros random

import math #Librer

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
negro = (0,0,0)
BLANCO = (255,255,255)

def dibujarCuadrosYCirculos(ventana): #Función para dibujar cuadrados y circulos
    for x in range(80):#For para dibujar cuadros
        pygame.draw.rect(ventana, negro, (400-(x*5),400-(x*5), x*10, x*10),1)

    for y in range(10,400,10): #For para dibujar circulos
        pygame.draw.circle(ventana,negro,(400,400),y,1)


def dibujarParabola(ventana):#Función para dibujar parabola

    for x in range(0, 401, 10):
        color = randint(0, 255), randint(0, 255), randint(0, 255)  # color aleatorio
        pygame.draw.line(ventana, color, (x, 400), (400, 400+x)) #sector izquierdo abajo
        pygame.draw.line(ventana,color,(800-x,400),(400,400+x)) #sector derecho abajo
        pygame.draw.line(ventana,color,(x,400),(400,400-x)) #sector izquierdo arriba
        pygame.draw.line(ventana,color,(800-x,400),(400,400-x)) #sector derecho arriba

def dibujarCaracol(ventana): #Función para dibujar el espiral
    for x in range (0, 400, 10):
        pygame.draw.line(ventana, negro, (400 + (x + 10), 400 + x), (400 + (x + 10), 400 - (x + 10)),1)  # dibuja el cuarto de la derecha
        pygame.draw.line(ventana, negro, (400 - x, 400 + x), (400 - x, 400 - x), 1)  # dibuja el cuarto de la izquierda
        pygame.draw.line(ventana, negro, (400 - x, 400 + x), (400 + (x + 10), 400 + x), 1) #Dibuja el cuarto de abajo
        pygame.draw.line(ventana, negro, (400 - x, 400 - x), (400 + x, 400 - x), 1) #dibuja el cuarto de arriba




def dibujarCirculos(ventana): #Función para dibujar círculos que se intersectan
    radio=150 #radio de cada circulo
    angulo=math.pi/6  #conversión de degrees a radianes

    for circulos in range(13):
        pygame.draw.circle(ventana, negro, ((400) + (int(radio * math.cos((angulo * circulos)))), #movimiento en "x" y "y" usando trigonometría
                                            (400) + (int(radio * math.sin((angulo * circulos))))), radio,
                           1)

def aproximarPI(): #Función para proximar PI
    terminos = int(input("Numero de términos: ")) #El usuario da el numero de terminos a usar
    suma = 0 #Acumulador comienza en 0
    for n in range (1, terminos+1): #Se define el rango desde 1 hasta el valor dado por el usuario
        suma += (1/n**4) #Suma = suma + 1/n*4. El acumulador va a añadir las cantidades que vaya obteniendo

    ap= (suma*90)**0.25 #despeje de la formula original
    print(ap) #imprime el valor de pi


def dividirEntreNumero(): #función para encontrar numeros divisibles entre 19
    cuenta = 0 #contador comienza en 0
    for i in range(100, 1000): #numeros de 100 a 999 (3 dígitos)
        if i % 19 == 0: #numero módulo de 19 da 0
            cuenta = cuenta + 1 #si pasa eso, el contador suma 1 a su cuenta
    print("Desde 100 hasta 999 hay",cuenta,"divisibles entre 19") #Imprime la cantidad de numeros divisibles entre 19

def calcularNumerosPiramide(): #Función para formar 2 pirámides de números
    contador=0 #contador1 comienza en 0
    for x in range (1,10): #la pirámide es de 9 escalones
        primerValor = (contador*10)+x #función para ir aumentando 1 dígito a la derecha
        resultado= (primerValor*8)+x #cálculo del resultado
        print(primerValor,"*8+",x,"=",resultado) #imprime el resultado
        contador = primerValor #el contador recibe lo obtenido por el primer valor
    print()
    cuenta=0 #contador2 comienza en 0
    for y in range (1,10): #la pirámide es de 9 escalones
        cuenta = (cuenta*10)+1 #función para aumentar 1 a la derecha
        resultado = cuenta*cuenta #el resultado se obtiene multiplicando el valor de cuenta por si mismo
        print (cuenta,"*",cuenta,"=",resultado) #imprime el valor obtenido


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

        if opcion==1:
            dibujarCuadrosYCirculos(ventana)
        if opcion==2:
            dibujarParabola(ventana)
        if opcion==3:
            dibujarCaracol(ventana)
        if opcion==4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def leerOpcionMenu():#Función para que el usuario escoga el programa a correr
    print()
    print("Misión 5: Seleccione qué quiere hacer")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. AproximarPi")
    print("6. Contar divisibles entre 19")
    print("7. Imrpimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    opcion = int(input("Teclea tu opción: "))
    return opcion

# Función principal, aquí resuelves el problema
def main():
    opcion = leerOpcionMenu()
    while opcion!=0:
        if opcion >=1 and opcion <=4:
            dibujar(opcion)
        if opcion==5:
            aproximarPI()
        if opcion ==6:
            dividirEntreNumero()
        if opcion==7:
            calcularNumerosPiramide()
        elif opcion>7:
            print("Ingrese un valor en el rango permitido")

        opcion=leerOpcionMenu()




# Llamas a la función principal
main()