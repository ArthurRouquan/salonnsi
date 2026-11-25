---
title: Seconde SNT
---

# Seconde SNT

## TP

/// html | div.check-list
* :lucide-circle-check:{ .done } [TP Capytale – Premier pas en Python](https://capytale2.ac-paris.fr/web/c/557a-11939519/atr)
* :lucide-circle-check:{ .done } [Jeu – Exécubot](https://execubot.fr)
* :lucide-circle-check:{ .done } [TP Capytale – Répéter du code avec la boucle `#!py while`](https://capytale2.ac-paris.fr/web/c/c121-12730610/atr)
* :lucide-circle: [TP Capytale – Le paradoxe du duc de Toscane](https://capytale2.ac-paris.fr/web/c/2500-13124590/atr)
///

## Mémo Python

L'instruction `#!py print` permet d'**afficher** des valeurs :

```python
print("Un cercle de rayon 7 a pour périmètre :")
print(2 * 7 * 3.14)  # 3.14 : un point, pas une virgule
```

```console
Un cercle de rayon 7 a pour périmètre :
43.96
```

---

Une **variable** permet de stocker une valeur :

```python
x = 42  # on met 42 dans une variable nommée x
x = 90  # on met 90 dans x (écrase la valeur précédente)
print(x * 2)  # x est remplacé par sa valeur courante (90)
```

```console
180
```

```python
age = 29
age = age + 1  # on calcule à droite (29 + 1) puis on range le résultat dans age
print("J'ai", age, "ans.")  # plusieurs valeurs séparées par des virgules
```

```console
J'ai 30 ans.
```

---

Une boucle `#!py while` permet de **répéter** un bloc de code (décalé) **tant que** la condition est vraie :

//// html | div.grid-aside
/// html | div
```python
compteur = 0
while compteur < 5:  # tant que ... on répète :
    print(compteur)
    compteur = compteur + 1
print("Fin !")
```

```console
0
1
2
3
4
Fin !
```
///
/// html | div
| Python    | Maths      |
| :-------: | :--------: |
| `#!py <`  | $<$        |
| `#!py >`  | $>$        |
| `#!py <=` | $\leq$     |
| `#!py >=` | $\geq$     |
| `#!py ==` | $=$        |
| `#!py !=` | $\neq$     |
///
////

---

L'instruction `#!py if` permet d'exécuter un bloc de code (décalé) **si** la condition est vraie :

```python
age = 20
if age >= 18:  # si ... alors :
    print("Tu es majeur.")
    print("Tu peux voter.")
print("Fin !")
```

```console
Tu es majeur.
Tu peux voter.
Fin !
```
