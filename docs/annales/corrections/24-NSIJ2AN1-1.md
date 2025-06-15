---
title: 24-NSIJ2AN1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2AN1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2AN1.pdf){ .md-button }
[:material-arrow-right:](24-NSIJ2AN1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
def echange(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]
```

    Ou plus simplement :

    ```python
    def echange(tab, i, j):
        copie  = tab[i]
        tab[i] = tab[j]
        tab[j] = copie
    ```

2. 
```python hl_lines="6 7 8"
def triStooge(tab, i, j):
    if tab[i] > tab[j]:
        echange(tab, i, j)
    if j - i > 1:
        k = (j - i + 1) // 3
        triStooge(tab, i, j - k)
        triStooge(tab, i + k, j)
        triStooge(tab, i, j - k)
```

3. Cet algorithme est récursif car la fonction `triStooge` fait appel à elle-même (ligne 6 à 8).

4. Lors du premier appel, `#!py i = 0` et `#!py j = 5` donc `#!py k = (5 – 0 + 1) // 3 = 2`.

5. Sans compter l'appel initial, le nombre d'appels récursifs est **39** en comptant le nombre de nœuds, en excluant la racine, de l'arbre des appels.

6.  * Case 1 : `#!py triStooge(A, 1, 3)`
    * Case 2 : `#!py triStooge(A, 2, 3)`
    * Case 3 : `#!py triStooge(A, 0, 3)`

7. 
|           Appel           | Valeur de `A` avant l'appel | Valeur de `A` après l'appel |
| :-----------------------: | :-------------------------: | :-------------------------: |
| `#!py triStooge(A, 0, 3)` |     `#!py [5, 6, 4, 2]`     |     `#!py [2, 6, 4, 5]`     |
| `#!py triStooge(A, 0, 2)` |     `#!py [2, 6, 4, 5]`     |     `#!py [2, 6, 4, 5]`     |
| `#!py triStooge(A, 1, 3)` |     `#!py [2, 4, 6, 5]`     |     `#!py [2, 4, 6, 5]`     |
| `#!py triStooge(A, 0, 2)` |     `#!py [2, 4, 5, 6]`     |     `#!py [2, 4, 5, 6]`     |

1. Puisque $2 = \frac{6}{3} < \frac{8}{3}$, le **tri par insertion** (ou **le tri par sélection**) dont le coût en temps dans le pire des cas est **quadratique** $O(n^2)$, présente un meilleur coût. On aurait pu aussi citer le **tri fusion** de complexité quasilinéaire $O(n \log n)$.

</div>
