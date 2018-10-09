# Autor: Jocelyn López Ortíz
# Misión 5: Funciones con for

import pygame   # Librería de pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)



def dibujarCuadrosYCirculos(ventana):
    for alfa in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - alfa, ALTO // 2 - alfa, alfa * 2, alfa * 2), 1)
    for beta in range(10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), beta, 1)


def dibujarParabolas(ventana):
    for delta in range(0, ALTO // 2, 10):

        colorRandom = (random.randrange(255), random.randrange(255), random.randrange(255))

        pygame.draw.line(ventana, colorRandom, (ANCHO // 2, delta), (ANCHO // 2 - delta, ALTO // 2))
        pygame.draw.line(ventana, colorRandom, (ANCHO // 2, delta), (ANCHO // 2 + delta, ALTO // 2))
        pygame.draw.line(ventana, colorRandom, (ANCHO // 2, ALTO - delta), (ANCHO // 2 + delta, ALTO // 2))
        pygame.draw.line(ventana, colorRandom, (ANCHO // 2, ALTO - delta), (ANCHO // 2 - delta, ALTO // 2))


def dibujarEspiral(ventana):
    for delta in range(0, ANCHO, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - delta, ALTO // 2 + delta), (ANCHO // 2 + 10 + delta, ALTO // 2 + delta))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 10 - delta, ALTO // 2 - 10 - delta), (ANCHO // 2 + 10 + delta, ALTO // 2 - 10 - delta))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 10 - delta, ALTO // 2 - 10 - delta), (ANCHO // 2 - 10 - delta, ALTO // 2 + delta + 10))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 10 + delta, ALTO // 2 - 10 - delta), (ANCHO // 2 + 10 + delta, ALTO // 2 + delta))


def dibujarCirculos(ventana):
    for alfa in range(0, 360 , 30):
        x = int(150*math.cos(math.radians(alfa)))
        y = int(150*math.sin(math.radians(alfa)))
        pygame.draw.circle(ventana, NEGRO, (x+ANCHO//2, y+ALTO//2), 150, 1)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(numero):
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

        #Realizar acción seleccionada
        if numero == 1:
            dibujarCuadrosYCirculos(ventana)
        elif numero == 2:
            dibujarParabolas(ventana)
        elif numero == 3:
            dibujarEspiral(ventana)
        elif numero == 4:
            dibujarCirculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def aproximarValorPI(terminos):
    suma = 0
    for d in range (1, terminos + 1, 1):
        suma += 1/d**2
    return (6*suma)**0.5


def contarDivisibles():
    counter = 0
    for numero in range (100,1000):
        if numero%19 == 0:
            counter = counter + 1
    return counter


def imprimirPiramides():
    valor = 0
    for numero in range (1, 10):
        valor = valor * 10 + numero
        resultado = valor * 8 +numero
        print (valor, "* 8 +", numero, "=",resultado )
    print()

    valor = 0
    for numero in range (1, 10):
        multiplicacion = valor * 10 + 1
        resultado = multiplicacion * multiplicacion
        print(multiplicacion, "*", multiplicacion, "=", resultado)
        valor = valor * 10 + 1
        
        
def leerOpcionMenu():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    numero = int(input("¿Qué desea hacer? "))
    return numero


def main():
    numero = leerOpcionMenu()
    while numero != 0:
        if numero > 0 and numero < 5:
            dibujar(numero)
        elif numero == 5:
            terminos = (int(input("Términos que deseas usar: ")))
            aproximacionPI = aproximarValorPI(terminos)
            print("PI = %f" % (aproximacionPI))
        elif numero == 6:
            divisibles = contarDivisibles()
            print("Hay %d números de 3 dígitos divisibles entre 19" % divisibles)
        elif numero == 7:
            imprimirPiramides()
        else:
            print()
            print("Error")
            print("Elija otra opción")
        print()
        numero = leerOpcionMenu()
    print("Fin del programa c:")


# Llamas a la función principal
main()
