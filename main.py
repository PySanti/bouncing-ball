#!dependencies/bin/python3.8
from sys import path
path.clear();
path.append("dependencies/lib/python3.8/site-packages/")
import pygame
from pygame.locals import *
from random import randint

Color = pygame.Color
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
momentum_x_para_colision = 12 
disminucion_de_momentum_en_y = 0.2
diferencia_de_momentum_en_x = 0.02

class Pelota:
    def __init__(self):
        self.posicion = [100,100]
        self.width = 100
        self.height = 100
        self.form = pygame.image.load('pelota-grande.jpg')
        self.form = pygame.transform.scale(self.form,(self.width, self.height))
        self.momentum_y = 0
        self.momentum_x = 20
        self.velocidad = 10
    @property
    def efecto_rebote(self):
        pygame.mixer.init()
        pygame.mixer.music.load('pelota.wav')
        pygame.mixer.music.play()
    def comprobar_colision_con_pared(self, direccion):
        if direccion == 'derecha':
            if self.posicion[0] + self.width >= screen_width:
                self.momentum_x = -momentum_x_para_colision
                self.efecto_rebote
        else:
            if self.posicion[0] <= 0:
                self.momentum_x = momentum_x_para_colision
                self.efecto_rebote

    def event_handling(self, event):
        if event.key == K_LEFT:
            if not self.posicion[0] <= 0:
                self.posicion[0] -= self.velocidad
            else:
                self.comprobar_colision_con_pared('izquierda')
        elif event.key == K_RIGHT:
            if not self.posicion[0] + self.form.get_width() >= screen_width:
                self.posicion[0] += self.velocidad
            else:
                self.comprobar_colision_con_pared('derecha')
    def y_momentum_check(self):
        if self.posicion[1] > screen_height - self.form.get_height():
            self.efecto_rebote
            self.momentum_y = -self.momentum_y
        else:
            self.momentum_y += disminucion_de_momentum_en_y
        self.posicion[1] += self.momentum_y
    def x_momentum_check(self):
        if circle.momentum_x != 0:
            circle.posicion[0] += circle.momentum_x
            if circle.momentum_x > 0:
                circle.momentum_x -= diferencia_de_momentum_en_x
            else:
                circle.momentum_x += diferencia_de_momentum_en_x


salir = False
circle = Pelota()
fps = pygame.time.Clock()
tecla_pulsada = False
ultimo_evento = None

while not salir:

    screen.fill(Color('white'))
    screen.blit(circle.form, circle.posicion)
    circle.y_momentum_check()
    circle.x_momentum_check()
    circle.comprobar_colision_con_pared('derecha')
    circle.comprobar_colision_con_pared('izquierda')
    for event in pygame.event.get():
        if event.type == QUIT:
            salir = True
        elif event.type == KEYUP:
            tecla_pulsada = False
        elif event.type == KEYDOWN:
            ultimo_evento = event
            tecla_pulsada = True
            circle.event_handling(event)
    if tecla_pulsada:
        circle.event_handling(ultimo_evento)



    pygame.display.update()
    fps.tick(100)

pygame.quit()



