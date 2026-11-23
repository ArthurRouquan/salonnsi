"""Programme de référence complet du mini-projet « Cellules ».

Voir docs/projets/agario.md. Le jeu tourne à 60 images par seconde :
toutes les vitesses sont exprimées en pixels par image.
"""

import math

import pyxel

LARGEUR_ECRAN = 240
HAUTEUR_ECRAN = 160
LARGEUR_MONDE = 400
HAUTEUR_MONDE = 400
NB_GRAINS = 1000  # 300 tant que le monde a la taille de l'écran
NB_BOTS = 10
MASSE_DEPART = 10


class Cellule:
    def __init__(self, x, y, masse, couleur):
        self.x = x
        self.y = y
        self.masse = masse
        self.couleur = couleur
        self.vivante = True

    def rayon(self):
        # La surface d'un disque (pi * r²) est proportionnelle à la masse,
        # donc le rayon est proportionnel à la racine carrée de la masse.
        return math.sqrt(self.masse)

    def peut_manger(self, autre):
        if not self.vivante or not autre.vivante:
            return False
        if self.masse <= autre.masse:
            return False
        # Le centre de l'autre doit être dans notre disque : d < r,
        # c'est-à-dire d² < r². Or r² = masse : pas besoin de racine carrée.
        dx = autre.x - self.x
        dy = autre.y - self.y
        return dx * dx + dy * dy < self.masse

    def vitesse(self):
        # En pixels par image.
        return 1

    def manger(self, autre):
        self.masse = self.masse + autre.masse
        autre.vivante = False

    def deplacer_vers(self, cible_x, cible_y):
        dx = cible_x - self.x
        dy = cible_y - self.y
        d = math.sqrt(dx * dx + dy * dy)
        if d > self.vitesse():
            # (dx / d, dy / d) est un vecteur de longueur 1 :
            # on le multiplie par la vitesse.
            self.x = self.x + dx / d * self.vitesse()
            self.y = self.y + dy / d * self.vitesse()
        else:
            self.x = cible_x
            self.y = cible_y
        # On reste dans le monde.
        self.x = max(0, min(LARGEUR_MONDE, self.x))
        self.y = max(0, min(HAUTEUR_MONDE, self.y))

    def update(self, jeu):
        # Un grain de nourriture ne bouge pas.
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, self.rayon(), self.couleur)


class Joueur(Cellule):
    def update(self, jeu):
        # La souris donne des coordonnées écran : on les convertit
        # en coordonnées monde en ajoutant la position de la caméra.
        cible_x = pyxel.mouse_x + jeu.camera_x
        cible_y = pyxel.mouse_y + jeu.camera_y
        self.deplacer_vers(cible_x, cible_y)


class Bot(Cellule):
    def update(self, jeu):
        # Recherche de la cellule mangeable la plus proche.
        cible = None
        distance_min = 0
        for autre in jeu.grains + jeu.bots + [jeu.joueur]:
            if autre.vivante and self.masse > autre.masse:
                dx = autre.x - self.x
                dy = autre.y - self.y
                d = math.sqrt(dx * dx + dy * dy)
                if cible is None or d < distance_min:
                    cible = autre
                    distance_min = d
        if cible is not None:
            self.deplacer_vers(cible.x, cible.y)


class Jeu:
    def __init__(self):
        pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN, title="Cellules", fps=60)
        pyxel.mouse(True)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.joueur = Joueur(LARGEUR_MONDE / 2, HAUTEUR_MONDE / 2, MASSE_DEPART, 11)
        self.grains = []
        self.update_grains()
        self.bots = []
        self.update_bots()
        self.camera_x = 0
        self.camera_y = 0
        self.placer_camera()

    def placer_camera(self):
        self.camera_x = self.joueur.x - LARGEUR_ECRAN / 2
        self.camera_y = self.joueur.y - HAUTEUR_ECRAN / 2

    def update(self):
        if not self.joueur.vivante:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.reset()
            return

        # 1. Déplacements
        self.joueur.update(self)
        for bot in self.bots:
            bot.update(self)
        self.placer_camera()

        # 2. Repas : on marque les cellules mangées sans les supprimer
        mangeurs = [self.joueur] + self.bots
        for mangeur in mangeurs:
            for grain in self.grains:
                if mangeur.peut_manger(grain):
                    mangeur.manger(grain)
            for autre in mangeurs:
                if mangeur.peut_manger(autre):
                    mangeur.manger(autre)

        # 3. Après les boucles seulement : on retire les cellules mangées.
        self.update_grains()
        self.update_bots()

    def update_grains(self):
        """Retire les grains mangés et en fait apparaître de nouveaux."""
        vivants = []
        for grain in self.grains:
            if grain.vivante:
                vivants.append(grain)
        self.grains = vivants
        while len(self.grains) < NB_GRAINS:
            x = pyxel.rndf(0, LARGEUR_MONDE)
            y = pyxel.rndf(0, HAUTEUR_MONDE)
            self.grains.append(Cellule(x, y, 1, pyxel.rndi(1, 15)))

    def update_bots(self):
        """Retire les bots mangés et en fait apparaître de nouveaux."""
        vivants = []
        for bot in self.bots:
            if bot.vivante:
                vivants.append(bot)
        self.bots = vivants
        while len(self.bots) < NB_BOTS:
            x = pyxel.rndf(0, LARGEUR_MONDE)
            y = pyxel.rndf(0, HAUTEUR_MONDE)
            # On évite de faire apparaître un bot juste à côté du joueur.
            if abs(x - self.joueur.x) > 60 or abs(y - self.joueur.y) > 60:
                self.bots.append(Bot(x, y, pyxel.rndi(4, 30), 8))

    def draw(self):
        pyxel.cls(0)
        pyxel.camera(self.camera_x, self.camera_y)
        for i in range(0, LARGEUR_MONDE + 1, 20):
            pyxel.line(i, 0, i, HAUTEUR_MONDE, 1)
        for i in range(0, HAUTEUR_MONDE + 1, 20):
            pyxel.line(0, i, LARGEUR_MONDE, i, 1)
        for grain in self.grains:
            grain.draw()
        for bot in self.bots:
            bot.draw()
        if self.joueur.vivante:
            self.joueur.draw()

        pyxel.camera()
        pyxel.text(2, 2, "Masse : " + str(int(self.joueur.masse)), 7)
        if not self.joueur.vivante:
            pyxel.text(106, 70, "Perdu !", 8)
            pyxel.text(80, 80, "Cliquez pour rejouer", 7)


Jeu()
