# Zoe Caballero Domínguez A01747247
# Este es el programa de la misión 5. Dibuja algunas imágenes en la pantalla, calcula pirámides de múmeros, aproxima a PI, entre otras funciones.


#Librerias
import pygame
import random
import math

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


#Dibuja una serie de cuadros y círculos en la pantalla
def dibujarCirculosCuadrados(ventana):
    x = 395
    y = 395

    for lado in range(10, ANCHO - 10, 10):  # Cuadrados
        pygame.draw.rect(ventana, NEGRO, (x, y, lado, lado), 1)
        x = x - 5
        y = y - 5

    for radio in range (10, (ANCHO//2) - 5, 10): #Círculos
        pygame.draw.circle(ventana, NEGRO, (400, 400), radio, 1)


#Dibuja una espiral en la pantalla
def dibujarEspiral(ventana):
    x = 400
    y = 400
    i = 10

    for i in range (0, 400, 10):
        pygame.draw.line(ventana, NEGRO, (x - i, y + i), (x + (i + 10), y + i), 1)
        pygame.draw.line(ventana, NEGRO, (x + (i + 10), y + i), (x + (i + 10), y - (i + 10)), 1)

    for i in range(0, 400, 10):
        pygame.draw.line(ventana, NEGRO, (x - i, y + i), (x - i, y - i), 1)
        pygame.draw.line(ventana, NEGRO, (x - i, y - i), (x + i, y - i), 1)


#Dibuja las parábolas, con colores aleatorios.
def dibujarParabolas(ventana):
    for i in range (0, 400,10):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #colores
        pygame.draw.line(ventana, c, (400 + i, 400), (400, 800 - i), 1)
        pygame.draw.line(ventana, c, (400 + i, 400), (400, 0 + i), 1)
        pygame.draw.line(ventana, c, (400 - i, 400), (400, 0 + i), 1)
        pygame.draw.line(ventana, c, (400 - i, 400), (400, 800 - i), 1)


#Dibuja una flor con círculos
def dibujarCirculos(ventana):
    for i in range (12):
        x = 150 * math.cos(math.radians(-30 * i))
        y = 150 * math.sin(math.radians(-30 * i))
        pygame.draw.circle(ventana, NEGRO, (400 + int(x),400 + int(y)), 150, 1)
        x += 1
        y += 1


#Función dibujar tiene la configuración de pygame y llama a el dibujo elegido por el usuario
def dibujar(opcion):
    # Pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)

        # Llamar a la función del dibujo elegido por el usuario
        dibujo = opcion
        if dibujo == 1:
            dibujarCirculosCuadrados(ventana)
        elif dibujo == 2:
            dibujarParabolas(ventana)
        elif dibujo == 3:
            dibujarEspiral(ventana)
        else:
            dibujarCirculos(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()  # Termina pygame


# El usuario proporciona un número de términos y la función calcula PI siguiendo una fórmula
def aproximarPI(terminos):
    suma = 0  # acumulador

    for i in range(1, terminos + 1):
        suma += (1 / i ** 4)
    aproximacion = (suma * 90) ** 0.25
    return aproximacion


#Calcula los números de tres dígitos divisibles entre 19
def numerosDivisibles():
    contador = 0

    for numero in range (100,1000):
        if numero%19 == 0:
            contador += 1
        else:
            pass
    return contador


#Calcula dos pirámides de numeros
def calcularPiramide1():
    acumulador1 = 0
    acumulador2 = 0

    for contador in range (1,10):
        primerTermino = (acumulador1 * 10) + contador
        restultado = (primerTermino * 8) + contador
        print( primerTermino, "* 8 +", contador,"=", restultado)
        acumulador1 = primerTermino

    for contador in range(1,10):
        termino = (acumulador2 * 10) + 1
        restultado = termino * termino
        print(termino, "*", termino, "=", restultado)
        acumulador2 = termino


#Lee el menú de opciones para el usuario
def leerOpcionMenu():
    print("Misión 5. Seleccione qué quiere hacer.")
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


#Función principal
def main():
    opcion = leerOpcionMenu()

    while opcion != 0:

        if opcion <= 4 and opcion >= 1:
            dibujar(opcion)
        elif opcion == 5:
            terminos = int(input("Numero de terminos: "))
            valorPI = aproximarPI(terminos)
            print("PI = ", valorPI)
        elif opcion == 6:
            print("Los numeros de 3 digitos divisibles entre 19 son: ", numerosDivisibles())
        elif opcion == 7:
            calcularPiramide1()
        elif opcion > 0 or opcion < 7:
            print("Recuerda que las opciones son del 0 al 7")

        opcion = leerOpcionMenu()
    print("Fin del programa. ¡Hasta luego!")


main()
