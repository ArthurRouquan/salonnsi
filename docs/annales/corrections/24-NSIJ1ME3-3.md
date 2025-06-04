---
title: 24-NSIJ1ME3-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ1ME3-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ1ME3-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ1ME3.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<style>
@font-face {
    font-family: "Noto Sans Mayan Numerals";
    src: url('/assets/NotoSansMayanNumerals-Regular.ttf') format('truetype');
}

.maya {
    font-family: "Noto Sans Mayan Numerals", monospace;
}
</style>


<div class="circle-ol" markdown>

1. 
| Étage |        Écriture Maya        | Valeur du chiffre de l'étage | Valeur dans la conversion |
| :---: | :-------------------------: | :--------------------------: | :-----------------------: |
|   3   | <span class="maya">𝋨</span> |             $8$              |   $8 \cdot 20^2 = 3200$   |
|   2   | <span class="maya">𝋫</span> |             $11$             |   $11 \cdot 20^1 = 220$   |
|   1   | <span class="maya">𝋯</span> |             $15$             |   $15 \cdot 20^0 = 15$    |

2. En sommant les valeurs dans la conversion, le nombre représente bien $3200 + 220 + 15 = \boxed{3435}$.

3. 
```python
M = Maya()
M.ajouter([0, 0, 3])
M.ajouter([0, 1, 2])
M.ajouter([0, 3, 1])
```

4. 
```python
def nbEtage(self):
	return len(self.nombre)
```

5. 
```python
def valeurChiffre(L):
	_, nb_points, nb_traits = L
	return nb_points + 5 * nb_traits
```
6. 
```python hl_lines="2 4 5 7"
def MayaToDec(self):
	coeff = 20 ** (self.nbEtages() - 1)
	ch_Dec = 0
	while not self.estVide():
		ch_Maya = self.retirer()
		ch_Dec = ch_Dec + valeurChiffre(ch_Maya) * coeff
		coeff = coeff // 20
	return ch_Dec
```

7. 
```python
def decompChiffre(n):
	if n == 0:
		return [1, 0, 0]
	return [0, n % 5, n // 5]
```

8. 
```python
def DecToMaya(n):
	M = Maya()
	for chiffre in DecToVige(n):
		M.ajouter(decompChiffre(chiffre))
	return M
```

9. 
```python
def multiplie(self):
    M = Maya()
    M.nombre = [[1, 0, 0]] + self.nombre
	return M
```

1.  La fonction `mystere` effectue l'addition de deux chiffres Maya et d'une retenue et renvoie le résultat.
    
    * `#!py mystere([0, 1, 1], [0, 3, 1], 0)` renvoie `#!py ([0, 4, 2], 0)`.

    * `#!py mystere([0, 1, 1], [0, 4, 2], 0)` renvoie `#!py ([1, 0, 0], 1)`.

    Le programme présenté est truffé d'erreurs :

    ```python
    def mystere(m1, m2, ret):
        c = 0
        p = (m1[1] + m2[1] + ret) % 5
        if m1[1] + m2[1] + ret >= 5:  # correction indentation
            ret = 1
        else:
            ret = 0
        t = (m1[2] + m2[2] + ret) % 4
        if m1[2] + m2[2] + ret < 4:
            ret = 0
        else:
            ret = 1
        if (m1[0] == 1 and m2[0] == 1) or (p + t == 0 and ret == 1):  # correction
            c = 1
        return ([c, p, t], ret)
    ```

11. 
```python
def somme(self, maya2):
    assert self.nbEtages() == maya2.nbEtages()  # supposé par la consigne
    retenue = 0
    for i in range(self.nbEtages()):
        self.nombre[i], retenue = mystere(self.nombre[i], maya2.nombre[i], retenue)
    if retenue == 1:
        self.ajouter([0, 1, 0])
```

</div>
