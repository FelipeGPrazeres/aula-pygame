import pygame, random
#carregando imagens
imagemTubarao= pygame.image.load("img/gokuflying.png")
imagemPeixe= pygame.image.load("img/dragonball.png")
imagemFundo= pygame.image.load("img/fundoo.jpg")
#definindo outras constantes do jogo
LARGURAJANELA=800
ALTURAJANELA=700
LARGURAPEIXE=80
ALTURAPEIXE=30
LARGURATUBARAO=290
ALTURATUBARAO=190
VEL=6
ITERACOES=30
#redimensionando as imagens
imagemFundo = pygame.transform.scale(imagemFundo, (LARGURAJANELA, ALTURAJANELA))
imagemPeixe = pygame.transform.scale(imagemPeixe, (LARGURAPEIXE, ALTURAPEIXE))
imagemTubarao = pygame.transform.scale(imagemTubarao, (LARGURATUBARAO, ALTURATUBARAO))
# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordeDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]
    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]
    if teclas["direita"] and jogador["objRect"].right < bordeDireita:
        jogador["objRect"].x += jogador["vel"]
    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]
    if teclas["baixo"] and jogador["objRect"].bottom < bordaInferior:
        jogador["objRect"].y += jogador["vel"]
# definindo a função moverBloco(), que registra a posição do bloco
def moverPeixe(peixe):
    peixe["objRect"].x += peixe["vel"]

# inicializando pygame
pygame.init()

# instanciando método Clock para variavel relogio
relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Imagem e Som")

# criando jogador
jogador = {"objRect": pygame.Rect(300, 100, LARGURATUBARAO, ALTURATUBARAO), 
           "imagem": imagemTubarao, 
           "vel": VEL,
           "colisaoRect": pygame.Rect(300+50,100+50,LARGURATUBARAO-100, ALTURATUBARAO-100)
           }

#configurando o som
somComer = pygame.mixer.Sound("mp3/comer.mp3")

#Carregar a musica de fundo
pygame.mixer.music.load('mp3/soundtrack.mp3')

#Definir o volume
pygame.mixer.music.set_volume(0.2)

#Reproduzir a música em loop
pygame.mixer.music.play(-1,0.0)
somAtivado = True

# definindo o dicionario que guardará as direcoes pressionadas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

# inicializando outras variáveis
contador = 0
peixes = []
deve_continuar = True
# loop do jogo
while deve_continuar:
    # checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
                deve_continuar = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False
            if evento.key == pygame.K_m:
                if somAtivado:
                    pygame.mixer.music.stop()
                    somAtivado = False
                else:
                    pygame.mixer.music.play(-1,0.0)
                    somAtivado = True

        # quando um botao do mouse é pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            peixes.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], LARGURAPEIXE, ALTURAPEIXE), "imagem": imagemPeixe, "vel": VEL - 3})
        
    # Verifique o estado atual das teclas
    teclas = pygame.key.get_pressed()
    teclas = {
        "esquerda": teclas[pygame.K_LEFT] or teclas[pygame.K_a],
        "direita": teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
        "cima": teclas[pygame.K_UP] or teclas[pygame.K_w],
        "baixo": teclas[pygame.K_DOWN] or teclas[pygame.K_s],
    }

    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posX = random.randint(0, (LARGURAJANELA - ALTURAPEIXE))
        posY = -LARGURAPEIXE
        velRandom = random.randint(VEL - 3, VEL + 3)
        peixes.append({"objRect": pygame.Rect(posX, posY, LARGURAPEIXE, ALTURAPEIXE), "imagem": imagemPeixe, "vel": velRandom})
    
    #Preenchendo a janela
    janela.blit(imagemFundo, (0,0))

    #Movendo jogador
    moverJogador(jogador,teclas,(LARGURAJANELA, ALTURAJANELA))

    # desenhando jogador
    janela.blit(jogador["imagem"], jogador["objRect"])

    #Na parte do loop onde verifica colisoes, utilize o novo rect
    for peixe in peixes:
        comeu = jogador["colisaoRect"].colliderect(peixe["objRect"])
        if comeu and somAtivado:
            somComer.play()
        if comeu or peixe["objRect"].x > ALTURAJANELA:
            peixes.remove(peixe)
    
    #Não esqueça de atualizar a posição do rect de colisão a cada movimento do jogador
    jogador["colisaoRect"].topleft=(jogador["objRect"].x + 50, jogador["objRect"].y + 50)

    #Movendo e desenhando os peixes
    for peixe in peixes:
        moverPeixe(peixe)
        janela.blit(peixe["imagem"], peixe["objRect"])
    
    # atualizando a janela
    pygame.display.update()

    # FPS
    relogio.tick(60)

# encerrando módulos de Pygame
pygame.quit()      