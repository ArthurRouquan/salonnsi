---
title: 25-NSIJ2PO1-2
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ2PO1-1.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ2PO1-2.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ2PO1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ2PO1-3.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```sql
SELECT nom FROM champignon
WHERE lamelle = 'oui' AND couleur = 'orange';
```

2. 
```sql
SELECT nom FROM champignon
WHERE chapeau_min <= 15 AND 15 <= chapeau_max AND pied_max = 0;
```

3. La clé étrangère de la table `champignon` est `id_ordre` qui fait référence à l'attribut `id` de la table `ordre`.

4. 
```sql
SELECT champignon.nom
FROM champignon
JOIN ordre ON ordre.id = champignon.id_ordre
WHERE classe = 'agaricomycètes';
```

5. 
```sql
INSERT INTO champignon
VALUES (56, 'amanite solitaire', 4, 'oui', 'blanc', 6, 20, 4, 10); 
```


</div>
