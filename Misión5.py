#Autor: Diana Marisol Medina Bravo
#Misión 5 ciclos, se hace un menú con varias opciones
#Se tienen 4 figuras en pygame y tres problemas.

import pygame   # Librería de pygame
import numpy as np #libreria numpy
import random      #Libreria random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Color
NEGRO=(5,5,5)
BLANCO = (255, 255, 255)
VERDE = (125, 200, 125)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


BAJAR=10 #Distancia entre las lineas

#Función para dibujar la figura uno de cuadrados y circulos
def dibujarFigura1(ventana):
    for a in range(11, ANCHO//2, 10):
        cuadrado = (a, a, (ANCHO - a*2), (ALTO-a*2) )
        pygame.draw.rect(ventana, NEGRO, cuadrado, 2)


    for g in range (21,ANCHO,20):
        pygame.draw.circle(ventana,NEGRO,((ALTO)//2,(ANCHO)//2),(ANCHO-g)//2,2)


#Función para dibujar la figura dos de parabolas
def dibujarFigura2(ventana):
    for a in range(11, ANCHO//2, 10):
        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [ANCHO // 2, a], [ALTO // 2 - a, ALTO // 2])
        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [ANCHO // 2, a], [ALTO // 2 + a, ALTO // 2])

        pygame.draw.line(ventana, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), [ANCHO // 2, ALTO - a], [ALTO // 2 - a, ALTO // 2])
        pygame.draw.line(ventana,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) , [ANCHO // 2, ALTO - a], [ALTO // 2 + a, ALTO // 2])


#Función para dibujar la figura tres de espiral
def dibujarFigura3(ventana):
    #for a in range(800-10,ALTO,ANCHO):
    for b in range (11, (ANCHO//2 + 1) ,10):
        pygame.draw.line(ventana, NEGRO, (b, ALTO-b), (ANCHO-b,ALTO-b))
        pygame.draw.line(ventana, NEGRO, (b,ALTO-b ),(b,b ))
        pygame.draw.line(ventana, NEGRO, (b,b),(ANCHO-(b+10),b))
        pygame.draw.line(ventana, NEGRO, ((ANCHO - (b + 10)), b),(ANCHO-(b+10),ALTO-(b+10)))


#Función para dibujar la figura cuatro de circulos
def dibujarFigura4(ventana):
   # for c in range ():
   y = ALTO//2
   x = ANCHO//2

   for a in range (1, 13):
       pygame.draw.circle(ventana,NEGRO,pol2cart(150, 30*a, x, y),150,1)


#FUnción que convierte de coordenadas polares a cartesianas
#dx y dy para que quede en el centro
#angulo en grados
#ayuda a dibujar la figura cuatro
def pol2cart(r, angle, dx, dy):
    rad = np.radians(angle)
    x = r * np.cos(rad) + dx
    y = r * np.sin(rad) + dy
    return(int(x), int(y))


# Estructura básica de un programa que usa pygame para dibujar
def dibujar1():
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

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarFigura1(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Estructura básica de un programa que usa pygame para dibujar
def dibujar2():
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

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarFigura2(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Estructura básica de un programa que usa pygame para dibujar
def dibujar3():
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

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarFigura3(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Estructura básica de un programa que usa pygame para dibujar
def dibujar4():
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

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarFigura4(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Función para hacer una aproximación de pi con los terminos que el usuario proporcione
def aproximarPi(terminos):
    suma=0  #acumulador
    for n in range(1,terminos+1):
        suma += (1/n**4) #suma= suma+ 1/n**2

    ap= (suma*6)**0.5
    return ap


#Función para calcular los multiplos de 19 con numeros que tengan 3 cifras
def calcularMultiplos():
    multiplos=0
    for a in range(101,1000):
        for b in range(2,11):
            if a/b ==19:
                multiplos += 1
                #print (a,"es múltiplo de 19") -- si se quieren mostrar los mútiplos de 19
    print("Hay",multiplos,"múltiplos de 19")


#Función para calcular operacions
def calcularOperaciones():
        acumulador = 0
        segundo = 8
        for a in range(1, 10):
            primero = 10
            acumulador = acumulador * primero + a
            resultado = acumulador * 8 + a
            print(acumulador, "*", segundo, "+", a, "=", resultado)

        print ("")
        acumulador=0
        for b in range(1, 10):
            primero = 10
            acumulador = acumulador * primero + 1
            dos=acumulador
            resultado = acumulador*dos
            print(acumulador, "*", dos, "=", resultado)


#Función para leer la opción proporcionada en el menu por el usuario
def leerOpcionMenu():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y circulos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("¿Qué desea hacer?")
    opcion = int(input("Teclea tu opción: "))
    return opcion


# Función principal, aquí resuelves el problema
def main():
    opcion =leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujar1()
        elif opcion == 2:
            dibujar2()
        elif opcion == 3:
            dibujar3()
        elif opcion == 4:
            dibujar4()
        elif opcion == 5:
            terminos = int(input("Número de términos: "))
            valorPi = aproximarPi(terminos)
            print("Pi=", valorPi)
        elif opcion == 6:
            calcularMultiplos()
        elif opcion == 7:
            calcularOperaciones()
        opcion = leerOpcionMenu()
    print("Termina programa")

main()
