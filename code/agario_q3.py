"""Corrigé des questions 2 et 3 (section « Une classe, des centaines d'objets ») de docs/projets/agario.md."""

import math
import pyxel

LARGEUR_ECRAN = 240
HAUTEUR_ECRAN = 160
NB_GRAINS = 300


class Cellule:
    def __init__(self, x, y, masse, couleur):
        self.x = x
        self.y = y
        self.masse = masse
        self.couleur = couleur

    def rayon(self):
        return math.sqrt(self.masse)

    def draw(self):
        pyxel.circ(self.x, self.y, self.rayon(), self.couleur)


class Jeu:
    def __init__(self):
        pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN, title="Cellules", fps=60)
        self.cellule = Cellule(120, 80, 100, 11)
        self.grains = []
        for i in range(NB_GRAINS):
            x = pyxel.rndf(0, LARGEUR_ECRAN)
            y = pyxel.rndf(0, HAUTEUR_ECRAN)
            couleur = pyxel.rndi(1, 15)
            self.grains.append(Cellule(x, y, 1, couleur))
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        for grain in self.grains:
            grain.draw()
        self.cellule.draw()


Jeu()
