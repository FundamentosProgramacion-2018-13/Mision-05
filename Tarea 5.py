#Autor Patricio Mondragón A01748352
#Tarea 5 menu de hace diferentes funciones
import random
import math
import pygame  # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
# Esta función imprime 12 circulos entrelazados
def dibujarcirculos():
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
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        for angulo in range (1,12):
            x=int(150*math.cos(math.radians(-30*(angulo+1))))
            y = int(150 * math.sin(math.radians(-30 * (angulo + 1))))
            pygame.draw.circle(ventana, NEGRO, (ANCHO//2+x, ALTO//2+y), 150, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

# esta función imprime una pirámide de números multiplicados por 8 y sumados.
def calcularnumeros2():
    valor2= 1
    for numero2 in range(9):
        numeronuevo2 = valor2*valor2
        print(valor2, "*", valor2, "=", numeronuevo2)
        valor2= valor2*10+1




# Esta función imprime una pirámide de números multiplcados por 10 y después les suma 1
def calcularNumeros():
    valor = 1
    numerosumado = 1

    for numero in range(10):
        numeronuevo = valor *8 + numerosumado
        numerosumado = numerosumado +1
        valor = valor *10 + numerosumado

        print(valor,"*",8 ,"+",numerosumado,"=",numeronuevo)


#Esta función calcula el total números de tres cifre divisibles entre 19 en un numero dado.
def determinardivisores(divisor,cantidad):

    for divisores in range(1,divisor+1,1):


        if divisores%19 ==0 and divisores > 99:
            cantidad = cantidad + 1


    print("Hay",cantidad,"numeros divisibles de tres cifras entre 19 en",divisor)


# Esta función calcula el valor de PI a partir de un número de terminos dado.
def calcularPI():
    terminos = int(input("Ingresa el numero de terminos para calcular PI:"))
    valor= 0
    sumatoria= 0
    for denominador in range (1, terminos + 1):
        valor = 1/ denominador**4
        sumatoria = sumatoria + valor
    sumatoria= (sumatoria*90)**(1/4)


    print(sumatoria)


#Esta función dibuja una figura que hace parabolas con lineas rectas
def dibujarfigura3(ANCHO,ALTO,):
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()
    pygame.init()
    ventana.fill(BLANCO)
    x1= ANCHO//2
    y1= 0
    x2 = ANCHO//2
    y2 = ALTO//2
    x12= ANCHO//2
    y12= 0
    x22=ANCHO//2
    y22= ALTO//2
    x13= ANCHO//2
    y13= 800
    x23= ANCHO//2
    y23= ALTO//2
    x14 = ANCHO // 2
    y14 = 800
    x24 = ANCHO // 2
    y24 = ALTO // 2
    for sector1 in range (0, 40):
        pygame.draw.line(ventana,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)) , (x1,y1), ( x2,y2 ))
        y1= y1 +10
        x2 = x2 -10
    for sector1 in range (0, 40):
        pygame.draw.line(ventana, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (x12,y12), ( x22,y22 ))
        y12= y12+10
        x22= x22 +10
    for sector1 in range (0, 40):
        pygame.draw.line(ventana, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (x13,y13), ( x23,y23 ))
        x23= x23 -10
        y13= y13-10
    for sector1 in range (0, 40):
        pygame.draw.line(ventana, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (x14,y14), ( x24,y24 ))
        x24= x24 +10
        y14= y14-10






    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(40)



    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
    pygame.quit()  # termina pygame


#Esta funcion Dibuja un laberinto
def dibujarLaberinto(ANCHO,ALTO):
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.init()
    ventana.fill(BLANCO)
    x1 = ANCHO//2-10
    y1 = ALTO//2-10
    x2 = ANCHO//2+5
    y2 = ALTO//2-10
    x11 = ANCHO // 2
    y11 = ALTO // 2
    x22 = ANCHO // 2 + 5
    y22 = ALTO // 2
    x112 = ANCHO // 2-10
    y112 = ALTO // 2-10
    x222 = ANCHO // 2 -10
    y222 = ALTO // 2+10
    x1123 = ANCHO // 2 +5
    y1123 = ALTO // 2 - 10
    x2223 = ANCHO // 2+5
    y2223 = ALTO // 2

    for lineasHarriba in range(40):
        pygame.draw.line(ventana, NEGRO, (x1, y1), (x2, y2))
        x1 = x1-10
        y1 = y1-10
        x2 = x2+10
        y2 = y2-10
    for lineasHabajo in range(40):
        pygame.draw.line(ventana, NEGRO, (x11, y11), (x22, y22))
        x11 = x11 - 10
        y11 = y11 + 10
        x22 = x22 + 10
        y22 = y22 + 10
    for lineasVizquierda in range(40):
        pygame.draw.line(ventana, NEGRO, (x112, y112), (x222, y222))
        x112 = x112 - 10
        y112 = y112 - 10
        x222 = x222 - 10
        y222 = y222 + 10
        for lineasVderecha in range(45):
            pygame.draw.line(ventana, NEGRO, (x1123, y1123), (x2223, y2223))
            x1123 = x1123 + 10
            y1123 = y1123 - 10
            x2223 = x2223 + 10
            y2223 = y2223 + 10


    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(40)  # 40 fps

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
    pygame.quit()  # termina pygame



# Esta funcion dibuja circulos y rectangulos paulatinamente
def dibujarfigura1( ANCHO, ALTO):

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    pygame.init()
    ventana.fill(BLANCO)
    DIAMETRO = 10
    LADO1 = 791
    LADO2 = 791
    xCor = 5
    yCor = 5

    for circulo in range(39):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), DIAMETRO, 1)
        DIAMETRO = DIAMETRO + 10

    for rectangulo in range(40):
        pygame.draw.rect(ventana, NEGRO, (xCor, yCor, LADO1, LADO2), 1)
        LADO1 = LADO1 - 20
        LADO2 = LADO2 - 20
        xCor = xCor + 10
        yCor = yCor + 10
    pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(40)



    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)
    pygame.quit()  # termina pygame


def imprimirmenuprincipal():
    print("0:Salir")
    print("1:Imprime figura uno")
    print("2:Imprime laberinto")
    print("3:Imprime figura 3")
    print("4:Imprime círculos")
    print("5: Calcula el valor de PI en base a terminos")
    print("6: Calcula números de tres digitos divisibles entre 19 en un número  ")
    print("7: Imprime pirámides de números")
    opcion = int(input("Teclea tu opcion del 1 al 7:"))
    return opcion




def main():


    opcion= imprimirmenuprincipal()
    while opcion != 0:
        if opcion ==1 :
            dibujarfigura1(ANCHO,ALTO)
        elif opcion == 2:
            dibujarLaberinto(ANCHO,ALTO)
        elif opcion == 3:
            dibujarfigura3(ANCHO, ALTO)
        elif opcion == 4:
            dibujarcirculos()
        elif opcion == 5:
            calcularPI()
        elif opcion == 6:
            divisor = int(input("Ingresa una numero mayor a 100:"))
            cantidad = 0
            determinardivisores(divisor,cantidad)
        elif opcion== 7:
            calcularNumeros()
            calcularnumeros2()
        else:
            print("La opcion tiene que ser del 1 al 7")
        opcion = imprimirmenuprincipal()
    print("Termina programa")









main()