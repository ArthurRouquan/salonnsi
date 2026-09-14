

# Exercices

## Somme d'un tableau

Écrire une fonction `somme` qui prend en paramètre un tableau de nombres et renvoie la somme de ses valeurs. Si la liste est vide, la fonction renvoie `#!py 0`. Par exemple :

```python
>>> somme([10, 20, 37])
67
>>> somme([])
0
```

!!! warning ""
    La fonction Python `#!py sum` n'est pas autorisée.

??? tip "Aide" 
    L'idée est d'initialiser une variable `total` à `#!py 0` puis de parcourir les valeurs du tableau. Pour chaque valeur, on l'ajoute à la variable `total`. Après le parcours, la variable `total` a bien accumulé toutes les valeurs : on la renvoie.

