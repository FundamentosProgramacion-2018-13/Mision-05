# Autor: Luis Humberto Burgueño Paz
# El programa muestra un menú para que el usuario decida que es lo que quiere hacer entre 7 opciones distintas (y salir)

import pygame
import random
import math
# Dimensiones de la Pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)       # sin ningún color


# Dibuja varios cuadros y círculos negros con el mismo centro que van aumentando de tamaño
def dibujarCuadrosCirculos(ventana):
    for radio in range(10, ALTO // 2 + 1, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO // 2, ALTO // 2), radio, 1)
    x = ANCHO // 2 - 5
    y = ALTO // 2 - 5
    a = 10
    b = 10
    for rectangulo in range(10, ALTO // 2 + 1, 10):
        pygame.draw.rect(ventana, NEGRO, (x, y, a, b), 1)
        x = x - 10
        y = y - 10
        a = a + 20
        b = b + 20


# Dibuja 4 Parábolas que forman una especie de estrella, cada línea tiene un color aleatorio
def dibujarParabolas(ventana):
   delta = ANCHO
   beta = ALTO
   alfa = 0
   gama = 0
   variableRandom=random.choice(range(256))


   pygame.draw.line(ventana, (variableRandom,variableRandom, variableRandom), (ANCHO//2, 0), (ANCHO//2, ALTO))
   for y in range(ALTO//2, ALTO, 10):
       pygame.draw.line(ventana, (random.choice(range(256)), random.choice(range(256)), random.choice(range(256))), (ANCHO//2, y), (delta, ALTO//2))
       delta = delta-10
   for x in range(ALTO//2, 0, -10):
       pygame.draw.line(ventana, (random.choice(range(256)), random.choice(range(256)), random.choice(range(256))), (ANCHO//2, x), (beta, ALTO//2))
       beta = beta-10
   for a in range(ALTO//2, ALTO, 10):
       pygame.draw.line(ventana, (random.choice(range(256)), random.choice(range(256)), random.choice(range(256))), (ANCHO//2, a), (alfa, ALTO//2))
       alfa = alfa + 10
   for b in range(ALTO//2, 0, -10):
       pygame.draw.line(ventana, (random.choice(range(256)), random.choice(range(256)), random.choice(range(256))), (ANCHO//2, b), (gama, ALTO//2))
       gama = gama+10


# Dibuja un espiral con forma de cuadrado de color negro
def dibujarEspiral(ventana):
    for x in range(10, ANCHO // 2, 10):
        pygame.draw.line(ventana, NEGRO, (x, x), (ANCHO - x, x))
        pygame.draw.line(ventana, NEGRO, (x, ALTO - x), (ANCHO - x + 10, ALTO - x))
        pygame.draw.line(ventana, NEGRO, (x, x), (x, ALTO - x))
        pygame.draw.line(ventana, NEGRO, (ANCHO - x, x), (ANCHO - x, ALTO - x - 10))
        pygame.draw.line(ventana, NEGRO, (x + 10, ALTO - x - 10), (ANCHO - x, ALTO - x - 10))


# Dibuja 12 círculos de radio 150 para formar una figura parecida a una flor
def dibujarCirculos(ventana):
   radio =150
   for x in range(1, 13):
       pygame.draw.circle(ventana, NEGRO, (ANCHO//2+int(radio*math.cos(math.radians(-30*x))), ALTO//2+int(radio*math.sin(math.radians(-30*x)))), radio, 1)



# Inicializa las funciones de pygame y manda a llamar a las funciones cuando el usuario introduce un número entre 1 y 4
def dibujar(programa):
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

       if programa == 1:
           dibujarCuadrosCirculos(ventana)
       elif programa == 2:
           dibujarParabolas(ventana)
       elif programa == 3:
           dibujarEspiral(ventana)
       elif programa == 4:
           dibujarCirculos(ventana)



       pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
       reloj.tick(1)  # 1 fps


# Aproxima el valor de PI usando una fórmula y ciclos, el último denominador es el que el usuario introduzca.
def aproximarPi(parametro):
    resultado = 0
    for x in range(1, parametro + 1, 1):
        division = 1 / (x * x * x * x)
        resultado = resultado + division
    pi = (resultado * 90) ** 0.25
    return pi


# Muestra cuantos números de tres cifrass son divisibles entre 19
def contarDivisibles():
   contador = 0
   for x in range(100, 1000):
       if x % 19 == 0:
           contador = contador + 1
   return contador


# Imprime dos pirámides de números utilizando contadores y acumuladores.
def imprimirPiramides():
 contador = 1
 acumulador = 1
 acumulador2 = 1
 for x in range(1, 10):
     resultado = acumulador * 8 + contador
     print("%d *8 + %d = %d" % (acumulador, contador, resultado))
     contador = contador + 1
     acumulador = acumulador * 10 + contador
 for x in range(1, 10):
     total = acumulador2 ** 2
     print("%d * %d = %d" % (acumulador2, acumulador2, total))
     acumulador2 = acumulador2 * 10 + 1


# Función Principal. Muestra el menú y manda a llamar a las otras funciones.
def leerOpcionPrograma():
   print("Misión 5. Seleccione qué quiere hacer.")
   print("1. Dibujar cuadros y círculos")
   print("2. Dibujar parábolas")
   print("3. Dibujar espiral")
   print("4. Dibujar círculos")
   print("5. Aproximar PI")
   print("6. Contar divisibles entre 19")
   print("7. Imprimir pirámides de números")
   print("0. Salir")
   programa=int(input("¿Qué desea hacer? "))
   return programa


def main():
   programa = leerOpcionPrograma()
   while programa != 0:
       if programa<0 or programa>7:
           print("Por favor ingrese un número válido")
       elif programa > 0 and programa <5:
           dibujar(programa)
       elif programa == 5:
           parametro = int(input("¿Cuál quieres que sea el último divisor?"))
           pi = aproximarPi(parametro)
           print("El valor aproximado de pi es:", pi)
       elif programa == 6:
           numerosDivisibles = contarDivisibles()
           print("Hay", numerosDivisibles, "números de 3 cifras divisibles entre 19")
       elif programa == 7:
           imprimirPiramides()
       programa = leerOpcionPrograma()
   print("Termina programa")








main()

