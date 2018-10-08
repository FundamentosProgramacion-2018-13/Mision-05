# Autor: Alejandro Torices Oliva
# Es un programa que despliega un menú y permite al usuario escoger entre 7 tareas.

# Import
import pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


# Es una función que despliega el menu y regresa la orden elegida.
def leerOrden():
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("")
    orden = int(input("¿Qué desea hacer?"))
    print("")
    return orden


# Es una función que regresa un color aleatorio
def colorearAleatorio():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Es una función que dibuja cuadros y círculos de distintos tamaños que tienen un centro en común.
def dibujarCuadrosYCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for radio in range(390, 0, -10):
            pygame.draw.circle(ventana, NEGRO, (400, 400), radio, 1)

        for y in range(400, 0, -10):
            pygame.draw.rect(ventana, NEGRO, (y, y, (400-y)*2, (400-y)*2), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


# Es una función que dibuja una figura compuesta de varias lineas de colores aleatorios.
def dibujarParabolas():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for x in range(0, 401, 10):
            pygame.draw.line(ventana, colorearAleatorio(), (x, 400), (400, 400-x), 1)
            pygame.draw.line(ventana, colorearAleatorio(), (400+x, 400), (400, x), 1)
            pygame.draw.line(ventana, colorearAleatorio(), (x, 400), (400, 400+x), 1)
            pygame.draw.line(ventana, colorearAleatorio(), (400+x, 400), (400, 800-x), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


# Es una función que dibuja una espiral compuesta de líneas rectas.
def dibujarEspiral():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for x in range(0, 400, 10):
            pygame.draw.line(ventana, NEGRO, (400 - x, 400 - x), (400 - x, 400 + x), 1)
            pygame.draw.line(ventana, NEGRO, (400 - x, 400 + x), (405 + x, 400 + x), 1)
        for y in range(0, 390, 10):
            pygame.draw.line(ventana, NEGRO, (390 - y, 390 - y), (405 + y, 390 - y), 1)
            pygame.draw.line(ventana, NEGRO, (405 + y, 390 - y), (405 + y, 400 + y), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


# Es una función que dibuja 12 circulos del mismo radio que se tocan entre sí.
def dibujarCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for angulo in range(0, 360, 30):
            radianes = (angulo / 180) * math.pi
            x = math.sin(radianes) * 150
            y = math.cos(radianes) * 150

            x = int(x)
            y = int(y)

            pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)
        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


# Es una función que aproxima el valor de PI dado un número de términos.
def aproximarPI(terminos):
    suma = 0  # ACUMULADOR
    for n in range(1, terminos + 1):
        suma += (1 / n ** 4)  # suma = suma + 1/n**2
    ap = (suma * 90) ** 0.25
    return ap


# Es una función que calcula cuántos números de 3 digitos son divisibles entre 19.
def contarDivisibles19():
    multiplos19 = list(range(114, 1000, 19))  # 114 es el primer multiplo de 19 de 3 digitos
    cuenta = len(multiplos19)
    return cuenta


# Es una función que calcula e imprime dos pirámides de números.
def imprimirPiramides():
    print("")
    factor = 0
    for x in range(1, 10):
        factor = factor * 10 + x
        resultado = factor * 8 + x
        print(factor, "* 8 +", x, "=", resultado)

    print("")
    factores = 1
    for multiplo in range(1, 10):
        resultado = factores * factores
        print(factores, "*", factores, "=", resultado)
        factores = factores * 10 + 1


# Es la función principal.
def main():
    orden = leerOrden()
    while orden != 0:
        if orden == 1:
            dibujarCuadrosYCirculos()
        elif orden == 2:
            dibujarParabolas()
        elif orden == 3:
            dibujarEspiral()
        elif orden == 4:
            dibujarCirculos()
        elif orden == 5:
            print("")
            terminos = int(input("Número de términos: "))
            print("")
            valorPI = aproximarPI(terminos)
            print("PI =", valorPI)

        elif orden == 6:
            divisibles = contarDivisibles19()
            print("")
            print("La cantidad de números de 3 digitos divisibles entre 19 es:", divisibles)

        elif orden == 7:
            imprimirPiramides()

        else:
            print("")
            print("error, ingrese una opción valida.")
            print("")
        orden = leerOrden()
    print("Termina programa.")


main()
