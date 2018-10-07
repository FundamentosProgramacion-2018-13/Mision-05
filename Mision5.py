# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800




# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0) #Ausencia de color


# Estructura básica de un programa que usa pygame para dibujar
def dibujarFigura1():
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
        for radio in range(1,ANCHO//2+1,10):
            pygame.draw.circle(ventana,NEGRO,(ANCHO//2,ALTO//2),radio,1)
            pygame.draw.rect(ventana,NEGRO,(ANCHO//2-radio,ALTO//2-radio,radio*2,radio*2),1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarFigura2():
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
        for separacion in range(1,ANCHO//2+1,10):
            if separacion % 3:
                color1=VERDE_BANDERA
            elif separacion % 2:
                color1=ROJO

            pygame.draw.line(ventana, color1, (ANCHO // 2, ALTO // 2 - separacion), (0 + separacion, ALTO // 2))
            pygame.draw.line(ventana, color1, (ANCHO // 2, ALTO // 2 - separacion), (ANCHO - separacion, ALTO // 2))
            pygame.draw.line(ventana, color1, (ANCHO//2, ALTO//2+separacion), (0 + separacion, ALTO // 2))
            pygame.draw.line(ventana, color1, (ANCHO//2, ALTO//2+separacion), (ANCHO - separacion, ALTO // 2))


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarFigura3():
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
        for separacion in range(1,ANCHO//2+1,10):

            pygame.draw.line(ventana,NEGRO,(ANCHO//2-separacion,ALTO//2+separacion),((ANCHO//2+5)+separacion,ALTO//2+separacion))
            pygame.draw.line(ventana, NEGRO, ((ANCHO//2-10)-separacion, (ALTO // 2-10)-separacion ),((ANCHO // 2 - 10)-separacion, (ALTO // 2+10)+separacion ))
            pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 - 10)-separacion, (ALTO // 2 - 10)-separacion),(((ANCHO // 2 + 10)+separacion)-5, (ALTO // 2 - 10)-separacion))
            pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 + 5)+separacion,(ALTO // 2 )+separacion),((ANCHO // 2 + 5)+separacion, (ALTO // 2 - 10)-separacion))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarFigura4():
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


        pygame.draw.circle(ventana,NEGRO,((ANCHO//2),(ALTO//2-150)),150,1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2), (ALTO // 2 + 150)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2)-150, (ALTO // 2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2) + 150, (ALTO // 2)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 75), (ALTO // 2 - 130)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 130), (ALTO // 2 - 75)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 75), (ALTO // 2)+130), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 - 130), (ALTO // 2) + 75), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 +130), (ALTO // 2 + 75)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, ((ANCHO // 2 + 75), (ALTO // 2 + 130)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2+130, (ALTO // 2-75)), 150, 1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2 + 75, (ALTO // 2 - 130)), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def calcularDivisibles():

    for numero in range(100,1000):
        if numero % 19 == 0:
            print (numero)


def calcularOperaciones():
    numero1=0
    for numero in range (1,10):
        numero1=numero1*10+(numero)
        ##print (numero1,"*",8,"+",numero,"=",numero1*8+numero)
        print(numero1,"*",8,"+",numero,"=",numero1*8+numero)

    numero1=0
    for numero in range(1,10):
        numero1 = (numero-numero)+(1+numero1)*10
        print(numero1//10,"*",numero1//10,"=",(numero1//10)*(numero1//10))


def aproximaValorPi(terminos):
    suma=0
    for denominador in range (1,terminos+1):
        suma += 1 / denominador**2
    return(6*suma)**0.5


# Función principal, aquí resuelves el problema
def main():
    print("Misión 5. Seleccione qué quiere hacer.")
    print("1. Dibujar Cuadros y Círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar Pi")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámide de números")
    print("0. Salir")

    entrada = int(input(""))

    if entrada == 1:
        dibujarFigura1()
    elif entrada == 2:
        dibujarFigura2()
    elif entrada == 3:
        dibujarFigura3()
    elif entrada == 4:
        dibujarFigura4()
    elif entrada == 5:
        terminos = int(input("# de Términos:"))
        aproximaValorPi(terminos)
        print(aproximaValorPi(terminos))
    elif entrada == 6:
        calcularDivisibles()
    elif entrada == 7:
        calcularOperaciones()
    else:
        exit()


# Llamas a la función principal
main()