---
title: 25-NSIJ1ME3-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ1ME3-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1ME3-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1ME3.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Une clé primaire est un ou plusieurs attributs qui identifient de manière **unique** un enregistrement d'une relation.

2. Plusieurs papillons partagent le même habitat, par exemple `Prairies` dans l'extrait donné. Cet attribut n'étant pas unique, il ne peut constituer une clé primaire. 

3. 
|  `taille`  |
| :-----: |
| 85 |

4. 
```sql
UPDATE papillon
SET taille = 50
WHERE nomCo = 'Petite Tortue';
```

5. 
```sql
SELECT nomCo
FROM papillon
WHERE habitat = 'Prairies' AND taille < 55;
```

6. 
|  `nomSc`  |
| :-----: |
| Papaver rhoeas |

7. 
```sql
SELECT papillon.nomCo, plante.nomCo
FROM papillon
JOIN plante ON papillon.habitat = plante.habitat
WHERE papillon.taille < 55;
```

8. 
|  `papillon.nomCo`  | `plante.nomCo` |
| :-----: | :-----: |
| Paon-du-jour | Lilas |

9. 
```sql
SELECT papillon.nomCo
FROM papillon
JOIN plante ON papillon.zone = plante.zone
WHERE plante.nomCo = 'Coquelicot';
```

10. 
```py hl_lines="4 5 7 9"
def tri_collec(collec):
    for i in range(1, len(collec)):
        pap = collec[i]
        j = i
        while j > 0 and collec[j - 1]["taille"] > pap["taille"] :
            collec[j] = collec[j - 1]
            j = j - 1
        collec[j] = pap
    return collec
```

11. Il s'agit d'un **tri par insertion**.

12. Le coût en temps de ce tri, dans le pire des cas, est **quadratique**.

13. Soit une nouvelle donnée à classifier, l'algorithme des $k$ plus proches voisins lui attribue la classe majoritaire des $k$ plus proches données (en distance) déjà classifiées.

14. 
```py hl_lines="4 6"
def recherche_seq(seq, chaine):
    for i in range(len(chaine) - len(seq) + 1):
        j = 0
        while j < len(seq) and seq[j] == chaine[i + j]:
            j += 1
        if j == len(seq) :
            return i
    return -1
```

15. À chaque étape, contrairement à la recherche linéaire qui décale le motif d'un seul caractère, l'algorithme BMH effectue un plus grand saut en fonction du dernier caractère de la portion de texte considéré. Cette longueur de saut est précalculé en amont, à partir du motif, dans une **table de décalage**. Cette stratégie réduit considérablement le nombre de comparaisons nécessaires, rendant l'algorithme bien plus rapide qu'une recherche linéaire.

</div>
