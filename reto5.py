#Autor: Jose Luis Mata Lomelí
#Matricula: A01377205
#Objetivo: Crear un menu para usuario que realice diferentes acciones y regreseal menu una vez hecho

#Librerias
import pygame
import random


#Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

#Dimensiones del area de trabajo
Ancho = 800         #en x
Largo = 800         #en y


def dibujarCuadroCirculos(ventana):
    for DELTA in range(1, Largo // 2, 10):
        pygame.draw.rect(ventana, AZUL, (Ancho // 2 - DELTA, Largo // 2 - DELTA, DELTA * 2, DELTA * 2), 1)
        pygame.draw.circle(ventana, AZUL, (Ancho // 2, Largo // 2), DELTA, 1)


def dibujarRombo(ventana):
    for x in range(0, Ancho // 2, 10):
        al_azar = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        pygame.draw.line(ventana, al_azar, (x, Ancho // 2), (Ancho // 2, Largo // 2 - x))  # Lado Izquierdo Superioi
        pygame.draw.line(ventana, al_azar, (x, Ancho // 2), (Ancho // 2, Largo // 2 + x))  # Lado Izquierdo Inferior
        pygame.draw.line(ventana, al_azar, (Ancho - x, Ancho // 2),(Ancho // 2, Largo // 2 - x))  # Lado Derecho Superior
        pygame.draw.line(ventana, al_azar, (Ancho - x, Ancho // 2),(Ancho // 2, Largo // 2 + x))  # Lado Derecho Inferior


def dibujarSerpiente(ventana):
    #Inicio desde el centro a la derecha, avanzo...
    pygame.draw.line(ventana, ROJO, (410, Largo // 2), (405, Largo // 2))
    #luego doy la vuelta a la izquierda y sigo
    pygame.draw.line(ventana, ROJO, (410, Largo // 2 - 10), (410, Largo // 2))

    for y in range(10, 400, 10):
        # Lineas de Arriba
        pygame.draw.line(ventana, AZUL, (Ancho // 2 - y, Largo // 2 - y), (Ancho // 2 + y, Largo // 2 - y))
        # Lineas de Izquierda
        pygame.draw.line(ventana, AZUL, (Ancho // 2 - y, Largo // 2 - y), (Ancho // 2 - y, Largo // 2 + y))
        # Lineas de Abajo
        pygame.draw.line(ventana, AZUL, (Ancho // 2 - y, 400 + y), (410 + y, Largo // 2 + y))
        # Lineas de Derecha
        pygame.draw.line(ventana, AZUL, (410 + y, 390 - y), (410 + y, Largo // 2 + y))


def dibujaRosa(ventana):
    # 1
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 + 130, Largo // 2 + 75), 150, 1)

    # 2
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 + 75, Largo // 2 + 130), 150, 1)

    # 3
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2, Largo // 2 + 150), 150, 1)

    # 4
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 - 75, Largo // 2 + 130), 150, 1)

    # 5
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 - 130, Largo // 2 + 75), 150, 1)

    # 6
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 - 150, Largo // 2), 150, 1)

    # 7
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 - 130, Largo // 2 - 75), 150, 1)

    # 8
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 - 75, Largo // 2 - 130), 150, 1)

    # 9
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2, Largo // 2 - 150), 150, 1)  # Posible Problema

    # 10
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 + 75, Largo // 2 - 130), 150, 1)

    # 11
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 + 130, Largo // 2 - 75), 150, 1)

    # 12
    pygame.draw.circle(ventana, NEGRO, (Ancho // 2 + 150, Largo // 2), 150, 1)



def dibujar(opcion):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((Ancho, Largo))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        if opcion == 1:
            dibujarCuadroCirculos(ventana)

        if opcion == 2:
            dibujarRombo(ventana)

        if opcion == 3:
            dibujarSerpiente(ventana)

        if opcion == 4:
            dibujaRosa(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps



def aproximarPi(terminos):
    suma = 0  # Acumulador

    for denominador in range(1, terminos + 1):
        suma += 1 / denominador ** 2

    return (6 * suma) ** 0.5




def leerOpcionMenu():

    print("Menú principal")
    print("1. Dibujar Cuadrados y Circulos")
    print("2. Dibujar Parabolas")
    print("3. Dibujar Espirales")
    print("4. Dibujar Circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir piramides de numeros")
    print("0. Salir")
    opcion = int(input("Teclea tu opción: "))

    return opcion


def operacion():


    producto1 = 0

    for x in range(1, 10):

        #Este multiplica a si mismo por 10 mas la x y hace que vaya 1, 12, 123, 1234...
        producto1 = producto1 * 10 + x

        #Este aplica la multiplicacion de producto 1*8 y lo suma con x para conseguir los mismos datos que producto1en visceversa
        producto2 = producto1 * 8 + x

        #Imprimimos los datos de la operacion
        print(producto1, "* 8 + ", (x), " = ", producto2)



def multiplos19():

    for multiplos in range(100, 1000):
        multiplos = 0  # Contador
        valor = 1
        while valor <= multiplos:
            if valor % 19 == 0:
                multiplos += 1  # cuenta
            valor += 1

        print("Existen %d multiplos entre 100 y 1000" % (valor))



def main():

    opcion = leerOpcionMenu()

    while opcion != 0:

        if opcion == 1:
            dibujar(opcion)

        elif opcion == 2:
            dibujar(opcion)

        elif opcion == 3:
            dibujar(opcion)

        elif opcion == 4:
            dibujar(opcion)

        elif opcion == 5:
            terminos = int(input("Teclea la cantidad de terminos deseados: "))
            aproximacionPi = aproximarPi(terminos)
            print("Pi = ", aproximacionPi)

        elif opcion == 6:

            multiplos19()

        elif opcion == 7:
            operacion()

        opcion = leerOpcionMenu()
    print("Termina programa")

main()