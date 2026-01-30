---
title: 24-NSIJ1ME1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ1ME1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ1ME1.pdf){ .md-button }
[:material-arrow-right:](24-NSIJ1ME1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Aucune autre site ne cite le site 2 (`s2`), il n'a donc pas de prédécesseurs. Ainsi la ligne 9 affecte à l'attribut `predecesseurs` de `s2` une liste vide.

2. 
```python
s4.predecesseurs = [(s1, 1), (s2, 2)]
s5.predecesseurs = [(s1, 2), (s3, 3), (s4, 6)]
```

3. `#!py s2.successeurs[1][1]` renvoie la valeur associée au second successeur de `s2`, soit le nombre de citations de `s2` vers `s3`, soit `#!py 5`.

4. La valeur de popularité du site 1 est 4 + 2 = **6**.

5. 
```python
def calculPopularite(self):
    self.popularite = 0
    for site, nb_citations in self.predecesseurs:
        self.popularite += nb_citations
    return self.popularite
```

6. La liste `listeS` est manipulée comme une **file** (premier arrivé, premier sorti).

7. La fonction `parcoursGraphe` réalise **un parcours en largeur**.

8. L'appel `parcoursGraphe(s1)` renvoie `[s1, s3, s4, s5]`. Le sommet `s2` n'est pas visité car il n'a pas de prédécesseur, et qu'il n'est pas le sommet de départ.

9. 
```python hl_lines="6 7"
def lePlusPopulaire(listeSites):
	maxPopularite = 0
	siteLePlusPopulaire = listeSites[0]
	for site in listeSites:
		if site.popularite > maxPopularite:
			maxPopularite = site.popularite
			siteLePlusPopulaire = site
	return siteLePlusPopulaire
```

1.   L'expression `lePlusPopulaire(parcoursGraphe(s1)).nom` renvoie `#!py 'site3'`.

2.   Quelques points :
	* L'implémentation actuelle du parcours en largeur est sous-optimale en raison de l'utilisation de `.pop(0)` — de complexité linéaire — pour défiler un sommet de la file. Dans le pire des cas, cette opération est effectuée jusqu'à $n$ fois, la complexité finale atteint $O(n² + m)$.
	* Cette complexité quadratique est inefficace même pour quelques milliers de sites. En négligeant le traitement des arcs, car $m = O(n^2)$, et en considérant 10000 sites, et un temps de calcul pour une opération entre 1 µs et 100 µs, le temps d'exécution total varierait entre 2 minutes et 3 heures.
	* De plus, ce parcours ne garantit pas que tous les sites soient visités, car certains peuvent être inaccessibles depuis le sommet de départ. Une solution pourrait être de considérer le graphe comme non orienté, en incluant les prédécesseurs au voisinage d'un sommet.
	* Plus simplement, il suffit de stocker initialement tous les sites dans une liste et appeler directement `lePlusPopulaire` de complexité linéaire.

</div>