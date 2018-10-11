#Diego Armando Ayala Hernández
#Menú que da diferentes opciones para diferentes programas como pygame o sacar valores
import pygame
import random
import math
#limito el tamaño y colores para pygame
ANCHO = 800
ALTO = 800
BLANCO = (245, 245, 245)
NEGRO = (20, 20, 20)
#Dibuja cuadados y circulos con 10 pixeles de separación
def dibujarCuadradosCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for cuadradoyciculo in pygame.event.get():
            if cuadradoyciculo.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for cuadros in range(1, ALTO // 2, 10):
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - cuadros, ALTO // 2 - cuadros, cuadros * 2, cuadros * 2), 1)
        for radio in range(1, ANCHO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Dibuja una parabola que toma colores random para sus lineas y las va cambiando hasta que se cierre la ventana
def dibujarParabolaDeColores():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for parabola in range(0, ALTO // 2 + 1, 10):
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 + parabola, ALTO // 2), (ANCHO // 2, ALTO - parabola), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 + parabola, ALTO // 2), (ANCHO // 2, 0 + parabola), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 - parabola, ALTO // 2), (ANCHO // 2, ALTO - parabola), 1)
            pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (ANCHO // 2 - parabola, ALTO // 2), (ANCHO // 2, 0 + parabola), 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
#Usa un for para ir agregando distancia con cada línea que dibuja
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
        for espiral in range(0, ALTO // 2, 10):
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + 5 + espiral, ALTO // 2 + 5 + espiral),
                                 (ANCHO // 2 + 5 + espiral, ALTO // 2 - 5 - espiral))
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 5 - espiral, ALTO // 2 - 5 + espiral),
                                 (ANCHO // 2 - 5 + espiral, ALTO // 2 - 5 + espiral))
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 5 - espiral, ALTO // 2 - 5 + espiral),
                                 (ANCHO // 2 - 5 - espiral, ALTO // 2 - 5 - espiral))
                pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - 5 -espiral, ALTO // 2 - 5 - espiral),
                                 (ANCHO // 2 + 5 + espiral, ALTO // 2 - 5 - espiral))
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()
#GENERA circulos cambiando el angulo de donde va a empezar
def dibujarDoceCirculos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        for angulodelcirculo in range(0, 360, 30):
            pygame.draw.circle(ventana, NEGRO, (int(ANCHO // 2 + 150 * math.sin(math.radians(angulodelcirculo))), int(ALTO // 2 + 150 * math.cos(math.radians(angulodelcirculo)))), 150, 1)
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()

#Recibe los terminos que se van a usar para ver si se aproxima a PI

def aproximarPi():
    terminos = int(input("¿Cuántos términos quieres sumar? "))
    suma = 0
    for denominador in range(1, terminos):
        suma = 1/denominador**4 + suma
    pi = (suma*90)**.25
    print("pi = ", pi)

#Busca la cantidad de numeros de 3 digitos que son divisibles entre 19
def calcularDivisibles():
    contador = 0
    for numero in range(100, 1000):
        if numero % 19 == 0:
            contador += 1
        else:
            pass
    print("Hay %d números de tres dígitos divisibles entre 19" % contador)
#Crea una piramide de numeros apartir de multipliciones en un rango de terminado
def multiplicarPiramides():
    suma = 0
    for n in range(1, 10):
        suma = (suma*10) + n
        print(suma, "* 8 + %d = " % n, suma * 8 + n)
    contador = 0
    suma = 0
    for x in range(9):
        suma = (suma*10) + 1
        print("%d * %d =" % (suma, suma), suma**2)
        contador += 1
#Presenta y recibe las opciones que se tienen disponibles
def leerOpcion():
    print("""Misión 5. Seleccione qué quiere hacer.
    Opciones:
    ------------------------------ 
    1. Dibujar cuadros y círculos 
    2. Dibujar parábolas 
    3. Dibujar espiral 
    4. Dibujar círculos 
    5. Aproximar PI 
    6. Contar divisibles entre 19 
    7. Imprimir pirámides de números 
    0. Salir
    -------------------------------""")

    opcion = int(input("¿Qué desea hacer? "))
    return opcion
#Recibe la opcion de leerOpcion() y llama a la función que se debe usar
def main():
    opcion = leerOpcion()
    while opcion != 0:
        if opcion == 1:
            dibujarCuadradosCirculos()
        elif opcion == 2:
            dibujarParabolaDeColores()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarDoceCirculos()
        elif opcion == 5:
            aproximarPi()
        elif opcion == 6:
            calcularDivisibles()
        elif opcion == 7:
            multiplicarPiramides()
        opcion = leerOpcion()
    print("¡Hasta Luego!")
main()
