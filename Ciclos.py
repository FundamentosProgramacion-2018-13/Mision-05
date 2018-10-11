# encoding: UTF-8
# Autor: David Isaí López Jaimes           A01748363
# Muestra un menu que ofrece distintas opciones como dibujar figuras ó hacer cálculos completos

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)       # Ausencia de color o sea negro


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
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
        dibujarCuadrosyCirculos(ventana)      # Llamo a la función para que realize el dibujo dentro de pygame

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def leerOpcionMenu():
    print("Menú principal")
    print("1. Dibujar cuadros y circulos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar circulos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")
    print("¿Qué desea hacer?")
    opcion = int(input("Teclea tu opción: "))
    return opcion


def dibujarCuadrosyCirculos(ventana):
    for DELTA in range(10, ALTO // 2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO // 2 - DELTA, ALTO // 2 - DELTA, 2 * DELTA, 2 * DELTA), 1)
    for radio in range(10, ALTO // 2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)


def dibujarParabolas():
    pass


def dibujarEspiral():
    pass


def dibujarCirculos():
    pass


def divisibles19():
    divisible = 0                      #Contador
    for total in range(1, 1000):
        if total%19 == 0:
            divisible += 1
    print("Hay %d numeros de 3 digitos divisibles entre 19 sin contar el 0" % (divisible))


def piramidesNumeros():
    inicio = 1
    for cociente in range(inicio, 112,10):
        inicio +=1
        total = cociente * cociente
        print("%d * %d = %d" % (cociente, cociente, total))





def aproximarValorPI(terminos):
    suma = 0    # Acumulador
    for denominador in range(1, terminos + 1):
        suma += 1/denominador**4

    return(90*suma)**0.25



def main():
    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            dibujar()
        elif opcion == 2:
            dibujarParabolas()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion == 5:
            terminos = int(input("Teclea cuántos términos quieres: "))
            aproximacionPI = aproximarValorPI(terminos)
            print("PI =", aproximacionPI)
        elif opcion == 6:
            divisibles19()
        elif opcion == 7:
            piramidesNumeros()
        opcion = leerOpcionMenu()
    print("Termina programa")
    


# Llamas a la función principal
main()