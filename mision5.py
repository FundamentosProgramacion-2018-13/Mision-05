# Autor: Jesús Emmanuel Alcalá Nava
# Descripción: este programa te da un menú con diferentes opciones y el usuario elije lo que desea que el programa haga

#librerias
import pygame
import random
import math

# ancho y alto de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


#color aleatorio
def colorAleatorio():
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    color = (x, y, z)
    return color


# función que dibuja las parábolas con colores aleatorios
def dibujarParabola():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        pantalla.fill(BLANCO)
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(pantalla, colorAleatorio(), (x, 400), (400, 400 - x))
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(pantalla, colorAleatorio(), (x, 400), (400, 400 + x))
        for x in range(0, 400 + 1, 10) :
            pygame.draw.line(pantalla, colorAleatorio(), (800 - x, 400), (400, 400 - x))
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(pantalla, colorAleatorio(), (800 - x, 400), (400, 400 + x))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


# dibuja los círculos con los cuadrados
def dibujarCirculo():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False
    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        pantalla.fill(BLANCO)
        pygame.draw.circle(pantalla, NEGRO, (400, 400), 1, 1)
        for radio in range(1, 40):
            pygame.draw.circle(pantalla, NEGRO, (400, 400), radio*10, 1)
        for x in range(390, 0, -10):
            pygame.draw.rect(pantalla, NEGRO, (x, x, (400 - x) * 2, (400 - x) * 2), 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


#Funcion que dibuja el espiral
def dibujarEspiral():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False

    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        pantalla.fill(BLANCO)
        for x in range(0, ANCHO + 1, 10):
            if x < 400:
                pygame.draw.line(pantalla, NEGRO, (800 - x, 800 - x), (0 + x, 800 - x))
        for x in range(0, ANCHO + 1, 10):
            if x < 400:
                pygame.draw.line(pantalla, NEGRO, (0 + x, 800 - x), (0 + x, x))
        for x in range(0, ANCHO + 1, 10):
            if x > 400:
                pygame.draw.line(pantalla, NEGRO, (800 - x, 800 - x), (x - 10, 800 - x))
        for x in range(0, ANCHO + 1, 10):
            if x > 400:
                pygame.draw.line(pantalla, NEGRO, (0 + x - 10, 800 - x), (0 + x - 10, x - 10))
        pygame.draw.line(pantalla, BLANCO, (790, 0), (790, 789), 1)
        pygame.draw.line(pantalla, BLANCO, (0, 0), (0, 800), 1)
        pygame.draw.line(pantalla, BLANCO, (0, 0), (800, 0), 1)

        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


#Dibujar los doce círculos
def dibujarCirculos():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    end = False
    while not end:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                end = True
        pantalla.fill(BLANCO)
        for teta in range(0, 360, 30):
            radianes = (teta * math.pi)/180
            y = int(math.sin(radianes) * 150)
            x = int(math.cos(radianes) * 150)
            pygame.draw.circle(pantalla, NEGRO, (400 + x, 400 + y), 150, 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


# función que regresa el resultado de la cantidad de veces que 19 es divisible entre numeros de tres dígitos
def tresDigitos():
    numero = 0
    for n in range(114, 1000, 19):
        numero = numero+19
    veces = numero//19
    print("El número de veces que 19 es divisible en números de 3 dígitos es: ", veces)
    print("")
    return veces


# función que toma el número de términos y regresa la aproximación
def aproximarPI():
    terminos = int(input("Numero de términos: "))
    suma = 0
    for n in range(1, terminos+1):
        suma += (1/n**4)
    aproximacion = (suma*90)**0.25
    print("PI = ", aproximacion)


# funcion que imprime las pirámides de números
def imprimirPiramides():
    numero = 0
    for x in range(1, 10):
        numero = numero * 10 + x
        resultado = numero * 8 + x
        print("%d x 8 + %d = " % (numero, x), resultado)
    print("")
    numero2 = 1
    for multiplo in range(1, 10):
        resultado = numero2 * numero2
        print("%d x %d = " % (numero2, numero2), resultado)
        numero2 = numero2 * 10 + 1
    print("")


# función para escoger la opción que se desea, cada que se cierra la impresión se repite el menú
def elegirOpcion():
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas ")
    print("3. Dibujar espiral")
    print("4. Dibujar círculo")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir ")
    opcion = int(input("¿Qué desea hacer? "))
    return opcion


# funcion principal
def main():
    opcion = elegirOpcion()
    while opcion != 0:
        if opcion == 1:
            dibujarCirculo()
        elif opcion == 2:
            dibujarParabola()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            aproximarPI()
        elif opcion == 6:
            tresDigitos()
        elif opcion == 7:
            imprimirPiramides()
        opcion = elegirOpcion()
    print("El programa ha terminado")


# llama a la función principal
main()