# Autor: Claudio Mayoral García
# Es un programa que tiene un menu con diferentes opciones que seleccionar. Y cada una de ellas
# llama a un programa en particular.

import pygame   # Librería de pygame
import random   # Libreria para numeros al azar
import math     # Libreria para matemáticas de python

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)


#Esta función da un color aleatorio
def ponerColor():
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    color = (x, y, z) #Da valores aleatorios para cada valor del color
    return color


#Función que dibuja una parábola con lineas de colores aleatorias
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


#Función que dibuja círculos y cuadrados que aumentan su tamaño de 10 pixeles
def dibujarCirculo():
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
        ventana.fill(BLANCO)
        pygame.draw.circle(ventana, NEGRO, (400, 400), 1, 1)
        for radio in range(1, 40):
            pygame.draw.circle(ventana, NEGRO, (400, 400), radio*10, 1)

        for x in range(390, 0, -10):
            pygame.draw.rect(ventana, NEGRO, (x, x, (400 - x) * 2, (400 - x) * 2), 1)
        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


#Funcion que dibuja una espiral
def dibujarPiramide():
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


#Función que dibuja doce círculos que interceptan en el centro de la figura creada
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

        ventana.fill(BLANCO)
        for teta in range(0, 360, 30):
            radianes = (teta * math.pi)/180  #Convierte a PI Radianes
            y = int(math.sin(radianes) * 150)
            x = int(math.cos(radianes) * 150)
            pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)

        pygame.display.flip()
        reloj.tick(1)
    pygame.quit()


#Función que regresa el resultado de la cantidad de veces que 19 es divisible entre numeros de tres cifras
def tresDigitos():
    numero = 0
    for m in range(114, 1000, 19):
        numero = numero+19
    cantidadDeVeces = numero//19
    print("El número de veces que 19 es divisible en números de 3 dígitos es: ", cantidadDeVeces)
    print("")
    return cantidadDeVeces


#Función que toma el número de terminos y regresa la aproximación
def aproximarPI():
    terminos = int(input("Numero de terminos: "))
    suma = 0   #acomulador
    for n in range(1, terminos+1):
        suma += (1/n**4) # suma = suma + 1/n**2

    ap = (suma*90)**0.25
    print("PI = ", ap)


#Funcion que imprime pirámides con multiplicaciones
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


#Función que imprime las opciones pra elegir en el menu
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
    print("")
    return opcion


#Funcion principal
def main():
    opcion = elegirOpcion()
    while opcion != 0:
        if opcion == 1:
            dibujarCirculo()
        elif opcion == 2:
            dibujarParabola()
        elif opcion == 3:
            dibujarPiramide()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            aproximarPI()
        elif opcion == 6:
            tresDigitos()
        elif opcion == 7:
            imprimirPiramides()
        else:
            print("")
            print("No es una opción válida")
            print("")
        opcion = elegirOpcion()
    print("El programa ha terminado")


#Llama a la función principal
main()