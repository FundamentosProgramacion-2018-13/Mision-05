#Autor: Saúl Figueroa Conde.
#Matrícula: A01747306.
#Grupo 02.
#Este programa muestra un menú en el cual se pueden ejecutar las distintas funciones: dibujar cuadros y círculos,
#dibujar parábolas, dibujar espiral, dibujar círculos, aproximar PI, Contar divisibles entre 19 e imprimir pirámides de
#números. En el menú se incluye una opción para salir. Cada función hace uso de al menos un ciclo "for" y algunas de
#hacen uso de la librería pygame para dibujar distintas figuras.
#----------------------------------------------------------------------------------------------------------------------

import pygame   # Se importa la librería de pygame (se usará para dibujar figuras).
import random   # Se importa el módulo random.
import math # Se importa el módulo math.

# Estas son las dimensiones de la pantalla.
ANCHO = 800
ALTO = 800

# Colores RGB:
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)       # ausencia de colores para dar negro

# Se crea una lista con los valores de 5 a 255 para generar valores en el rango de colores RGB. Esta se mezcla para que
# la asignación de colores, cuando otra función llame a esta lista, sea aleatoria.
colorList = []
for colores in range(5, 256, 5):
    colorList.append(colores)
    random.shuffle(colorList)
#----------------------------------------------------------------------------------------------------------------------


# Se declara la función imprimirPiramides. No recibe ningún parámetro. Se emplean dos ciclos, uno para imprimir cada
# pirámide. Se calcula y se imprimen los valores correspondientes sin usar cadenas o listas. Se incluye una variable
# "pausa" para dar tiempo al usuario de leer lo que imprime el programa.
def imprimirPiramides():
    num = 8
    for i in range(0, 9):
        secuencia = int(round((10**i+2*10**(i-1)+3*10**(i-2)+4*10**(i-3)+5*10**(i-4)+6*10**(i-5)+7*10**(i-6)+8*10**(i-7)+9*10**(i-8)),1))
        resultado = secuencia * num + (i+1)
        print("{} * {} + {} = {}".format(secuencia, num, i, resultado))
    pausa = input("Presione enter para continuar...")

    for j in range(0, 9):
        secuencia = int(round((10 ** j + 1 * 10 ** (j - 1) + 1 * 10 ** (j - 2) + 1 * 10 ** (j - 3) + 1 * 10 ** (j - 4) + 1 * 10 ** (j - 5) + 1 * 10 ** (j - 6) + 1 * 10 ** (j - 7) + 1 * 10 ** (j - 8)), 1))
        resultado = secuencia * secuencia
        print("{} * {} = {}".format(secuencia, secuencia, resultado))
    pausa = input("Presione enter para continuar...")


# Se declara la función contarDivisibles. No recibe parámetros. Esta función calcula y regresa cuántos números de 3
# dígitos son divisibles entre 19. Esta función hace uso de un solo ciclo "for" para checar qué numeros del 100 al 999
# son divisibles entre 19.
def contarDivisibles():
    numberCount = 0

    for numeros in range(100, 1000, 1):
        if numeros % 19 == 0:
            numberCount = numberCount + 1
        else:
            pass
    return numberCount


# Se declara la función aproximarPI. Recibe como parámetro el valor de la variable "divisor". Antes de realizar las
# operaciones pertinentes, la función checa si el valor de divisor es menor o igual a 0. En tal caso, el programa
# imprime un mensaje de error. Si el valor de divisor es mayor a 0, entonces el programa calcula y regresa una
# aproximación al valor de Pi con base en una serie dada.
def aproximarPI(divisor):
    pi = 0

    if divisor <= 0:
        print("Error: ha tecleado un valor inválido. Inténtelo de nuevo.")

    else:

        for i in range(1, divisor + 1):
            pi = pi + (i**-4)

        pi = pi * 90
        pi = pi ** (1/4)
    return pi


# Se declara la función dibujarCirculos. No recibe parámetros. Esta función dibuja, en una ventana de 800x800 pixeles,
# 12 círculos negros de radio = 150; alrededor del centro de la pantalla de 30 en 30 grados. Se hace uso de un solo
# ciclo "for".
def dibujarCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        radio = 150
        θ = 30

        for circulos in range(1, 13):
            pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + (int(radio * math.cos(math.radians(θ * circulos)))),
            (ALTO // 2) + (int(radio * math.sin(math.radians(θ * circulos))))), radio, 1)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps

    # Después del ciclo principal
    pygame.quit()  # terminar pygame


# Se declara la función dibujarEspiral. No recibe parámetros. Esta función dibuja, en una ventana de 800x800 pixeles,
# líneas negras que se van acercando cada vez más al centro en forma de espiral. La separación entre líneas es de 10
# pixeles. Se hace uso de un solo ciclo "for".
def dibujarEspiral():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for posicion in range(10, ALTO//2, 10):
            pygame.draw.line(ventana, NEGRO, ((ANCHO + 5) - posicion, ALTO - posicion), (0 + posicion, ALTO - posicion), 1)
            pygame.draw.line(ventana, NEGRO, (0 + posicion, ALTO - posicion), (0 + posicion, 0 + posicion), 1)
            pygame.draw.line(ventana, NEGRO, (0 + posicion, 0 + posicion), (ANCHO - (posicion), 0 + posicion), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - posicion, 0 + posicion), (ANCHO - posicion, ALTO - (posicion + 10)), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO - posicion, ALTO - (posicion + 10)), ((ANCHO - 7) - posicion, ALTO - (posicion + 10)), 1)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps

    # Después del ciclo principal
    pygame.quit()  # terminar pygame


# Se declara la función dibujarParabolas. No recibe parámetros. Esta función dibuja, en una ventana de 800x800 pixeles,
# líneas, con colores aleatorios, para formar parábolas. La separación entre líneas es de 10 pixeles. Se emplea un ciclo
# for para dibujar por cada cuadrante (4 en total).
def dibujarParabolas():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        numero = 0

        for posicion1 in range(10, ALTO//2 + 1, 10):

            ALEATORIO = (colorList[numero], colorList[numero + 1], colorList[numero + 2])
            pygame.draw.line(ventana, ALEATORIO, (ANCHO - posicion1, ALTO//2), (ANCHO//2, ALTO//2 - posicion1), 1)
            numero = numero + 1

        numero = 0

        for posicion2 in range(10, ALTO//2 + 1, 10):

            ALEATORIO = (colorList[numero], colorList[numero + 1], colorList[numero + 2])
            pygame.draw.line(ventana, ALEATORIO, (0 + posicion2, ALTO//2), (ANCHO//2, ALTO//2 - posicion2), 1)
            numero = numero + 1

        numero = 0

        for posicion3 in range(10, ALTO // 2 + 1, 10):

            ALEATORIO = (colorList[numero], colorList[numero + 1], colorList[numero + 2])
            pygame.draw.line(ventana, ALEATORIO, (0 + posicion3, ALTO // 2), (ANCHO // 2, ALTO // 2 + posicion3), 1)
            numero = numero + 1

        numero = 0

        for posicion4 in range(10, ALTO // 2 + 1, 10):

            ALEATORIO = (colorList[numero], colorList[numero + 1], colorList[numero + 2])
            pygame.draw.line(ventana, ALEATORIO, (ANCHO - posicion4, ALTO // 2), (ANCHO // 2, ALTO // 2 + posicion4), 1)
            numero = numero + 1

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps

    # Después del ciclo principal
    pygame.quit()  # terminar pygame


# Se declara la función dibujarCuadradosYCirculos. No recibe parámetros. Esta función dibuja, en una ventana de 800x800
# pixeles, cuadros y círculos negros con una separación de 10 pixeles entre líneas. Las figuras se dibujan del centro
# hacia a afuera. Se usan dos ciclos "for", uno para los cuadros y otro para los círculos.
def dibujarCuadradosYCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia suponiendo que no.

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Se termina el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for rect in range(2, ALTO, 20):
            pygame.draw.rect(ventana, NEGRO, [(ANCHO // 2 - rect // 2), (ALTO // 2 - rect // 2), rect, rect], 1)

        for radio in range(1, ALTO//2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2) , radio, 1)

        pygame.display.flip()  # Actualiza los trazos
        reloj.tick(60)  # 60 fps

    # Después del ciclo principal
    pygame.quit()  # terminar pygame


# Se declara la función principal. Aquí se muestra un menú al usuario para resolver los problemas planteados. Si el
# usuario teclea un valor no válido, a la hora de indicar una opción, se imprime un mensaje de error.
def main():
    opcion = -1
    while opcion != 0:

        print("Misión 5. Seleccione qué quiere hacer.")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar parábolas")
        print("3. Dibujar espiral")
        print("4. Dibujar círculos")
        print("5. Aproximar PI")
        print("6. Contar divisibles entre 19")
        print("7. Imprimir pirámides de números")
        print("0. Salir")
        opcion = int(input("¿Qué desea hacer?"))

        if opcion == 1:
            dibujarCuadradosYCirculos()

        elif opcion == 2:
            dibujarParabolas()

        elif opcion == 3:
            dibujarEspiral()

        elif opcion == 4:
            dibujarCirculos()

        elif opcion == 5:
            divisor = int(input("Teclee el valor del último divisor: "))
            pi = aproximarPI(divisor)
            print(pi)
            pausa = input("Presione enter para continuar...")

        elif opcion == 6:
            numberCount = contarDivisibles()
            print("{} números de 3 dígitos son divisibles entre 19".format(numberCount))
            pausa = input("Presione enter para continuar...")

        elif opcion == 7:
            imprimirPiramides()

        elif opcion == 0:
            print("Adiós!")

        else:
            print("Error: indique un valor correcto.")
            pausa = input("Presione enter para continuar...")

#Se llama a la función principal para ejecutar el programa.
main()