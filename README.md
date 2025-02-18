# Pong em Python

Projeto desenvolvido para a disciplina de **Computação Gráfica** na faculdade, com o objetivo de recriar o clássico **Pong**. O jogo foi construído em **Python**, utilizando a biblioteca **Pygame**, para demonstrar conceitos de **animação 2D**, **desenho de elementos gráficos** e **detecção de colisões** em tempo real.

---

## Visão Geral

- **Linguagem**: Python  
- **Biblioteca**: Pygame  
- **Recursos Implementados**:
  - Menus de seleção de modo de jogo (*Dois Jogadores* ou *Contra CPU*).
  - Movimentação e colisão de objetos (bola e raquetes).
  - Sistema de pontuação simples para os jogadores.
  - Ajuste de dificuldade incremental a cada colisão, para tornar o jogo dinâmico.

O projeto reforça habilidades de programação gráfica, animação e manipulação de eventos, reproduzindo a jogabilidade envolvente do Pong original.

---

## Imagens do Projeto
 
![Tela Inicial](https://github.com/user-attachments/assets/0e296840-537e-4ba9-bb3e-2cacd5e6e94a)
![Jogo em andamento](https://github.com/user-attachments/assets/358d1e57-2ec0-4fe4-b4d1-6be9d4f6b307)
![Movimento da Bola](https://github.com/user-attachments/assets/251cce6d-7395-4d26-9972-6db5bdcfc01d)

---

## Instruções Básicas

1. **Menu Inicial**: Selecione o modo de jogo (**1** para dois jogadores ou **2** para jogar contra a CPU).  
2. **Controles**:
   - Jogador 1: Setas de direção para cima (*↑*) e para baixo (*↓*).  
   - Jogador 2 (ou CPU): Usa *W* e *S* (ou controle automático no modo CPU).  
3. **Pontuação**: Cada vez que a bola sai pela lateral, o adversário marca ponto.  
4. **Saída para Menu**: Pressione a tecla **M** a qualquer momento para voltar ao menu inicial.  

---

## Destaques Técnicos

- **Movimentação**: A bola e as raquetes se movem a cada frame de renderização, com **colisões** detectadas entre a bola, as paredes e as raquetes.  
- **Modo CPU**: Uma lógica simples controla a raquete do computador, definindo seu movimento com base na posição da bola.  
- **Variáveis de Velocidade**: A cada colisão com uma raquete, a velocidade da bola aumenta ligeiramente, deixando o jogo mais desafiador.  

---

<p align="center">
  Desenvolvido com 💛 por <strong>@mayasrl</strong>.
</p>
