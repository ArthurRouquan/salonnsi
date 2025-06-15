---
title: 24-NSIJ2JA1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2JA1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2JA1.pdf){ .md-button }
[:material-arrow-right:](24-NSIJ2JA1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Pour être strictement majoritaire dans une liste de taille 10, un élément doit apparaître au moins $\left\lceil \frac{10}{2} \right\rceil = \boxed{6}$ fois.

2. 
```python
def effectif(val, lst):
    compteur = 0
    for valeur in lst:
        if valeur == val:
            compteur += 1
    return compteur
```

3. La fonction `effectif` effectue une comparaison par élément. Puisqu'il y a 9 éléments ici, elle effectue **9** comparaisons.

4. 
```python
def majo_abs1(lst):
	seuil = len(lst) // 2
	for valeur in lst:
		if effectif(valeur, lst) > seuil:
			return valeur
	return None
```

5. Dans le pire des cas où il n'y a pas d'élément strictement majoritaire, cet appel effectue 9 × 9 + 9 = **90** comparaisons.

6. 
```python hl_lines="3 4 5 7"
def eff_dico(lst):
	dico_sortie = {}
	for val in lst:
		if val in dico_sortie:
			dico_sortie[val] += 1
		else:
			dico_sortie[val] = 1
	return dico_sortie
```

7. 
```python
def majo_abs2(lst):
	compteurs = eff_dico(lst)
	seuil = len(lst) // 2
	for val in compteurs:
		if compteurs[val] > seuil:
			return val
	return None
```

8. Si la liste possède un seul élément alors `lst[0]` est absolument majoritaire.

9. Si ni `lst1` ni `lst2` n'admet d'élément absolument majoritaire, dans le cas plus extrême, un élément apparaît au plus $\left\lfloor \frac{n}{4} \right\rfloor$ fois dans les deux-sous listes. Ainsi dans la liste initiale `lst`, cet élément apparaît au plus $2 \times \left\lfloor \frac{n}{4} \right\rfloor \leq \left\lfloor \frac{n}{2} \right\rfloor$ fois. Or, le seuil pour qu'il soit strictement majoritaire est d'au moins $\left\lfloor \frac{n}{2} \right\rfloor + 1$. Donc `lst` n'admet pas d'élément strictement majoritaire.

10. On compte le nombre d'occurence de cet élément `maj1` dans la liste initiale `lst`, s'il est strictement supérieur à $\left\lfloor \frac{n}{2} \right\rfloor$ alors il est strictement majoritaire.

11. 
```python hl_lines="4 11 13 15 17"
def majo_abs3(lst):
	n = len(lst)
	if n == 1:
		return lst[0]
	else:
		lst_g = lst[:n//2]
		lst_d = lst[n//2:]
		maj_g = majo_abs3(lst_g)
		maj_d = majo_abs3(lst_d)
		if maj_g is not None:
			eff = effectif(maj_g, lst)
			if eff > n / 2:
				return maj_g
		if maj_d is not None:
			eff = effectif(maj_d, lst)
			if eff > n / 2:
				return maj_d
	return None
```


</div>
