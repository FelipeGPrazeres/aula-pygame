import pygame
import time

PRETO = (0,0,0)
AMARELO = (255,255,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

larguraJanela=800
alturaJanela=700

def mover(figura,dimensaoJanela):
    borda_esquerda=0
    borda_superior=0
    borda_direita=dimensaoJanela[0]
    borda_inferior=dimensaoJanela[1]
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]