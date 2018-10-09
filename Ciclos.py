# Autor: Zabdiel Valentín Garduño Vivanco
# A traves de ciclos, se realizo diversas funciones que al final se muestran en una pantalla seleccionable.

import pygame   # Librería de pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCuadricula(ventana):
    DELTA=10
    #Lineas horizontales
    for y in range(0,410,DELTA):
        LUL=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.line(ventana,LUL, (y,ALTO//2),(ANCHO//2,ALTO//2-y))
        pygame.draw.line(ventana,LUL, (ANCHO-y,ALTO//2),(ANCHO//2,ALTO//2-y))
        pygame.draw.line(ventana,LUL, (y,ALTO//2),(ANCHO//2,ALTO//2+y))
        pygame.draw.line(ventana,LUL, (ANCHO-y,ALTO//2),(ANCHO//2,ALTO//2+y))

def dibujarCirculosCuadros(ventana):
    for radio in range(1,ALTO//2,10):
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2,ALTO//2), radio,1)
        pygame.draw.rect(ventana,NEGRO,(ANCHO//2-radio,ALTO//2-radio,radio*2,radio*2),1)

def dibujarCuadro(ventana):
    pygame.draw.line(ventana,NEGRO,(410 ,ALTO//2-10),(410,ALTO//2))
    pygame.draw.line(ventana,NEGRO,(410,ALTO//2),(405,ALTO//2))
    for y in range(10,400,10):
        pygame.draw.line(ventana,NEGRO,(ANCHO//2-y,ALTO//2-y),(ANCHO//2+y,ALTO//2-y))
        pygame.draw.line(ventana,NEGRO,(ANCHO//2-y,ALTO//2-y),(ANCHO//2-y,ALTO//2+y))
        pygame.draw.line(ventana,NEGRO,(ANCHO//2-y,400+y),(410+y,ALTO//2+y))
        pygame.draw.line(ventana,NEGRO,(410+y,390-y),(410+y,ALTO//2+y))


def dibujarCirculos(ventana):
    for radio in range(0,152,150):
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2,250+2*radio),150,1)
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2-radio,250+radio),150,1)
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2+radio,250+radio),150,1)
    for x in range(0,77,76):
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2-x,250+(x//4)),150,1)
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2+x,250+(x//4)),150,1)
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2-x,550-(x//4)),150,1)
        pygame.draw.circle(ventana,NEGRO, (ANCHO//2+x,550-(x//4)),150,1)
    for y in range(0,141,140):
        pygame.draw.circle(ventana,NEGRO, (250+(y//8),400-(y//2)),150,1)#250,400   270,330
        pygame.draw.circle(ventana,NEGRO, (550-(y//8),400-(y//2)),150,1)
        pygame.draw.circle(ventana,NEGRO, (250+(y//8),400+(y//2)),150,1)
        pygame.draw.circle(ventana,NEGRO, (550-(y//8),400+(y//2)),150,1)

def dibujar01():
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

        dibujarCirculosCuadros(ventana)

        #dibujarCuadricula(ventana)

        #dibujarCuadro(ventana)


        #dibujarCirculos(ventana)
        #Lineasverticales(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame
def dibujar02():
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

        #dibujarCirculosCuadros(ventana)

        dibujarCuadricula(ventana)

        #dibujarCuadro(ventana)


        #dibujarCirculos(ventana)
        #Lineasverticales(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame
def dibujar03():
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

        #dibujarCirculosCuadros(ventana)

        #dibujarCuadricula(ventana)

        dibujarCuadro(ventana)


        #dibujarCirculos(ventana)
        #Lineasverticales(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame
# Función principal, aquí resuelves el problema
def dibujar04():
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

        #dibujarCirculosCuadros(ventana)

        #dibujarCuadricula(ventana)

        #dibujarCuadro(ventana)


        dibujarCirculos(ventana)
        #Lineasverticales(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame
# Función principal, aquí resuelves el problema
def aproximarValorPi(terminos):
    suma= 0 #Acumulador
    for den in range (1,terminos+1):
        suma +=1/den**4

    return (90*suma)**0.25

def diviseble03():
    for x in range(100,1000):
        if x%19==0:
            print(x)
def sumatoria():
    suma=0
    for x in range(1,10):
        suma=suma*10+1
        print(suma,"*",suma,"=",suma*suma)

    suma=0
    for x in range(1,10 ):
        suma=(suma*10)+x
        print(suma,"*","8","+",x,"=",suma*8+x)
def leerOpcionMenu():
    print("Misión 05. Seleccione qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    opcion = int(input("Teclea tu opción: "))
    return opcion

def main():
    opcion= leerOpcionMenu()
    while opcion!=0:
        if opcion==1:
            dibujar01()
        elif opcion==2:
            dibujar02()
        elif opcion==3:
            dibujar03()
        elif opcion==4:
            dibujar04()
        elif opcion==5:
            terminos= int(input("Teclea cuantos terminos quieres: "))
            aproximacionPi=aproximarValorPi(terminos)
            print("PI=",aproximacionPi)
        elif opcion==6:
            diviseble03()
        elif opcion==7:
            sumatoria()
        elif opcion==0:
            print("Adios!")
        opcion=leerOpcionMenu()
    print("Termina programa")
# Llamas a la función principal
main()
