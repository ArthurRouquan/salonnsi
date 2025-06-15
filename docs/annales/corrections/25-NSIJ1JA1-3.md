---
title: 25-NSIJ1JA1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ1JA1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1JA1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1JA1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```sql
SELECT "id-kimono"
FROM location
WHERE fin = '';
```

    !!! info "Remarque"
        Le sujet utilise un tiret `-` dans le nom des attributs à la place du traditionnel tiret bas `_`. Cela oblige à entourer le nom avec des guillemets doubles pour éviter que le tiret ne soit interprété comme une soustraction.

2. 
```sql
SELECT COUNT(*)
FROM kimono
WHERE "taille-kimono" = 130;
```

3. 
```sql
SELECT nom, prenom
FROM adherent
JOIN location ON location."numero-licence" = adherent."numero-licence"
WHERE "id-kimono" = 42 AND fin = '';
```

4. 
```sql
UPDATE adherent
SET "taille-adherent" = "taille-adherent" + 10
WHERE "taille-adherent" < 160;
```

5. 
```sql
DELETE FROM location WHERE "id-kimono" = 25;
DELETE FROM kimono   WHERE "id-kimono" = 25;
```

6. Son numéro de licence serait possiblement **M12102021NIRRE01**.

7. Cet adhérent est né le **23/09/1974** et a un nom commençant par MARTI, probablement **MARTIN**.

8. L'expression `#!py tab_adherents[1]['prenom']` renvoie **`#!py 'STEPHANIE'`**.

9. La valeur `#!py 'F03071997DUPON01'` est obtenue grâce à l'instruction **`#!py tab_adherents[0]['numero-licence']`**.

10. 
```python
def nombre_adherents(table, annee):
    compteur = 0
    for adherent in table:
        if adherent['annee'] == annee:
            compteur += 1
    return compteur
```

1.  
```python
def adherent_plus_age(table):
    annee = '2024'
    for adherent in table:
        if adherent['annee'] < annee:
            annee = adherent['annee']
    return [a for a in table if a['annee'] == annee]
```

</div>