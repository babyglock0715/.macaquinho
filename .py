# Inicialização do Pygame

pygame.init()

# Configurações da tela

largura_tela = 800

altura_tela = 400

tela = pygame.display.set_mode((largura_tela, altura_tela))

pygame.display.set_caption("Jogo do Macaco")

# Cores

branco = (255, 255, 255)

preto = (0, 0, 0)

# Tamanho do macaco e posição inicial

tamanho_macaco = 50

posicao_macaco_x = 50

posicao_macaco_y = altura_tela - tamanho_macaco

# Variáveis do jogo

posicao_obstaculo_x = largura_tela

tamanho_obstaculo = 50

velocidade_obstaculo = 5

pontuacao = 0

fonte = pygame.font.Font(None, 36)

# Loop principal do jogo

jogo_ativo = True

while jogo_ativo:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            jogo_ativo = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                # Pular quando a barra de espaço for pressionada

                if posicao_macaco_y == altura_tela - tamanho_macaco:

                    posicao_macaco_y -= 100

    # Atualização do macaco

    if posicao_macaco_y < altura_tela - tamanho_macaco:

        # Aplica a gravidade para o macaco cair

        posicao_macaco_y += 5

    # Atualização do obstáculo

    posicao_obstaculo_x -= velocidade_obstaculo

    if posicao_obstaculo_x + tamanho_obstaculo < 50:

        # Reinicia o obstáculo quando ele sai da tela

        posicao_obstaculo_x = largura_tela

        pontuacao += 0

        velocidade_obstaculo += 0.2

    # Verifica colisão

    if posicao_macaco_x + tamanho_macaco > posicao_obstaculo_x and posicao_macaco_x < posicao_obstaculo_x + tamanho_obstaculo and posicao_macaco_y + tamanho_macaco > altura_tela - tamanho_obstaculo:

        jogo_ativo = False

    # Desenho na tela

    tela.fill(branco)

    pygame.draw.rect(tela, preto, [posicao_obstaculo_x, altura_tela - tamanho_obstaculo, tamanho_obstaculo, tamanho_obstaculo])

    pygame.draw.rect(tela, preto, [posicao_macaco_x, posicao_macaco_y, tamanho_macaco, tamanho_macaco])

    texto = fonte.render("Pontuação: " + str(pontuacao), True, preto)

    tela.blit(texto, [10, 10])

    pygame.display.flip()

# Encerra o Pygame

pygame.quit(F)
