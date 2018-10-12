#Sebastian Macias ibarra - A01376492
# Por medio de ciclos, realizar varios programas que se mostrarán al momento que el usuario los seleccione

import pygame  # Librería de pygame
import random  # Librería para realizar números al azar

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)

'''Estructura básica de un programa que usa pygame para dibujar'''

#Dibuja una imagen de circulos y cuadrados
def dibujarCiclo_Circulos_Cuadrados(ventana):
    for radio in range(2, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - radio, ALTO // 2 - radio, radio * 2, radio * 2), 1)


#Dibuja una estrella de 4 puntas con solo líneas. Colores aleatorios
def dibujarParabola(ventana):
    separacion = 10

    # Lineas horizontales
    for x in range(0, 410, separacion):
        colorLineas = (random.randint(0, 255), random.randint(0, 255),
                       random.randint(0, 255))  # Se encarga de pones las lineas de colores
        """Se dibuja la figura"""
        pygame.draw.line(ventana, colorLineas, (x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))
        pygame.draw.line(ventana, colorLineas, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 - x))
        pygame.draw.line(ventana, colorLineas, (x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))
        pygame.draw.line(ventana, colorLineas, (ANCHO - x, ALTO // 2), (ANCHO // 2, ALTO // 2 + x))


#Realiza un dibujo parecido a un espiral cuadrado
def dibujarCiclo_de_lineas(ventana):
    pygame.draw.line(ventana, NEGRO, (410, ALTO // 2 - 10), (410, ALTO // 2))
    pygame.draw.line(ventana, NEGRO, (410, ALTO // 2), (405, ALTO // 2))

    for largo in range(10, 400, 10):

        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - largo, ALTO // 2 - largo),
                         (ANCHO // 2 + largo, ALTO // 2 - largo))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - largo, ALTO // 2 - largo),
                         (ANCHO // 2 - largo, ALTO // 2 + largo))
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - largo, 400 + largo), (410 + largo, ALTO // 2 + largo))
        pygame.draw.line(ventana, NEGRO, (410 + largo, 390 - largo), (410 + largo, ALTO // 2 + largo))


#Dibuja un total de 12 círculos, cuyos centros están cada 30 grados
def dibujarCirculos(ventana):
    for radio in range(0, 152, 150):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, 250 + 2 * radio), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 - radio, 250 + radio), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + radio, 250 + radio), 150, 1)

    for radio1 in range(0, 77, 76):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 - radio1, 250 + (radio1 // 4)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + radio1, 250 + (radio1 // 4)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 - radio1, 550 - (radio1 // 4)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + radio1, 550 - (radio1 // 4)), 150, 1)

    for radio2 in range(0, 141, 140):
        pygame.draw.circle(ventana, NEGRO, (250 + (radio2 // 8), 400 - (radio2 // 2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (550 - (radio2 // 8), 400 - (radio2 // 2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (250 + (radio2 // 8), 400 + (radio2 // 2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (550 - (radio2 // 8), 400 + (radio2 // 2)), 150, 1)


#Función que se encarga de escoger los dibujos por medio de una condicional.
def dibujar(opcion):
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
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        """El programa, dependiendo de la eleccion, invocará el dibujo requerido"""

        if opcion == 1:
            dibujarCiclo_Circulos_Cuadrados(ventana)
        elif opcion == 2:
            dibujarParabola(ventana)
        elif opcion == 3:
            dibujarCiclo_de_lineas(ventana)
        elif opcion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # Termina pygame


#Se calcula PI dependiendo del límite impuesto por el usuario con la ayuda de un ciclo y un acumulador
def aproximarValorPI(limite):
    acumulador = 0  # Acumulador
    for x in range(1, limite + 1):
        acumulador += 1 / x ** 4

    return (90 * acumulador) ** 0.25


def contarDivisiblesEntre_19():
    contador = 0 #Acumulador
    for x in range(100, 1000):
        if x % 19 == 0:
            contador += 1

    return contador


        #Se calculan pirámides de operaciones matemáticas. Se ocupa un acumulador y se repite con un ciclo definido
def calcularPiramidesNumeros():
    suma = 0    #Acumulador
    for x in range(1, 10):  #Ciclo
        suma = (suma * 10) + x
        print(suma, "* 8 +", x, "=", suma * 8 + x)

    print("")

    suma = 0   #Acumulador
    for x in range(1, 10):   #Ciclo
        suma = suma * 10 + 1
        print(suma, "*", suma, "=", suma * suma)


#Menú de opciones para que el usuario
def leerMenu():
    print("Misión 05. Seleccione qué quiere hacer.")
    print("1. Dibujar Cuadros y Círculos")
    print("2. Dibujar Parábolas")
    print("3. Dibujar Espiral")
    print("4. Dibujar Círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    eleccionUsuario = int(input("Teclea tu opción: "))  #Espacio donde se recibe la respuesta del usuario
    return eleccionUsuario      #Regresa la respuesta a main()


def main():
    eleccionUsuario = leerMenu() #Se le otorga una variable a la elección del usuario

    '''Este es el ciclo que ayudará  a preguntar repetidas veces al usuario hasta que termine el programa'''
    #También se encarga de ejecutar las funciones que se le pide
    while eleccionUsuario != 0:
        if eleccionUsuario == 1:
            dibujar(eleccionUsuario)
            print("")

        elif eleccionUsuario == 2:
            dibujar(eleccionUsuario)
            print("")

        elif eleccionUsuario == 3:
            dibujar(eleccionUsuario)
            print("")

        elif eleccionUsuario == 4:
            dibujar(eleccionUsuario)
            print("")

        elif eleccionUsuario == 5:
            limite = int(input("Teclea el número de términos que quieres: "))   #Se le pregunta al usuario un límite
            aproximacionPI = aproximarValorPI(limite)
            print("PI =", aproximacionPI)
            print("")

        elif eleccionUsuario == 6:
            print("")
            print( "La cantidad de números de 3 dígitos que son divisibles entre 19 es:")
            print("   ", contarDivisiblesEntre_19())
            print("")

        elif eleccionUsuario == 7:
            print("")
            calcularPiramidesNumeros()
            print("")

        elif eleccionUsuario == 0:
            pass

        eleccionUsuario = leerOpcionMenu() #Repite el ciclo
    print("")
    print("Termina programa")
    print("Que tenga un buen día")


# Llamas a la función principal
main()
