#Autor: Arturo Márquez Olivar. A01376086.
#Crea distintas figuras utilizando pygame, ademas de que usa los cilos for para hacer aproximaciones de PI.

import pygame   # Librería de pygame
import math #Librería de matemáticas.

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0 , 0)


#Dibuja cuadrados con separación de 10 pixeles, y a su vez también va dibujando círculos.
def dibujarCuadradosYCirculos(ventana):
    #Si solo quieres llegar al limite en Y, se le suma uno al radio.
    for radio in range(10, ALTO//2, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)

    for delta in range(10, ALTO//2, 10):
        pygame.draw.rect(ventana, NEGRO, (ANCHO//2-delta, ALTO//2-delta, delta*2, delta*2), 1)


#Dibuja una parábola usando pygame.
def dibujarParabola(ventana):
    for punto1 in range(ALTO, ALTO//2, -50):
        for punto2 in range(ALTO // 2, ANCHO, 50):
           pygame.draw.line(ventana, ROJO, (ANCHO // 2, punto1), (punto2, ALTO // 2))


#Dibuja una figura como un cuadrado, pero se sin que se corte la figura cada vez que crece el cuadrado.
def dibujarCuadro(ventana):
    for raya in range(10, ALTO//2, 10):
        pygame.draw.line(ventana, NEGRO, (raya, ANCHO//2),(ALTO//2, raya))


#Dibuja una figura con varios círculos.
def dibujarCirculos(ventana):
    catetoAdyacente = 170
    hipotenusa =  catetoAdyacente / math.cos(30)
    catetoOpuesto = int(math.sqrt((hipotenusa**2) - (catetoAdyacente**2)))
    circulo = pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), catetoAdyacente, 1)

    for circulo in range(570, 400, catetoOpuesto):
        pygame.draw.circle(ventana, NEGRO, (circulo, circulo), catetoAdyacente, 1)


#Recibe un rango de números que al evaluarlos, obtiene una aproximación de PI.
def calcularAproximacion(valor):
    suma = 0
    for denominador in range(1, valor+1):
        suma = 1/denominador**4

    return (90*suma)**(1/4)


#Calcula cuántos números son divisibles entre 19 del 1 al 1000 para asegurar que son números de 3 dígitos.
def calculaMultiplos():
    multiplos = 0
    for posiblesValores in range(15, 1000, 1):
        if posiblesValores % 19 == 0:
               multiplos += 1 #Eso es igual a "multiplo = multiplo + 1".

    print ("Hay %d números de 3 dígitos que son multiplos de 19" % multiplos)


#Calcula operaciones normales porque no se pueden usar cadenas o listas y tiene que ser manual.
def calcularPiramides():
    print("""1 * 8 + 1 = 9
          12 * 8 + 2 = 98
          123 * 8 + 3 = 987
          1234 * 8 + 4 = 9876
          12345 * 8 + 5 = 98765
          123456 * 8 + 6 = 987654
          1234567 * 8 + 7 = 9876543
          12345678 * 8 + 8 = 98765432
          123456789 * 8 + 9 = 987654321
    """)

    print("""1 * 1 = 1
    11 * 11 = 121
    111 * 111 = 12321
    1111 * 1111 = 1234321
    11111 * 11111 = 123454321
    111111 * 111111 = 12345654321
    1111111 * 1111111 = 1234567654321
    11111111 * 11111111 = 123456787654321
    111111111 * 111111111 = 12345678987654321
    """)



#Muestra el menú de las posibles tareas a realizar y recibe el valor de la tarea a realizar.
def seleccionarAccion():
    seleccion = int( input("""Misión 5. Seleccione qué quiere hacer.
        1. Dibujar cuadros y círculos.
        2. Dibujar parábolas.
        3. Dibujar espiral.
        4. Dibujar círculos.
        5. Aproximar PI.
        6. Contar divisibles entre 19.
        7. Imprimir pirámides de números.
        0. Salir.
        ¿Que desea hacer? """))
    return seleccion


#Se encarga de poder realizar los dibujos de las distintas funciones posibles.
def dibujar(seleccion):
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

        if seleccion == 1:
            dibujarCuadradosYCirculos(ventana)
        elif seleccion == 2:
            dibujarParabola(ventana)
        elif seleccion == 3:
            dibujarCuadro(ventana)
        elif seleccion == 4:
            dibujarCirculos(ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps.

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, realiza la tarea que el usuario solicitó y sigue desplegando el menú hasta que el usuario decida cerrar el programa.
def main():
    seleccion = seleccionarAccion()

    while seleccion != 0:
        if seleccion == 1:
            dibujar(seleccion)

        elif seleccion == 2:
            dibujar(seleccion)

        elif seleccion == 3:
            dibujar(seleccion)

        elif seleccion == 4:
            dibujar(seleccion)

        elif seleccion == 5:
            valor = int(input("¿Cuál es el valor que deseas aproximar?"))
            valoraproximado = calcularAproximacion(valor)
            print("El valor aproximado de PI con ese valor es de: ", valoraproximado)

        elif seleccion == 6:
            calculaMultiplos()

        elif seleccion == 7:
            calcularPiramides()
        seleccion = seleccionarAccion()
    exit()



# Llamas a la función principal
main()