---
title: Cheatsheet Python
icon: material/language-python
---

## Valeurs, types et variables

* Les **valeurs** manipulées par un programme sont caractérisées par leur **type**. Les types de base :

    | Type             | Terme anglais | Signification                | Exemples de valeur                        |
    | ---------------- | ------------- | ---------------------------- | ----------------------------------------- |
    | `#!python int  ` | *integer*     | Nombre entier                | `#!py 45` `#!py -255` `#!py 1998`         |
    | `#!python float` | *float*       | Nombre décimal (ou flottant) | `#!py 3.1412` `#!py -1.14152` `#!py 45.0` |
    | `#!python str  ` | *string*      | Chaîne de caractères (texte) | `#!py 'Bonjour'` `#!py "42"`              |
    | `#!python bool ` | *boolean*     | Booléen                      | `#!py True` `#!py False`                  |

* Si cela a du sens, on peut convertir une valeur vers un autre type :

    ```py
    >>> int(17.6)
    17
    >>> int('2')
    42
    >>> str(3.14)
    '3.14'
    ```

* Les opérateurs arithmétiques ont un sens différent suivant le type des opérandes :

    ```python
    >>> 2 + 2  # addition classique
    4
    >>> 'chat' + 'chien'  # concaténation
    'chatchien'
    >>> 'AY' * 5
    'AYAYAYAYAY'
    ```

* Une **variable** permet de stocker une valeur de n'importe quel **type** et est identifée par un **nom**.

    ```python
    toto = 10  # affection de la valeur 10 dans la variable nommée toto
    toto = 40  # une nouvelle affectation écrase l'ancienne valeur, toto vaut 40
    ```

* Lors de l’évaluation d’une expression contenant une variable, elle est remplacée par sa valeur courante :

    ```python
    x = 25 * 2    # l'affectation se déroule toujours en dernier
    print(x + 3)  # substitution : équivalent à print(50 + 3), affiche 53
    ```


* Le symbole `=` ne signifie pas « est égal à », c’est **l’opérateur d’affectation**.
  
* La première affectation à une variable est appelée **initialisation**. Si une variable n'est pas initialisée, elle ne contient aucune valeur courante. Si vous tentez de l'évaluer, Python vous retournera  l'erreur :

    <div class="red-text" style="font-family: var(--md-code-font); font-size: .85em; text-align: center;">NameError: name '...' is not defined</div>

    Une variable n’est pas une inconnue comme en mathématiques, elle contient toujours une valeur.

## Évaluation d'une expression

* Une ligne de code correspond à une **expression**, généralement composée de plusieurs opérations, que la machine **évalue**. Par exemple, pour l'expression :

    ```python
    x = 42 * 2 + 5
    ```

    La machine effectue trois opérations. Dans l'ordre, une multiplication, puis une addition, et enfin une affectation. Il est important de savoir visualiser le flot d'éxécution d'une ligne de code donnée.

## Conditions 

### Opérateurs de comparaison et logiques

### Les structures conditionnelles `#!py if elif else`

## Boucles

### Boucle non-bornée `#!py while`

### Boucle bornée `#!py for`

## Fonctions `#!py def`

## Conteneurs (structures de données)

### Tableaux dynamiques  `#!py list`

### Tuples `#!py tuple`

### Dictionnaires `#!py dict`

### Structures imbriquées 

## Modules `#!py import`

## Autres

### Assertion `#!py assert`
