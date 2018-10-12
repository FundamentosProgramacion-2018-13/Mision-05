#Rodolfo Anibal Altamirano Sánchez, A01377949
#Un programa que reliza diversas instrucciones dependiendo lo que el usuario quiera


import pygame
import random
import math


ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
VERDE = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)



def dibujarCuadradosCirculos():
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo


        ventana.fill(BLANCO)

        for circulos in range(1, ANCHO // 2, 10):
            pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), 1 + circulos, 1)
            pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - circulos, ALTO // 2 - circulos, circulos * 2, circulos * 2),
                             1)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()





def dibujarParabolas():
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

            for x in range(0, ANCHO // 2+1, 10):
                colorRandom = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                pygame.draw.line(ventana, colorRandom, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 - x), 1)
                pygame.draw.line(ventana, colorRandom, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x), 1)
                pygame.draw.line(ventana, colorRandom, (ANCHO - x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x), 1)
                pygame.draw.line(ventana, colorRandom, (ANCHO - x, ANCHO // 2), (ANCHO // 2, ALTO // 2 - x), 1)

            pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
            reloj.tick(40)  # 40 fps
        pygame.quit()  # termina pygame

    # Función principal, aquí resuelves el problema


def dibujarEspiral():
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
        pygame.draw.line(ventana, NEGRO, (ANCHO // 2, ALTO // 2 + 10), (ANCHO // 2 + 10, ALTO // 2 + 10), 1)

        for x in range(10, ANCHO // 2, 10):
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 - x), (ANCHO // 2 + x, ALTO // 2 - x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 + x, ALTO // 2 - x), (ANCHO // 2 + x, ALTO // 2 + x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 + 10 + x), (ANCHO // 2 - x, ALTO // 2 - x), 1)
            pygame.draw.line(ventana, NEGRO, (ANCHO // 2 - x, ALTO // 2 + 10 + x),
                             (ANCHO // 2 + 10 + x, ALTO // 2 + 10 + x), 1)

        pygame.display.flip()
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

    # Función principal, aquí resuelves el problema

def dibujarCirculos():
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    ventana.fill(BLANCO)
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    for x in range(1, 13, 1):
        pygame.draw.circle(ventana, NEGRO, (
        ANCHO // 2 + int(150 * math.cos(math.radians(30 * x))), ALTO // 2 + int(150 * math.sin(math.radians(30 * x)))),
                           150, 1)

    corX = (math.cos(math.radians(30)) * 150)
    corY = (math.sin(math.radians(30)) * 150)

    if (corY + 1) % corY > 1:
        corY = +corY((corY + 1) % corY)

    pygame.display.flip()
    reloj.tick(40)  # 40 fps


# Después del ciclo principal
pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema

def calcularPi(numeroDeValores):
    suma=0
    for n in range (1,numeroDeValores+1):
        suma += (1/n**4)#suma = suma+1/n**4
    aproxPi = (suma*90)**0.25
    return aproxPi


def contarDivisiblesEntre19():
    contador = 0
    for n in range(100, 1000, 1):
        if n % 19 == True:
            contador = contador + 1

    return contador


def ImprimirPiramidesDeNumeros():

        contador = 0
        for x in range(0, 10):
            contador = contador * 10 + 1
            print(contador,"*",contador,"=",contador**2)

        acumulador = 0
        for x in range(1, 10):
            acumulador = (acumulador * 10 + x)

            print(acumulador, "* 8", "+", x, "=", acumulador * 8 + x)



def leerMain():
    print("1. Dibujar cuadrados y circulos")
    print("2. Dibujar parabolas")
    print("3. Dibujar espiral")
    print("4. Dibujar circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir piramides de numeros")
    print("0. Salir")
    selector1 = int(input("¿Que desea hacer? "))
    return selector1
def main():

    selector=leerMain()
    while selector != 0:

        if selector == 1:
            dibujarCuadradosCirculos()


        elif selector == 2:
            dibujarParabolas()

        elif selector == 3:
            dibujarEspiral()

        elif selector == 4:
            dibujarCirculos()

        elif selector == 5:
            numeroDeValores = int(input("Numero de terminos: "))
            valorPi = calcularPi(numeroDeValores)
            print("Pi =", valorPi)

        elif selector == 6:
            divisores = contarDivisiblesEntre19()
            print("Hay", divisores, "números de 3 dígitos divisibles entre 19")

        elif selector == 7:
            ImprimirPiramidesDeNumeros()
        elif selector == 0:
            print("Saliste")
        elif selector>7 and selector >7:
            print("Te equivocaste. Vueleve a intentar")


        selector = leerMain()



main()












