---
title: 25-NSIJ1JA1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1JA1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1JA1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ1JA1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. À la fin de l'exécution du programme, la variable `x` contient **0** et `y` contient **20**.

2. Un programme Python est une suite de caractères enregistrée dans un simple fichier textuel d'extension `.py`. Il peut donc être vu comme une simple chaîne de caractères.

3. Les programme **3 et 5 se terminent**. Les programmes **4 et 6 ne se terminent pas**.

4. La fonction `arret_essai1` renvoie `True` si le programme donné en paramètre s'arrête. Dans le cas où ce programme ne s'arrête pas, alors `arret_essai1` ne s'arrête pas non plus. **Elle ne permet donc pas de répondre au problème initial**, car elle ne renvoie pas `False` quand le problème ne s'arrête pas.

5. L'algorithme de Boyer-Moore permet de rechercher efficacement un motif dans un texte. Il repose sur une comparaison **à l'envers** des caractères du motif avec ceux du texte et sur la construction au préalable, à partir du motif, de **tables de décalage**. Ces tables indiquent, selon les caractères rencontrés, de combien on peut avancer au mieux la fenêtre de recherche sans risquer de manquer une occurrence, ce qui permet d'éviter de nombreuses comparaisons inutiles.

6. 
```python
def arret_essai2(programme):
    return not rechercher('while', programme)
```

7. * Un programme peut ne pas s'arrêter et pourtant ne pas contenir de boucle `#!py while`. Un exemple notable :

        ```python
        def f():
            f()
        f()
        ```

        Cependant, ce programme « théorique » se terminera en pratique en renvoyant l'erreur `RecursionError` après un trop grand nombre d'appels récursifs.

    * Et un programme peut s'arrêter et contenir une boucle `#!py while`, comme les programmes 3 et 5 de l'exercice.

8. 
```python
def terminaison_inverse(programme):
    if arret(programme):
        boucle_infinie()
```

9. * Si `programme_paradoxal` termine, alors `terminaison_inverse(programme_paradoxal)` termine aussi. Par définition de la fonction `terminaison_inverse`, cela implique que `programme_paradoxal` ne termine pas : contradiction.
    
    * Inversement, s'il ne termine pas, alors `terminaison_inverse(programme_paradoxal)` ne termine pas non plus, ce qui implique que `programme_paradoxal` termine : contradiction.
    
    Dans tous les cas, on aboutit à une contradiction : **`programme_paradoxal` ne peut ni terminer ni ne pas terminer.**

10. Cette contradiction montre que l'hypothèse de départ, l'existence de la fonction `arret`, est fausse. **La fonction `arret` ne peut pas exister.**

11. **Non, cette impossibilité n’est pas due aux limitations du langage Python.** Le problème de l'arrêt est indécidable pour tout langage Turing-complet.


</div>
