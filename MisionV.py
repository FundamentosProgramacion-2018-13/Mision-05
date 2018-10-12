#Autor: Marco González Elizalde
#Programa donde el usuario pueda elegir entre 7 diferentes acciones a realizar


import pygame# Librería de pygame
import math #Libreria de matemáticas
import random # LIbreria para generacion de valores aleatorios

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO = (0, 0, 0)
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
AMARILLO = (255,240,60)
VIOLETA  = (238, 130, 238)
CYAN = (0, 255, 255)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCuadrosyCirculos():
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

        #Figuras a trazar
        for lado in range (0, ANCHO, 20):
            pygame.draw.rect(ventana, NEGRO, (ANCHO//2 -lado//2,ALTO/2 -lado//2,lado,lado),1)
        for radio in range (10, ALTO//2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def colorAleatorio(valor):
    if (valor == 1):
        return NEGRO
    if (valor == 2):
        return VERDE_BANDERA
    if (valor == 3):
        return ROJO
    if (valor == 4):
        return AZUL
    if (valor == 5):
        return AMARILLO
    if (valor == 6):
        return VIOLETA
    if (valor == 7):
        return CYAN


def dibujarParabola():
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

        #Figuras a trazar
        y = ALTO // 2
        for x in range(0, ANCHO // 2, 10):
            valor = random.randint(1, 7)
            pygame.draw.line(ventana, colorAleatorio(valor), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y -= 10
        y = ALTO // 2
        for x in range(ANCHO, ANCHO // 2, -10):
            valor = random.randint(1, 7)
            pygame.draw.line(ventana, colorAleatorio(valor), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y -= 10
        y = ALTO // 2
        for x in range(0, ANCHO // 2, 10):
            valor = random.randint(1, 7)
            pygame.draw.line(ventana, colorAleatorio(valor), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y += 10
        y = ALTO // 2
        for x in range(ANCHO, ANCHO // 2, -10):
            valor = random.randint(1, 7)
            pygame.draw.line(ventana, colorAleatorio(valor), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y += 10

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEspiral():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Figuras a trazar
        x = ANCHO // 2
        y = ALTO // 2
        for incremento in range(5,ANCHO,20):
            pygame.draw.line(ventana,NEGRO,(x+5,y), (x+incremento,y),1)
            pygame.draw.line(ventana, NEGRO, (x - 5, y - incremento - 5), (x - 5, y + 10), 1)
            x = x - 10
            y = y + 10
        x = ANCHO // 2
        y = ALTO // 2
        for incremento in range (10,ANCHO,20):
            pygame.draw.line(ventana,NEGRO,(x+5,y-10),(x+5,y+incremento-10),1)
            pygame.draw.line(ventana, NEGRO, (x-incremento+5, y - 10), (x + 5, y - 10), 1)
            x= x +10
            y = y - 10
            
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarCirculos():
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

        #Figuras a trazar
        for x in range(0, 361, 30):
            pygame.draw.circle(ventana, NEGRO,(ANCHO//2 + int(150*math.cos(math.radians(x))),(ANCHO//2 + int(150 * math.sin(math.radians(x))))), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def aproximarPi(valores):
    suma = 0
    for denominador in range(1, valores +1):
        suma += 1 / denominador**4
    Pi = (90*suma) ** 0.25
    print("Pi es aproximadamente",Pi)
    print("")


def contarDivisibles():
    i = 0
    for x in range(100,1000):
        if x%19 == 0:
            i += 1
        else:
            pass
    print("Hay",i,"números de 3 digitos divisibles entre 19")
    print("")


def imprimirPiramides():
    piramide = 0
    for nivel in range(1,10):
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


def imprimirMenu():
    print("""1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar espiral
4. Dibujar círculos
5. Aproximar PI
6. Contar divisibles entre 19
7. Imprimir pirámides de números
0. Salir""")


def main():
    while(True):
        imprimirMenu()
        opcion = int(input("¿Qué desea hacer? "))
        print("")
        
        if opcion == 1:
            dibujarCuadrosyCirculos()
        elif opcion == 2:
            dibujarParabola()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            valores = int(input("¿Con cuántos valores? "))
            aproximarPi(valores)
        elif opcion == 6:
            contarDivisibles()
        elif opcion == 7:
            imprimirPiramides()
        elif opcion == 0:
            break


#Corre el programa principal
main()
