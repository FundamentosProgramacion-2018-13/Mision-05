"""
#Autor: Alexys Martín Coate Reyes
#Descripción: Elaborar un menú que te de a elegir diversas opciones y que termine el programa al introducir 0

"""

import pygame
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
NEGRO = (0,0,0)


def leerMenu():

    print("1. Dibujar Cuadrados y Círculos")
    print("2. Dibujar Parábolas")
    print("3. Dibujar Espiral")
    print("4. Dibujar Círculos")
    print("5. Aproximar Pi")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion

def dibujarCuadrados(ventana):
    for i in range(-10,400,10):
        nuevaX = i+10
        nuevaY = i+10
        ladoNuevo = ANCHO - (2*i+20)
        pygame.draw.rect(ventana, NEGRO, (nuevaX, nuevaY, ladoNuevo, ladoNuevo), 1)
def dibujarCirculo(ventana):
    # Características del círculo
    posCirculoX = 400
    posCirculoY = 400
    anchoCirculo = 1
    for radio in range(10,401,10):
        pygame.draw.circle(ventana, NEGRO,(posCirculoX,posCirculoY), radio, anchoCirculo)

def dibujarParabolas(ventana):

    for color in range (4):
        lista = [VERDE_BANDERA, ROJO, AZUL, NEGRO]
        color = random.choice(lista)

    for color1 in range(4):
        lista = [VERDE_BANDERA, ROJO, AZUL, NEGRO]
        color1 = random.choice(lista)

    for color2 in range(4):
        lista = [VERDE_BANDERA, ROJO, AZUL, NEGRO]
        color2 = random.choice(lista)

    for color3 in range(4):
        lista = [VERDE_BANDERA, ROJO, AZUL, NEGRO]
        color3 = random.choice(lista)

# Dibuja el sector inferior izquierdo
    for division in range(0,400,10):
        centro = ANCHO/2
        xInicial = division
        yInicial = centro
        xFinal = centro
        yFinal = division + 410
        posicionInicial = (xInicial,yInicial)
        posicionFinal = (xFinal,yFinal)
        pygame.draw.line(ventana, color, posicionInicial, posicionFinal,1)

#Dibuja el sector inferior derecho
    for division in range(0, 400, 10):
        centro = ANCHO / 2
        xInicial = 800 - division
        yInicial = centro
        xFinal = centro
        yFinal = division + 410
        posicionInicial = (xInicial, yInicial)
        posicionFinal = (xFinal, yFinal)
        pygame.draw.line(ventana, color3, posicionInicial, posicionFinal, 1)


# Dibuja el sector superior izquierdo
    for division in range(0, 400, 10):
        centro = ANCHO / 2
        xInicial = division
        yInicial = centro
        xFinal = centro
        yFinal = 410 - division
        posicionInicial = (xInicial, yInicial)
        posicionFinal = (xFinal, yFinal)
        pygame.draw.line(ventana, color2, posicionInicial, posicionFinal, 1)

# Dibuja el sector superior derecho
    for division in range(0, 400, 10):
        centro = ANCHO / 2
        xInicial = 800 - division
        yInicial = centro
        xFinal = centro
        yFinal = 410 - division
        posicionInicial = (xInicial, yInicial)
        posicionFinal = (xFinal, yFinal)
        pygame.draw.line(ventana, color1, posicionInicial, posicionFinal, 1)

def dibujarEspiral(ventana):
    for x in range(0, 800, 10):
        if x <= 399:
            pygame.draw.line(ventana,NEGRO,(x,x+5),(800-x,x+5), 1)
            pygame.draw.line(ventana, NEGRO, (800-x,x+5), (800-x, 800-x), 1)
            pygame.draw.line(ventana, NEGRO, (800-x, 800 - x), (x+10,800-x), 1)
            pygame.draw.line(ventana, NEGRO, (x+10,800-x), (x + 10, x+10+5), 1)

def dibujarCirculos(ventana):
    radio = 150
    for angulo in range(0,361,30):
        anguloRadianes = math.radians(angulo)
        x = int(radio*(math.cos(anguloRadianes)))
        y = int(radio *(math.sin(anguloRadianes)))
        pygame.draw.circle(ventana, NEGRO,(x+400,y+400), radio, 1)

def aproximarPI(terminos):
    suma = 0  # Acomulador
    for n in range(1,terminos+1):
        suma += 1/(n**4)
    ap = (suma*90)**(1/4)
    return ap

def multiplosDe19():
    base = 19
    veces = 1000//base
    min = 100//base
    numerosDivisibles = veces-min
    print("Numeros divisibles: {}" .format(numerosDivisibles))

def piramides():
    resultado = 0
    primerNumero1 = 0
    primerNumero2 = 0

    for suma in range (0,9):
        primerNumero1 = suma+1+(primerNumero1*10)
        segundoNumero1 = 8
        tercerNumero1 = suma+1
        resultado1 = primerNumero1*segundoNumero1+tercerNumero1
        print("%d * %d + %d = %d" % (primerNumero1, segundoNumero1, tercerNumero1, resultado1))


    for paso in range(0,9):
        potencia = 10**paso
        primerNumero2 = (1*potencia)+primerNumero2
        resultado2 = primerNumero2**2
        print("%d * %d = %d" % (primerNumero2, primerNumero2, resultado2))

def main():
    opcion = leerMenu()

    while opcion != 0:
        if opcion == 1:
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
                        termina = True  # Queremos terminar el ciclo

                # Borrar pantalla
                ventana.fill(BLANCO)

                # Dibujar, aquí haces todos los trazos que requieras
                # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
                # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
                dibujarCirculo(ventana)
                dibujarCuadrados(ventana)


                pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
                reloj.tick(1)  # 40 fps
            pygame.quit()  # termina pygame

        elif opcion == 2:
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
                        termina = True  # Queremos terminar el ciclo

                # Borrar pantalla
                ventana.fill(BLANCO)

                # Dibujar, aquí haces todos los trazos que requieras
                # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
                # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
                dibujarParabolas(ventana)

                pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
                reloj.tick(1)  # 40 fps
            pygame.quit()  # termina pygame

        elif opcion == 3:
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
                        termina = True  # Queremos terminar el ciclo

                # Borrar pantalla
                ventana.fill(BLANCO)

                # Dibujar, aquí haces todos los trazos que requieras
                # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
                # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
                dibujarEspiral(ventana)

                pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
                reloj.tick(1)  # 40 fps
            pygame.quit()  # termina pygame

        elif opcion == 4:
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
                        termina = True  # Queremos terminar el ciclo

                # Borrar pantalla
                ventana.fill(BLANCO)

                # Dibujar, aquí haces todos los trazos que requieras
                # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
                # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
                dibujarCirculos(ventana)

                pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
                reloj.tick(1)  # 40 fps
            pygame.quit()  # termina pygame

        elif opcion == 5:
            terminos = int(input("Número de términos; "))
            valorPI = aproximarPI(terminos)
            print("PI = ", valorPI)
            aproximarPI(terminos)
        elif opcion == 6:
            multiplosDe19()
        elif opcion == 7:
            piramides()
        else:
            print("Ingresa un nuevo número")
        opcion = leerMenu()

    print("Termina el programa")

# Llamas a la función principal
main()


