---
title: Python 1ère
icon: material/language-python
---

## Valeurs, types et variables

Les **valeurs** manipulées par un programme sont caractérisées par leur **type** :

<div class="center-table full-width-table" markdown>
| Type             | Terme anglais | Signification                | Exemples de valeur                        |
| ---------------- | ------------- | ---------------------------- | ----------------------------------------- |
| `#!python int  ` | *integer*     | Nombre entier                | `#!py 45` `#!py -255` `#!py 1998`         |
| `#!python float` | *float*       | Nombre décimal (ou flottant) | `#!py 3.1412` `#!py -1.14152` `#!py 45.0` |
| `#!python str  ` | *string*      | Chaîne de caractères (texte) | `#!py 'Bonjour'` `#!py "42"`              |
| `#!python bool ` | *boolean*     | Booléen                      | `#!py True` `#!py False`                  |
</div>

<div class="grid" markdown>
```py title="Conversion entre types"
>>> int(17.6)
17
>>> float('42')
42.0
>>> str(3.14)
'3.14'
```

```python title="Chaque type est manipulé différemment"
>>> 2 + 3  # addition classique
5
>>> 'chat' + 'chien'  # concaténation
'chatchien'
>>> 'AH' * 5  # répétition
'AHAHAHAHAH'
```
</div>

Une **variable** permet de stocker une et une seule valeur :

```python
toto = 10    # affection de la valeur 10 dans la variable nommée toto
toto = 40    # une nouvelle affectation écrase la valeur courante, toto contient 40
x = 25 * 2   # l'affectation se déroule toujours en dernier
```

Lors de son évaluation, elle est remplacée par sa valeur courante :

```python
print(toto)   # Python remplace toto par sa valeur courante : affiche 40
print(x + 3)  # affiche 53
```

Il est confortable d'utiliser **la syntaxe abrégée** pour modifier relativement une variable :

<div class="grid" markdown>
```python title="Syntaxe classique"
x = 52

x = x + 1  # x contient 53
x = x * 2  # x contient 106
x = x - 6  # x contient 100
x = x / 4  # x contient 25.0
```

```python title="Syntaxe abrégée"
x = 52

x += 1 
x *= 2  
x -= 6  
x /= 4  
```
</div>

??? info "Précisions supplémentaires"

    * Le nom d'une variable ne peux pas contenir d'espaces ou commencer par un chiffre.

    * Le symbole `=` ne signifie pas « est égal à », c'est **l'opérateur d'affectation**. Des vieux langages utlisent plutôt `←` mais ce symbole n'est pas immédiatement disponible sur un clavier moderne.

    * Une variable n'est pas une inconnue comme en mathématiques, **une variable contient toujours une valeur courante** au moment de l'exécution !

    * La première affectation à une variable est appelée **initialisation**. Si une variable n'est pas initialisée, elle ne contient aucune valeur courante. Si vous tentez de l'évaluer, Python donnera l'erreur :

        <center>
        <span class="red-text hl-red" style="font-family: var(--md-code-font); font-size: .85em;">NameError: name '...' is not defined</span>
        </center>

    * On dit qu'on **incrémente** une variable si on lui ajoute 1 (`#!py x += 1`) et qu'on la **décremente** si on lui soustrait 1.

<!-- ## Évaluation d'une expression

* Une ligne de code correspond à une **expression**, généralement composée de plusieurs opérations, que la machine **évalue**. Par exemple, pour l'expression :

    ```python
    x = 42 * 2 + 5
    ```

    La machine effectue trois opérations. Dans l'ordre, une multiplication, puis une addition, et enfin une affectation. Il est important de savoir visualiser le flot d'éxécution d'une ligne de code donnée. -->




## Conditions 

Les opérateurs de comparaison permettent de comparer des valeurs entre-elles :

### Opérateurs de comparaison et logiques

### Les structures conditionnelles `#!py if elif else`

## Boucles

### Boucle non-bornée `#!py while`

### Boucle bornée `#!py for`

```python
for variable_d_iteration
```

## Fonctions `#!py def`

## Structures de données

### Tableaux dynamiques  `#!py list`

```python
tab = [42, 37, 88, 13, 96]

tab[0]  # renvoie 42
tab[2]  # renvoie 88
tab[-1] # renvoie 96

tab[0] = 'X'  # ['X', 37, 88, 13, 96]

tab.append(96) 
tab.remove(88)
tab.pop(0)

for valeur in tab:  # parcours par élément
    print(valeur)

for i in range(len(tab)):  # parcours par indice
    print(i, tab[i])
```