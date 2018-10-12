#Autor: Daniel Córdóva Bermúdez
#Grupo: 02
#Descripción: El programa corre una serie de funciones que dibujan figuras, calculan datos e imprime un meno con los resultados y dibujos.


#Importa libreria de pygame, math y random.
import pygame
import random
import math

# Dimensiones de la pantalla & colores
ANCHO = 800
ALTO = 800
NEGRO = (0, 0, 0)
BLANCO = (255,255,255)


#Función se encarga de dibujar los cuadrados y circulos con un for, el cual aumenta de 10 pixeles hasta llegar a 400.
def dibujarCuadradosyCirculos(ventana):

    for delta in range(1, 401, 10):
      pygame.draw.circle(ventana, NEGRO, (400, 400), delta, 1)
      pygame.draw.rect(ventana, NEGRO, (400 - delta, 400 - delta, delta * 2, delta * 2), 1)


#Función que se encarga de crear colores random.
def color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


#DibujarParabola se encarga de dibujar 4 porabolas en los 4 cuadrantes de la ventana.
def dibujarParabola(ventana):

    for x in range(1,401, 10):

        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 - x), (0 + x, ALTO // 2))
        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 - x), (ANCHO - x, ALTO // 2))
        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 + x), (0 + x, ALTO // 2))
        pygame.draw.line(ventana, color(), (ANCHO // 2, ALTO // 2 + x), (ANCHO - x, ALTO // 2))


#DibujarEspiral se encarga de dibujar lineas de manera gradual para crear una espiral.
def dibujarEspiral(ventana):

    for pixeles in range(1,401,10):
        pygame.draw.line(ventana,NEGRO,(ANCHO//2-pixeles,ALTO//2+pixeles),((ANCHO//2+5)+pixeles,ALTO//2+pixeles))
        pygame.draw.line(ventana, NEGRO, ((ANCHO//2-10)-pixeles, (ALTO // 2-10)-pixeles ),((ANCHO // 2 - 10)-pixeles, (ALTO // 2+10)+pixeles))
        pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 + 5) + pixeles, (ALTO // 2) + pixeles),((ANCHO // 2 + 5) + pixeles, (ALTO // 2 - 10) - pixeles))
        pygame.draw.line(ventana, NEGRO, ((ANCHO // 2 - 10)-pixeles, (ALTO // 2 - 10)-pixeles),(((ANCHO // 2 + 10)+pixeles)-5, (ALTO // 2 - 10)-pixeles))


#Dibujar circulos se encarga de calcular las coordenadas de los 12 circulos con la ayuda de la libreria math. Despues dibuja los circulos.
def dibujarCiculos(ventana):

    for grado in range(0, 361, 30):
        radianes =  (math.pi * grado) / 180
        x = int(math.sin(radianes) * 150)
        y = int(math.cos(radianes) * 150)
        pygame.draw.circle(ventana, NEGRO, (400 + x, 400 + y), 150, 1)


#La función calcularPI aproxima un el valor de PI con los terminos indicados en el menu.
def calcularPI(numero):

    suma=0
    for denominador in range (1,numero+1):
        suma += 1 / denominador**2
    return(6*suma)**0.5


#La función calcularDivisibles calcula e imprime los numeros divisbles por 19 entre un rango de 100 a 1000.
def calcularDivisibles():

    for numero in range(100, 1000):
        if numero % 19 == 0:
            print(numero)


#La función calcularOperaciones imprime las operaciones usando un for.
def calcularOperaciones():

    valor = 0
    for numero in range(1, 10):
        valor = valor * 10 + numero
        resultado = valor * 8 + numero
        print(valor, "* 8 ", "+",numero,"=", resultado)

    numero2 = 1
    for x in range(1, 10):
        resultado = numero2 * numero2
        print(numero2, "x",numero2, resultado)
        numero2 = numero2 * 10 + 1


#La función iniciarPygame se inciliza Pygame y se elige que se va a dibujar.
def iniciarPyGame(opcion):

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
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        if opcion == 1:
            dibujarCuadradosyCirculos(ventana)
        if opcion == 2:
            dibujarParabola(ventana)
        if opcion == 3:
            dibujarEspiral(ventana)
        if opcion == 4:
            dibujarCiculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

    pygame.quit()

    # Después del ciclo principal


#Funcion que imprime las opciones del menu.
def leerOpcionMenu():

  opcion = int(input("""
  Misión 5. Seleccione qué quiere hacer.
  1. Dibujar cuadros y circulos.
  2. Dibujar Parábolas
  3. Dibujar Espiral.
  4. Dibujar Circulos 
  5. Aproximar PI
  6. Contar divisibles entre 19.
  7. Imprimir pirámides de números.
  0. Salir.
  ¿Qué desea hacer? :
  """))
  return opcion


#Función principal main se encarga del menu del programa.
def main():

    opcion = leerOpcionMenu()
    while opcion != 0:
        if opcion == 1:
            iniciarPyGame(opcion)
        elif opcion == 2:
            iniciarPyGame(opcion)
        elif opcion == 3:
            iniciarPyGame(opcion)
        elif opcion == 4:
            iniciarPyGame(opcion)
        elif opcion == 5:
            numero = int(input("Teclea el valor del ultimo divisior: "))
            print("PI =",calcularPI(numero))
        elif opcion == 6:
            calcularDivisibles()
        elif opcion == 7:
            calcularOperaciones()
        else:
            print("No existe la opción")

        opcion = leerOpcionMenu()
    print("Termina programa")


#Se llama a main.
main()