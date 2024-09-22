import pygame
import sys
import random
import os

pygame.init()

LARGURA, ALTURA = 1280, 720
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong!")

def carregar_fonte(tamanho, negrito=False):
    try:
        return pygame.font.Font(None, tamanho)
    except:
        return pygame.font.SysFont("Consolas", tamanho, bold=negrito)

FONTE = carregar_fonte(int(LARGURA / 15))
FONTE_PEQUENA = carregar_fonte(int(LARGURA / 40))

RELOGIO = pygame.time.Clock()

jogador = pygame.Rect(LARGURA - 110, ALTURA / 2 - 50, 10, 100)
oponente = pygame.Rect(110, ALTURA / 2 - 50, 10, 100)
bola = pygame.Rect(LARGURA / 2 - 10, ALTURA / 2 - 10, 20, 20)

velocidade_x, velocidade_y = 4, 4
pontuacao_jogador, pontuacao_oponente = 0, 0
modo_jogo = None

def mostrar_menu():
    TELA.fill("black")
    titulo = FONTE.render("Pong", True, "white")
    TELA.blit(titulo, (LARGURA / 2 - titulo.get_width() / 2, ALTURA / 4 - 50))
    espaco_entre_opcoes = 80
    modo_2_jogadores = FONTE.render("1: Dois Jogadores", True, "white")
    modo_cpu = FONTE.render("2: Contra CPU", True, "white")
    fechar_jogo = FONTE.render("ESC: Fechar Jogo", True, "white")
    TELA.blit(modo_2_jogadores, (LARGURA / 2 - modo_2_jogadores.get_width() / 2, ALTURA / 2))
    TELA.blit(modo_cpu, (LARGURA / 2 - modo_cpu.get_width() / 2, ALTURA / 2 + espaco_entre_opcoes))
    TELA.blit(fechar_jogo, (LARGURA / 2 - fechar_jogo.get_width() / 2, ALTURA / 2 + espaco_entre_opcoes * 2))
    instrucao = FONTE_PEQUENA.render("Pressione 'M' durante o jogo para voltar ao menu", True, "gray")
    TELA.blit(instrucao, (LARGURA / 2 - instrucao.get_width() / 2, ALTURA - 80))
    pygame.display.update()

def movimento_cpu():
    if oponente.centery < bola.centery and oponente.bottom < ALTURA:
        oponente.y += 4
    if oponente.centery > bola.centery and oponente.top > 0:
        oponente.y -= 4

def reiniciar_jogo():
    global pontuacao_jogador, pontuacao_oponente, bola, velocidade_x, velocidade_y
    pontuacao_jogador = 0
    pontuacao_oponente = 0
    bola.center = (LARGURA / 2, ALTURA / 2)
    velocidade_x = random.choice([4, -4])
    velocidade_y = random.choice([4, -4])

while True:
    if modo_jogo is None:
        mostrar_menu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    reiniciar_jogo()
                    modo_jogo = "2_jogadores"
                if evento.key == pygame.K_2:
                    reiniciar_jogo()
                    modo_jogo = "vs_cpu"
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        continue

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_m:
                modo_jogo = None

    teclas_pressionadas = pygame.key.get_pressed()

    if teclas_pressionadas[pygame.K_UP]:
        jogador.y -= 5
    if teclas_pressionadas[pygame.K_DOWN]:
        jogador.y += 5

    if jogador.top < 0:
        jogador.top = 0
    if jogador.bottom > ALTURA:
        jogador.bottom = ALTURA

    if modo_jogo == "2_jogadores":
        if teclas_pressionadas[pygame.K_w]:
            oponente.y -= 5
        if teclas_pressionadas[pygame.K_s]:
            oponente.y += 5
    elif modo_jogo == "vs_cpu":
        movimento_cpu()

    if oponente.top < 0:
        oponente.top = 0
    if oponente.bottom > ALTURA:
        oponente.bottom = ALTURA

    bola.x += velocidade_x
    bola.y += velocidade_y

    if bola.top <= 0 or bola.bottom >= ALTURA:
        velocidade_y *= -1

    if bola.left <= 0:
        pontuacao_jogador += 1
        bola.center = (LARGURA / 2, ALTURA / 2)
        velocidade_x = random.choice([4, -4])
        velocidade_y = random.choice([4, -4])
    if bola.right >= LARGURA:
        pontuacao_oponente += 1
        bola.center = (LARGURA / 2, ALTURA / 2)
        velocidade_x = random.choice([4, -4])
        velocidade_y = random.choice([4, -4])

    if bola.colliderect(jogador) and velocidade_x > 0:
        velocidade_x *= -1.1
    if bola.colliderect(oponente) and velocidade_x < 0:
        velocidade_x *= -1.1

    TELA.fill("black")
    pygame.draw.rect(TELA, "light pink", jogador)
    pygame.draw.rect(TELA, "light blue", oponente)
    pygame.draw.ellipse(TELA, "light yellow", bola)

    texto_pontuacao_jogador = FONTE.render(str(pontuacao_jogador), True, "white")
    texto_pontuacao_oponente = FONTE.render(str(pontuacao_oponente), True, "white")
    TELA.blit(texto_pontuacao_oponente, (LARGURA / 2 - 60, 50))
    TELA.blit(texto_pontuacao_jogador, (LARGURA / 2 + 20, 50))

    pygame.display.update()
    RELOGIO.tick(60)
