---
title: 24-NSIJ1ME3-1
---

<div class="circle-ol" markdown>

1. L’attribut `CP` peut être de type `#!sql INT` (entier) ou `#!sql TEXT` si l’on souhaite conserver les éventuels zéros initiaux des codes postaux.

2. Cette requête renvoie une **erreur** car les noms d'attributs ne doivent pas être entourés de guillemets simples en SQL.

3. L'attribut `Telephone` peut être utilisé comme clé primaire s'il est **unique** pour chaque enregistrement, c'est-à-dire **si chaque agence a un numéro de téléphone différent**.

4. Le schéma relationnel de cette nouvelle table :

    <center><tt style="font-size: .8em">couple_voitures_agences(#<u>id_voiture</u>: INT, #id_agence: INT)</tt></center>

    On suppose que chaque véhicule de location appartient à une unique agence.

5. 
```sql
INSERT INTO couple_voitures_agences
VALUES (2, 5);
```

6. 
```sql
UPDATE couple_voitures_agences
SET id_agence = 2
WHERE id_voiture = 2;
```

7. 
```sql
SELECT type, marque, Agence
FROM couple_voitures_agences AS Couples
JOIN Voitures ON Voitures.id_voiture = Couples.id_voiture
JOIN Agences  ON Agences.id_agence   = Couples.id_agence
```

8. En supposant l'existance d'une fonction `dernier_id_voiture` qui renvoie l'identifiant auto-généré de la dernière voiture ajouté :

    ```python
    def insert_voiture(liste_valeurs, id_agence):
        valeurs = "'{}', '{}', {}, {}, '{}', '{}'".format(*liste_valeurs)
        r1 = execute_requete_insert(f'INSERT INTO Voitures VALUES ({valeurs})')
        id_voiture = dernier_id_voiture()
        r2 = execute_requete_insert(f'INSERT INTO couple_voitures_agences VALUES ({id_voiture}, {id_agence})')
        return r1 and r2
    ```

9. Il est nécessaire de vérifier que `liste_valeurs` correspond bien aux attributs de la table `Voitures` et que `id_agence` existe au préalable dans la table `Agences`.

</div>
