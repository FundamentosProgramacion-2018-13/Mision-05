# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 02
# Programa que muestra un menu con diferentes acciones, pregunta al usuario cual desea realizar, las realiza y
# vuelve al menu, hasta que el usuario decida salir

#Llamado a librerias usadas
import pygame
import random
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)         #Negro, total ausencia de color


# Función para dibujar cuadros y círculos
def dibujarCuadrosYCirculos(ventana):
    for origen in range(10, ALTO//2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO//2-origen, ALTO//2-origen, 2*origen, 2*origen), 1)

    for radio in range(10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)


# Función que crea parábolas que cambian de color aleatoriamente
def dibujarParabolaColoresAleatorios(ventana):
    DELTA = 20

    for y in range(0, ALTO, DELTA):
        Factor1 = random.randint(0, 255)
        Factor2 = random.randint(0, 255)
        Factor3 = random.randint(0, 255)
        aleatorio1 = (Factor3, Factor2, Factor1)
        aleatorio2 = (Factor2, Factor3, Factor1)

        pygame.draw.line(ventana, aleatorio1, (ANCHO//2, ALTO-y//2), (ANCHO//2+y//2, ALTO//2))
        pygame.draw.line(ventana, aleatorio2, (ANCHO//2, ALTO-y//2), (ANCHO//2-y//2, ALTO//2))

    for x in range(0, ANCHO, DELTA):
        Factor1 = random.randint(0, 255)
        Factor2 = random.randint(0, 255)
        Factor3 = random.randint(0, 255)
        aleatorio1 = (Factor1, Factor2, Factor3)
        aleatorio2 = (Factor2, Factor3, Factor1)

        pygame.draw.line(ventana, aleatorio1, (ANCHO//2, x//2), (ANCHO//2+x//2, ALTO//2))
        pygame.draw.line(ventana, aleatorio2, (ANCHO//2, x//2), (ANCHO//2-x//2, ALTO//2))


# Función que dibuja un espiral cuadrado, como un laberinto lineal
def dibujarEspiral(ventana):

    inicx = ANCHO//2
    inicy = ALTO//2
    resultado = 0
    for x in range (200):
        resultado = resultado+5
        angulo = -90*x+44.7
        pygame.draw.line(ventana, NEGRO, (inicx, inicy), (int(ANCHO//2+resultado*math.cos(angulo*math.pi/180)), int(ALTO//2+resultado*math.sin(angulo*math.pi/180))), 1)
        inicx = int(ANCHO//2+resultado*math.cos(angulo*math.pi/180))
        inicy = int(ALTO//2+resultado*math.sin(angulo*math.pi/180))


# Función que dibuja 12 círculos que parecen una flor
def dibujarCirculos(ventana):
    for x in range(12):
        angulo = x*30
        pygame.draw.circle(ventana, NEGRO, (int(ANCHO//2 + 150 * math.cos(angulo * math.pi/180)), int(ALTO//2 + 150 * math.sin(angulo * math.pi/180))), 150, 1)


# Función que aproima al valor dde PI, de acuerdo a una fórmula y los elementos dados de la misma
def aproximarAPi():
    aproximación = 0
    elementos = int(input("""Ingrese el número de elementos que desee evaluar 
    (mientras más elementos más se tardará el ordenador en calcular, pero será más exacto el cálculo): """))
    for n in range (1, elementos+1, ):
        aproximación = aproximación + 1/n**4
    print("El valor aproximado a pi es: ", (aproximación*90)**(1/4))


# Función que cuenta los números divisibles entre 19 y sean de 3 dígitos
def calcularMultiplosde19():
    numeros = 0
    for x in range(0,1000):
        if x%19==0 and x>=100:
            numeros+=1

    print("La cantidad de números de 3 dígitos que se pueden dividir entre 19 son: ", numeros)


# Función que crea pirámides de números
def calcularOperaciones():
    y=0
    w=0
    for x in range (1,10):
        y = y * 10 + x
        resultado = y * 8 + x

        listado1 = str(y)
        listado2 = str(x)
        listado3 = str(resultado)

        print(listado1 + " * 8 + " + listado2 + " = " + listado3)

    for z in range(1,10):
        w = w * 10 + 1
        resultado2 = w * w

        listado4 = str(w)
        listado5 = str(resultado2)

        print(listado4 + " * " + listado4 + " = " + listado5)


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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        # Se evalúa la opción dada en el menu para identificar y ejecutar la acción seleccionada
        if opcion == 1:
            dibujarCuadrosYCirculos(ventana)
        elif opcion == 2:
            dibujarParabolaColoresAleatorios(ventana)
        elif opcion == 3:
            dibujarEspiral(ventana)
        elif opcion == 4:
            dibujarCirculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí se presenta le menu y se llama a otras funciones
def main():
    # Opcion es igual a 1 porque el programa se ejecuta por lo menos una vez
    opcion = 1
    while opcion != 0:
        #menu
        print("Misión 5. Seleccione qué quiere hacer")
        print("1. Dibujar cuadros y círculos")
        print("2. Dibujar parábolas")
        print("3. Dibujar espiral")
        print("4. Dibujar círculos")
        print("5. Aproximar a PI")
        print("6. Contar numeros de 3 dígitos divisibles entre 19")
        print("7. Imprimir pirámides de números")
        print("0. Salir")

        opcion = int(input("Ingrese el número de la opción de lo que quiere hacer: ")) #Lectura de la acción a realizar
        print("")
        print("")

        #evaluación de opcion y llamado a funciones
        if opcion>= 1 and opcion<=4:
            dibujar(opcion)
            print("")
            print("")
        elif opcion == 5:
            aproximarAPi()
            print("")
            print("")
        elif opcion == 6:
            calcularMultiplosde19()
            print("")
            print("")
        elif opcion == 7:
            calcularOperaciones()
            print("")
            print("")
        elif opcion == 0:
            print("Termina el programa")
        else:
            print("No se admiten números negativos ni números mayores a 7, seleccione una opción válida")


# Se llama a la función principal para iniciar el programa
main()