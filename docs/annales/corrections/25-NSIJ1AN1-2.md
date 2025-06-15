---
title: 25-NSIJ1AN1-2
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ1AN1-1.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1AN1-2.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1AN1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ1AN1-3.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
def passer_transit(self):
    self.etat = 'transit'
```

2. 
```python
def ajouter_colis(liste, colis):
    if colis.poids <= 25:
        liste.append(colis)
    else:
        print('Dépassement du poids maximal autorisé')
```

3. 
```python
def nb_colis(liste):
    return len(liste)
```

4. 
```python
def poids_total(liste):
    total = 0
    for c in liste:
        total = total + c.poids
    return total
```

5. 
```python
def liste_colis_etat(liste, statut):
    return [c for c in liste if c.etat == statut]
```

6. La fonction `tri_decroissant` implémente un **tri par sélection** de coût $O(n^2)$ dans le pire des cas.

7. Le **tri fusion**, dont le coût est $O(n \log n)$ dans le pire de cas, aurait pu être utilisé.

8. 
```python
def chargement_glouton(liste, rang, capacite):
    if rang == len(liste):
        return []
    elif liste[rang].poids <= capacite:
        return [liste[rang]] + chargement_glouton(liste, rang + 1, capacite - liste[rang].poids)
    else:
        return chargement_glouton(liste, rang + 1, capacite)
```

9. En python, le nombre d'appels récursifs est limité à 1000 par défaut. Lorsque `chargement_glouton` dépasse ce seuil, Python affiche cette erreur.

10.  
```python
def chargement_glouton2(liste, capacite):
    colis_a_charger = []
    for colis in liste:
        if colis.poids <= capacite:
            colis_a_charger.append(colis)
            capacité -= colis.poids
    return colis_a_charger
```

</div>