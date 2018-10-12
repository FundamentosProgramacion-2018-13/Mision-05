#Autor: Joshua Sánchez Martínez A01274269
#Abre un menu para escoger entre 8 diferentes opciones


import pygame
import random
import math


ANCHO = 800
ALTO = 800


BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


#Función para elegir una opcion del menu
def menu():
    print("Mision 5: Seleccione que quiere hacer")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Qué desea hacer?"))
    return opcion


#Función para colores aleatorios
def colorAleatorio():
     return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


#Funcion para dibujar cuadros y circulos
def figuraUno():
    pygame.init()
    fondo = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        fondo.fill(BLANCO)

        for radio in range(ANCHO // 2, 0, -10):
            pygame.draw.circle(fondo, NEGRO, (400, 400), radio, 1)

        for y in range(ANCHO // 2, 0, -10):
            pygame.draw.rect(fondo, NEGRO, (y, y, (400-y)*2, (400-y)*2), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


#Funcion para dibujar con parabolas
def figuraDos():
    pygame.init()
    fondo = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        fondo.fill(BLANCO)

        for x in range(0, ANCHO // 2 + 5, 10):
            pygame.draw.line(fondo, colorAleatorio(), (x, 400), (400, 400 - x), 1)
            pygame.draw.line(fondo, colorAleatorio(), (400 + x, 400), (400, x), 1)
            pygame.draw.line(fondo, colorAleatorio(), (x, 400), (400, 400 + x), 1)
            pygame.draw.line(fondo, colorAleatorio(), (400 + x, 400), (400, ANCHO - x), 1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


#Funcion para dibujar una espiral
def figuraTres():
    pygame.init()
    fondo = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        fondo.fill(BLANCO)

        for x in range(0, ANCHO // 2 , 10):
            pygame.draw.line(fondo,NEGRO,(ANCHO // 2 - x,ANCHO // 2 + x),(405 + x, ANCHO//2 + x),1)
            pygame.draw.line(fondo, NEGRO, (390 - x, 390 - x), (ANCHO // 2 - x -10, ANCHO // 2 + x + 10), 1)

        for y in range (0, ANCHO // 2 ,10):
            pygame.draw.line(fondo,NEGRO,(400 - y -10, 390 - y),(400 + y + 5, 400 - y - 10),1)
            pygame.draw.line(fondo, NEGRO,(400 + y + 5, 400 + y),(400 + y + 5, 400 - y - 10),1)

        pygame.display.flip()
        reloj.tick(1)

    pygame.quit()


#Funcion que dibuja 12 circulos
def figuraCuatro():
     pygame.init()
     fondo = pygame.display.set_mode((ANCHO, ALTO))
     reloj = pygame.time.Clock()
     termina = False

     while not termina:
         for evento in pygame.event.get():
             if evento.type == pygame.QUIT:
                 termina = True

         fondo.fill(BLANCO)

         for n in range(12):
             x = int(150 * math.cos(math.radians(-30 * (n + 1))))
             y = int(150 * math.sin(math.radians(-30 * (n + 1))))
             pygame.draw.circle(fondo, NEGRO, (ANCHO // 2 + x, ANCHO // 2 + y), 150, 1)

         pygame.display.flip()
         reloj.tick(1)

     pygame.quit()


# Funcion que calcula una aproximacion a Pi
def aproximarPI(terminos):
    suma = 0                      # ACUMULADOR
    for n in range(1,terminos + 1):
        suma += (1 / n**4)          # suma es igual a suma mas 1 entre n al cuadrado

    PI = (suma * 90) ** 0.25
    return PI


#Función que calcula numeros de 3 digitos que son divisibles entre 19.
def dividirNumeros():
    contador = 0
    for divisor in range(100, 1000):
         if divisor % 19 == 0:
             contador = contador + 1

    return contador

#Funcion que calcula e imprime dos piramides que estan haciendo operaciones aritmeticas
def imprimirPiramides():
   contador = 1
   acumuladorA = 1
   acumuladorB = 1

   for p1 in range(1, 10):
       operacion = acumuladorA * 8 + contador
       print("%d * 8 + %d = %d" % (acumuladorA, contador, operacion))
       contador = contador + 1
       acumuladorA = acumuladorA * 10 + contador

   for p2 in range(1, 10):
       resultado = acumuladorB ** 2
       print("%d * %d = %d" % (acumuladorB, acumuladorB, resultado))
       acumuladorB = acumuladorB * 10 + 1


# Función principal.
def main():
     opcion = menu()
     while opcion != 0:
         if opcion == 1:
             figuraUno()
         elif opcion == 2:
             figuraDos()
         elif opcion == 3:
             figuraTres()
         elif opcion == 4:
             figuraCuatro()

         elif opcion == 5:
             terminos = int(input("Número de términos: "))
             valorPI = aproximarPI(terminos)
             print("La aproximación de Pi = ", valorPI)

         elif opcion == 6:
             numeros = dividirNumeros()
             print("Hay %d numeros de 3 digitos que son divisibles entre 19" % (numeros))

         elif opcion == 7:
             imprimirPiramides()

         else:
             print("ERROR, Ingrese otra opción.")
         opcion = menu()

print("Termina programa")

# Llama a la función principal
main()