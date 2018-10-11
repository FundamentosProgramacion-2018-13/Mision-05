#JEsús Roberto Herrera Vieyra // A01377230
#Programa para elegir entre 7 opciones (Misión 5)


import pygame# Librería de pygame
import random
import math


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
MORADO = (87,35,100)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCuadrosyCirculos():
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

            for lado in range (0, ANCHO, 20):
                pygame.draw.rect(ventana, NEGRO, (ANCHO//2 -lado//2,ALTO//2 -lado//2,lado,lado),1)
            for radio in range (10, ALTO//2, 10):
                pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

            pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
            reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def colorAleatorio():
    opciones= [NEGRO, MORADO, ROJO, AZUL,VERDE_BANDERA]
    color = random.choice(opciones)
    return color

def dibujarParabola():
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

        y = ALTO // 2
        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, colorAleatorio(), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y -= 10
        y = ALTO // 2
        for x in range(ANCHO, ANCHO // 2, -10):
            pygame.draw.line(ventana, colorAleatorio(), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y -= 10
        y = ALTO // 2
        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, colorAleatorio(), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y += 10
        y = ALTO // 2
        for x in range(ANCHO, ANCHO // 2, -10):
            pygame.draw.line(ventana, colorAleatorio(), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y += 10

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEspiral():
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

        x = ANCHO // 2
        y = ALTO // 2

        for incremento in range(5, ANCHO-20, 20):
            pygame.draw.line(ventana, NEGRO, (x, y), (x + incremento, y), 1)
            x = x + incremento
            pygame.draw.line(ventana, NEGRO, (x, y), (x, y - (incremento + 5)), 1)
            y = y - (incremento + 5)
            pygame.draw.line(ventana, NEGRO, (x, y), ((x - (incremento + 10)), y), 1)
            x = x - (incremento + 10)
            pygame.draw.line(ventana, NEGRO, (x, y), (x, (y + (incremento + 15))), 1)
            y = y + (incremento + 15)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(1)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarCirculos():
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

        for x in range(0, 12, 1):
            pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + (int(150 * math.cos(math.radians(-30 * (x))))),
                                                (ANCHO // 2) + (int(150 * math.sin(math.radians(-30 * (x)))))), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps


def aproximarPi(valor):
    suma = 0
    for denominador in range(1, valor +1):
        suma += 1 / denominador**4
    Pi = (90*suma) ** 0.25
    print("Pi se aproxima a: ",Pi)



def contarDivisibles():
    num = 0
    for rango in range(100,1000):
        if rango%19 == 0:
            num = num+1
    print("Existen",num,"números de 3 dígitos que son divisibles entre 19")



def imprimirPiramides():
    piramide = 0
    for linea in range(1,10):
        piramide = piramide * 10 + linea
        resultado = piramide * 8 + linea
        print(piramide,"* 8 +",linea," = ",resultado)
    print("")

    piramide = 1
    for linea in range(1, 10):
        resultado = piramide * piramide
        print(piramide,"*",piramide,"=",resultado)
        piramide = (piramide * 10) + 1



def leerOpciones():
    print("""
1. Dibujar cuadros y círculos
2. Dibujar estrella
3. Dibujar espirales
4. Dibujar círculos
5. Aproximar Pi
6. Contar números divisibles entre 19 que tengoan 3 cifras
7. Pirámides de números
0. Salir""")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion

def main():

    opcion = leerOpciones()

    while opcion != 0:

        if opcion == 1:
            dibujarCuadrosyCirculos()

        elif opcion == 2:
            dibujarParabola()

        elif opcion == 3:
            dibujarEspiral()

        elif opcion == 4:
            dibujarCirculos()

        elif opcion == 5:
            valor = int(input("¿Con qué valor? "))
            aproximarPi(valor)

        elif opcion == 6:
            contarDivisibles()

        elif opcion == 7:
            imprimirPiramides()

        opcion= leerOpciones()
    print("Vuelva pronto!!")


main()