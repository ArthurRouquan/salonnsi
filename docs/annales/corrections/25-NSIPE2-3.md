---
title: 25-NSIPE2-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIPE2-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIPE2-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIPE2.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. `#!py a4.duree = 12`

2. L'expression `#!py a2.voisines[2][1]` renvoie `#!py 4`.

3. La ligne 7 renseigne pour l’attraction « Train fantôme » (`a3`) la liste de ses attractions voisines ainsi que leur distance (en minutes) respective :
    * `a1` (Grand huit) à 5 minutes
    * `a2` (Petits chevaux) à 3 minutes
    * `a4` (Grande roue) à 6 minutes

4. `#!py a4.voisines = [(a2, 4), (a3, 6)]`

5. On peut supposer que le temps de trajet entre deux attractions est le même dans les deux sens. Il n’est donc pas utile de modéliser cette situation avec un graphe orienté, sauf en cas d’asymétrie dans les trajets, par exemple s’il existe des pentes.

6. La durée de la balade est la somme de la durée totale des attractions (11 + 6 + 9 = 26) et des trajets intermédiaires (7 + 3 = 10), soit 26 + 10 = **36 minutes**.

7. Il n'y a pas d'arête entre `a1` (Grand huit) et `a4` (Grande roue), donc de trajet entre ces deux attractions, ce n'est pas une balade valide.

8. 
```python
def sont_voisines(a, b):
    for voisine, duree in a.voisines:
        if b == voisine:
            return True
    return False
```

9. 
```python
def est_balade(attractions):
    for i in range(len(attractions) - 1):
        if not sont_voisines(attractions[i], attractions[i + 1]):
            return False
    return True
```

10. La fonction `parcours` repose sur un **parcours en profondeur** récursif

11. Après exécution, le tableau `balade` contient `#!py [a4, a2, a1, a3]`.

12. Après exécution, le tableau `tableau` contient `#!py [a3, a1, a2, None]`.

13. La variable `deja_vues` est un dictionnaire dont les clés sont les sommets (attractions) visités lors du parcours, afin d'éviter de les revisiter. Puisque la valeur associée à chaque clé n’a pas d’importance, on aurait tout aussi bien pu utiliser un ensemble (`#!py set`) à la place.

14. Une clé primaire est un ou plusieurs attributs qui identifient de manière unique un enregistrement d'une relation. Une clé étrangère est un ou plusieurs attributs qui fait référence à une clé primaire d'une autre relation.

15. 
```sql
SELECT DISTINCT nom, prenom
FROM visiteur
WHERE date = '2025-01-11';
```

16. 
```sql
SELECT SUM(prix)
FROM visiteur
JOIN photo ON photo.id_visiteur = visiteur.id
WHERE visiteur.prenom = 'Alan' 
    AND visiteur.nom = 'Turing' 
    AND visiteur.date >= '2024-01-01'
    AND visiteur.date < '2025-01-01'
```

17. La requête cherche à identifier le prénom et le nom des visiteurs présents sur une photo prise sur la grande roue le 26 juillet 2024 à 12h34.

18. On peut ajouter à la base de données :
    
    * La table `format` qui décrit les différents formats et supports proposés (A5, A6, poster, porte-clé, etc.), dont le schéma relationnel serait :
        <center><tt style="font-size: .8em">format(<u>id</u>: INT, nom: TEXT, prix: FLOAT)</tt></center>

    * La table `commande` qui modélise les différentes commandes :
        <center><tt style="font-size: .8em">commande(<u>id</u>: INT, #id_photo: INT, #id_format: INT, quantite: INT)</tt></center>

    La table `photo` n’a alors plus besoin de l'attribut <tt>prix</tt>.

</div>
