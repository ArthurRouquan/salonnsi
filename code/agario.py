"""Corrigé des questions 13 à 17 (section « Un monde plus grand que l'écran ») de docs/projets/agario.md.

C'est aussi le programme complet du projet.
"""

import math
import pyxel

LARGEUR_ECRAN = 240
HAUTEUR_ECRAN = 160
LARGEUR_MONDE = 400
HAUTEUR_MONDE = 400
NB_GRAINS = 1000
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
        return math.sqrt(self.masse)

    def vitesse(self):
        # En pixels par image.
        return 1

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
        # Q17 : on reste dans le monde.
        self.x = max(0, min(LARGEUR_MONDE, self.x))
        self.y = max(0, min(HAUTEUR_MONDE, self.y))

    def peut_manger(self, autre):
        if not self.vivante or not autre.vivante:
            return False
        if self.masse <= autre.masse:
            return False
        dx = autre.x - self.x
        dy = autre.y - self.y
        return dx * dx + dy * dy < self.masse

    def manger(self, autre):
        self.masse = self.masse + autre.masse
        autre.vivante = False

    def update(self, jeu):
        # Un grain ne bouge pas.
        pass

    def draw(self):
        pyxel.circ(self.x, self.y, self.rayon(), self.couleur)


class Joueur(Cellule):
    def update(self, jeu):
        # Q16 : la souris donne des coordonnées écran. Le joueur est au centre
        # de l'écran : on se décale de l'écart entre la souris et ce centre.
        cible_x = self.x + pyxel.mouse_x - LARGEUR_ECRAN / 2
        cible_y = self.y + pyxel.mouse_y - HAUTEUR_ECRAN / 2
        self.deplacer_vers(cible_x, cible_y)


class Bot(Cellule):
    def update(self, jeu):
        # Recherche de minimum : la cellule mangeable la plus proche.
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
        # Crée tous les objets : au lancement et à chaque nouvelle partie.
        self.joueur = Joueur(LARGEUR_MONDE / 2, HAUTEUR_MONDE / 2, MASSE_DEPART, 11)
        self.grains = []
        self.update_grains()
        self.bots = []
        self.update_bots()

    def update(self):
        # Partie perdue : on attend seulement un clic.
        if not self.joueur.vivante:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.reset()
            return

        # Déplacements : le même appel, mais chacun sa méthode update.
        self.joueur.update(self)
        for bot in self.bots:
            bot.update(self)

        # Repas : on marque seulement les cellules mangées...
        mangeurs = [self.joueur] + self.bots
        for mangeur in mangeurs:
            for grain in self.grains:
                if mangeur.peut_manger(grain):
                    mangeur.manger(grain)
            for autre in mangeurs:
                if mangeur.peut_manger(autre):
                    mangeur.manger(autre)

        # ... puis on les retire après les boucles.
        self.update_grains()
        self.update_bots()

    def update_grains(self):
        vivants = []
        for grain in self.grains:
            if grain.vivante:
                vivants.append(grain)
        self.grains = vivants
        while len(self.grains) < NB_GRAINS:
            x = pyxel.rndf(0, LARGEUR_MONDE)
            y = pyxel.rndf(0, HAUTEUR_MONDE)
            couleur = pyxel.rndi(1, 15)
            self.grains.append(Cellule(x, y, 1, couleur))

    def update_bots(self):
        vivants = []
        for bot in self.bots:
            if bot.vivante:
                vivants.append(bot)
        self.bots = vivants
        while len(self.bots) < NB_BOTS:
            x = pyxel.rndf(0, LARGEUR_MONDE)
            y = pyxel.rndf(0, HAUTEUR_MONDE)
            # Pas trop près du joueur, sinon défaite immédiate.
            if abs(x - self.joueur.x) > 40 or abs(y - self.joueur.y) > 40:
                masse = pyxel.rndi(4, 30)
                self.bots.append(Bot(x, y, masse, 8))

    def draw(self):
        pyxel.cls(0)
        # Q14 : caméra centrée sur le joueur, puis le contour du monde.
        pyxel.camera(self.joueur.x - LARGEUR_ECRAN / 2, self.joueur.y - HAUTEUR_ECRAN / 2)
        pyxel.rectb(0, 0, LARGEUR_MONDE, HAUTEUR_MONDE, 1)
        for grain in self.grains:
            grain.draw()
        for bot in self.bots:
            bot.draw()
        if self.joueur.vivante:
            self.joueur.draw()

        # Q15 : retour en coordonnées écran pour le texte.
        pyxel.camera()
        pyxel.text(2, 2, "Masse : " + str(int(self.joueur.masse)), 7)
        if not self.joueur.vivante:
            pyxel.text(106, 70, "Perdu !", 8)
            pyxel.text(80, 80, "Cliquez pour rejouer", 7)


Jeu()
