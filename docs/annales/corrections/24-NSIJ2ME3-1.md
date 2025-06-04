---
title: 24-NSIJ2ME3-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2ME3-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2ME3.pdf){ .md-button }
[:material-arrow-right:](24-NSIJ2ME3-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. La variable `i` prend successivement les valeurs : 7, 8, 9 et enfin 10. `#!py f1(7)` **se termine** donc.

2. `#!py f1(-2)` **se termine** et **renvoie 10**.

3. Les 5 premières valeurs prises par `i` sont 12, 13, 14, 15 et 16. La fonction **ne se termine pas** car `i` n'atteindra jamais 10.

4. L'appel `#!py f(n)` **se termine** si et seulement si `n` est un entier inférieur ou égal à 10.

5. `#!py f2(4)` **se termine** et renvoie 4 + 2 + 0 = **6**.

6. `#!py f2(5)` **ne se termine pas** car le cas de base n’est jamais atteint. En effet, chaque appel diminue la valeur de 2 : `#!py f2(5)` appelle `#!py f2(3)` qui appelle `#!py f2(1)`, `#!py f2(-1)`, `#!py f2(-3)`, etc. sans jamais atteindre une condition d’arrêt, ce qui entraîne une récursion infinie.

7. L'appel `#!py f2(n)` se termine si et seulement si `n` est un **entier positif ou nul pair**.

8. 
```python
def infini(n):
    infini(0)
```

9. Si `#!py arret(code_paradoxe, code_paradoxe)` renvoie `#!py True` alors la prochaine instruction à être exécutée est `#!py infini(42)`, ainsi l'appel `#!py paradoxe(code_paradoxe)` **ne se termine pas**.

10. Sinon, si `#!py arret(code_paradoxe, code_paradoxe)` renvoie `#!py False` alors la prochaine instruction à être exécutée est `#!py return 0`, ainsi l'appel `#!py paradoxe(code_paradoxe)` **termine**.

11. On a supposé que la fonction `arret` existait, mais cette hypothèse conduit à une situation paradoxale décrite par les deux questions précédentes. En effet, lorsque `arret` affirme que `paradoxe` s’arrête, ce dernier ne s’arrête pas, et lorsque `arret` affirme que `paradoxe` ne s’arrête pas, il s’arrête. On aboutit donc à une contradiction. Par conséquent, notre hypothèse de départ est fausse : la fonction `arret` ne peut pas exister. Il s’agit d’un raisonnement par l’absurde.


</div>