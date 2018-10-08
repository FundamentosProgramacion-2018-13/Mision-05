#Autor: Marco González Elizalde
#Programa donde el usuario pueda elegir entre 7 diferentes acciones a realizar


import pygame# Librería de pygame


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

            for lado in range (0, ANCHO, 20):
                pygame.draw.rect(ventana, NEGRO, (ANCHO//2 -lado//2,ALTO/2 -lado//2,lado,lado),1)
            for radio in range (10, ALTO//2, 10):
                pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

            pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
            reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def colorAleatorio(valor):
    if valor %50 == 0:
        return NEGRO
    if valor %15 == 0:
        return AMARILLO
    if valor %7 == 0:
        return ROJO
    if valor %2 == 0:
        if valor %10 ==0:
            return AZUL
        else:
            return VERDE_BANDERA


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

        y = ALTO // 2
        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, colorAleatorio(x), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y -= 10
        y = ALTO // 2
        for x in range(ANCHO, ANCHO // 2, -10):
            pygame.draw.line(ventana, colorAleatorio(x), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y -= 10
        y = ALTO // 2
        for x in range(0, ANCHO // 2, 10):
            pygame.draw.line(ventana, colorAleatorio(y), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y += 10
        y = ALTO // 2
        for x in range(ANCHO, ANCHO // 2, -10):
            pygame.draw.line(ventana, colorAleatorio(y), (x, ALTO // 2), (ANCHO // 2, y), 1)
            y += 10


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarEspiral():
    pass #Me doy por vencido


def dibujarCirculos():
    pass #Me doy por vencido


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


def main():
    while(True):
        print("""1. Dibujar cuadros y círculos
2. Dibujar parábolas
3. Dibujar espiral
4. Dibujar círculos
5. Aproximar PI
6. Contar divisibles entre 19
7. Imprimir pirámides de números
0. Salir""")
        opcion = int(input("¿Qué desea hacer? "))
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
