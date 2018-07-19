import pygame,sys
from pygame.locals import *
from clases import Nave
from clases import Invasor as Enemigo

from random import randint

#variables globales
ancho = 900
alto = 480
listaEnemigo = []

def detenerTodo():
    for enemigo in listaEnemigo:
        for disparar in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparar)

        enemigo.conquista=True

def cargarEnemigos():
    posx = 100
    for x in range(1,5):
        enemigo =Enemigo(posx,100,40,'imagenes/pipe1.png','imagenes/pipe2.png',)
        listaEnemigo.append(enemigo)
        posx = posx + 200

    posx = 100
    for x in range(1,5):
        enemigo =Enemigo(posx,0,40,'imagenes/Marciano2A.jpg','imagenes/Marciano2B.jpg',)
        listaEnemigo.append(enemigo)
        posx = posx + 200

    posx = 100
    for x in range(1,5):
        enemigo =Enemigo(posx,-100,40,'imagenes/Marciano3A.jpg','imagenes/Marciano3B.jpg',)
        listaEnemigo.append(enemigo)
        posx = posx + 200

def CHIRRILAND():

    #sentencia obligatoria para usarpygame
    pygame.init()

    # Objeto ventana tipo superficie generamos una superficie
    ventana = pygame.display.set_mode((ancho,alto))
    #Agregamos un mensaje en la parte superior de la ventana
    pygame.display.set_caption("CHIRRILAND")
    ImagenFondo = pygame.image.load('imagenes/Fondo.jpg')

    pygame.mixer.music.load('sonidos/sm.mp3')
    pygame.mixer.music.play()

    fuente = pygame.font.SysFont("Arial",30)
    texto=fuente.render("FIN DEL JUEGO",0,(120,100,40))


    jugador = Nave.naveEspacial(ancho,alto)
    cargarEnemigos()



    enJuego =True

    reloj = pygame.time.Clock()
    #Loop infinito mientas sea verdad
    while True:

        reloj.tick(38)

        #jugador.movimiento()

        tiempo = pygame.time.get_ticks()/1000

    # para comparar los eventos usamos el for
        for event in pygame.event.get():
    #pregunta si es tipo QUIT
            if event.type ==QUIT:
    #si es asi cierra los modulos de pygame
                pygame.quit()
                sys.exit()


            if enJuego==True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.movimientoIzquierda()

                    elif event.key == K_RIGHT:
                        jugador.movimientoDerecha()

                    elif event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
            


    #Actualiza la ventana


        ventana.blit(ImagenFondo,(0,0))





        jugador.dibujar(ventana)

        if len (jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top <10:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)





        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego=False
                    detenerTodo()

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego= False
                            detenerTodo()

                        if x.rect.top >900:
                            enemigo.listaDisparo.remove(x)

                        else:
                            for disparar in jugador.listaDisparo:
                                if x.rect.colliderect(disparar.rect):
                                    jugador.listaDisparo.remove(disparar)
                                    enemigo.listaDisparo.remove(x)




        if enJuego==False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(texto,(300,300))

        pygame.display.update()

CHIRRILAND()
