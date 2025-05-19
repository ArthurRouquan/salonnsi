import pyxel
import random

LARGEUR, HAUTEUR = 15, 9
VITESSE_SERPENT = 4


def reinitialiser():
    global serpent, direction, direction_demandée, score, gameover
    serpent = [(3, 4), (2, 4), (1, 4)]  # coordonnées de chaque bloc du serpent
    direction = (1, 0)  # direction courante du serpent
    direction_demandée = (1, 0)  # direction demandée par le joueur pour le prochain déplacement
    score = 0
    gameover = False
    placer_pomme()


def placer_pomme():
    global pomme
    while True:
        pomme = (random.randint(0, LARGEUR - 1), random.randint(0, HAUTEUR - 1))
        if pomme not in serpent:  # on évite que la pomme soit placée sur le serpent
            break


def update():
    global direction, direction_demandée, serpent, score, gameover

    if pyxel.btnp(pyxel.KEY_R):
        reinitialiser()
    if gameover:
        return

    # gestion des entrées clavier
    if pyxel.btnp(pyxel.KEY_UP) and direction != (0, 1):
        direction_demandée = (0, -1)
    if pyxel.btnp(pyxel.KEY_DOWN) and direction != (0, -1):
        direction_demandée = (0, 1)
    if pyxel.btnp(pyxel.KEY_RIGHT) and direction != (-1, 0):
        direction_demandée = (1, 0)
    if pyxel.btnp(pyxel.KEY_LEFT) and direction != (1, 0):
        direction_demandée = (-1, 0)

    if pyxel.frame_count % VITESSE_SERPENT == 0:  # toutes les VITESSE_SERPENT images
        # déplacement du serpent
        x, y = serpent[0]  # tête du serpent
        dx, dy = direction = direction_demandée
        serpent.insert(0, ((x + dx) % LARGEUR, (y + dy) % HAUTEUR))
        if serpent[0] == pomme:  # collision serpent-pomme
            placer_pomme()  # on replace la pomme
            score += 1
        else:
            serpent.pop()  # on enlève la queue si on n'a pas mangé une pomme
        gameover = serpent[0] in serpent[1:]  # collision serpent-serpent


def draw():
    for x in range(LARGEUR):
        for y in range(HAUTEUR):
            pyxel.blt(8 * x, 8 * y, 0, 0, 8, 8, 8, 0)  # fond
    for x, y in serpent:
        pyxel.blt(8 * x, 8 * y, 0, 8, 0, 8, 8, 1)  # corps du serpent
    x, y = serpent[0]
    pyxel.blt(8 * x, 8 * y, 0, 0, 0, 8, 8, 1)  # tête du serpent
    pyxel.blt(8 * pomme[0], 8 * pomme[1], 0, 16, 0, 8, 8, 0)  # pomme

    if gameover:
        pyxel.rect(16, 16, 88, 40, 1)
        pyxel.rectb(16, 16, 88, 40, 12)
        pyxel.text(26, 1 + 24, '    GAME OVER     ', 6)
        pyxel.text(24, 9 + 24, 'PRESS R TO RESTART', 6)
        pyxel.text(24, 17 + 24, f' YOUR SCORE IS {score}', 6)


pyxel.init(LARGEUR * 8, HAUTEUR * 8, 'Snake', capture_scale=1, capture_sec=10)
pyxel.load('snake.pyxres')
reinitialiser()
pyxel.run(update, draw)
