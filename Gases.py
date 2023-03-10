#Importo las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import random

####### Primera parte, una sola bola #######

def dar_pasito(x, y, vx, vy, dt):
    # Actualizamos las posiciones con las fórmulas
    x = x + vx*dt
    y = y + vy*dt
    return x, y # devolvemos las nuevas posiciones actualizadas

# Funciones rebotar. Similares salvo las desigualdades del if.
# Si se cumple la condición, corregimos, si no, no.
def rebotar_der(x, vx, x_max):
    if x > x_max:
        x = x - 2 * (x - x_max)
        vx = -vx
    return x, vx

def rebotar_izq(x, vx, x_min):
    if x < x_min:
        x = x - 2*(x-x_min)
        vx = -vx
    return x, vx

def rebotar_arriba(y, vy, y_max):
    if y > y_max:
        y = y - 2 * (y - y_max)
        vy = -vy
    return y, vy

def rebotar_abajo(y, vy, y_min):
    if y < y_min:
        y = y - 2 * (y - y_min)
        vy = - vy
    return y, vy

def simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos):
    # Listas de posiciones con las condiciones iniciales
    posiciones_x = [x]
    posiciones_y = [y]
    for i in range(n_pasos):
        x, y = dar_pasito(x, y, vx, vy, dt) # Primero actualizamos la posición con MRU
        x, vx = rebotar_der(x, vx, L)       # Después nos fijamos si hay que corregir por rebote
        x, vx = rebotar_izq(x, vx, -L)
        y, vy = rebotar_arriba(y, vy, L)
        y, vy = rebotar_abajo(y, vy, -L)
        # Agregamos las posiciones nuevas a las listas
        posiciones_x.append(x) 
        posiciones_y.append(y)
    return posiciones_x, posiciones_y


### Usamos simular_bola_ocho y graficamos sus resultados

#Defino los parámetros de las funciones
x = 0
y = 0
vx = 1.0
vy = 1.35
dt = 0.01
L = 5
v_max = 2
n_bolas = 10
n_pasos = 10000

posiciones_x, posiciones_y = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos)

#Los gráficos de la primera parte, ahora comentados

# fig, ax = plt.subplots() #Creamos una figura y un eje de matplotlib
# ax.plot( posiciones_x , posiciones_y ) #Grafica la pelotita (COMPLETAR)
# ax.set_aspect("equal") #Hace que la escala de los ejes sea la misma
# #Graficamos los bordes de la mesa: vlines y hlines dibujan rectas verticales
# # y horizontales respectivamente:
# ax.vlines(-5, ymin=-5, ymax=5, color="black") #Izquierda
# ax.vlines(5, ymin=-5, ymax=5, color="black") #Derecha
# ax.hlines(-5, xmin=-5, xmax=5, color="black") #Abajo
# ax.hlines(5, xmin=-5, xmax=5, color="black") #Arriba
# #Seteamos ticks (las lineas en los numeros de la posicion)
# #Largos cada dos metros:
# ax.set_xticks(np.arange(-6, 7, 2))
# ax.set_yticks(np.arange(-6, 7, 2))
# #Cortos (por eso el minor=True) cada 0.5 metros:
# ax.set_xticks(np.arange(-7, 7, 0.5), minor=True)
# ax.set_yticks(np.arange(-7, 7, 0.5), minor=True)
# ax.grid(which="both") #Dibujamos la grilla
# ax.set_xlim([-7, 7]) #Seteamos limites del grafico en x
# ax.set_ylim([-7, 7]) #idem en y
# plt.show()


def pelicula_bola_ocho(x, y, vx, vy, dt, L, n_pasos, nombre):
    archivo = open(nombre + ".txt", "w")  # Abrimos el archivo en modo escritura ("w" es de write)
    print(1,"\n",file=archivo) # Imprimimos la cantidad de bolas (en esta función es siempre 1) y una linea vacia ("\n" es el simbolo de nueva linea)
    
    # Reutilizamos simular_bola_ocho
    posiciones_x, posiciones_y = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos)
    # Escribimos en el archivo
    for i in range(len(posiciones_x)): # Podria ser len(posiciones_y) tambien (deberian tener el mismo largo)
        print(1, posiciones_x[i], posiciones_y[i], file=archivo)
    archivo.close() # Cerramos el archivo

## Utilizamos pelicula_bola_ocho, ahora tenemos un parametro adicional que es el nombre del archivo

#Definimos los parámetros de las funciones

# Solo definimos el nuevo parametro nombre, los otros los podemos modificar mas arriba
nombre = "pelicula_bola_ocho"
pelicula_bola_ocho(x, y, vx, vy, dt, L, n_pasos, nombre)

####### Segunda parte - muchas bolas #######

def cond_ini(L, v_max, n_bolas):
    # Inicializamos las listas
    posiciones_x = []
    posiciones_y = []
    velocidades_x = []
    velocidades_y = []
    for i in range(n_bolas):
        #Genero las posiciones random en [-L, L]x[-L, L]
        x = (random.random()*2 - 1)*L
        y = (random.random()*2 - 1)*L
        #Genero las velocidades random en [-v_max, v_max]x[-v_max, v_max]
        vx = (random.random()*2 - 1)*v_max
        vy = (random.random()*2 - 1)*v_max
        #Agrego las cantidades a las listas
        posiciones_x.append(x)
        posiciones_y.append(y)
        velocidades_x.append(vx)
        velocidades_y.append(vy)
    return posiciones_x, posiciones_y, velocidades_x, velocidades_y

def pelicula_muchas(dt, L, v_max, n_pasos, n_bolas, nombre):
    archivo = open(nombre + ".txt", "w") # Abrimos el archivo
    print(n_bolas,"\n",file=archivo) # Imprimimos la cantidad de bolas y una linea vacia ("\n" es el simbolo de nueva linea)
    posiciones_x, posiciones_y, velocidades_x, velocidades_y = cond_ini(L, v_max, n_bolas) # Generamos las condiciones iniciales
    for j in range(n_pasos):
        for i in range(n_bolas):
            x, y, vx, vy = posiciones_x[i], posiciones_y[i], velocidades_x[i], velocidades_y[i]
            print(i, x, y, file=archivo) # Imprimimos el número de bola y las posiciones
            # Calculamos y corregimos posiciones igual que en simular_bola_ocho
            x, y = dar_pasito(x, y, vx, vy, dt)
            x, vx = rebotar_der(x, vx, L)
            x, vx = rebotar_izq(x, vx, -L)
            y, vy = rebotar_arriba(y, vy, L)
            y, vy = rebotar_abajo(y, vy, -L)
            posiciones_x[i], velocidades_x[i], posiciones_y[i], velocidades_y[i] = x, vx, y, vy
    archivo.close() # Cerramos el archivo

## Utilizamos peliculas_muchas

#Definimos los parámetros de las funciones
x = 0
y = 0
dt = 0.01
L = 5
v_max = 2
n_bolas = 10
n_pasos = 5000
nombre = "trayectorias_muchas_bolas"

pelicula_muchas(dt, L, v_max, n_pasos, n_bolas, nombre)
