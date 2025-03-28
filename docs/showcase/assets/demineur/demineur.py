import pyxel as px  # un alias plus concis !
from time import time
import random

""" Définition des constantes de jeu. """

FICHIER_RESSOURCE = 'demineur.pyxres'

# construction d'un dictionnaire IMAGES pour nommer les différentes images (sprites) du jeu
POSITION = {
    'curseur': (0, 8),
    'horloge': (0, 16), 'mine-bleu': (8, 16), 'drapeau-bleu': (16, 16),
    'smiley-repos': (0, 24), 'smiley-attente': (8, 24), 'smiley-victoire': (16, 24), 'smiley-defaite': (24, 24), 'smiley-recommencer': (32, 24),
    'drapeau': (0, 32), 'drapeau-incorrect': (8, 32), 'drapeau-correct': (16, 32),
    'mine': (0, 40),
    'case-impair': (0, 48), 'case-pair': (8, 48),
}
VOISINS = {i: (8 * i, 0) for i in range(9)}
POSITION.update(VOISINS)
IMAGES = {name: (0, *p, 8, 8, 4) for name, p in POSITION.items()}  # px.blt(x, y, *IMAGES['...']) est plus lisible !
#
VOISINAGE = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# valeurs symboliques pour différencier les différentes phases du jeu
DEBUT, EN_COURS, DEFAITE, VICTOIRE = 0, 1, 2, 3


class Demineur:
    def __init__(self, largeur, hauteur, nb_mines):
        self.largeur, self.hauteur = largeur, hauteur
        self.nb_mines = nb_mines
        self.reset()
        px.init(self.largeur * 7, (self.hauteur + 1) * 7, 'Démineur', fps=60)
        px.load(FICHIER_RESSOURCE)
        px.run(self.update, self.draw)

    def valide(self, i, j):
        """ Renvoie True si (i, j) sont des coordonnées valides de la grille, False sinon. """
        return 0 <= i < self.largeur and 0 <= j < self.hauteur

    def indices_grille(self):
        """ Renvoie tous les indices de la grille sous la forme d'un générateur. """
        return ((i, j) for i in range(self.largeur) for j in range(self.hauteur))

    def indices_voisins(self, i, j):
        """ Renvoie les indices des cases adjacentes autour de (i, j) sous la forme d'un générateur. """
        return ((i + di, j + dj) for di, dj in VOISINAGE if self.valide(i + di, j + dj))

    def placer_mines(self):
        """ Place aléatoirement les mines sur la grille tout en mettant à jour la matrice des voisins. """
        self.mines = [[False] * self.hauteur for _ in range(self.largeur)]
        self.voisins = [[0] * self.hauteur for _ in range(self.largeur)]
        indices_aleatoires = random.sample(list(self.indices_grille()), self.nb_mines)
        for i, j in indices_aleatoires:
            self.mines[i][j] = True
            for vi, vj in self.indices_voisins(i, j):
                self.voisins[vi][vj] += 1

    def reset(self):
        """ Réinitialise le jeu. """
        self.placer_mines()
        self.visible = [[False] * self.hauteur for _ in range(self.largeur)]
        self.drapeau = [[False] * self.hauteur for _ in range(self.largeur)]
        self.etat = DEBUT

        self.nb_nonvisibles = self.largeur * self.hauteur
        self.nb_drapeaux = 0
        self.nb_drapeaux_corrects = 0
        self.temps = 0

    def case_info(self, i, j):
        """ Renvoie toutes les informations de la case (i, j). """
        return self.mines[i][j], self.voisins[i][j], self.visible[i][j], self.drapeau[i][j]

    def est_fin(self):
        return self.etat == VICTOIRE or self.etat == DEFAITE

    def curseur_case(self):
        """ Renvoie les coordonnées de la case pointée par le curseur. """
        return px.mouse_x // 7, px.mouse_y // 7

    def curseur_sur_smiley(self):
        """ Renvoie True si le curseur est sur le smiley, False sinon. """
        x, y = 7 * (self.largeur // 2), 7 * self.hauteur
        return x <= px.mouse_x < x + 7 and y <= px.mouse_y < y + 7

    def basculer_drapeau(self, i, j):
        """ Dépose un drapeau sur la case (i, j), ou l'enlève si un est déjà posé. """
        mine, _, _, drapeau = self.case_info(i, j)
        self.drapeau[i][j] ^= True  # la porte XOR est utile pour inverser un bit
        self.nb_drapeaux += -1 if drapeau else 1
        if mine:
            self.nb_drapeaux_corrects += -1 if drapeau else 1

    def tout_reveler(self):
        """ Révèle toutes les cases de la grille (pour la fin de partie). """
        for i, j in self.indices_grille():
            self.visible[i][j] = True

    def explorer(self, i, j):
        """ Révèle la case (i, j) puis révèle récursivement les cases adjacentes si son nombre de voisins est nul. """
        mine, voisins, visible, drapeau = self.case_info(i, j)
        if visible or drapeau:
            return
        self.visible[i][j] = True
        self.nb_nonvisibles -= 1
        if self.etat == DEBUT:
            self.tdebut = time()
            self.etat = EN_COURS
        if mine:
            self.etat = DEFAITE
            self.tout_reveler()
        if voisins == 0:
            for vi, vj in self.indices_voisins(i, j):
                if self.drapeau[vi][vj]:  # supprime les drapeaux inutiles au passage
                    self.basculer_drapeau(vi, vj)
                self.explorer(vi, vj)

    def drapeau_complet(self, i, j):
        """ Renvoie True si le joueur a posé le bon nombre de drapeaux autour de (i, j). """
        return self.voisins[i][j] == sum(self.drapeau[vi][vj] for vi, vj in self.indices_voisins(i, j))

    def update(self):
        if px.btnp(px.KEY_R) or px.btnp(px.MOUSE_BUTTON_LEFT) and self.curseur_sur_smiley():
            self.reset()

        i, j = self.curseur_case()
        if not self.valide(i, j) or self.est_fin():
            return

        _, _, visible, drapeau = self.case_info(i, j)

        if (px.btnp(px.MOUSE_BUTTON_RIGHT) or px.btnp(px.KEY_D)) and not visible:
            self.basculer_drapeau(i, j)

        if px.btnp(px.MOUSE_BUTTON_LEFT):
            self.selection = (i, j)  # permet au joueur d'annuler son clic s'il déplace le curseur

        if px.btnr(px.MOUSE_BUTTON_LEFT) and (i, j) == self.selection:
            if drapeau:
                self.basculer_drapeau(i, j)
            elif visible and self.drapeau_complet(i, j):
                for vi, vj in self.indices_voisins(i, j):
                    self.explorer(vi, vj)
            else:
                self.explorer(i, j)

        if self.nb_drapeaux_corrects == self.nb_mines == self.nb_nonvisibles:
            self.etat = VICTOIRE
            self.tout_reveler()

        if self.etat == EN_COURS:
            self.temps = time() - self.tdebut

    def draw(self):
        px.cls(1)

        # dessine la grille
        for i, j in self.indices_grille():
            mine, voisins, visible, drapeau = self.case_info(i, j)
            sprite = 'case-impair' if (i + j) & 1 else 'case-pair'  # un nombre est pair s'il finit par 0 en binaire
            if visible:
                sprite = 'mine' if mine else voisins
            if drapeau:
                sprite = 'drapeau' + (('-correct' if mine else '-incorrect') if self.est_fin() else '')
            x, y = i * 7, j * 7
            px.blt(x, y, *IMAGES[sprite])

        # dessine le rectangle de sélection du curseur
        i, j = self.curseur_case()
        if not self.est_fin() and self.valide(i, j):
            mine, voisins, visible, drapeau = self.case_info(i, j)
            selection = px.btn(px.MOUSE_BUTTON_LEFT) and self.selection == (i, j)
            montrer_voisinage = visible and voisins and not mine
            rectangle = (7 * (i - 1) - 1, 7 * (j - 1) - 1, 3 * 7 + 2, 3 * 7 + 2) if montrer_voisinage else (7 * i - 1, 7 * j - 1, 7 + 2, 7 + 2)
            if not (visible and not voisins):
                px.rectb(*rectangle, 0 if selection else 7)

        # dessine le menu
        y = 7 * self.hauteur
        px.rect(0, y, self.largeur * 7, 7, 1)
        px.blt(0, y, *IMAGES['horloge'])
        px.text(7, y + 1, str(int(self.temps)), 6)

        x = 7 * (self.largeur - 4)
        px.blt(x, y, *IMAGES['mine-bleu'])
        px.text(x + 7, y + 1, str(self.nb_mines), 6)
        px.blt(x + 14, y, *IMAGES['drapeau-bleu'])
        px.text(x + 20, y + 1, str(self.nb_drapeaux), 6)

        x = 7 * (self.largeur // 2)
        etat = 'recommencer' if self.curseur_sur_smiley() else 'victoire' if self.etat == VICTOIRE else 'defaite' if self.etat == DEFAITE else 'attente' if px.btn(px.MOUSE_BUTTON_LEFT) else 'repos'
        px.blt(x, y, *IMAGES['smiley-' + etat])

        # dessine le curseur
        px.blt(px.mouse_x - 2, px.mouse_y, *IMAGES['curseur'])


if __name__ == '__main__':
    Demineur(40, 16, 99)
