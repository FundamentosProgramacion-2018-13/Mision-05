# Autor: Mariana Caballero Cabrera
# Funciones con ciclos que el usuario escoge en un menú

import pygame   # Librería de pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (38,38,38)


# Función para hacer los colores random
def colorAleatorio():

    return random.randint(0,255),random.randint(0,255),random.randint(0,255)


#Función que dibuja cuadrados y círculos de más grande a má chico
def dibujarReduccion (ventana):
    pygame.init()
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

        for x in range(10, ANCHO // 2 + 1, 10):
            pygame.draw.rect(ventana, NEGRO, (x, x, ANCHO - 2 * x, ALTO - 2 * x), 1)
            pygame.draw.circle(ventana, NEGRO, (400, 400), (ANCHO // 2 + 1 - x), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

#Función que dibuja 12 círculos con radio de 150
def dibujarCirculos (ventana):
    pygame.init()
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

        for x in range(0, 12, 1):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + int(150 * math.cos(math.radians(-30 * (x)))),ANCHO // 2 + int(150 * math.sin(math.radians(-30 * (x))))), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame



#función para dibujar una espiral
def dibujarEspiral(ventana):
    pygame.init()
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
        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ANCHO // 2 + x), (405 + x, ANCHO // 2 + x), 1)
            pygame.draw.line(ventana, NEGRO, (390 - x, 390 - x), (ANCHO // 2 - x - 10, ANCHO // 2 + x + 10), 1)

        for y in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, NEGRO, (400 - y - 10, 390 - y), (400 + y + 5, 400 - y - 10), 1)
            pygame.draw.line(ventana, NEGRO, (400 + y + 5, 400 + y), (400 + y + 5, 400 - y - 10), 1)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Función para dibujar un rombo de colores
def dibujarRombo(ventana):
    pygame.init()
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

        for x in range (0,ANCHO//2,10):
            pygame.draw.aaline(ventana,colorAleatorio(),(400-x,400),(400,x),1)
            pygame.draw.aaline(ventana,colorAleatorio(),(400+x,400),(400,x),1)
            pygame.draw.aaline(ventana,colorAleatorio(),(400-x,400),(400,800-x),1)
            pygame.draw.aaline(ventana,colorAleatorio(),(400+x,400),(400,800-x),1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

        # Después del ciclo principal
    pygame.quit()  # termina pygame


#Función para im´rimir una piramide de datos en cierto rango
def piramideDatos ():
    x = 0

    for n in range(0, 10, 1):
        print(x * 10 + n + 1, "*", 8, "+", n + 1, "=", ((x * 10) + n + 1) * 8 + n + 1)
        x = x * 10 + n + 1
    print()
    print()

    x = 0

    for n in range(9):
        print(x * 10 + 1, "*", x * 10 + 1, "=", (x * 10 + 1) ** 2)
        x = x * 10 + 1


#función para aproximar PI dependiendo los términos que se le den
def aproximarPI(terminos):
    suma = 0      #acumulador
    for n in range (1,terminos+1):
        suma += (1/n**4)    # suma = suma+ 1/n**2

    ap = (suma*90)**.25

    return ap

#Función para calcular cuántos numeros de tres dígitos divisibles entre 19 hay
def numerosTresDigitos():
    num = 0
    for n in range(100, 1001, 1):

        if n % 19 == 0:
            num += 1

    print("Hay", num, "números de tres dígitos entre 100 y 1000 divisibles entre 19")


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
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
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarCirculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Función para preguntar al usuario la opción del menú
def leerOpcionMenu():
  print("Misión 5. Seleccione que quiere hacer.")
  print("1. Dibujar cuadros y círculos")
  print("2. Dibujar parábolas")
  print("3. Dibujar espiral")
  print("4. Dibujar círculos")
  print("5. Aproximar PI")
  print("6. Contar divisibles entre 19")
  print("7. Imprimir pirámides de números")
  print("0. Salir")
  opcion = int(input("Teclea tu opción: "))
  return opcion





# Función principal
def main():
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujarReduccion(ventana)
        elif opcion == 2:
            dibujarRombo(ventana)
        elif opcion ==3:
            dibujarEspiral(ventana)
        elif opcion ==4:
            dibujarCirculos(ventana)
        elif opcion == 6:
            print()
            print()
            numerosTresDigitos()
            print()
            print()
        elif opcion == 5:
            terminos = int(input("Número de términos: "))
            valorPI = aproximarPI(terminos)
            print("PI= ", valorPI)
            print()
            print()
        elif opcion == 7:
            print()
            print()
            piramideDatos()
            print()
            print()

        opcion = leerOpcionMenu()
    print("Termina programa")



# Llamas a la función principal
main()