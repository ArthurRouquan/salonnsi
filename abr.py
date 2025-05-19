class Noeud:
    def __init__(self, v, g=None, d=None):
        self.valeur = v
        self.gauche = g
        self.droite = d


def string(arbre: Noeud):
    return f'({string(arbre.gauche)} {arbre.valeur} {string(arbre.droite)})' if arbre else '.'


def inserer_en_place(arbre: Noeud, x):
    if x < arbre.valeur:
        if arbre.gauche is None:
            arbre.gauche = Noeud(x)
        else:
            inserer_en_place(arbre.gauche, x)
    else:
        if arbre.droite is None:
            arbre.droite = Noeud(x)
        else:
            inserer_en_place(arbre.droite, x)


def inserer_fonctionnel(arbre: Noeud, x):
    if arbre is None:
        return Noeud(x)
    if x < arbre.valeur:
        arbre.gauche = inserer_fonctionnel(arbre.gauche, x)
    else:
        arbre.droite = inserer_fonctionnel(arbre.droite, x)
    return arbre


a = Noeud(2, Noeud(1))
inserer_fonctionnel(a, -1)
inserer_fonctionnel(a, 8)
inserer_fonctionnel(a, 9)
inserer_fonctionnel(a, 8.5)
print(string(a))
