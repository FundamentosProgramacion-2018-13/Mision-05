#Jesus Zabdiel Sánchez Chávez

#Mision 05

import pygame
import math
import random


def dibujarFigura1 ():
    ANCHO = 800
    ALTO = 800
    NEGRO = (0,0,0)
    BLANCO = (250,250,250)
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        x = 10
        y = 10
        for x in range (x,ANCHO+1,10):
            for y in range (y ,ALTO+1,10):
                pygame.draw.rect(ventana, NEGRO, (x, y, ANCHO - 2 * x, ALTO - 2 * y), 1)
                for z in range (10,391,10):
                    pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), z ,1)
                x += 10
                y += 10


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarFigura2 ():
    ANCHO = 800
    ALTO = 800
    NEGRO = (0, 0, 0)
    BLANCO = (250, 250, 250)
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        random1 = random.randint (0,255) , random.randint(0,255), random.randint (0,255)
        random2 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        random4 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)




        puntoInicial = 0
        for x in range(0, (ANCHO // 2 + 1), 10):
            pygame.draw.line(ventana, random1, (ANCHO // 2, (ALTO // 2 - x)), (puntoInicial, ALTO // 2),1)
            puntoInicial += 10
        puntoInicial = 0
        for x in range(0, (ALTO // 2 + 1), 10):
            pygame.draw.line(ventana, random2, (puntoInicial, ALTO // 2), (ANCHO // 2, ALTO // 2 + x),1)
            puntoInicial += 10
        puntof = ANCHO
        for x in range(ANCHO // 2, (ANCHO + 1), 10):
            pygame.draw.line(ventana, random3, (ANCHO // 2, (ALTO - x)), (puntof, ALTO // 2),1)
            puntof -= 10
        puntof = ANCHO
        for x in range(ANCHO // 2, (ANCHO + 1), 10):
            pygame.draw.line(ventana, random4, (puntof, ALTO // 2), (ANCHO // 2, x), 1)
            puntof -= 10

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def dibujarFigura3():
    ANCHO = 800
    ALTO = 800
    NEGRO = (0, 0, 0)
    BLANCO = (250, 250, 250)
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        x = 10
        y = 10
        for x in range(x, ANCHO, 10):
            for y in range(y, ALTO, 10):
                pygame.draw.line(ventana, NEGRO, (x,y) , (ANCHO-x,y),1)
                pygame.draw.line(ventana, NEGRO, (ANCHO-x,y), (ANCHO-x,ALTO - y),1)
                x += 10
                y += 10

        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarFigura4():
    ANCHO = 800
    ALTO = 800
    NEGRO = (0, 0, 0)
    BLANCO = (250,250,250)
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        hipotenusa = 150
        pi = math.pi

        for angulo in range (0,361,30):
            radianes = angulo * pi/180
            catetoOpuesto = math.sin(radianes) * hipotenusa
            catetoAdyacente = math.cos(radianes) * hipotenusa
            pygame.draw.circle(ventana,NEGRO,(int (ANCHO//2 + catetoAdyacente),int(ALTO//2 + catetoOpuesto)),150,1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def calcularEjercicio3():
    contador = 0
    for x in range (1000):
        if x % 19 == 0:
            print (x)
            contador = contador +1
    print ("Existen",contador,"números de 3 dígitos divisibles entre 19")


def calcularEjercicio2(nTerminos):
    suma = 0
    for x in range (1,nTerminos+1):
        valor = 1 / x**4
        suma = suma + valor
        aproximacion = (suma * 90) **.25
    return aproximacion


def calcularEjercicio4():
    suma = 0
    for x in range(1,10):
        suma = suma * 10 +x
        resultado = suma * 8 + x
        print (resultado)

    suma2 = 0
    for y in range (1,10):
        suma2 = suma2 * 10 + 1
        resultado2 = suma2 ** 2
        print (resultado2)


def menuPrincipal():
    print(":::::: Misión 05. Menú Principal ::::::")
    print ("¿Qué desea hacer?:")
    print ("1. Dibujar cuadros y círculos")
    print ("2. Dibujar Parabolas")
    print("3. Dibujar Espiral")
    print("4. Dibujar Círculos")
    print("5. Aproximar PI")
    print("6. Contar Divisibles entre 19 ")
    print ("7. Imprimir pirámide de números")
    print ("0. Salir")
    opcion = int(input("Teclea la opción que desees: "))
    return opcion



def main():
    opcion = menuPrincipal()
    while opcion != 0:
        if opcion == 1:
            dibujarFigura1()
        elif opcion == 2:
            dibujarFigura2()
        elif opcion == 3:
            dibujarFigura3()
        elif opcion == 4:
            dibujarFigura4()
        elif opcion == 5:
            nTerminos = int(input("Número de terminos para aproximar: "))
            calcularEjercicio2(nTerminos)
        elif opcion == 6:
            calcularEjercicio3()
        elif opcion == 7:
            calcularEjercicio4()
        elif opcion > 7 or opcion < 0:
            print("Error, por favor, teclea una opción correcta")
        opcion = menuPrincipal()
    print ("Terminó el programa")


main()