# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que genera figuras, realiza operaciones, e imprime un menu con diferentes opciones a elegir.

import pygame
import random
import math

ANCHO = 800
ALTO = 800
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


# La siguiente función genera colores aleatorios.
def color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# La siguiente función dibuja los cuadros y círculos de la pregunta a.
def dibujarCuadroyCirculoA(ventana):

    for delta in range(1, 401, 10):
      pygame.draw.circle(ventana, NEGRO, (400, 400), delta, 1)
      pygame.draw.rect(ventana, NEGRO, (400 - delta, 400 - delta, delta * 2, delta * 2), 1)


# La siguiente función dibuja parábolas para generar la figura de la pregunta b.
def dibujarParabolaB(ventana):

    for x in range(1,401, 10):

        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 - x), (0 + x, ALTO // 2))
        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 - x), (ANCHO - x, ALTO // 2))
        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 + x), (0 + x, ALTO // 2))
        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 + x), (ANCHO - x, ALTO // 2))


# La siguiente función se encarga de dibujar la espiral de la pregunta c.
def dibujarEspiralC(ventana):

    for pixeles in range(1, 401, 10):
        pygame.draw.line(ventana, NEGRO, (ANCHO//2-pixeles, ALTO//2+pixeles), ((ANCHO//2+5)+pixeles, ALTO//2+pixeles))
        pygame.draw.line(ventana, NEGRO, ((ANCHO//2-10)-pixeles, (ALTO // 2-10)-pixeles), ((ANCHO // 2 - 10)-pixeles, (ALTO // 2+10)+pixeles))
        pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 + 5) + pixeles, (ALTO // 2) + pixeles), ((ANCHO // 2 + 5) + pixeles, (ALTO // 2 - 10) - pixeles))
        pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 - 10)-pixeles, (ALTO // 2 - 10)-pixeles), (((ANCHO // 2 + 10)+pixeles)-5, (ALTO // 2 - 10)-pixeles))


# La siguiente función calcula las coordenadas de los círculos de la pregunta d y luego los dibuja.
def dibujarCirculoD(ventana):

    for grado in range(0, 361, 30):
        radianes = (math.pi * grado) / 180
        x = int(math.sin(radianes) * 150)
        y = int(math.cos(radianes) * 150)
        pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)


# La siguiente función calcula un valor aproximado de PI con los valores introducidos en el menu.
def calcularAproximacionPI(numero):

    suma=0
    for denominador in range (1,numero+1):
        suma += 1 / denominador**2
    return(6*suma)**0.5


# La siguiente función calcula e imprime los números que son divisbles entre 19.
def calcularDivisibles():

    for numero in range(100, 1000):
        if numero % 19 == 0:
            print(numero)


# La siguiente función calcula las operaciones para la pirámide.
def calcularOperacion():

    valor = 0
    for numero in range(1, 10):
        valor = valor * 10 + numero
        resultado = valor * 8 + numero
        print(valor, "* 8 ", "+", numero, "=", resultado)

    numero2 = 1
    for x in range(1, 10):
        resultado = numero2 * numero2
        print(numero2, "x", numero2, "=", resultado)
        numero2 = numero2 * 10 + 1


# La siguiente función inicializa pygame y prepara los dibujos.
def dibujar(opciones):

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
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        if opciones == 1:
            dibujarCuadroyCirculoA(ventana)
        if opciones == 2:
            dibujarParabolaB(ventana)
        if opciones == 3:
            dibujarEspiralC(ventana)
        if opciones == 4:
            dibujarCirculoD(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    pygame.quit()

    # Después del ciclo principal


# La siguiente función imprime el menu.
def elegirOpcionesMenu():

  opciones = int(input("""
  Misión 5. Seleccione qué quiere hacer.
  1. Dibujar cuadros y circulos
  2. Dibujar Parábolas
  3. Dibujar Espiral
  4. Dibujar Círculos 
  5. Aproximar PI
  6. Contar divisibles entre 19
  7. Imprimir pirámides de números
  0. Salir
  ¿Qué desea hacer? :
  """))
  return opciones


# La función principal se encarga de manejar las opciones del menu.
def main():

    opciones = elegirOpcionesMenu()
    while opciones != 0:
        if opciones == 1:
            dibujar(opciones)
        elif opciones == 2:
            dibujar(opciones)
        elif opciones == 3:
            dibujar(opciones)
        elif opciones == 4:
            dibujar(opciones)
        elif opciones == 5:
            numero = int(input("Teclea el valor del ultimo divisor: "))
            print("PI =", calcularAproximacionPI(numero))
        elif opciones == 6:
            calcularDivisibles()
        elif opciones == 7:
            calcularOperacion()
        else:
            print("No existe esa opción")

        opciones = elegirOpcionesMenu()
    print("Termina programa")


# Llamada a la función main.
main()
