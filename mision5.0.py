#Danhel Alejandro Mercado Velasco
#Este es un progarma que utiliza ciclo for
#que te permite elegir diferentes opciones al usuario

import math
import random
import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)


#Esta función permite al usuario ver la figura de una espiral o laberinto
def dibujarEspiral(ventana):
    delta = 10
    for x in range(0, 410, delta):
        pygame.draw.line(ventana, NEGRO, (x, x), (ANCHO + 6 - x, x))
        pygame.draw.line(ventana, NEGRO, (x, x), (x, ALTO + 9 - x))
        pygame.draw.line(ventana, NEGRO, (ANCHO + 6 - x, x), (ANCHO + 6 - x, ALTO - x))
    pygame.draw.line(ventana, NEGRO, (x + 10, ALTO - x), (ANCHO + 6 - x, ALTO - x))

#En esta función permite al usurio ver la figura de cuadrados y circulos ensimados de diferentes tamaños
def dibujarCuadrosCirculos(ventana):
    for circulo in range (410,11,-10):
        pygame.draw.circle(ventana,NEGRO,(400,400),circulo,1)
    for cuadrado in range (80):
        pygame.draw.rect(ventana,NEGRO,(400-(cuadrado*5),400-(cuadrado*5),cuadrado*10,cuadrado*10),1)

#Función que permite al usuario ver la imagen de diferentes lineas de diferentes colores que construyen a una figura
def dibujarParabola(ventana):
    for x in range(0, ANCHO // 2, 10):
        color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        pygame.draw.line(ventana,color,(x,ANCHO//2),(ANCHO//2,ANCHO//2+x))
        pygame.draw.line(ventana, color, (x ,ANCHO // 2), (ANCHO // 2, ANCHO // 2 - x))
        pygame.draw.line(ventana, color, (ANCHO-x, ANCHO // 2),(ANCHO//2, ANCHO // 2+x))
        pygame.draw.line(ventana, color, (ANCHO - x, ANCHO // 2), (ANCHO // 2, ANCHO // 2 - x))



#Esta función permite que el usuario vea la figura de circulos entrecruzados
def dibujarCirculos(ventana):
        for angulo in range(0, 331, 30):
            anguloRadianes = angulo * math.pi / 180
            pygame.draw.circle(ventana, NEGRO, (
            int(math.cos(anguloRadianes) * 150 + ANCHO // 2), int(math.sin(anguloRadianes) * 150 + ALTO // 2)), 150, 1)

#Esta función permite que las figuras se muestren en ventanas particulares
def dibujar(figura):

    pygame.init()

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
        if figura == 1:
            dibujarCuadrosCirculos(ventana)
        elif figura == 2:
            dibujarParabola(ventana)
        elif figura == 3:
            dibujarEspiral(ventana)
        elif figura == 4:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#función que calcula el valor de PI aporximado
def aproximarPi(terminos):
    suma=0
    for pi in range(1,terminos+1):
        suma+=1/pi**4
    aprox=(suma*90)**0.25
    return aprox

#función que calcula numeros de tres digitos que son divisibles entre 19
def calcularDivisibles19():
    contador = 0
    for f in range(1000, 10000):
        if f % 19 == 0:
            print(f, "es un número divisible entre 19")
            contador += 1
    print("hay", contador, "números divicibles entre 19")

#función que permite al usurio ver un piramide de operaciones de numeros
def calcularOperaciones():
    acumulador1 = 1
    acumulador2 = 1
    acumulador3 = 10
    print(acumulador1, "* 8 +", acumulador1, "=", (acumulador1 * 8 + acumulador1))
    for f in range(2, 10):
        acumulador1 += acumulador3
        acumulador2 += acumulador1
        acumulador3 *= 10
        print(acumulador2, "* 8 +", f, "=", (acumulador2 * 8 + f))
    print("\n")
    acumulador1 = 1
    acumulador2 = 10
    print(acumulador1, "*", acumulador1, "=", acumulador1 * acumulador1)
    for g in range(8):
        acumulador1 += acumulador2
        acumulador2 *= 10
        print(acumulador1, "*", acumulador1, "=", acumulador1 * acumulador1)


#Esta es la función que permite seleccionar las opciones
def menuOpciones():
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas ")
    print("3. Dibujar espiral")
    print("4. Dibujar círculo")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir ")
    opcion = int(input(" ¿Qué desea hacer? "))
    print("")
    return opcion

#función pricipal
def main():
    opcion=menuOpciones()
    while opcion !=0:
        if opcion == 1:
            dibujar(opcion)
        elif opcion == 2:
            dibujar(opcion)
        elif opcion == 3:
            dibujar(opcion)
        elif opcion == 4:
            dibujar(opcion)
        elif opcion == 5:
            terminos = int(input("Número de terminos: "))
            valorPI = aproximarPi(terminos)
            print("PI=", valorPI)
        elif opcion==6:
            divisores = calcularDivisibles19()
            print("Hay", divisores, "números de tres dígitos que son dividibles entre 19 ")
        elif opcion == 7:
            calcularOperaciones()
        opcion =menuOpciones()
    print("Termina Programa")


main()#llamada a la función