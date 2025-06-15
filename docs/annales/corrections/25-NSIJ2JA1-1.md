---
title: 25-NSIJ2JA1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ2JA1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ2JA1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ2JA1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
self.jour = jour
self.mois = mois
self.annee = annee
```

2. L'instance `d` représente le **1er mai 2000**.

3. `#!py d = Date(19, 6, 2024)`

4. 
```python
def get_annee(self):
    return self.annee
```

5. 
```python
def set_mois(self, mois):
    self.mois = mois
```

6. 
```python
if self.est_bissextile():
    self.nb_jours_par_mois[1] = 29
```

7. 
```python
def est_bissextile(self):
    a = self.annee
    return (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0)
```

8. Les instructions affichent ici `#!py 79`.

9. 
```python
def nb_jours_restants(self):
    j = 365
    if self.est_bissextile():
        j = 366
    return j - self.nb_jours_passes()
```

10.  
```python
>>> d1.nb_jours_depuis(d2)
0
>>> d1.nb_jours_depuis(d3)
-1
>>> d1.nb_jours_depuis(d4)
-1
>>> d1.nb_jours_depuis(d5)
731  # (365 - 166) + 365 + (166 + 1)
```

1.  
```python
def timestamp(self):
    d = Date(1, 1, 1970)
    return self.nb_jours_depuis(d) * 24 * 3600
```

</div>

