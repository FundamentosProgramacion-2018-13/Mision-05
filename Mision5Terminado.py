# encoding: UTF-8
# Autor:Jonathan Sanabria Rocha
# Utilizar PyGame para resolucion de problemas


import pygame   # Librería de pygame
import random   # Libreria random
import math   #Libreria matematicas


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)
CentroX= ANCHO//2     #variables para dividir la pantalla y poder realizar las figuras
CentroY= ALTO//2



def dibujarCuadrosYCicrulos (ventana):
    for circulo in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), circulo, 1)
    for cuadrado in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - cuadrado, ALTO // 2 - cuadrado, cuadrado * 2, cuadrado * 2), 1)



#Dibuja una estrella usando pygame.
def dibujarParabola(ventana):
    for inicio in range(40):
        colores = (random.randint(0,254), random.randint(0,254), random.randint(0,254))
        pygame.draw.line(ventana, colores, (CentroX, (inicio * 10)), (CentroX - (inicio * 10), CentroY), 1)
        pygame.draw.line(ventana, colores, (CentroX, (inicio*10)), (CentroX + (inicio * 10), CentroY),1)
        pygame.draw.line(ventana, colores, (CentroX - (inicio * 10), CentroY), (CentroX, ALTO - (inicio * 10)), 1)
        pygame.draw.line(ventana, colores, (CentroX +(inicio*10), CentroY), (CentroX, ALTO - (inicio *10)),1)


def dibujarEspiral(ventana):
    for espiral in range(0,CentroY,10):
        pygame.draw.line(ventana,NEGRO,(CentroX+5+espiral,CentroY+5+espiral),
              (CentroX+5+espiral,CentroY-5-espiral))
        pygame.draw.line(ventana, NEGRO, (CentroX - 5 - espiral, CentroY - 5 + espiral),
              (CentroX - 5 + espiral, CentroY - 5 + espiral))
        pygame.draw.line(ventana, NEGRO, (CentroX - 5 - espiral, CentroY - 5 + espiral),
              (CentroX - 5 - espiral, CentroY - 5 - espiral))
        pygame.draw.line(ventana, NEGRO, (CentroX - 5 - espiral, CentroY - 5 - espiral),
              (CentroX + 5 + espiral, CentroY - 5 - espiral))



# Funcion que dibuja circulos de radio 150 pero cambiando la direccion del punto de origen
def dibujarCirculos(ventana):
    for circulos in range(12): # Numero de circulos
        ubicacionx = int(150*math.cos(-0.52*(circulos*1))) # Posicion en x va moviendose en el mismo punto con otro angulo
        ubicaciony = int(150*math.sin(-0.52*(circulos*1))) # Posicion en y va moviendose en el mismo punto con otro angulo
# Va dibujando con respecto a las posiciones en x y y con el mismo radio
        pygame.draw.circle(ventana, NEGRO, (CentroX+ubicacionx,CentroY+ubicaciony), 150,1)



# Recibe el valor del ultimo divisor y regresa una aproximacion al valor de Pi
def aproximarPi(numero):
    total = 0
    for valor in range(1, numero):
        total += (-1) ** (valor + 1) * ((1.0 / (valor * 2 + 1)))
    aproximado = 4 * (1 - total)
    return aproximado



# Funcion que obtiene los numeros de 3 digitos divisibles entre 10 con el rango de 100,10000
def calcularDivisibles():
    divisible = 0
    for valor in range(100, 10000):   #Rango en el que se evaluara
        if valor % 19 == 0: # Condicion para evaluar en el rango
            divisible += 1
    return divisible



# Imprime una piramide de numeros en forma de piramides
def calcularOperaciones():
    piramide = 0
    for nivel in range (1,10):
        piramide = piramide * 10 + nivel
        resultado = piramide * 8 + nivel
        print("%d * 8 + %d = %d" % (piramide, nivel, resultado))
    print("")

    piramide = 1
    for nivel in range(1, 10):
        resultado = piramide * piramide
        print(piramide,"*",piramide,"=",resultado)
        piramide = (piramide * 10) + 1
    print("")



# Estructura básica de un programa que usa pygame para dibujar
def dibujar(eleccion):
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
        if eleccion == 1:
            dibujarCuadrosYCicrulos(ventana)
        elif eleccion == 2:
            dibujarParabola(ventana)
        elif eleccion == 3:
            dibujarEspiral(ventana)
        elif eleccion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():

 eleccion=-1
 while eleccion !=8 :

    eleccion = int(input("""Eliga lo que quiere hacer:
        1. Dibujar Cuadros y Circulos
        2. Dibujar Parabolas
        3. Dibujar Espiral
        4. Dibujar Circulos
        5. Aprximar Pi
        6. Contar divisibles entre 19
        7. Imprimir piramides de numeros
        8. Salir

        ¿Que desea hacer?: """))

    if eleccion == 1:
     dibujar(eleccion)
    elif eleccion == 2:
     dibujar(eleccion)
    elif eleccion == 3:
     dibujar(eleccion)
    elif eleccion == 4:
     dibujar(eleccion)
    elif eleccion == 5:
     valor = int(input("Ingrese divisor: "))
     print ("Valor aproximado es: ", (aproximarPi(valor)))
    elif eleccion == 6:
     print ("Los numeros de 3 digitos divisibles entre 19 son: ", calcularDivisibles())
    elif eleccion == 7:
     calcularOperaciones()
    elif eleccion == 8:
     print("Exit")
    else:
     print("Error")


# Llamas a la función principal
main()