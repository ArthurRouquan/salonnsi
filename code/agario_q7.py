"""Corrigé des questions 4 à 7 (section « Le joueur mange les grains ») de docs/projets/agario.md."""

import math
import pyxel

LARGEUR_ECRAN = 240
HAUTEUR_ECRAN = 160
NB_GRAINS = 300
MASSE_DEPART = 10


class Cellule:
    def __init__(self, x, y, masse, couleur):
        self.x = x
        self.y = y
        self.masse = masse
        self.couleur = couleur
        self.vivante = True

    def rayon(self):
        return math.sqrt(self.masse)

    def deplacer_vers(self, cible_x, cible_y):
        dx = cible_x - self.x
        dy = cible_y - self.y
        d = math.sqrt(dx * dx + dy * dy)
        if d < self.vitesse():
            # Trop près : on se place directement sur la cible.
            self.x = cible_x
            self.y = cible_y
        else:
            # Vecteur unité (dx / d, dy / d), multiplié par la vitesse.
            self.x = self.x + dx / d * self.vitesse()
            self.y = self.y + dy / d * self.vitesse()

    def peut_manger(self, autre):
        if not self.vivante or not autre.vivante:
            return False
        if self.masse <= autre.masse:
            return False
        dx = autre.x - self.x
        dy = autre.y - self.y
        return dx * dx + dy * dy < self.masse

    def vitesse(self):
        # En pixels par image.
        return 1

    def manger(self, autre):
        self.masse = self.masse + autre.masse
        autre.vivante = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.rayon(), self.couleur)


class Jeu:
    def __init__(self):
        pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN, title="Cellules", fps=60)
        pyxel.mouse(True)
        self.joueur = Cellule(LARGEUR_ECRAN / 2, HAUTEUR_ECRAN / 2, MASSE_DEPART, 11)
        self.grains = []
        self.update_grains()  # la liste vide est remplie
        pyxel.run(self.update, self.draw)

    def update(self):
        self.joueur.deplacer_vers(pyxel.mouse_x, pyxel.mouse_y)

        # Pendant la boucle, on marque seulement les grains mangés...
        for grain in self.grains:
            if self.joueur.peut_manger(grain):
                self.joueur.manger(grain)

        # ... puis on les retire après la boucle.
        self.update_grains()

    def update_grains(self):
        # On garde les grains vivants dans une nouvelle liste...
        vivants = []
        for grain in self.grains:
            if grain.vivante:
                vivants.append(grain)
        self.grains = vivants
        # ... puis on complète avec des grains placés au hasard.
        while len(self.grains) < NB_GRAINS:
            x = pyxel.rndf(0, LARGEUR_ECRAN)
            y = pyxel.rndf(0, HAUTEUR_ECRAN)
            couleur = pyxel.rndi(1, 15)
            self.grains.append(Cellule(x, y, 1, couleur))

    def draw(self):
        pyxel.cls(0)
        for grain in self.grains:
            grain.draw()
        self.joueur.draw()


Jeu()
