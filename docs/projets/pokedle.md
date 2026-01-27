---
icon: custom/pokeball
---

# Pokédle

## Introduction

Une **API** (*Application Programming Interface*) web, c'est comme un serveur dans un restaurant :

* Vous (le **client**) : Vous passez une commande (une **requête**).
    
* L'API (le **serveur**) : Elle prend votre commande, va en cuisine, et vous ramène le plat (la **réponse** / les données).


On se propose d'utiliser l'API Web [Tyradex](https://tyradex.app/), une base de données gratuite (et française !) qui contient tout sur les Pokémon. Elle nous permettra de coder un jeu de type [Pokédle](https://pokedle.net/classic) en Python.

## Analyse des données à la main

Avant de coder, regardons à quoi ressemble une réponse de l'API : 

<center markdown>
[https://tyradex.app/api/v1/pokemon/pikachu](https://tyradex.app/api/v1/pokemon/pikachu){ .hl-link }
</center>

Vous recevez ici toutes les données concernant Pikachu au format **JSON** (*JavaScript Object Notation*). Un format similaire aux dictionnaires en Python.

??? question

    En exploitant les données de cette colossale réponse, donnez :

      * Le **poids** de Pikachu
      * Les **points de vie** de Pikachu
      * Le **type** de Pikachu

    Rechercher les données d'un **autre Pokémon**. Attention les noms sont en anglais !

![](https://img.pokemondb.net/sprites/red-blue/normal/pikachu.png){ .center-img .pixelart width="156px" }

## Utiliser l'API avec Python

Pour que Python puisse effectuer des requêtes sur Internet, nous avons besoin d'installer le module `requests` (il est préinstallé sur Capytale). Une fois installé, assuez-vous que le code suivant fonctionne :

```python
import requests

url = "https://tyradex.app/api/v1/pokemon/pikachu"
reponse = requests.get(url)  # effectue la requête (lent)

if reponse.status_code == 200:  # Code 200 = OK
    data = reponse.json()  # transforme le JSON en dictionnaire
    poids = data['weight']
    print(f"Pikachu pèse {poids}.")
```

Le projet consiste à implémenter le jeu [Pokédle](https://pokedle.net/classic) dans la console Python. Quelques indications :

* Analyser les caractéristiques utilisées dans le jeu [Pokédle](https://pokedle.net/classic) et les extraire du dictionnaire `data`. La fonction `pprint`du module éponyme  et son paramètre `depth` peut être utile.

    ```python
    from pprint import pprint
    ...
    pprint(data, depth=1)
    ```

* Besoin d'un Pokémon aléatoire ou la liste des Pokémons de première génération ? N'hésitez pas à consulter [le site officiel Tyradex](https://tyradex.app/) pour voir les possibilités de l'API !

!!! info "Je n'aime pas Pokémon !"

    Rien de vous empêche de choisir un thème autre que Pokémon... cependant, vous devez au moins utiliser une API Web. C'est le sujet du jour... pourquoi pas un « Météodle » en utilisant l'API [OpenWeather](https://openweathermap.org/api)  par exemple.


## Une interface graphique avec `tkinter`

Utilisez le module **Tkinter** pour créer une interface graphique à votre jeu. Il existe d'innombrables tutoriels sur le Web. Bon courage.