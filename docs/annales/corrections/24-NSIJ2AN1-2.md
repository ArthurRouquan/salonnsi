---
title: 24-NSIJ2AN1-2
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ2AN1-1.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2AN1-2.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2AN1.pdf){ .md-button }
[:material-arrow-right:](24-NSIJ2AN1-3.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
| `nom_client` | `prenom_client` |
| :----------: | :-------------: |
|    Dufour    |      Marc       |
|    Martin    |     Sophie      |

2. 
```sql
SELECT nom_medic
FROM medicament
WHERE prix < 3;
```

3. 
```sql
INSERT INTO client
VALUES (3, 'Nathalie', 'Durand', '269054958815780')
```

4. Dans la table `ordonnance`, les deux clés étrangères sont les attributs :
 
    * `id_client` qui permet d'établir un lien avec la table `client`,
    * et `id_medic` qui permet d'établir un lien avec la table `medicament`.

5. D'après l'ordonnance fournie, la patiente doit prendre sur la totalité du traitement :

    * au maximum 3 × 2 = 6 comprimés de paracétamol, soit **1 boîte** de 8.
    * 7 × 4 = 28 comprimés d'acide ascorbique, soit **3 boîtes** de 10.

6. 
```sql
UPDATE medicament
SET quantite = quantite - 3
WHERE nom_medic = 'Acide ascorbique';
```

7. Le coût total est de (1 × 3.50) + (3 × 5.50) = **20€**.

8. 
```sql
SELECT nom_medic
FROM medicament
JOIN ordonnance ON ordonnance.id_medic = medicament.id_medic
WHERE id_ordo = 6;
```


</div>
