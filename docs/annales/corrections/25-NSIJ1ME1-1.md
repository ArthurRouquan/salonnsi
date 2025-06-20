---
title: 25-NSIJ1ME1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1ME1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1ME1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ1ME1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. L'attribut `num_ser` ne permet pas d'identifier de manière unique chaque enregistrement de la relation `inventaire`. Par exemple, la valeur 81757532 apparaît deux fois dans l'extrait de la table, ce numéro de série étant utilisé par coïncidence par deux fabriquants différents. Cet attribut ne peut donc pas être utilisé comme clé primaire.

2. 
| `marque` |     `modele`     |
| :------: | :--------------: |
|  Gibson  | Les Paul Goldtop |
|  Fender  |   Stratocaster   |

3. 
```sql
SELECT annee
FROM inventaire
WHERE modele = 'Les Paul Standard';
```

4. 
```sql
SELECT modele
FROM inventaire
WHERE marque = 'Gibson'
ORDER BY annee;
```

5. 
```sql
UPDATE inventaire
SET annee = 1957
WHERE id = 1;
```

6. Afin de respecter la contrainte d'intégrité référentielle, les tables doivent être créees dans l'ordre : `marque`, puis `modele` et enfin `guitare`.

7. 
```sql
SELECT num_ser, annee
FROM guitare
JOIN modele ON modele.id = guitare.id_modele
WHERE nom = 'Les Paul Standard';
```

8. 
```sql
DELETE FROM guitare
WHERE id = 3;
```

9. 
```sql
INSERT INTO marque  VALUES (3, 'BC Rich');
INSERT INTO modele  VALUES (5, 'Mockingbird', 3);
INSERT INTO guitare VALUES (9, 5, 1992, '92R', 5000);
```

10. 
```sql
SELECT SUM(prix)
FROM guitare
JOIN modele ON modele.id = guitare.id_modele
WHERE nom = 'Stratocaster';
```

</div>
