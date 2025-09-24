---
title: 25-NSIJ2PO1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ2PO1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ2PO1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ2PO1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
class Carte:
    def __init__(self, valeur):
        self.valeur = valeur
        self.TdB = self.calcul_TdB()
```

2. 
```python
def calcul_TdB(self):
    tdb = 0
    if self.valeur % 11 == 0:
        tdb += 5
    if self.valeur % 10 == 0:
        tdb += 3
    if self.valeur % 10 == 5:
        tdb += 2
    if tdb == 0:
        tdb = 1
    return tdb

# alternative
def calcul_TdB(self):
    v = self.valeur
    return max(1, (v % 11 == 0) * 5 + (v % 10 == 0) * 3 + (v % 10 == 5) * 2)
```

3. 
```python
def est_superieure_a(self, autre):
    return self.valeur > autre.valeur
```

4. 
```python hl_lines="6 7 10"
class Paquet:
    def __init__(self, L):
        self.contenu = L

    def afficher(self):
        for carte in self.contenu:
            print(carte.valeur)

    def ajouter_carte(self, carte):
        self.contenu.append(carte)
```

5. 
```python
def nombre_TdB(self):
    total = 0
    for carte in self.contenu:
        total += carte.TdB
    return total

# alternative
def nombre_TdB(self):
    return sum(carte.TdB for carte in self.contenu)
```

6. 
```python
def distribuer(self, nbr):
    paquets = [Paquet([]) for j in range(nbr)]
    for i in range(10):
        for j in range(nbr):
            paquets[j].ajouter_carte(self.contenu.pop())
    return paquets
```

7. 
```python
J1 = Joueur('Joueur 1', L[0])
```

8. 
```python hl_lines="3 5 6"
from random import *

jeu = [Carte(i) for i in range (1, 105)]
shuffle(jeu)
jeu_initial = Paquet(jeu)
distri = jeu_initial.distribuer(2)

Ordi = Joueur('Ordi', distri[0])
J1 = Joueur('J1', distri[1])
```

</div>
