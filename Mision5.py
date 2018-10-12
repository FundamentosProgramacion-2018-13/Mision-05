#Luis Mario Cervantes Ortiz
#Descripción: Uso de dibujos y menu
import pygame   # Librería de pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)
NEGRO= (0,0,0)

def dibujar1(): #Cuadros y Circulos
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
        dibujarCuadrado(ventana)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujar2():#Parabola

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina= False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)
        dibujarCuadricula(ventana)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()


def dibujar3():#Espiral

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarSnake(ventana)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def dibujar4():#Circulos

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarCir(ventana)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()


def dibujarCuadricula(ventana): #Dibujar la parábola
    for x in range (0,409,10):
        loco = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(ventana,loco,(x,ANCHO//2),(ANCHO//2,ALTO//2-x))
        pygame.draw.line(ventana, loco, (800 - x, ANCHO // 2), (ANCHO // 2, ALTO // 2 - x))
        pygame.draw.line(ventana, loco, (x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x))
        pygame.draw.line(ventana, loco, (800 - x, ANCHO // 2), (ANCHO // 2, ALTO // 2 + x))




def dibujarCuadrado(ventana): #Dibujar los cuadros y circulos
    for delta in range (1,ALTO//2,10):
        pygame.draw.rect(ventana, NEGRO ,(ANCHO//2-delta, ALTO//2-delta, delta*2, delta*2),1)
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), delta , 1)


def dibujarSnake(ventana): #Dibujar la espiral
    pygame.draw.line(ventana, NEGRO, (410, 390), (410, 400))
    pygame.draw.line(ventana, NEGRO, (410, 400), (410, 400))
    for line in range (0,400,10):
        pygame.draw.line(ventana,NEGRO,(400-line,400-line),(400-line,400+line)) #izquierda
        pygame.draw.line(ventana, NEGRO, (400 + line, 400 + line), (400 - line, 400 + line)) #abajo
        pygame.draw.line(ventana, NEGRO, (400 + line, 390 - line), (400 + line, 400 + line)) #derecha
        pygame.draw.line(ventana, NEGRO, (400 - line, 400 - line), (390 + line, 400 - line)) #arriba



def dibujarCir(ventana): #dibujar los circulos
    x=400
    y=400
    for radio in range (150,360 ,360):


        pygame.draw.circle(ventana, NEGRO, (x+150, y),radio , 1) #0
        pygame.draw.circle(ventana, NEGRO, (x +129, y-75), radio, 1)  # 30

        pygame.draw.circle(ventana, NEGRO, (x + 75, y - 129), radio, 1)#60
        pygame.draw.circle(ventana, NEGRO, (x + 0, y - 150), radio, 1)#90
        pygame.draw.circle(ventana, NEGRO, (x -75, y -129), radio, 1)#120
        pygame.draw.circle(ventana, NEGRO, (x -129, y - 75), radio, 1)#150
        pygame.draw.circle(ventana, NEGRO, (x -150, y -0 ), radio, 1)#180
        pygame.draw.circle(ventana, NEGRO, (x -129, y + 75), radio, 1)#210
        pygame.draw.circle(ventana, NEGRO, (x -75, y + 129), radio, 1)#240
        pygame.draw.circle(ventana, NEGRO, (x + 0, y +150), radio, 1)#270
        pygame.draw.circle(ventana, NEGRO, (x + 75, y + 129), radio, 1)#300
        pygame.draw.circle(ventana, NEGRO, (x + 129, y + 75), radio, 1)#330
        pygame.draw.circle(ventana, NEGRO, (x + 150, y + 0), radio, 1)#360

def numeroDivisible(): #numeros divisibles entre 19 de 3 digitos
        for x in range(100, 1000):
            if x % 19 == 0:
                print(x)


def piramideNum(): #Pirámide de numeros
    suma = 0
    for x in range(1, 10):
        suma = suma * 10 + x
        print(suma, "* 8 +", x , " =", suma * 8 + x)

    suma = 0
    for x in range(1, 10):
        suma = suma *10+ 1
        print(suma, "*", suma ,"=", suma * suma )




def aproximarValorPI(terminos): #Saber el valor de Pi dependiendo cuantos numeros pidan
    suma=0        #Acumulador
    for den in range(1, terminos+1):
        suma+=1/den**4
    return (90*suma)**.25

def leerOpcionMenu():
    print("Menú principal")
    print("1. Dibujar Cuadros y Círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar Espiral")
    print("4. Dibujar Circulo")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    opcion = int(input("¿Que desea hacer?"))
    return opcion


def main():
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujar1()
        elif opcion == 2:
            dibujar2()
        elif opcion == 3:
            dibujar3()
        elif opcion == 4:
            dibujar4()
        elif opcion == 5:
            terminos = int(input("Teclea cuantos terminos quieres: "))
            aproximar = aproximarValorPI(terminos)
            print("PI= ", aproximar)
        elif opcion == 6:
            numeroDivisible()
        elif opcion == 7:
            piramideNum()
        opcion = leerOpcionMenu()
    print("Termina programa")


main()