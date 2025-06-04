---
title: 24-NSIJ1PO1-2
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ1PO1-1.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ1PO1-2.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ1PO1.pdf){ .md-button }
[:material-arrow-right:](24-NSIJ1PO1-3.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
def possible_avec_penalites_seules(score):
    return score % 3 == 0
```

2. 
| Score | Liste des solutions                                      | Nombre de solutions |
| :---: | :------------------------------------------------------- | :-----------------: |
|   0   | `#!py [0]`                                               |          1          |
|   1   | `#!py []`                                                |          0          |
|   2   | `#!py []`                                                |          0          |
|   3   | `#!py [0, 3]`                                            |          1          |
|   4   | `#!py []`                                                |          0          |
|   5   | `#!py [0, 5]`                                            |          1          |
|   6   | `#!py [0, 3, 6]`                                         |          1          |
|   7   | `#!py [0, 7]`                                            |          1          |
|   8   | `#!py [0, 5, 8]`, `#!py [0, 3, 8]`                       |          2          |
|   9   | `#!py [0, 3, 6, 9]`                                      |          1          |
|  10   | `#!py [0, 3, 10]`,  `#!py [0, 7, 10]`, `#!py [0, 5, 10]` |          3          |

3. On vérifie bien :
   
    \[
    \begin{align*}
    f(10) &= f(10 - 3) + f(10 - 5) + f(10 - 7) \\
          &= f(7) + f(5) + f(3) \\
          &= 1 + 1 + 1 \\
          &= \boxed{3}
    \end{align*}    
    \]

4. 
|  $n$  | $f(n)$ |
| :---: | :----: |
|   0   |   1    |
|   1   |   0    |
|   2   |   0    |
|   3   |   1    |
|   4   |   0    |
|   5   |   1    |
|   6   |   1    |

5. 
```python
def nb_solutions(n):
    if n <= 6:
        return (1, 0, 0, 1, 0, 1, 1)[n]
    return nb_solutions(n - 3) + nb_solutions(n - 5) + nb_solutions(n - 7)
```

1. La fonction `nb_solutions` est appelée plusieurs fois avec les mêmes entrées, ce qui entraîne une redondance des calculs. Pour y palier, on peut mémoriser dans un cache les résultats déjà calculés. Cette technique est appelée **mémoïsation**. Comme on décompose le problème en sous-problèmes et qu'on mémorise les résultats intermédiaires, on applique ici plus généralement une stratégie de **programmation dynamique**.


7. Pour atteindre un score de 11 soit :

    * On marque au préalable 11 – 3 = 8 points (`#!py [0, 3, 8]` ou `#!py [0, 5, 8]`) puis on marque 3 points.
    * On marque au préalable 11 – 5 = 6 points (`#!py [0, 3, 6]`) puis on marque 5 points.
    * On marque au préalable 11 – 7 = 4 points (impossible) puis on marque 7 points.

    Ainsi, `#!py solutions_possibles(11)` renvoie `#!py [[0, 3, 8, 11], [0, 5, 8, 11], [0, 3, 6, 11]]`.

8. Le code à trou proposé est erroné.

    ```python hl_lines="5 8 11"
    def solutions_possibles(score):
        if score < 0:
            resultat = []
        elif score == 0:
            resultat = [[0]] 
        else:
            resultat = []
            for coup in [3, 5, 7]:
                liste = solutions_possibles(score - coup)
                for solution in liste:
                    resultat.append(solution + [score])  # correction
        return resultat
    ```

</div>
