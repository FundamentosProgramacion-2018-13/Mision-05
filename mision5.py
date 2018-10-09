#Samantha Martínez Franco
#Practica de ciclo for
import pygame   # Librería de pygame
import random   #libreria para colores random
import math     #calculos de mate (seno y coseno)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)


#función que dibuja cuadros y circulos en la misma ventana que aumenta de 10 en 10
def dibujarCuadrosyCirculos(ventana):
    for circulo in range (410,11,-10):
        pygame.draw.circle(ventana,NEGRO,(400,400),circulo,1)
    for cuadrado in range (80):
        pygame.draw.rect(ventana,NEGRO,(400-(cuadrado*5),400-(cuadrado*5),cuadrado*10,cuadrado*10),1)


#función que dibuja diferentes lineas formando parabolas (tiene colores aleatorios
def dibujarParabolas(ventana):
    for x in range(0, ANCHO // 2, 10):
        color=random.randint(0,255),random.randint(0,255),random.randint(0,255)      #color aleatorio
        pygame.draw.line(ventana,color,(x,ANCHO//2),(ANCHO//2,ANCHO//2+x))
        pygame.draw.line(ventana, color, (x ,ANCHO // 2), (ANCHO // 2, ANCHO // 2 - x))
        pygame.draw.line(ventana, color, (ANCHO-x, ANCHO // 2),(ANCHO//2, ANCHO // 2+x))
        pygame.draw.line(ventana, color, (ANCHO - x, ANCHO // 2), (ANCHO // 2, ANCHO // 2 - x))


#función que dibuja una espiral con 10 pixeles de separación
def dibujarEspiral(ventana):
    for x in range(0,ANCHO//2,10):
        pygame.draw.line(ventana,NEGRO,(ANCHO//2-x,ANCHO//2+x),(ANCHO//2+5+x,ANCHO//2+x),1)  #punto 1 (x+10, y+0
        pygame.draw.line(ventana, NEGRO, (ANCHO//2-10-x, ANCHO//2-10-x), (ANCHO // 2-x-10, ANCHO // 2 +x+10), 1)
    for y in range (0,ANCHO//2,10):
        pygame.draw.line(ventana,NEGRO,(ANCHO//2-y-10,ANCHO//2-10-y),(ANCHO//2+y+5,ANCHO//2-y-10),1)
        pygame.draw.line(ventana, NEGRO,(ANCHO//2+y+5,ANCHO//2+y),(ANCHO//2+y+5,ANCHO//2-y-10),1)


#función que dibuja circulos
def dibujarCirculos(ventana):
    for n in range (12):
        x=int(150*math.cos(math.radians(-30 * (n + 1))))
        y=int(150 * math.sin(math.radians(-30 * (n + 1))))
        pygame.draw.circle(ventana,NEGRO,(ANCHO//2+x,ANCHO//2+y),150,1)


#función que se utiliza para dibujar usando pygame así como escoger cual usar para dibujar
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

        #depende de la opción que escogen, cual dibuja
        if opcion == 1:
            dibujarCuadrosyCirculos(ventana)
        elif opcion == 2:
            dibujarParabolas(ventana)
        elif opcion == 3:
            dibujarEspiral(ventana)
        elif opcion == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#función que calcula la aproximación de PI de acuerdo a formula
def aproximarPi(terminos):
    suma=0     #suma los terminos (acumulador)
    for pi in range(1,terminos+1):
        suma+=1/pi**4
    ap=(suma*90)**0.25    #ap=aproximacion de pi
    return ap





def dividirEntre19():
    contador = 0
    for divisor in range(100, 1000):
        if divisor % 19 == 0:
            contador = contador + 1

    return contador


def calcularOperaciones():
    numero = 0
    for multiplicador in range(1,10):  # no puedo usar listas (n*10+contador)

        numero = numero * 10 + multiplicador
        resultado = numero * 8 + multiplicador
        print(numero, " * 8 + ", multiplicador, " = ", resultado)

    numero = 0
    for n in range(10):
        numero = numero * 10 + 1
        resultado = numero * numero
        print(numero, "*", numero, "=", resultado)


#función que lee la opcion de menu
def leerOpcionMenu():
    print('''Mision 5. Seleccione qué quiere hacer.
            1. Dibujar cuadros y círculos
            2. Dibujar parábolas
            3. Dibujar espiral
            4. Dibujar círculos
            5. Aproximar PI
            6. Contar divisibles entre 19
            7. Imprimir pírámides de números
            0. Salir''')
    opcion = int(input("Qué desea hacer?"))
    return opcion


#función principal
def main():
    opcion=leerOpcionMenu()
    while opcion !=0:
        if opcion == 1 or opcion==2 or opcion==3 or opcion==4:
            dibujar(opcion)

        elif opcion == 5:
            terminos = int(input("Número de terminos: "))
            valorPI = aproximarPi(terminos)
            print("PI=", valorPI)

        elif opcion==6:
            divisores = dividirEntre19()
            print("Hay", divisores, "números de tres dígitos que son dividibles entre 19 ")

        elif opcion == 7:
            calcularOperaciones()
        opcion=leerOpcionMenu()
    print("Termina Programa")


main()