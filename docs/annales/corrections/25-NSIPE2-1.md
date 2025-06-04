---
title: 25-NSIPE2-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIPE2-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIPE2.pdf){ .md-button }
[:material-arrow-right:](25-NSIPE2-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Ces quatre premiers mots ont un total de 2 + 9 + 4 + 2 = 17 caractères, donc le nombre d'espaces nécessaires est de 25 – 17 = **8**.

2. La seule proposition correcte est `An---algorithm---must--be`. En effet, la division euclidenne de 8 par 4 — 1 = 3 donne 2 espaces intermots, et un reste de 2 espaces à répartir de gauche à droite un par un.

3. 
```python
assert nb_caracteres + (nb_mots - 1) <= justification
```

4. 
```python hl_lines="7 13 15"
def ajout_espace(liste_mots, justification):
    nb_caracteres = sum([len(mot) for mot in liste_mots])
    nb_mots = len(liste_mots)
    assert nb_caracteres + (nb_mots - 1) <= justification
    nb_espace_total = justification - nb_caracteres
    if nb_mots == 1:
        return liste_mots[0] + ' ' * nb_espace_total
    else:
        q = nb_espace_total // (nb_mots - 1)
        r = nb_espace_total % (nb_mots - 1)
        reponse = liste_mots[0]
        for i in range(1, r + 1):
            reponse = reponse + ' ' * (q + 1) + liste_mots[i]
        for i in range(r + 1, nb_mots):
            reponse = reponse + ' ' * q + liste_mots[i]
        return reponse
```

5. On parcourt un à un les mots du texte et on les ajoute à la ligne en cours, espace inclus. Si l’ajout du mot suivant fait dépasser la largeur de justification, alors on revient à la ligne après le dernier mot ajouté, puis on continue avec les mots suivants.

6. 
```python
def affiche_justifie(liste_mots, decoupage, justification):
    for i, j in decoupage:
        ligne_justifiee = ajout_espace(liste_mots[i:j], justification)
        print(ligne_justifiee)
```

7. 
| Indice du mot de début | Indice du mot de fin + 1 | # mots | # caractères | # d’espaces supplémentaires pour atteindre 15 caractères |  Coût  |
| :--------------------: | :----------------------: | :----: | :----------: | :------------------------------------------------------: | :----: |
|           0            |            2             |   2    |      11      |                            3                             |   9    |
|           2            |            4             | **2**  |    **6**     |                          **8**                           | **64** |
|           4            |            7             | **3**  |    **8**     |                          **5**                           | **25** |
|           7            |            8             | **1**  |    **8**     |                          **7**                           | **49** |

    On vérifie bien que 9 + 64 + 25 + 49 = **147**.

8. 
```python
def cout(i, j, liste_mots, justification):
    nb_mots = j - i
    nb_caracteres = 0
    for i in range(i, j):
        nb_caracteres += len(liste_mots[i])
    nb_espaces = justification - (nb_caracteres + (nb_mots - 1))
    if nb_espaces < 0:
        return 1000000
    cout = nb_espaces * nb_espaces
    return cout
```

9. Une découpe du texte de $n$ mots peut être codée comme un mot binaire de $n - 1$ bits. Chaque mot — sauf le dernier — est associé un bit : 0 s’il n’y a pas de retour à la ligne après ce mot, 1 s’il y en a un. Tester toutes les découpes possibles revient donc à tester tous les mots binaires de $n-1$ bits, soit $2^{n-1}$ possibilités. Une recherche exhaustive aurait donc une complexité en temps d'au moins $O(2^n)$. Cette croissance exponentielle rend cette approche par recherche exhaustive trop lente dès que $n$ devient un peu trop grand.

10. La fonction `#!py cout` est appelée $\boxed{O(n^2)}$ fois.

11. `#!py cout_mini[i]` est calculé à partir des valeurs suivantes `#!py cout_mini[i + 1:]`. Plus précisément :
    
    $$
    \footnotesize
    \texttt{cout\_mini[$i$]} = \begin{cases}
        \ 0 & \text{si } i = n - 1 \\
        \ \min \left\{ \ \begin{align*}
            &c(i,\ n) \\ 
            &\texttt{cout\_mini[$i + 1$]} + c(i,\ i + 1) \\
            &\texttt{cout\_mini[$i + 2$]} + c(i,\ i + 2) \\
            &\cdots \\ 
            &\texttt{cout\_mini[$n - 1$]} + c(i,\ n - 1) \\
        \end{align*} \right. & \text{sinon}
    \end{cases} 
    $$

    Où $c(i, j)$ est `#!py cout(i, j, liste_mots, justification)`.

12. On remplace la dernière ligne de la fonction par :
    ```python
    return decoupage, cout_mini[0]
    ```

    En effet, `#!py cout_mini[i]` représente le coût inesthétique minimal en considérant tous les mots de `#!py liste_mots[i:]`.

</div>