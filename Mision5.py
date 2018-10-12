# Author: Ivan Honc Ayón
# Descripción: Este programa es multiusos y cuenta con varias funciones, desde dibujos de pygame hasta pirámides algebraicas.
import math
import random
import pygame


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


# Esta función dibuja, a través de la librería pygame, rectangulos y circulos cada 10 pixeles de color negro y en una
# ventana de 800x800.
def dibujarCuadrosCirculos(ventana):
    for x in range(2, ALTO, 10):
        pygame.draw.rect(ventana, NEGRO, [(ANCHO // 2 - x // 2), (ALTO // 2 - x // 2), x, x], 1)

    for y in range(1, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), y, 1)


# Esta función dibuja, a través de la librería pygame, 4 parabolas centradas para formar una sola figura en una ventana
# de 800 x 800, asimismo, se usa la librería random para calcula aleatoriamente los colores de las parábolas.
def dibujarCuatroParabolas(ventana):
    for x in range(10, ALTO // 2 + 1, 10):
        color1 = (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))
        color2 = (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))
        color3 = (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))
        color4 = (random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))

        pygame.draw.line(ventana, color1, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))
        pygame.draw.line(ventana, color2, (0 + x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))
        pygame.draw.line(ventana, color3, (0 + x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))
        pygame.draw.line(ventana, color4, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))


# Esta función, a travpes de la librería pyga,e, dibuja líneas que en conjunto hacen un espiral.

def dibujarEspiralCuadrado(ventana):
    for x in range(10, ALTO // 2, 10):
        pygame.draw.line(ventana, NEGRO, ((ANCHO + 5) - x, ALTO - x), (0 + x, ALTO - x))
        pygame.draw.line(ventana, NEGRO, (0 + x, ALTO - x), (0 + x, 0 + x))
        pygame.draw.line(ventana, NEGRO, (0 + x, 0 + x), (ANCHO - x, 0 + x))
        pygame.draw.line(ventana, NEGRO, (ANCHO - x, 0 + x), (ANCHO - x, ALTO - (x + 10)))
        pygame.draw.line(ventana, NEGRO, (ANCHO - x, ALTO - (x + 10)), ((ANCHO - 7) - x, ALTO - (x + 10)))

# Esta función dibuja círculos a través de la librería pygame, a través de una circunferencia central, cada 30 grados se
# dibuja un cículo que parte del radio del círculo central.
def dibujarFlorCirculos(ventana):
    radio = 150
    angulo = 30
    for x in range(1, 13):
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + (int(radio * math.cos(math.radians(angulo * x)))),
                                            (ALTO // 2) + (int(radio * math.sin(math.radians(angulo * x))))),
                           radio, 1)


# Esta función inicia pygame y sus funciones, asimismo manda a llamar a las funciones que requieren de pygame.
def dibujarFiguras(numeroActividad):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        if numeroActividad == 1:
            dibujarCuadrosCirculos(ventana)
        elif numeroActividad == 2:
            dibujarCuatroParabolas(ventana)
        elif numeroActividad == 3:
            dibujarEspiralCuadrado(ventana)
        elif numeroActividad == 4:
            dibujarFlorCirculos(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


# Esta función recibe un calor de denominador y establece operaciones matemáticas para calcula el número más cercano a
# Pi con el número dado.
def calcularSeriePi(denominadorPi):
    suma = 0
    for denominador in range(1, denominadorPi + 1):
        suma += 1 / denominador ** 4
    numeroCercanoPi = (suma * 90) ** (1 / 4)

    return numeroCercanoPi

# Esta función determina cuantos números de tres digitos son divisibles entre 19 y regresa la cantidad de números.
def numerosTresDigitosDivisblesEntre19():
    numeroDivisble = 0
    for x in range(100, 1000):
        if x % 19 == 0:
            numeroDivisble=numeroDivisble+1
    return numeroDivisble


# Esta función hace dos pirámides con operaciones aritméticas.
def piramideNumeros():
    cadenaNumeros = 0
    cadenaUnos = 0

    for x in range(1,10):
        cadenaNumeros = cadenaNumeros*10+x
        resultado = cadenaNumeros*8+x
        print("%d*8+%d=%d" % (cadenaNumeros, x, resultado))
    for y in range(9):
        cadenaUnos = cadenaUnos*10+1
        resultadoDos = cadenaUnos*cadenaUnos
        print("%d*%d=%d" % (cadenaUnos, cadenaUnos, resultadoDos))


# Esta función mantiene el menú de opciones activo hasta que el usuario lo requiera.
def menu():
    numeroActividad = int
    while numeroActividad != 0:
        print("""
1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar espiral
4. Dibujar círculos
5. Aproximar PI
6. Contar divisibles de tres dígitos entre 19
7. Imprimir pirámides de números
0. Salir""")
        numeroActividad = int(input("¿Qué número de actividad deseas realizar? "))
        if 1 <= numeroActividad <= 4:
            dibujarFiguras(numeroActividad)
        if numeroActividad == 5:
            denominadorPi = int(input("¿Cuál es el valor del último divisor? "))
            numeroCercanoPi = calcularSeriePi(denominadorPi)
            print(numeroCercanoPi)
        if numeroActividad == 6:
            numeroDivisible19 = numerosTresDigitosDivisblesEntre19()
            print(numeroDivisible19)
        if numeroActividad == 7:
            piramideNumeros()
        if numeroActividad == 0:
            print("Terminando programa")
        if 7<=numeroActividad or numeroActividad<=0:
            print("Error: El número no está en las opciones")


# La función main solo manda llamar al menú, ahí se realiza el llamado a todas la funciones del programa.
def main():
    menu()


main()
