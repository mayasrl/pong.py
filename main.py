import pygame, sys, random
 
pygame.init()
 
LARGURA, ALTURA = 1280, 720
 
FONTE = pygame.font.SysFont("Consolas", int(LARGURA/20))
 
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong!")
RELOGIO = pygame.time.Clock()

jogador = pygame.Rect(LARGURA-110, ALTURA/2-50, 10, 100)
oponente = pygame.Rect(110, ALTURA/2-50, 10, 100)
pontuacao_jogador, pontuacao_oponente = 0, 0 

bola = pygame.Rect(LARGURA/2-10, ALTURA/2-10, 20, 20)
velocidade_x, velocidade_y = 1, 1

while True:
    teclas_pressionadas = pygame.key.get_pressed()

    if teclas_pressionadas[pygame.K_UP]:
        if jogador.top > 0:
            jogador.top -= 2
    if teclas_pressionadas[pygame.K_DOWN]:
        if jogador.bottom < ALTURA:
            jogador.bottom += 2

    if teclas_pressionadas[pygame.K_w]:
        if oponente.top > 0:
            oponente.top -= 2
    if teclas_pressionadas[pygame.K_s]:
        if oponente.bottom < ALTURA:
            oponente.bottom += 2

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if bola.y >= ALTURA:
        velocidade_y = -1
    if bola.y <= 0:
        velocidade_y = 1
    if bola.x <= 0:
        pontuacao_jogador += 1
        bola.center = (LARGURA/2, ALTURA/2)
        velocidade_x, velocidade_y = random.choice([1, -1]), random.choice([1, -1])
    if bola.x >= LARGURA:
        pontuacao_oponente += 1
        bola.center = (LARGURA/2, ALTURA/2)
        velocidade_x, velocidade_y = random.choice([1, -1]), random.choice([1, -1])
    if jogador.x - bola.width <= bola.x <= jogador.x and bola.y in range(jogador.top-bola.width, jogador.bottom+bola.width):
        velocidade_x = -1
    if oponente.x - bola.width <= bola.x <= oponente.x and bola.y in range(oponente.top-bola.width, oponente.bottom+bola.width):
        velocidade_x = 1

    bola.x += velocidade_x * 2
    bola.y += velocidade_y * 2

    texto_pontuacao_jogador = FONTE.render(str(pontuacao_jogador), True, "white")
    texto_pontuacao_oponente = FONTE.render(str(pontuacao_oponente), True, "white")

    TELA.fill("black")

    pygame.draw.rect(TELA, "light pink", jogador)
    pygame.draw.rect(TELA, "light blue", oponente)
    pygame.draw.circle(TELA, "light yellow", bola.center, 10)

    TELA.blit(texto_pontuacao_jogador, (LARGURA/2+50, 50))
    TELA.blit(texto_pontuacao_oponente, (LARGURA/2-50, 50))
 
    pygame.display.update()
    RELOGIO.tick(300)


