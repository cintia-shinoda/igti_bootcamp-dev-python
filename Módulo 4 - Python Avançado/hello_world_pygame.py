# coding: iso-8859-1 -*-

background_image_filename = 'foto-igti.jpg'
mouse_image_filename = 'selo-bootcamp.png'

import pygame
from pygame.locals import *
from sys import exit

# inicializando o console
pygame.init()

# definindo a tela
screen = pygame.display.set_mode((720, 640))
# adicionando um nome para a tela
pygame.display.set_caption("Olá, Mundo Game!")

# definindo a imagem de background e converte para o mesmo formato do display
background = pygame.image.load(background_image_filename).convert()
# definindo  a imagem do cursor (convert_alpha permite que as formas sejam desenhadas)
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get(): #loop infinito que fica esperando o evento que quit (clique no X da janela)
        if event.type == QUIT:
            pygame.quit()