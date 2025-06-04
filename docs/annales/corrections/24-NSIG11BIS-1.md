---
title: 24-NSIG11BIS-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIG11BIS-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIG11BIS.pdf){ .md-button }
[:material-arrow-right:](24-NSIG11BIS-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```
10
1  9
2  8
1  2  7
1  3  6
2  3  5
1  2  3  4
1  2  3  4  ◀─── État stable
...
```

2. 
```
9
1  8 
2  7 
1  2  6 
1  3  5 
2  3  4     
1  2  3  3  ◀──┐ 
1  2  2  4     │ Cycle
1  1  3  4     │
2  3  4     ───┘
...
```

3. 
```python hl_lines="2 9"
def suivante(self):
    self.precedents.append(self.courant)
    valeurs = self.courant
    suiv = [len(valeurs)]
    for v in valeurs:
        if v > 1:
            suiv.append(v - 1)
    suiv.sort()
    self.courant = suiv
```

4. 
```python
def est_stable(self):
    return self.precedents and self.courant == self.precedents[-1]
```

5. 
```python
def partie_stable(nb_cartes):
    partie = Partie(nb_cartes)
    while True:
        partie.suivante()
        if partie.est_stable():
            return True
        if partie.est_cyclique():
            return False
```

6. 
```python
assert partie_stable(1)
assert partie_stable(10)
assert partie_stable(15)
assert not partie_stable(12)
assert not partie_stable(9)
```

7. On souhaite ici effectuer **la dernière insertion du tri par insertion** en $O(n)$ car la séquence est déjà triée à l'exception du dernier élément.


</div>
