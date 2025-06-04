---
title: 24-NSIJ2ME1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ2ME1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2ME1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2ME1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. La classe `Piste` a pour attributs :
    * `self.nom` de type `#!py str`
    * `self.denivele` de type `#!py int` ou `#!py float`
    * `self.longueur` de type `#!py int` ou `#!py float`
    * `self.couleur` de type `#!py str`
    * `self.ouverte` de type `#!py bool`

2. 
```py
def set_couleur(self):
    if self.denivele >= 100:
        self.couleur = 'noire'
    elif self.denivele >= 70:
        self.couleur = 'rouge'
    elif self.denivele >= 40:
        self.couleur = 'bleue'
    else:
        self.couleur = 'verte'
```

3. **Proposition D** : `#!py lievre_blanc.get_pistes()` renvoie une liste d'objets de type `Piste`.

4. 
```python
for piste in lievre_blanc.get_pistes():
    if piste.get_couleur() == 'verte':
        piste.ouverte = False
```

5. 
```python
def pistes_de_couleur(lst: list, couleur: str):
    pistes = []
    for piste in lst:
        if piste.get_couleur() == couleur:
            pistes.append(piste.get_nom())
    return pistes

# alternative avec une liste en compréhension
def pistes_de_couleur(couleur: str, lst: list):
    return [piste.get_nom() for piste in lst if piste.get_couleur() == couleur]
```

6. 
```python hl_lines="2 6 7 8"
def semi_marathon(L):
    distance = 0
    liste_pistes = lievre_blanc.get_pistes()
    for nom in L:
        for piste in liste_pistes:
            if piste.get_nom() == nom:
                distance = distance + piste.get_longueur()
    return distance > 21.1
```

7. `#!py print(domaine['E']['F'])`

8. 
```python
def voisins(G, s):
    sommets_voisins = []
    for voisin in G[s]:
        sommets_voisins.append(voisin)
    return sommets_voisins

# alternative
def voisins(G, s):
    return list(G[s].keys())
```

9. 
```python hl_lines="2 5 6 7"
def longueur_chemin(G, chemin):
    precedent = chemin[0]
    longueur = 0
    for i in range(1, len(chemin)):
        longueur = longueur + G[precedent][chemin[i]]
        precedent = chemin[i]
    return longueur
```

10. La fonction `parcours` est récursive car elle s'appelle elle-même (ligne 7).

11. 
```python
def parcours_dep_arr(G, depart, arrivee):
    liste = parcours(G, depart)
    lst_chemins = []
    for chemin in liste:
        if chemin[-1] == arr and chemin not in lst_chemins:
            lst_chemins.append(chemin)
    return lst_chemins
```

12. 
```python hl_lines="3 7 8 9"
def plus_court(G, depart, arrivee):
    liste_chemins = parcours_dep_arr(G, depart, arrivee)
    chemin_plus_court = liste_chemins[0]
    minimum = longueur_chemin(G, chemin_plus_court)
    for chemin in liste_chemins:
        longueur = longueur_chemin(G, chemin)
        if longueur < minimum:
            minimum = longueur
            chemin_plus_court = chemin
    return chemin_plus_court
```

13. Le choix du pisteur-secouriste de privilégier la distance minimale est discutable car il ne prend pas en compte le dénivelé, qui influence le temps et l’effort nécessaires pour atteindre l’incident. Une piste plus courte mais avec un fort dénivelé pourrait en réalité être plus longue à parcourir. Un meilleur critère serait de calculer le temps estimé en fonction de la distance et du dénivelé pour choisir la piste la plus rapide.

</div>