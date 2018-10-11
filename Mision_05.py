# encoding: UTF-8
# Autor: Rubén Villalpando Bremont
# Programa que utiliza el ciclo for para varias cosas

import pygame   # Librería de pygame.
import random   # Librería para lo aleatorio.
import math     # Librería de matemáticas.

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
ROSA = (255, 51, 211)
MORADO = (206, 51, 255)
AZUL_CIELO = (17, 246, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)


# Dibuja muchos cuadrados y círculos negros con 10 pixeles de separación
def dibujarCirculosYCuadrados(ventana):
    for grosor in range(10, 401, 10):
        pygame.draw.circle(ventana, NEGRO, (400, 400), grosor, 1)
        pygame.draw.rect(ventana, NEGRO, [grosor, grosor, 800 - (grosor * 2), 800 - (grosor * 2)], 1)


# Función que dibuja líneas hasta formar cuatro parábolas de colores diferentes.
def dibujarParabolas(ventana):
    for x in range(0, 401, 10):
        numeroAleatorio = random.randint(1, 8)
        if numeroAleatorio == 1:
            color = VERDE_BANDERA
        elif numeroAleatorio == 2:
            color = ROJO
        elif numeroAleatorio == 3:
            color = AZUL
        elif numeroAleatorio == 4:
            color = ROSA
        elif numeroAleatorio == 5:
            color = AMARILLO
        elif numeroAleatorio == 6:
            color = AZUL_CIELO
        elif numeroAleatorio == 7:
            color = NEGRO
        elif numeroAleatorio == 8:
            color = MORADO
        pygame.draw.line(ventana, color, (400, x), (400 + x, 400), 1)
        pygame.draw.line(ventana, color, (x, 400), (400, 400 - x), 1)
        pygame.draw.line(ventana, color, (x, 400), (400, 400 + x), 1)
        pygame.draw.line(ventana, color, (400, 800 - x), (400 + x, 400), 1)


# Función que dibuja una espiral cuadrada.
def dibujarEspiral(ventana):
    for x in range(0, 401, 10):
        pygame.draw.line(ventana, NEGRO, (400 - x, 400 + x), (405 + x, 400 + x), 1)
        pygame.draw.line(ventana, NEGRO, (405 + x, 400 + x), (405 + x, 390 - x), 1)
        pygame.draw.line(ventana, NEGRO, (405 + x, 390 - x), (390 - x, 390 - x), 1)
        pygame.draw.line(ventana, NEGRO, (390 - x, 410 + x), (390 - x, 390 - x), 1)


# Dibuja una serie de círculos en
def dibujarCirculos(ventana):
    for anguloDelCentroDelCirculo in range(0, 361, 30):
        coordenadaX = 400 + round(150 * (math.cos(math.radians(anguloDelCentroDelCirculo))))
        coordenadaY = 400 - round(150 * (math.sin(math.radians(anguloDelCentroDelCirculo))))
        pygame.draw.circle(ventana, NEGRO, (coordenadaX, coordenadaY), 150, 1)



# aproxima el valor de pi mediante una sumatoria
def aproximarPi(numeroEnElQuePara):
    sumaTotal = 0
    for n in range(1, numeroEnElQuePara + 1):
        sumaTotal += 1 / (n ** 4)
    return (sumaTotal * 90) ** (1/4)


# Imprime 2 pirámides de números
def imprimirPiramides():
    numeroMultiplicado = 1
    for numeroSumado in range(1, 10):
        resultadoUno = numeroMultiplicado * 8 + numeroSumado
        print(numeroMultiplicado, " * 8 + ", numeroSumado, " = ", resultadoUno)
        numeroMultiplicado = numeroMultiplicado * 10 + numeroSumado + 1

    numeroMultiplicado = 1
    for n in range(1, 10):
        resultadoDos = numeroMultiplicado ** 2
        print(numeroMultiplicado, " * ", numeroMultiplicado, " = ", resultadoDos)
        numeroMultiplicado = 1 * 10 ** n + numeroMultiplicado


# Calcula los números de 1 a 1000 que son divisibles entre 19
def calcularNumerosDivisibles19():
    contador = 0
    for n in range(100, 1000):
        if n % 19 == 0:
            contador += 1
        else:
            pass
    return contador


# Ventana principal en la que se dibuja lo de pygame
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
        if opcion == 1:
            dibujarCirculosYCuadrados(ventana)
        elif opcion == 2:
            dibujarParabolas(ventana)
        elif opcion == 3:
            dibujarEspiral(ventana)
        else:
            dibujarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 10 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, menú donde el usuario decide qué hacer.
def main():
    termina = False
    while termina == False:
        print(
        '''
        Misión 5. Determine qué quiere hacer.
        1. Dibujar cuadros y círculos.
        2. Dibujar parábolas.
        3. Dibujar espiral.
        4. Dibujar cículos.
        5. Aproximar PI.
        6. Contar divisibles entre 19.
        7. Imprimir pirámides de números.
        0. Salir
        ''')
        opcionElegida = int(input("¿Qué deseas hacer? "))
        if 1 <= opcionElegida <= 4:
            dibujar(opcionElegida)
        elif opcionElegida == 5:
            numeroFinalDeSumatoria = int(input("Ingresa el número en el que para la sumatoria: "))
            print("La aproximación de PI es: ", aproximarPi(numeroFinalDeSumatoria))
        elif opcionElegida == 6:
            print("El número de números de 3 dígitos divisibles entre 19 son: ", calcularNumerosDivisibles19())
        elif opcionElegida == 7:
            imprimirPiramides()
        elif opcionElegida == 0:
            termina = True
        else:
            print("¡¡¡¡Error!!!! Sólo puedes ingresar los números de las opciones.")


# Llamas a la función principal
main()