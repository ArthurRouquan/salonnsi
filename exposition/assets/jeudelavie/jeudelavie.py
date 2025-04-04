import pyxel as px
from itertools import product
import random

VOISINAGE = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def grille_aleatoire(n, p=0.5):
    return [random.choices((0, 1), k=n) for _ in range(n)]


def indices_voisins(x, y, n):
    return (((x + dx) % n, (y + dy) % n) for dx, dy in VOISINAGE)


def calculer_voisins(grille):
    n = len(grille)
    voisins = [[0] * n for _ in range(n)]
    for x, y in product(range(n), repeat=2):
        if grille[x][y]:
            for vx, vy in indices_voisins(x, y, n):
                voisins[vx][vy] += 1
    return voisins


def calculer_grille_suivante(grille):
    voisins = calculer_voisins(grille)
    n = len(grille)
    grille_suivante = [[0] * n for _ in range(n)]
    for x, y in product(range(n), repeat=2):
        grille_suivante[x][y] = voisins[x][y] == 3 or (grille[x][y] and voisins[x][y] == 2)
    return grille_suivante


class JeuDeLaVie:
    def __init__(self, n):
        self.n = n
        self.grille = grille_aleatoire(self.n)
        self.pause = False
        self.frame = 1
        self.vitesse = 10  # nb. de frames requis avant une mise à jour de la grille
        px.init(n, n, 'Jeu de la vie', fps=60)
        px.run(self.update, self.draw)

    def update(self):
        if (not self.pause and self.frame % self.vitesse == 0) or px.btnp(px.KEY_RIGHT):
            self.grille = calculer_grille_suivante(self.grille)
        if px.btnp(px.KEY_R):  # réinitialiser aléatoirement la grille
            self.grille = grille_aleatoire(self.n)
        if px.btnp(px.KEY_BACKSPACE):  # effacer la grille
            self.grille = [[0] * self.n for _ in range(self.n)]
        if px.btnp(px.KEY_SPACE):  # mettre en pause
            self.pause ^= True
        if px.btnp(px.MOUSE_BUTTON_LEFT):  # garde en mémoire l'état de la 1ère cellule cliquée
            self.etat = self.grille[px.mouse_x][px.mouse_y]
        if px.btn(px.MOUSE_BUTTON_LEFT):  # dessiner / effacer des cellules
            self.grille[px.mouse_x][px.mouse_y] = self.etat ^ True

        self.vitesse = min(20, max(1, self.vitesse + px.btnp(px.KEY_DOWN) - px.btnp(px.KEY_UP)))  # modifier la vittese de jeu
        self.frame += 1

    def draw(self):
        col_mort = 1 if self.pause else 0
        col_vivant = 6 if self.pause else 7
        px.cls(col_mort)
        for x, y in product(range(self.n), repeat=2):
            if self.grille[x][y]:
                px.pset(x, y, col_vivant)
        x, y = px.mouse_x, px.mouse_y
        if self.pause:  # curseur croix
            px.line(x - 2, y, x - 1, y, 10)
            px.line(x + 1, y, x + 2, y, 10)
            px.line(x, y - 2, x, y - 1, 10)
            px.line(x, y + 2, x, y + 1, 10)
        else:  # curseur triangle
            px.tri(x, y, x + 2, y, x, y + 2, 10)


JeuDeLaVie(128)
