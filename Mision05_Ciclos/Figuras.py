# encoding: UTF-8
# Autor: Roberto Emmanuel González Muñoz
# Misión 5
from random import randrange

import pygame                               # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)                    # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)                # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)                          # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)                          # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)


# Dibuja la Primera Figura
def dibujarCuadradosCirculos(ventana):
    centro = (ANCHO // 2, ALTO // 2)

    #Dibuja rectángulos en la pantalla
    for delta in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - delta, ALTO // 2 - delta, 2 * delta, 2 * delta), 1)

    #Dibuja círculos en la pantalla
    for radio in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, centro, radio, 1)


# Dibuja la Segunda Figura
def dibujarCuadricula(ventana):
    DELTA = 10

    #Dibuja en 4 sectores una parábola de colores aleatorios.
    for x in range(0, 400, DELTA):
        pygame.draw.line(ventana, (randrange(0,255),randrange(0,255),randrange(0,255)), (x, ALTO//2), (ANCHO//2, x + ALTO//2))
        pygame.draw.line(ventana, (randrange(0,255),randrange(0,255),randrange(0,255)), (ANCHO//2, x), (x + ANCHO//2, ALTO//2))
        pygame.draw.line(ventana, (randrange(0,255),randrange(0,255),randrange(0,255)), (x, ALTO//2), (ANCHO//2, ALTO//2 - x))
        pygame.draw.line(ventana, (randrange(0,255),randrange(0,255),randrange(0,255)), (ANCHO - x, ALTO//2), (ANCHO//2, ALTO//2 + x))


def dibujarLaberinto(ventana):
    DELTA = 10

    # Lineas horizontales
    for x in range(0, 410, DELTA):
        pygame.draw.line(ventana, NEGRO, (x, x), (ANCHO+6 - x, x))
        pygame.draw.line(ventana, NEGRO, (x, x), (x, ALTO+9 - x))
        pygame.draw.line(ventana, NEGRO, (ANCHO+6 - x, x), (ANCHO+6 - x, ALTO - x))
        pygame.draw.line(ventana, NEGRO, (x + 10, ALTO - x), (ANCHO + 6 - x, ALTO - x))


def dibujarCirculos(ventana):
    radius = 150                                   # Radio círculo

    # Dibuja un circulo en las coordenadas en donde el radio tiene una separación de 30 grados.
    pygame.draw.circle(ventana, NEGRO, (550, ALTO//2), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (ANCHO//2, 250), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (250, ALTO//2), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (ANCHO//2, 550), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (475, 270), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (325, 270), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (530, 325), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (270, 325), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (475, 530), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (530, 475), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (270, 475), radius, 1)
    pygame.draw.circle(ventana, NEGRO, (325, 530), radius, 1)


def aproximarPi(terminos):
    sumatoria = 0                                   # Contador en 0.
    for denominador in range(1, terminos + 1):
        sumatoria += 1 / denominador ** 4
    return (sumatoria * 90) ** (1/4)


def divisibles19():
    numero = 0                                      # Contador en variable número.
    valor = 100
    while valor <= 999:
        if valor % 19 == 0:
            numero += 1                             # Cuenta en la variable número.
        valor += 1

    return numero


def piramidesNumericas():
    # Variables contadoras
    c = 1
    a = 0
    z = 0
    b = 1
    k = 0

    # Contador pirámide A
    for x in range(0, 9, 1):
        c = c * 10
        a = a + 1
        z = z * 10 + a
        b = b * 10 + (10 - a)
        print(z, "* 8", "+", a, "=", z * 8 + a)     # Con una cadena el resultado seria (b - c)

    # Contador pirámide B
    for y in range(0, 9, 1):
        k = (k*10)+1
        print(k, "*", k, "=", k*k)


def dibujar(e):
    # Inicializa el motor de pygame
    pygame.init()

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))# Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False                                 # para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:          # El usuario hizo click en el botón de salir
                termina = True                      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        #Evalúa cúal figura se tiene que dibujar dentro de la función Dibujar.
        if e == 1:
            dibujarCuadradosCirculos(ventana)
        elif e == 2:
            dibujarCuadricula(ventana)
        elif e == 3:
            dibujarLaberinto(ventana)
        elif e == 4:
            dibujarCirculos(ventana)
        pygame.display.flip()                       # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)                              # 40 fps (Frames per Second)

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def opcionesMenu():
    print("________________________________________________")
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1.- Dibujar cuadrados y círculos.")
    print("2.- Dibujar parábola.")
    print("3.- Dibujar espiral.")
    print("4.- Dibujar círculos.")
    print("5.- Aproximar Pi.")
    print("6.- Contar divisibles entre 19.")
    print("7.- Imprimir pirámides de números.")
    print("0.- Salir.")
    eleccion = int(input("Qué deseas hacer?"))
    print("________________________________________________")
    return eleccion


def main():
    opcion = opcionesMenu()
    while opcion != 0:
        if opcion == 1:
            dibujar(opcion)

        elif opcion == 2:
            dibujar(opcion)
            
        elif opcion == 3:
            dibujar(opcion)

        elif opcion == 4:
            dibujar(opcion)
            
        elif opcion == 5:
            numero = int(input("Indique el número de terminos: "))
            aproximado = aproximarPi(numero)
            print(aproximado)

        elif opcion == 6:
            total = divisibles19()
            print("Hay %d múltiplos de 19 entre los números de 3 digitos" % total)

        elif opcion == 7:
            piramidesNumericas()

        opcion = opcionesMenu()
    print("Termina programa")


# Llamas a la función principal
main()