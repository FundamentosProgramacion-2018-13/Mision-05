# encoding: UTF-8
# Autor: David Isaí López Jaimes           A01748363
# Muestra un menu que ofrece distintas opciones como dibujar figuras ó hacer cálculos completos

import pygame   # Librería de pygame
import random   # Libreria para cosas aleatorias
import math     # Libreria para usar funciones trigonométricas

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)       # Ausencia de color o sea negro

# Función para poner colores aleatorios
def colorRandom():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Función que dibuja la figura 1
def dibujarCuadrosCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)
        # Hace el dibujo
        for DELTA in range(10, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - DELTA, ALTO // 2 - DELTA, 2 * DELTA, 2 * DELTA), 1)
        for radio in range(10, ALTO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


    # Función del menú de opciones
def leerOpcionMenu():
    print("Menú principal")
    print("1. Dibujar cuadros y circulos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    opcion = int(input("Teclea tu opción: "))
    return opcion


# Función que dibuja la figura 2
def dibujarParabolas():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for x in range(0, ANCHO // 2 + 5, 10):
            pygame.draw.line(ventana, colorRandom(), (x, 400), (400, 400 - x), 1)
            pygame.draw.line(ventana, colorRandom(), (400 + x, 400), (400, x), 1)
            pygame.draw.line(ventana, colorRandom(), (x, 400), (400, 400 + x), 1)
            pygame.draw.line(ventana, colorRandom(), (400 + x, 400), (400, ANCHO - x), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


# Función que dibuja la figura 3
def dibujarEspiral():
        # Inicializa el motor de pygame
        pygame.init()
        # Crea una ventana de ANCHO x ALTO
        ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
        reloj = pygame.time.Clock()  # Para limitar los fps
        termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

        while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
            # Procesa los eventos que recibe
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                    termina = True  # Queremos terminar el ciclo

            # Borrar pantalla
            ventana.fill(BLANCO)

            # Hace el dibujo
            for x in range(0, ANCHO // 2, 10):
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ANCHO // 2 + x), (405 + x, ANCHO // 2 + x), 1)
                pygame.draw.line(ventana, NEGRO, (390 - x, 390 - x), (ANCHO // 2 - x - 10, ANCHO // 2 + x + 10), 1)

            for y in range(0, ANCHO // 2, 10):
                pygame.draw.line(ventana, NEGRO, (400 - y - 10, 390 - y), (400 + y + 5, 400 - y - 10), 1)
                pygame.draw.line(ventana, NEGRO, (400 + y + 5, 400 + y), (400 + y + 5, 400 - y - 10), 1)

            pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
            reloj.tick(40)  # 40 fps

        pygame.quit()  # termina pygame


# Función que dibuja la figura 4
def dibujarCirculos():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Hace el dibujo
        for n in range(12):
            x = int(150 * math.cos(math.radians(-30 * (n + 1))))
            y = int(150 * math.sin(math.radians(-30 * (n + 1))))
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + x, ANCHO // 2 + y), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


# Función que calcula numeros de 3 digitos divisibles entre 19
def divisibles19():
    contador = 0            #Contador
    for total in range(100, 1000):
        if total%19 == 0:
            contador += 1
    return contador


# Función que hace piramides con numeros multiplicandose y los calcla
def piramidesNumeros():
    contador = 1
    acumulador1 = 1
    acumulador2 = 1
    for piramide1 in range(1, 10):
        total = acumulador1 * 8 + contador
        print("%d * 8 + %d = %d" % (acumulador1, contador, total))
        contador = contador + 1
        acumulador1 = acumulador1 * 10 + contador

    for piramide2 in range(1, 10):
        total2 = acumulador2 ** 2
        print("%d * %d = %d" % (acumulador2, acumulador2, total2))
        acumulador2 = acumulador2 * 10 + 1


    #Función que aproxima el valor de PI
def aproximarValorPI(terminos):
    suma = 0    # Acumulador
    for denominador in range(1, terminos + 1):
        suma += 1/denominador**4

    return(90*suma)**0.25

# Función principal
def main():
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosCirculos()
        elif opcion == 2:
            dibujarParabolas()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            terminos = int(input("Teclea cuántos términos quieres: "))
            aproximacionPI = aproximarValorPI(terminos)
            print("PI =", aproximacionPI)
        elif opcion == 6:
            total = divisibles19()
            print("Hay %d numeros de 3 digitos divisibles entre 19" % (total))
        elif opcion == 7:
            piramidesNumeros()
        opcion = leerOpcionMenu()
    print("Termina programa")
    


# Llamamos a la función principal
main()