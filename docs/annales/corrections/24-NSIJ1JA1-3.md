---
title: 24-NSIJ1JA1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ1JA1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ1JA1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ1JA1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
personneA = Personne(112, 'LESIEUR', 'Isabelle', 1982, 2005)
```

2. 
```python
personneA.num_badge
```

3. 
```python
def annee_anciennete(self):
    return 2024 - self.annee_entree  # dépend de l'année courante
```

4. 
```python
def ajouter(self, personne):
    self.liste.append(personne)
```

5. 
```python
def effectif(self):
    return len(self.liste)
```

6. 
```python
def donne_nom(self,  num):
for elt in self.liste:
    if elt.num_badge == num:
        return elt.nom
return None
```

7. 
```python
def nb_personne_honneur(self,  annee_ceremonie):
    compteur = 0
    for personne in self.liste:
        if annee_ceremonie - personne.annee_entree == 10:
            compteur += 1
    return compteur
```

8. 
```python
def plus_anciens(self):
    annee = self.liste[0].annee_entree
    for personne in self.liste:
        if personne.annee_entree < annee:
            annee = personne.annee_entree
    return [p for p in self.liste if p.annee_entree == annee]
```

9. La requête renvoie **le nom et prénom des personnes qui travaillent dans le centre numéro 2**.

10.  
```sql
UPDATE Personnel
SET num_centre = 3
WHERE num_badge = 135;
```

11. Cela permet d'éviter **la redondances de données**.

12. La clé étrangère `num_centre` de la table `Personnel` fait référence à la clé primaire `num` dans la table `Centre`, ce qui les met en relation.

13. 
```sql
SELECT p.nom
FROM Personnel AS p
JOIN Centre    AS c ON p.num_centre = c.num
WHERE p.annee_debut >= 2015
    AND p.annee_debut <= 2020
    AND c.ville = 'Lille';
```

14. Cette requête renvoie une erreur car elle tente de supprimer un centre (`Normandie`) qui est encore référencé par des enregistrements dans la table `Personnel` via la clé étrangère `num_centre`. **Elle viole donc la contrainte d'intégrité référentielle**, qui impose que toute valeur de clé étrangère corresponde à une clé primaire existante. Pour corriger cela, il faut d’abord réaffecter les employés du centre `Normandie` vers un autre centre, avant de pouvoir supprimer ce centre.

</div>
