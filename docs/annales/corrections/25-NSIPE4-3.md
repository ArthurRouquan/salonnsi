---
title: 25-NSIPE4-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIPE4-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIPE4-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIPE4.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. L'appel renvoie `#!py [31, 45, 108, 127, 421]`.

2. Le tri dictatorial n'est pas un algorithme de tri car il ne conserve pas l'intégralité des éléments.

3. 
| Itération | Comparaison | `serie_triee` |
| :---: | :---: | :---: |
| – | – | `#!py [8]` |   
| 1 | $2 \ngeqslant 8$ | `#!py [8]` |
| 2 | $9 \geqslant 2$ | `#!py [8, 9]` |
| 3 | $6 \ngeqslant 9$ | `#!py [8, 9]` |
| 4 |  $12 \geqslant 6$ | `#!py [8, 9, 12]` |

4. Le programme tente d'accéder au premier élément (`#!py serie[0]`) d'une liste **vide**, cela lève donc l'erreur `IndexError`. On peut résoudre ce cas particulier au début de la fonction :

    ```py
    def tri_dictatorial(serie):
        if len(serie) == 0:  # ou if not serie:
            return []
        ...
    ```

5. Les tests ne montrent que la présence de bugs pour les cas spécifiques testés, mais ne peuvent jamais garantir l'absence totale de bugs pour tous les cas possibles (nombre d'entrées potentiellement infini).

6.  Le problème est que le code compare l'élément courant avec son prédécesseur dans la liste d'origine. Par exemple, 3 est incorrectement ajouté à la suite de 8 car il est précédé de 2 dans la liste d'origine. Comme correction, il suffit de vérifier l'élément courant avec le dernier élément ajouté à la liste triée :

    ```python
    if serie[i] >= serie_triee[-1]:
    ```

7. 
```python
m8 = Maillon(8, None)
m0 = Maillon(0, m8)
m1 = Maillon(1, m0)
ma_liste = Liste(m1)
```

8. 
    * `#!py m1.valeur == 1` renvoie `#!py True`
    * `#!py m1.suivant.valeur == 8` renvoie `#!py False` 
    * `#!py m1.suivant.suivant == None` renvoie `#!py False` 
    * `#!py m1.suivant.suivant.suivant == None` renvoie `#!py True` 

9. 
```python
m1.suivant = m1.suivant.suivant
```

10. 
```python
def tri_dictatorial_chaine(chaine):
    maillon = chaine.tete
    while maillon.suivant is not None:
        if maillon.valeur <= maillon.suivant.valeur
            maillon = maillon.suivant
        else:
            maillon.suivant = maillon.suivant.suivant
```

11. Une pile est une structure de données linéaire fondée sur le principe LIFO (Last In, First Out). On ne peut ajouter (empiler) ou retirer (dépiler) des éléments qu'au sommet de la pile.

12. 
```
si p n'est pas vide:
    on crée une pile intermédiaire p2 vide;
    on dépile p, on stocke l'élément obtenu dans la variable dernier_conservé et on l'empile dans p2;
    tant que p n'est pas vide:
        on dépile p et on stocke l'élément obtenu dans la variable candidat;
        si candidat est supérieure ou égal à dernier_conservé:
            dernier_conservé prend la valeur de candidat et l'empile dans p2
    tant que p2 n'est pas vide:
        on dépile p2 et on empile l'élément obtenu dans p;
```

13. 
```python
def tri_dictatorial_pile(p):
    if p.est_vide():
        return
    p2 = Pile()
    dernier_conserve = p.depiler()
    p2.empiler(dernier_conserve)
    while not p.est_vide():
        candidat = p.depiler()
        if candidat >= dernier_conserve:
            dernier_conserve = candidat
            p2.empiler(candidat)
    while not p2.est_vide():
        p.empiler(p2.depiler())
```

</div>
