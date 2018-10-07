# encoding: UTF-8
# Autor: Emiliano Heredia
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame
import random   # Libreria de random
import math     # Libreria de Matematicacs

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)
mitadX = ANCHO//2
mitadY = ALTO//2


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(opc):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    ventana.fill(BLANCO)
    if(opc==1):
        circulos(ventana)
    elif(opc==2):
        cuatro(ventana)
    elif(opc==3):
        snake(ventana)
    elif(opc==4):
        mandala(ventana)
    pygame.display.flip()
    
    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

          # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    main()


#Por cada for 
def circulos(ventana):
    pygame.draw.rect(ventana, NEGRO, (mitadX-1, mitadY-1, 2, 2), 1)
    for x in range(1,80):
        pygame.draw.rect(ventana, NEGRO, (mitadX-(x*5), mitadY-(x*5), (x*10), (x*10)), 1)
        pygame.draw.circle(ventana, NEGRO, (mitadX, mitadY), x*5, 1)

def cuatro(ventana):
    for x in range(40):
        temp = (random.randint(0,254), random.randint(0,254), random.randint(0,254))
        pygame.draw.line(ventana, temp, (mitadX, (x*10)), (mitadX + (x * 10), mitadY),1)
        pygame.draw.line(ventana, temp, (mitadX +(x*10), mitadY), (mitadX, ALTO - (x*10)),1)
        pygame.draw.line(ventana, temp, (mitadX -(x*10), mitadY), (mitadX, ALTO - (x*10)),1)
        pygame.draw.line(ventana, temp, (mitadX, (x*10)), (mitadX-(x*10), mitadY),1)

def snake(ventana):
    last =[mitadX, mitadY]
    sig = [mitadX+(10), mitadY]
    for x in range(1,81,2):
        pygame.draw.line(ventana, NEGRO, last, sig, 1)
        last = sig.copy()
        sig[1] -= (x*10)
        pygame.draw.line(ventana, NEGRO, last, sig, 1)
        x +=1 
        last = sig.copy()
        sig[0] -= (x*10)
        pygame.draw.line(ventana, NEGRO, last, sig, 1)
        last = sig.copy()
        sig[1] += (x*10)
        pygame.draw.line(ventana, NEGRO, last, sig, 1)
        x +=1
        last = sig.copy()
        sig[0] += (x*10)

def mandala(ventana):
    for x in range(12):
        posX = int(150*math.cos(x*0.523599))
        posY = int(150*math.sin(x*0.523599))
        pygame.draw.circle(ventana, NEGRO, (mitadX+posX,mitadY+posY), 150,1)


def zeta(ite):
    res = 0
    for x in range(1,ite+1):
        res += (1/(x**4))
    return (res*90)**(1./4)

def div():
    num = []
    for x in range(100,999):
        if(x%19==0):
            num.append(x)
    return num

def cascada():
    
    print("")
    third=9
    fir= 1
    res =0
    for x in range(9):
        fir = addUp(x)
        print (" %i * %i = %i"%(fir,fir,fir**2))
    print("")
    for x in range(9):
        res = addUp2(x,res)
        fir = addUp(x)
        print(" %i * 8 + %i = %i"%(res,x+1,(fir*10)-res))
        
    print("")

def addUp(x):
    res=0
    for i in range(x+1):
        res += 10**i
    return res

def addUp2(x,first):
    res=0
    for i in range(x+1):
        res += 10**i
    return res+first


        

# Función principal, aquí resuelves el problema
def main():
    pygame.quit() 
    print("________________________________")
    print("|Dibujos                       |") 
    print("--------------------------------")
    print("1) Cuadrados y circulos         ")
    print("2) Parábolas                    ")
    print("3) Espiral                      ")
    print("4) Círculos                     ")
    print("________________________________")
    print("5) Aproximar Pi         ")
    print("________________________________")
    print("6) Contar divisibles entre 19  ")
    print("________________________________")
    print("7) Imprimir piramides de números")
    print("________________________________")
    print("0) Salir")
    print("________________________________")
    opc = int(input("¿Que desea hacer? "))
    if(opc>0 and opc <5):
        dibujar(opc)
        
    elif(opc==5):
        ite = int(input("Cuantas iteraciones: "))
        print(zeta(ite))
        input("Presione enter para continuar")
        main()
    elif(opc==6):
        print(*div(), sep = ", ")
        input("Presione enter para continuar")
        main()
    elif(opc==7):
        cascada()
        input("Presione enter para continuar")
        main()


# Llamas a la función principal
main()
