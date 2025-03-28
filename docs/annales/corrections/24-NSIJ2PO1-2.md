---
title: 24-NSIJ2PO1-2
---

<div class="circle-ol" markdown>

1. 
    * Le nœud initial est appelé **racine**.
    * Un nœud qui n’a pas de fils est appelé **feuille**.
    * Un arbre binaire est un arbre dans lequel chaque nœud a **au maximum** deux fils.
    * Un arbre binaire de recherche est un arbre binaire dans lequel tout
   nœud est associé à une clé qui est :
        * supérieure à chaque clé de tous les nœuds de son **sous-arbre gauche**.
        * inférieure à chaque clé de tous les nœuds de son **sous-arbre droit**.
  
2. **1 → 0 → 2 → 3 → 4 → 5 → 6**

3. **0 → 1 → 2 → 6 → 5 → 4 → 3**

4. **0 → 1 → 2 → 3 → 4 → 5 → 6**

5. 
```python
arbre_no1 = ABR()
arbre_no2 = ABR()
arbre_no3 = ABR()
for cle_a_inserer in [1, 0, 2, 3, 4, 5, 6]:
    arbre_no1.inserer(cle_a_inserer)
for cle_a_inserer in [3, 2, 4, 1, 5, 0, 6]:
    arbre_no2.inserer(cle_a_inserer)
for cle_a_inserer in [3, 1, 5, 0, 2, 4, 6]:
    arbre_no3.inserer(cle_a_inserer)
```

6. 
|    Arbre    | Hauteur |
| :---------: | :-----: |
| `arbre_no1` |    5    |
| `arbre_no2` |    3    |
| `arbre_no3` |    2    |

7. 
```python
def est_present(self, cle_a_rechercher):
    if self.est_vide():
        return False
    elif cle_a_rechercher == self.cle():
        return True
    elif cle_a_rechercher < self.cle():
        return self.sag().est_present(cle_a_rechercher)
    else :
        return self.sad().est_present(cle_a_rechercher)
```

8. `arbre_no3.est_presente(7)` nécessitera ici le moins d'appels récursifs.

9. Un arbre *partiellement équilibré* est un arbre vide ou un arbre dont l'écart de hauteur entre ses deux sous-arbres est au plus de 1.

10. **Les arbres 2 et 3** sont partiellement équilibrés, car la différence de hauteur entre leurs sous-arbres est de 0. En revanche, pour l’arbre 1, cette différence est de 4.

11. **L'arbre 3** est le seul équilibré. L'arbre 2 n'est pas équilibré car son sous-arbre gauche (et droit) n'est pas partiellement équilibré. 

12. 
```python
def est_equilibre(self):
    return self.est_vide() or (self.est_partiellement_equilibre() and self.sag().est_equilibre() and self.sad().est_equilibre())

```

</div>
