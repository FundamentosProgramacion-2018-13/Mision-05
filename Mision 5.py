#Francisco Ariel Arenas Enciso
#A01369122
#Desarrollo de la misión 5 (ciclos, bucles y figruas en pygame)


#Primero se importa pygame con el fin de tener habilitadas las herramientas necesarias para trabajar.
import pygame

#Un método encontrado en internet para generar colores alternos es importando random y creando una función
import random

#Para la Figura D utilizaremos la libreria de math de python
import math

#Se crean los parametros para la ventana con la que vamos a trabajar
ANCHO = 800
ALTO = 800

#Se establecen los colores con los que se trabajarán
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
#Dentro de los colores se debe de crear una función especial para los colores aleatorios
def coloresRandom():
    colores = [(139, 0,0),
               (0, 100, 0),
               (0, 0, 139)]
    return random.choice(colores)


'''Se crea la función que dibuja la figura A (circulos con cuadrados) mediante las herramientas brindadas
por pygame. Cada sucesión aumenta 10 pixeles. '''
def dibujarFiguraA(ventana):
    for radio in range(10, ALTO//2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)
    for cuadrado in range(10, ALTO//2, 10):
            pygame.draw.rect(ventana, NEGRO, ((ANCHO//2 - cuadrado), (ALTO//2 - cuadrado), cuadrado * 2, cuadrado * 2 ), 1)


'''Esta función dibuja la figura B (parabolas) mediante las herramientas brindadas por pygame, así como de la
librería random de python'''
def dibujarFiguraB(ventana):
    color = coloresRandom()
    colorUno = coloresRandom()
    colorDos = coloresRandom()
    colorTres = coloresRandom()
    for linea in range(40):
        linea = (linea+1)*10
        pygame.draw.line(ventana, color, (400 - linea, 400), (400, linea), 1)
        pygame.draw.line(ventana, colorUno, (400 + linea, 400), (400, linea), 1)
        pygame.draw.line(ventana, colorDos, (400 - linea, 400), (400, 800 - linea), 1)
        pygame.draw.line(ventana, colorTres, (400 + linea, 400), (400, 800 - linea), 1)


'''Esta función dibuja la figura C (laberinto) con las herramientas brindadas por pygame. Esta se forma gracias a que 
a la coordenada inicial se le va restando 10 pixeles por cada que avanza.'''
def dibujarFiguraC(ventana):
    for coordenadaX in range(0, 801, 10):
        if (coordenadaX <= 399):
            pygame.draw.line(ventana,NEGRO,(coordenadaX, coordenadaX),(800-coordenadaX, coordenadaX), 1)
            pygame.draw.line(ventana, NEGRO, (800-coordenadaX,coordenadaX), (800-coordenadaX, 800-coordenadaX), 1)
            pygame.draw.line(ventana, NEGRO, (800-coordenadaX, 800-coordenadaX), (coordenadaX+10,800-coordenadaX), 1)
            pygame.draw.line(ventana, NEGRO, (coordenadaX+10,800-coordenadaX), (coordenadaX + 10, coordenadaX+10), 1)


'''Esta función mediante el uso de pygame dibuja doce circulos con un radio de 150. Para poder obtener la sucesión
de circulos se tuvo que emplear las funciones trigonometricas seno y coseno de la librería math, pues a partir de las
operaciones pitágoricas es que se obtienen las coordenadas tanto para x como para y.'''
def dibujarFiguraD(ventana):
    for angulo in range(0, 360, 30):       # Ciclo el cual aumenta de 30 en 30 grados hasta cumplir los 360.
            posicionEnX = int(math.sin(math.radians(angulo)) * 150)    #Esta operación permite obtener la cordenada x
            posicionEnY = int(math.cos(math.radians(angulo)) * 150)   #Esta operación permite obtener la cordenada y
            pygame.draw.circle(ventana, NEGRO, ((posicionEnX + ANCHO//2), (posicionEnY + ALTO //2)), 150, 1)


'''Esta función lo que permite hacer es alamcenar cada uno de los dibujos anteriores para que cuando el usuario
introduzca un número, este corresponda a la figura deseada.'''
def dibujarFiguras(opcion):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:  # Ciclo principal
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True     # Fin de ciclo principal

        ventana.fill(BLANCO)

        if opcion == 1:
            dibujarFiguraA(ventana)
        elif opcion == 2:
            dibujarFiguraB(ventana)
        elif opcion == 3:
            dibujarFiguraC(ventana)
        elif opcion == 4:
            dibujarFiguraD(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

        # Después del ciclo principal
    pygame.quit()  # termina pygame


'''Esta función recibe de main el total de términos que se emplearán en la sucesión dada en la tarea para aproximar el
valor de PI'''
def aproximarValorPi(terminos):
    suma = 0  # Acumulador
    for denominador in range(1, terminos + 1):
        suma += 1 / denominador ** 4

    return (90 * suma) ** 0.25


'''Esta función mediante un contador ("numeroDivisible") cuenta aquellos números cuya condición (numero % 19 == 0)
resulta cierta'''
def deteminarNumerosDivisibles():
    numeroDivisible = 0
    for numero in range(100, 1000):
        if numero % 19 == 0:
            numeroDivisible = numeroDivisible + 1
    print("Son %2d números con tres cifras los que son múltiplos de 19" % numeroDivisible)


'''Esta función mediante el uso de acumuladores relaiza cada una de las píramides solicitadas'''
def hacerPiramidesDeNumeros():
    valoresEnAumento = 0
    for numero in range(9):
        print((valoresEnAumento * 10 + numero + 1), "*", 8, "+", numero+1, "=", ((valoresEnAumento * 10 + numero + 1) * 8 + (numero+1)))
        valoresEnAumento = valoresEnAumento * 10 + numero + 1

    print("------------------------------")

    aumentoDeUno = 0
    for numero in range(9):
        print((aumentoDeUno * 10 + 1), "*", (aumentoDeUno * 10 + 1), "=", ((aumentoDeUno * 10 + 1)*(aumentoDeUno * 10 + 1)))
        aumentoDeUno = aumentoDeUno * 10 + 1


'''Función que controla todo el programa. Esta función será la que contenga el menú para el usuario'''
def main():
    opcion = -1
    while (opcion != 0):
        opcion = int(input('''
        -----------------------------------------------
        Misión 5. Seleccione qué quiere hacer
        1. Dibujar Dibujar cuadro y círculo
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
            dibujarFiguras(opcion)
        elif opcion == 2:
            dibujarFiguras(opcion)
        elif opcion == 3:
            dibujarFiguras(opcion)
        elif opcion == 4:
            dibujarFiguras(opcion)
        elif opcion == 5:
            print("Para calcular el valor de pi se necesita saber cuantos términos se usaran en la suscesión.")
            terminos = int(input("Para ello, teclea cuántos términos deseas usar: "))
            aproximacionPi = aproximarValorPi(terminos)
            print("PI = ", aproximacionPi)
        elif opcion == 6:
            deteminarNumerosDivisibles()
        elif opcion == 7:
            hacerPiramidesDeNumeros()
        elif opcion == 0:
            print("Gracias por correr el programa")
            break


main()