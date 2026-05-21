import pyxel

pyxel.init(240, 160, "Mon petit jeu", fps=60)


x = 110  # position x du joueur
y = 140  # position y du joueur
vy = 0  # vitesse y du joueur


def update():
    global x, y, vy

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.btn(pyxel.KEY_LEFT):
        x -= 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        x += 2
    if pyxel.btnp(pyxel.KEY_SPACE):
        vy = -5  # une impulsion vers le haut

    vy += 0.2  # la gravité est une accélération vers le bas !
    y += vy
    y = min(y, 140)  # le "sol" contraint y <= 140


def draw():
    pyxel.cls(1)
    pyxel.rect(x, y, 20, 20, 7)


pyxel.run(update, draw)
