# Alex Fernando Leyva Martínez, A01747078, 04
# Esta función proporciona un menú que permite hacer distintas acciones

import pygame  # Librería de pygame
import math     # Libreria para matemáticas de python
import random   # Libreria para valores aleatorios

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

#Esta función asigna un color aleatorio
def ponerColor():
    x = random.randint(0,255)
    y = random.randint(0,255)
    z = random.randint(0,255)
    color = (x, y, z)
    return color

#Función que dibuja una parábola
def dibujarParabola():
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

        # Dibujar, aquí haces todos los trazos que requieras
        ventana.fill(BLANCO)
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(ventana, ponerColor(), (x, 400), (400, 400 - x))
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(ventana, ponerColor(), (x, 400), (400, 400 + x))
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(ventana, ponerColor(), (800 - x, 400), (400, 400 - x))
        for x in range(0, 400 + 1, 10):
            pygame.draw.line(ventana, ponerColor(), (800 - x, 400), (400, 400 + x))

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Función que dibuja cuadros y círculos
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
                termina = True  # Queremos terminar el ciclo
        ventana.fill(BLANCO)
        pygame.draw.circle(ventana, NEGRO, (400, 400), 1, 1)
        for radio in range(1, 40):
            pygame.draw.circle(ventana, NEGRO, (400, 400), radio * 10, 1)
        for x in range(390, 0, -10):
            pygame.draw.rect(ventana, NEGRO, (x, x, (400 - x) * 2, (400 - x) * 2), 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


 # Funcion que dibuja una espiral
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
        ventana.fill(BLANCO)
        for x in range(0, ANCHO + 1, 10):
            if x < 400:
                pygame.draw.line(ventana, NEGRO, (800 - x, 800 - x), (0 + x, 800 - x))
        for x in range(0, ANCHO + 1, 10):
            if x < 400:
                pygame.draw.line(ventana, NEGRO, (0 + x, 800 - x), (0 + x, x))
        for x in range(0, ANCHO + 1, 10):
            if x > 400:
                pygame.draw.line(ventana, NEGRO, (800 - x, 800 - x), (x - 10, 800 - x))
        for x in range(0, ANCHO + 1, 10):
            if x > 400:
                pygame.draw.line(ventana, NEGRO, (0 + x - 10, 800 - x), (0 + x - 10, x - 10))
        pygame.draw.line(ventana, BLANCO, (790, 0), (790, 789), 1)
        pygame.draw.line(ventana, BLANCO, (0, 0), (0, 800), 1)
        pygame.draw.line(ventana, BLANCO, (0, 0), (800, 0), 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()

# Función que dibuja varios circulos que se intersectan en el centro de la ventana
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

        ventana.fill(BLANCO)
        for teta in range(0, 360, 30):
            radianes = (teta * math.pi) / 180  # Convierte a PI Radianes
            y = int(math.sin(radianes) * 150)
            x = int(math.cos(radianes) * 150)
            pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)

        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


# Esta función permite dar un valor aproximado al valor de PI con respecto al número de términos solicitados
def aproximarPI():
    terminos = int(input("Número de términos: "))
    suma = 0
    for n in range(1, terminos+1):
        suma += (1/n**4)

    aproximacion = (suma*90) ** .25
    print("PI = ", aproximacion)


# Esta función permite calcular la cantidad de números de 3 dígitos divisibles entre 19
def calcularDivisores():
    multiplos = 0
    valor = 100
    while valor <= 999:
        if valor % 19 == 0:
            multiplos += 1
        valor += 1
    print("Hay %d números entre 100 y 999 divisibles entre 19" % (multiplos))

#Esta función permite imprimir tablas de multiplicar en forma de pirámides
def imprimirPiramides():
    contador = 1
    adicion = 0
    multiplo = 0
    while contador < 10:
        adicion += 1
        contador += 1
        multiplo = multiplo * 10 + adicion
        producto = multiplo * 8 + adicion
        print(multiplo,"X","8","+",adicion,"=",producto)
    contador = 1
    elemento = -1
    multiplo = 0
    while contador < 10:
        contador += 1
        elemento += 1
        multiplo = multiplo * 10 + 1
        producto = multiplo * multiplo
        print(multiplo, "*", multiplo, "=", producto)

# Esta función muestra las opciones y permite elegir una
def leerOpcionMenu():
    print("Menú Principal")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("Qué desea hacer?"))
    return opcion

# Esta función llama a la función elegida
def main():
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadrosCirculos()
        elif opcion == 2:
            dibujarParabola()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            aproximarPI()
        elif opcion == 6:
            calcularDivisores()
        elif opcion == 7:
            imprimirPiramides()
        else:
            print("---Hay un error---")
        opcion = leerOpcionMenu()
    print("Termina Programa")

main()


