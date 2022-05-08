# Autor: Ana Beatriz Ferreira

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# Gerando a janela do jogo
window = Window(1000, 800)
window.set_title("ponguitos.py")

# Obtenção dos elementos da interface
background = GameImage('./assets/images/background.png')
padLeft = Sprite("./assets/images/bar.png", 1)
padRight = Sprite("./assets/images/bar.png", 1)
ball = Sprite("./assets/images/ball.png", 1)
startText = Sprite("./assets/images/inicio.png", 1)
winLeft = Sprite("./assets/images/vencedor-esquerda.png")
winRight = Sprite("./assets/images/vencedor-direita.png")
score = Sprite("./assets/images/placar.png")

# Posicionando as barras esquerda e direita na tela à 10px das margens
padLeft.x = 10
padLeft.y = window.height / 2 - padLeft.height / 2
padRight.x = window.width - padRight.width - 10
padRight.y = window.height / 2 - padRight.height / 2

# Posicionando o placar no topo da tela
score.y = 10
score.x = window.width / 2 - score.width / 2

# Posicionando a bola no centro da tela
ball.y = window.height / 2 - ball.height / 2
ball.x = window.width / 2 - ball.width / 2
vBallx = 0
vBally = 0

# Mostra a tela inicial com instrução pra começar
startText.x = window.width / 2 - startText.width / 2
startText.y = window.height / 2 - startText.height / 2

# Posicionando a tela final para ser chamada ao final
# da partida, dependendo do resultado
winLeft.x = -1100
winLeft.y = window.height / 2 - winLeft.height / 2
winRight.x = -1100
winRight.y = window.height / 2 - winRight.height / 2

points = [0, 0]
matchStarted = False

keys = window.get_keyboard()

# Game Loop
while(True):
    # Movimenta as barras com as teclas W e S ou UP e DOWN
    if keys.key_pressed('W') and padLeft.y >= 0:
        padLeft.y -= 400 * window.delta_time()
    if keys.key_pressed('S') and padLeft.y <= window.height - padLeft.height:
        padLeft.y += 400 * window.delta_time()
    if keys.key_pressed('UP') and padRight.y >= 0:
        padRight.y -= 400 * window.delta_time()
    if keys.key_pressed('DOWN') and padRight.y <= window.height - padRight.height:
        padRight.y += 400 * window.delta_time()

    # Movimenta a bola pelo eixo x
    ball.y += vBally * window.delta_time()
    ball.x += vBallx * window.delta_time()

    # Colisão com as barras
    if padLeft.collided_perfect(ball) and matchStarted:
        vBallx *= -1
        ball.x = padLeft.width + 10

    if padRight.collided_perfect(ball) and matchStarted:
        vBallx *= -1
        ball.x = window.width - padRight.width - ball.width - 10

    # Colisão com o limite superior ou inferior
    if ball.y > window.height - ball.height:
        vBally *= -1
        ball.y = window.height - ball.height - 1 # evita o deslizamento
    if ball.y < 0:
        vBally *= -1
        ball.y = 1
   
    if ball.x > window.width - ball.width:
        vBallx = vBally = 0
        ball.x = window.width / 2 - ball.width / 2
        ball.y = window.height / 2 - ball.height / 2
        matchStarted = False
        points[0] += 1
    if ball.x < 0:
        vBallx = vBally = 0
        ball.x = window.width / 2 - ball.width / 2
        ball.y = window.height / 2 - ball.height / 2
        matchStarted = False
        points[1] += 1


    # Atualiza o cenário
    background.draw()
    ball.draw()
    padRight.draw()
    padLeft.draw() 
    score.draw()
    winRight.draw()
    winLeft.draw()

    # Mostra o placar na tela
    window.draw_text(str(points[0]), 409.25, 60, 55, (255,179,108), "Inconsolata-Bold", False, False)
    window.draw_text(str(points[1]), 565, 60, 55, (255,179,108), "Inconsolata-Bold", False, False)
    
    if not matchStarted:
        startText.draw() # mantém a tela inicial enquanto o jogador não pressionar ENTER

    # Quando algum jogador atingir 5 pontos, o jogo encerra e imprime o vencedor
    if points[0] == 5:
        matchStarted = False
        
        winLeft.x = window.width / 2 - winLeft.width / 2 # posiciona a imagem do resultado no centro da tela
        
        points[0] = 0
        points[1] = 0

    if points[1] == 5:
        matchStarted = False

        winRight.x = window.width / 2 - winRight.width / 2 # posiciona a imagem do resultado no centro da tela

        points[0] = 0
        points[1] = 0

    # Quando ENTER for pressionado, a partida começa
    if keys.key_pressed('SPACE') and not matchStarted:
        startText.hide()

        winRight.x = -1100
        winLeft.x = -1100
        
        vBallx = -500
        vBally = -500
        
        matchStarted = True

    window.update()
