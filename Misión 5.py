# encoding: UTF-8
#Autor: Carlos Alberto Reyes Ortiz
#Usando de base un programa del Ing. Roberto Martínez Román en toda la parte de como dibujar en pygame

#El programa le muestra al usuario un menu en el cual puede elejir que función ejecutar.
#Son 7 funciones, abajo en cada funcións se explica que hace.


from math import cos, sin, radians
import pygame # Librería de pygame
import random


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
NEGRO= (0,0,0)
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad




def dibujarCuadrados_y_Circulos(): # Dibuja cuadrados y circulos con una separación de 10 pixeles

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

        for radio in range(1, 40):
            pygame.draw.circle(ventana, NEGRO, (ANCHO-400,ALTO-400), radio * 10, 1)
        for cuadrados in range(80):
            pygame.draw.rect(ventana, NEGRO, (ANCHO/2-(cuadrados*10), ALTO/2-(cuadrados*10), cuadrados*20, cuadrados*20),1)
   #En pygame.draw.rect "Rect" se lee:
   # El 1ro dice cuanto se mueve a la derecha,
   # El 2do cuanto para abajo
   # El 3ro que tan ancho en x
   # El 4to que tan ancho en y
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame




def dibujarParabolas(): #Dibuja un tipo de rombo con parábolas con colores aleatorios
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


        for n in range (10, 391, 10):
            colorAleatorio = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            pygame.draw.line(ventana, colorAleatorio, (ANCHO/2 -n, ALTO/2), (ANCHO/2, n), 1)
            pygame.draw.line(ventana, colorAleatorio, (ANCHO/2-n , ALTO/2), (ANCHO/2, ALTO-n), 1)
            pygame.draw.line(ventana, colorAleatorio, (ANCHO/2+n, ALTO/2), (ANCHO/2, n), 1)
            pygame.draw.line(ventana, colorAleatorio, (ANCHO/2+n, ALTO/2), (ANCHO/2, ALTO-n), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame





def dibujarEspiral(): #Dibuja un espiral empezando de la esquina inferior derecha
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


        for n in range (10, 391, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO-n, ALTO-n), (n, ALTO-n),1 )
            pygame.draw.line(ventana, NEGRO, (n, ALTO-n), (n, n),1)
            pygame.draw.line(ventana, NEGRO, (n, n), (ANCHO-10-n, n),1)
            pygame.draw.line(ventana, NEGRO, (ANCHO-10-n, n), (ANCHO-10-n, ALTO-10-n),1)
            pygame.draw.line(ventana, NEGRO, (ANCHO/2-5, ALTO/2), (ANCHO/2, ALTO/2), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame





def dibujarCirculos(): #Dibuja 12 círculos desde el perímetro de un círculo con el mismo radio
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

        for angulo in range(0, 361, 30):
            posX = int(150 * (cos(radians(angulo))))+ (ANCHO-400)
            posY = int(150 * (sin(radians(angulo))))+ (ALTO-400)
            pygame.draw.circle(ventana, NEGRO, (posX, posY), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame




def aproximarPI (terminos): #Aproxima a (PI^4)/90 entre más términos más certera cera la aproximación.

    operacion = 0
    for n in range (1, terminos+1):
        operacion = operacion + 1/n**4
    return operacion




def calcularDivisibleDe19(): #Te dice cuantos números con tres dígitos son divisibles entre 19

    cantidad_de_Numeros = 0
    for divisibles in range(100, 1000):
        if divisibles % 19 == 0:
            cantidad_de_Numeros = cantidad_de_Numeros + 1

    print(cantidad_de_Numeros, "son los números con tres dígitos que son divisibles entre 19")




def calcularPiramides_de_Numeros(): #Da dos pirámides de números artméticas.

    sumando = 0
    print("Primera tabla: ")
    print()
    for n in range(9):
        sumando = sumando * 10 + n + 1
        print(sumando, "*", 8, "+", n + 1, "=", (sumando * 8 + (n + 1)))
    print()
    print()
    print("Segunda Tabla: ")
    print()
    multiplicador = 0
    for n in range(1, 10):
        multiplicador = multiplicador * 10 + 1
        print(multiplicador, "*", multiplicador, "=", multiplicador * multiplicador)




def leerOpciones_del_Menu(): #Es el menu que se muestra al usuario con las opciones que tiene para eligir.

    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadrados y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    eleccion = int(input("¿Qué desea hacer? "))
    return eleccion




def main(): #Función principal:

    eleccion = leerOpciones_del_Menu()

    while eleccion != 0:

        if eleccion == 1:
            dibujarCuadrados_y_Circulos()

        elif eleccion == 2:
            dibujarParabolas()

        elif eleccion == 3:
            dibujarEspiral()

        elif eleccion == 4:
            dibujarCirculos()

        elif eleccion == 5:
            print()
            terminos = int(input("Dame el número de términos: "))
            operacion= aproximarPI(terminos)
            print(operacion)
            print()

        elif eleccion == 6:
            print()
            calcularDivisibleDe19()
            print()
        elif eleccion == 7:
            print()
            calcularPiramides_de_Numeros()
            print()

        elif eleccion < 0 or eleccion >7:
            print(""" "ERROR" Favor de introducir una cantidad válida""""")
            print()

        eleccion = leerOpciones_del_Menu()

    print()
    print("Programa finalizado.")






# Llamas a la función principal
main()


