import re
import pygame
from pygame.locals import *

def defino_escala(xmax,xmin,ymax,ymin): # esta funcion calcula los factores parar pasar de coordenadas decimales a coordenadas enteras en pixels para dibujarlo en la ventana
    xpixelscale=(1.0*WIDTH)/(xmax-xmin)
    ypixelscale=(1.0*HEIGHT)/(ymax-xmin)
    return xpixelscale,ypixelscale

'''
Programita para visualizar trayectorias escritas en formato xy.
Se deban ajustar los valores de los maximos valores del tamanio de la caja.
'''

############# Parametros a cambiar ###############

L=5      # tamaño de la caja
archivo="movimientoBolaDiapos.txt" # nombre del archivo a leer
FRAMERATE = 1  # cuadros por segundo (velocidad con que se muestra la pelicula)

################################# 

ajustable=False  # los vaores maximos y minimos se ajustan segun los valores que lee, ojo que si una bola se va lejos no se ve nada
h=1.0 # Tamaño de la sangría de la caja

WIDTH = 800  # ancho de la pantalla en pixels
HEIGHT = 800  # largo de la pantalla en pixels

xmax=L+h  # tamanio de la pantalla en x
ymax=L+h   # tamanio de la pantalla en y
xmin=-L-h
ymin=-L-h

coor=open(archivo,"r") # nombre del archivo a leer
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # abre la ventana
clock = pygame.time.Clock() # clock va a regular la velocidad de actualizacion de la pantalla
backgroundCol = Color('white') # color del fondo
pygame.display.set_caption(" Animación ") # mensaje en la ventanita
xoffset=WIDTH/2 # define el medio de la ventana en X
yoffset=HEIGHT/2 # idem en Y
xpixelscale,ypixelscale = defino_escala(xmax,xmin,ymax,ymin) # llamo a la funcion que calcula los factores de cambio de escala

linea=coor.readline() # lee la primer linea
npart=int(linea)      # la primer linea debe tener el numero de particulas
seguir=True
linea=coor.readline() # lee la primer linea
frame=0
myFont = pygame.font.SysFont("ubuntu", 24,bold=True)
while (seguir):
    clock.tick(FRAMERATE)  # espera a que se cumpla en tiempo de avanzar
    for event in pygame.event.get():   # lee los eventos del mouse 
        if event.type == pygame.QUIT: # para que cuando se apreta la cruz en la ventana el programa termine
            seguir = False
            pygame.quit()
    #print(npart)
    screen.fill(Color('white')) # llena la pantalla con blanco
    pygame.draw.line(screen, Color('black'), (int(xpixelscale*L+xoffset),int(ypixelscale*L+yoffset)), (int(xpixelscale*L+xoffset), int(xpixelscale*(-L)+xoffset)), 1) # Dibuja las cuatro lineas
    pygame.draw.line(screen, Color('black'), (int(xpixelscale*(-L)+xoffset),int(ypixelscale*(-L)+yoffset)), (int(xpixelscale*L+xoffset), int(xpixelscale*(-L)+xoffset)), 1) # 
    pygame.draw.line(screen, Color('black'), (int(xpixelscale*(-L)+xoffset),int(ypixelscale*(-L)+yoffset)), (int(xpixelscale*(-L)+xoffset), int(xpixelscale*(L)+xoffset)), 1) # 
    pygame.draw.line(screen, Color('black'), (int(xpixelscale*(-L)+xoffset),int(ypixelscale*(L)+yoffset)), (int(xpixelscale*(L)+xoffset), int(xpixelscale*(L)+xoffset)), 1) # 

    frame+=1
    diceDisplay = myFont.render("Frame="+ str(frame), 1, (0,0,0))
    screen.blit(diceDisplay, (WIDTH-200, HEIGHT-50))
    tamanio=int(max(30/xmax,1)) # define el tamanio que van a tener la pelotas dibujadas en función de la escala
    final=False
    i=0
    while i < npart and not final:# este loop es por cada particula
        i+=1
        linea=coor.readline()   # lee la linea
        if linea:
            separada=re.split("\s+",linea) # separa las columnas en la lista separada
            x=float(separada[1])   # el segundo numero es la posicion en x
            y=float(separada[2])   # el tercer numero en la posicion en y
            if (ajustable):    # encuentra nuevos maximos y minimos si se elije que se ajustable
                if(x>xmax):
                    xmax=x
                    print("nuevo xmax",xmax)
                    xpixelscale,ypixelscale = defino_escala(xmax,xmin,ymax,ymin)
                if(x<xmin):
                    xmin=x
                    print("nuevo xmin",xmin)
                    xpixelscale,ypixelscale = defino_escala(xmax,xmin,ymax,ymin)
                if(y>ymax):
                    ymax=y
                    print("nuevo ymax",ymax)
                    xpixelscale,ypixelscale = defino_escala(xmax,xmin,ymax,ymin)
                if(y<ymin):
                    ymin=y
                    print("nuevo ymin",ymin)
                    xpixelscale,ypixelscale = defino_escala(xmax,xmin,ymax,ymin)
                tamanio=int(max(30/xmax,1)) # define el tamanio que van a tener la pelotas dibujadas en función de la escala
            pygame.draw.circle(screen, Color('red'), (int(xpixelscale*x+xoffset),int(-ypixelscale*y+yoffset)), tamanio, 0) # va dibujando cada pelota
        else:
            coor.seek(0)
            linea=coor.readline()
            linea=coor.readline()
            frame=0
            final=True

    pygame.display.update() # muestra lo que se dibujó hasta ahora.


