#Autor: Luis Armando Miranda Alcocer
# Menú con 7 programas posibles


import pygame   # Librería de pygame
import random   #Librería para traer números al azar
import math     # Librería para utilizar senos y cosenos

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)


def dibujarCuadrosYCirculos():
    pygame.init()  # Inicializa el motor de pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Borrar pantalla

        for LADO in range(10, ALTO // 2 +1, 10): #Los lados son variables, aumentan de 10 en 10
            pygame.draw.rect(ventana, NEGRO, ((ANCHO // 2) - LADO, (ALTO // 2) - LADO, 2 * LADO, 2 * LADO), 1)
        for radio in range(10, ALTO // 2 +1, 10): #Radio variable, que aumente de 10 en 10
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def dibujarParabola():
    pygame.init()  # Inicializa el motor de pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará (ANCHO POR ALTO)
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Borrar pantalla
        DELTA = 10  # Separación de 10 pixeles
        for x in range(0, 400 + 1, DELTA):
            RANDOM = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Dentro del for para que cada linea tenga color aleatorio
            pygame.draw.line(ventana, RANDOM, (x, 400), (400, 400 + x))  # Punto Inicial (de cero a cuatrocientos en eje x, 400 en y), Punto Final (desde la mitad en eje x, y a la mitad hacia abajo en y)
            pygame.draw.line(ventana, RANDOM, (x, 400), (400, 400 - x))  # Punto inicial (de cero a cuatrocientos en eje x, 400 en y), y Punto Final (desde la mitad [400] en eje x, y a la mitad en eje y hacia arribA
            pygame.draw.line(ventana, RANDOM, (400, x), (400 + x, 400))
            pygame.draw.line(ventana, RANDOM, (400, 400 + x), (800 - x, 400))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def dibujarEspiral():
    pygame.init()  # Inicializa el motor de pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará (ANCHO POR ALTO)
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Borrar pantalla

        for x in range (0, 400+1, 10):
            pygame.draw.line(ventana, NEGRO, (400-x, 400+x),(400+x+10, 400+x), 1)
            pygame.draw.line(ventana, NEGRO, (400-x-10, 400+x-10),(400-x-10,400+x+10),1)

        for y in range (0, 400+1, 10):
            pygame.draw.line(ventana, NEGRO, (400-y,400-y-10), (400+y+10, 400-y-10), 1)
            pygame.draw.line(ventana, NEGRO, (400+y+10, 400+y), (400+y+10, 400-y-10), 1)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame



def dibujarCirculos():
    pygame.init()  # Inicializa el motor de pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará (ANCHO POR ALTO)
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        ventana.fill(BLANCO)  # Borrar pantalla
        pygame.draw.circle(ventana, BLANCO, (400, 400), 150,1)  # Marca para que pasen los demás círculos (ventana, color, puntos centro, radio, grosor)
        for x in range(12):  # Se repetirá 12 veces
            pygame.draw.circle(ventana, NEGRO, (400 + int(150 * math.cos(math.radians(30 * x))), 400 + int(150 * math.sin(math.radians(30 * x)))), 150, 1)
     #(ventana, color, punto central eje x ( mitad en eje x + 150cos30*(cada uno de los puntos para cada circulo)) y punto central eje y(mitad en eje y + 150sen30*(cada uno de los puntos para cada cículo)), radio, grosor)
        reloj.tick(40)  # 40 fps
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

    pygame.quit()  # termina pygame


def aproximarPI(terminos):
    suma = 0  # Acumulador inicia en 0
    for denominador in range(1, terminos + 1):
        suma += 1 / denominador ** 4  # Se suman, acorde al número de términos
    return (90 * suma) ** (1 / 4) #De acuerdo a la función del ejercicio, se multiplica por 90 y se saca raíz cuarta.


def contarDivisibles():
    contador = 0
    for x in range (100, 1000): #Entre 100 y 999
        if x % 19 ==0:  #Si un número entre 100 y 999 es divisible entre 19, el contador aumenta 1.
            contador=contador+1
 #           print (contador, x) Activar para ver los números divisibles entre 19
    print (contador) #Imprimir el número final del contador

def hacerPiramides():
    numeroInicial=0
    for suma in range (1,10): # suma es un valor, del 1 al 9, que se agregará al numero inicial multiplicado por 10
        numeroInicial = (numeroInicial*10)+suma
        print (numeroInicial,"* 8 +",suma,"=",numeroInicial*8+suma)
    print(" ") #Espacio

    acumulador=0
    for x in range(9): #Se va a repetir nueve veces
        acumulador = acumulador*10+1 #al acumulador aumenta por 10, +1: (1 *10+1 = 11, 11 *10+1 = 111...)
        print(acumulador,"*",acumulador,"=",acumulador*acumulador)

def main():
    seleccion = -1
    while seleccion != 0: #Menú, mientras seleccion no sea 0, se repetirá el menú
        print("Misión 5. Seleccione qué quiere hacer. ")
        print("1. Dibujar cuadros y círculos ")
        print("2. Dibujar parábolas ")
        print("3. Dibujar espiral ")
        print("4. Dibujar circulos ")
        print("5. Aproximar PI ")
        print("6. Contar dibisibles entre 19 ")
        print("7. Imprimir pirámides de números ")
        print("0. Salir ")
        seleccion = int(input("Misión 5. Seleccione qué quiere hacer. ")) #Se escoge qué programa abrir, si se teclea 0, termina el programa

        if seleccion ==1: #Si se selecciona un 1, funciona el primer programa.
            dibujarCuadrosYCirculos() #Llama a la función
            print(" ")

        if seleccion ==2: #Si se selecciona un 2, funciona el segundo programa.
            dibujarParabola() #Llama a la función
            print(" ")

        if seleccion==3: #Si se selecciona un 3, funciona el tercer programa.
            dibujarEspiral() #Llama a la función
            print(" ")

        if seleccion==4:#Si se selecciona un 4, funciona el cuarto programa.
            dibujarCirculos() #Llama a la función
            print(" ")

        if seleccion==5: #Si se selecciona un 5, funciona el quinto programa.
            terminos = int(input("Teclea cuántos términos quieres: ")) #Se pregunta el número de términos para la aproximación de PI (mientras mayor sean, más preciso es PI)
            aproximacionPI= aproximarPI(terminos) #Llama a la función
            print("PI = ", aproximacionPI)
            print(" ")

        if seleccion==6: #Si se selecciona un 6, funciona el sexto programa.
            contarDivisibles()
            print(" ")

        if seleccion==7: #Si se selecciona un 7, funciona el séptimo programa.
            hacerPiramides()
            print(" ")

main()