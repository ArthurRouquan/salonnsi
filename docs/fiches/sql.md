---
title: SQL & BDD
icon: material/database
---

## Syntaxe SQL

* Récupérer des données d'une table :

    ```{.sql .no-copy}
    SELECT colonne, autre_colonne, ...
    FROM nom_table
    WHERE condition AND/OR autre_condition AND/OR ...
    ORDER BY colonne ASC/DESC
    ```

* Récupérer des données de plusieurs tables (jointure) :
  
    ```{.sql .no-copy}
    SELECT table1.colonne, table2.colonne, ...
    FROM table1
    JOIN table2 ON table1.id = table2.id
    JOIN table3 ON table2.id = table3.id
    ...
    WHERE condition(s)
    ORDER BY colonne ASC/DESC
    ```

* Ajouter une ligne :

    ```{.sql .no-copy}
    INSERT INTO nom_table
    VALUES (valeur1, valeur2, ...)
    ```

* Mettre à jour une ou des lignes :

    ```{.sql .no-copy}
    UPDATE nom_table
    SET colonne = valeur_ou_expression, 
        autre_colonne = valeur_ou_expression, 
        ...
    WHERE condition(s)
    ```

* Supprimer une ou des lignes :

    ```{.sql .no-copy}
    DELETE FROM nom_table
    WHERE condition(s)
    ```

## Le modèle relationnel

TODO