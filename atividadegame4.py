import pygame

PRETO = (0,0,0)
AMARELO = (255,255,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BRANCO = (255,255,255)

LARGURAJANELA=800
ALTURAJANELA=700

def mover(bloco,dimensaoJanela):
    borda_esquerda=0
    borda_superior=0
    borda_direita = dimensaoJanela[0]
    borda_inferior = dimensaoJanela[1]
    # checa se a bloco ultrapassa o topo ou base da jane   la
    if bloco['objRect'].top < borda_superior or bloco['objRect'].bottom > borda_inferior:
        bloco['vel'][1] = -bloco['vel'][1]
    if bloco['objRect'].left < borda_esquerda or bloco['objRect'].right > borda_direita:
        bloco['vel'][0] = -bloco['vel'][0]
    bloco['objRect'].x += bloco['vel'][0]
    bloco['objRect'].y += bloco['vel'][1]

pygame.init()

relogio = pygame.time.Clock()

janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Colisão")

b1={"objRect":pygame.Rect(375,80,40,80), "cor": VERMELHO, "vel":[0,4]}
b2={"objRect":pygame.Rect(175,200,20,20), "cor": VERDE, "vel":[0,6]}
b3={"objRect":pygame.Rect(275,150,60,60), "cor": AZUL, "vel":[0,2]}
b4={"objRect":pygame.Rect(75,150,80,40), "cor": AMARELO, "vel":[0,8]}

blocos=[b1,b2,b3,b4]

bola = {"objRect":pygame.Rect(270,330,30,30), "cor": BRANCO, "vel":[30,30]}
deve_continuar = True
while deve_continuar:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
    

    for bloco in blocos:
        mover(bloco,(LARGURAJANELA,ALTURAJANELA))
        pygame.draw.rect(janela,bloco["cor"],bloco["objRect"])
        mudaCor = bola["objRect"].colliderect(bloco["objRect"])
        if mudaCor:
            bola["cor"]=bloco["cor"]

    mover(bola,(LARGURAJANELA,ALTURAJANELA))
    pygame.draw.ellipse(janela,bola["cor"],bola["objRect"])

    relogio.tick(60)
    pygame.display.update()
pygame.quit()