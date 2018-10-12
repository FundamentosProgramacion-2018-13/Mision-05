# encoding: UTF-8
# Autor: David Rodriguez
# Despliega un menú con varias opciones al usuario


import pygame# Librería de pygame
import math #Librería de matemáticas
import random #Librería para aleatorio


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)       #Color negro
MORADO = (153, 0, 153)  #Color morado
DORADO = (204, 204, 0)  #Color dorado
GRIS = (128, 128, 128)  #Color gris
NARANJA = (255, 102, 0) #Color naranja


#Dibuja cuadrados y círculos con una separación de 10 pixeles
def dibujarFigura1(ventana):
    for grosor in range(10, 401, 10):
        pygame.draw.circle(ventana, NEGRO, (400, 400), grosor, 1)
        pygame.draw.rect(ventana, NEGRO, [grosor, grosor, 800 - (grosor * 2), 800 - (grosor * 2)], 1)


#Dibuja lineas de colores hasta formar cuatro parábolas
def dibujarFigura2(ventana):
    for x in range(0, 401, 10):
        numeroAleatorio = random.randint(1, 8)
        if numeroAleatorio == 1:
            color = VERDE_BANDERA
        elif numeroAleatorio == 2:
            color = ROJO
        elif numeroAleatorio == 3:
            color = AZUL
        elif numeroAleatorio == 4:
            color = NEGRO
        elif numeroAleatorio == 5:
            color = MORADO
        elif numeroAleatorio == 6:
            color = DORADO
        elif numeroAleatorio == 7:
            color = GRIS
        elif numeroAleatorio == 8:
            color = NARANJA
        pygame.draw.line(ventana, color, (400, x), (400 + x, 400), 1)
        pygame.draw.line(ventana, color, (x, 400), (400, 400 - x), 1)
        pygame.draw.line(ventana, color, (x, 400), (400, 400 + x), 1)
        pygame.draw.line(ventana, color, (400, 800 - x), (400 + x, 400), 1)


#Dibuja una espiral cuadrada
def dibujarFigura3(ventana):
        for x in range(0, 401, 10):
            pygame.draw.line(ventana, NEGRO, (400 - x, 400 + x), (405 + x, 400 + x), 1)
            pygame.draw.line(ventana, NEGRO, (405 + x, 400 + x), (405 + x, 390 - x), 1)
            pygame.draw.line(ventana, NEGRO, (405 + x, 390 - x), (390 - x, 390 - x), 1)
            pygame.draw.line(ventana, NEGRO, (390 - x, 410 + x), (390 - x, 390 - x), 1)


#Dibuja varios círculos desfazados uno del otro en un eje redondo
def dibujarFigura4(ventana):
    for anguloCentral in range(0, 361, 30):
        X = 400 + round(150 * (math.cos(math.radians(anguloCentral))))
        Y = 400 - round(150 * (math.sin(math.radians(anguloCentral))))
        pygame.draw.circle(ventana, NEGRO, (X, Y), 150, 1)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(elección):
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
        if elección == 1:
            dibujarFigura1(ventana)
        elif elección == 2:
            dibujarFigura2(ventana)
        elif elección == 3:
            dibujarFigura3(ventana)
        elif elección == 4:
            dibujarFigura4(ventana)
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Calcula una aproximado de pi y su exactitud es basada en el número de términos ingresado
def aproximarPI(terminos):
    suma = 0        #ACUMULADOR
    for n in range(1, terminos+1):
        suma += (1/n**2)
    ap = (suma*6)**0.5
    return ap


#Calcula la cantidad de números de tres dígitos divisibles entr 19
def calcularNumerosDivisibles():
    contador = 0
    for n in range(100, 1000):
        if n % 9 == 0:
            contador += 1
    return contador


#Imprime la primera lista de números
def imprimirLista1():
    factor = 1
    for numeroSuma in range (1, 10):
        resultado = factor*8 + numeroSuma
        print(factor, "*8+", numeroSuma, "=", resultado)
        factor = (factor*10) + numeroSuma + 1


#Imprime la segunda lista de dígitos
def imprimirLista2():
    factor = 1
    for x in range(1, 10):
        resultado = factor * factor
        print(factor, "*", factor, "=", resultado)
        factor = (10**x) + factor


#Imprime el menú principal
def imprimirMenu():
    print("Misión 5. Determine qué quiere hacer.")
    print("1. Dibujar cuadros y círculos")
    print("2. Dibujar parábolas")
    print("3. Dibujar espiral")
    print("4. Dibujar círculos")
    print("5. Aproximar PI")
    print("6. Contar divisibles entre 19")
    print("7. Imprimir pirámides de números")
    print("0. Salir")


# Función principal, aquí resuelves el problema
def main():
    salir = 0
    while salir == 0:
        imprimirMenu()
        elección = int(input("¿Qué desea hacer?"))
        if elección == 1 or elección == 2 or elección == 3 or elección == 4:
            dibujar(elección)
        elif elección == 5:
            terminos = int(input("¿Cuantos términos?"))
            print("La aproximación de pi es:", aproximarPI(terminos))
        elif elección == 6:
            print("La cantidad de números de 3 dígitos divisibles entre 9 es de:", calcularNumerosDivisibles())
        elif elección == 7:
            imprimirLista1()
            imprimirLista2()
        elif elección == 0:
            salir = 1
        else:
            print("Por favor ingrese un número válido")


# Llamas a la función principal
main()