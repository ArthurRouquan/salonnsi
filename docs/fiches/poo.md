---
title: POO
icon: lucide/boxes
---

## Vocabulaire

| Terme            | Définition                                                                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Classe**       | Modèle qui définit les **attributs** (données) et **méthodes** (fonctions) communes à tous les objets créés à partir d'elle. |
| **Objet**        | Instance concrète d'une classe. Il possède ses **propres valeurs d'attributs**.                                              |
| **Instance**     | Synonyme d'objet. **Instancier** une classe, c'est créer un nouvel objet à partir d'elle.                                    |
| **Attribut**     | Donnée associée à un objet.                                                                                                  |
| **Méthode**      | Fonction définie dans une classe, qui agit spécifiquement sur les objets de cette classe.                                    |
| **Constructeur** | Méthode spéciale `__init__` appelée à la création d'un objet, qui initialise ses attributs.                                  |
| **`self`**       | Premier paramètre de chaque méthode : il désigne l'objet sur lequel la méthode est appelée.                                  |

## Exemple

```{ .python .no-copy  title="Définir une classe"}
class Pokemon:
    def __init__(self, nom, attaque, pv_max):  # constructeur
        self.nom = nom  # self.nom = attribut, nom = paramètre
        self.attaque = attaque
        self.pv_max = pv_max
        self.pv = pv_max  # attribut qui n'est pas un paramètre : initialisé à partir de pv_max

    def subir_degats(self, degats):  # méthode
        self.pv = self.pv - degats  # un attribut peut être modifié
        if self.pv < 0:
            self.pv = 0

    def est_ko(self):  # méthode
        return self.pv == 0

    def attaquer(self, autre):  # méthode qui prend un autre objet en paramètre
        autre.subir_degats(self.attaque)
```

```{ .python .no-copy  title="Instancier de nouveaux objets"}
p1 = Pokemon('Pikachu', 10, 30)  # appel du constructeur __init__
p2 = Pokemon('Salamèche', 15, 40)
p3 = Pokemon('Dracaufeu', 50, 180)
```

<div class="grid" markdown>

```{ .python .no-copy title="Récupérer un attribut"}
print(p1.nom)  # affiche « Pikachu »
```

```{ .python .no-copy title="Modifier un attribut"}
p3.pv = 100
```

</div>

<!-- !!! tip "Bonne pratique"
    Modifier directement un attribut est possible en Python, mais on préfère passer par une **méthode** (comme `subir_degats`), qui garantit que l'objet reste cohérent (par exemple, des PV jamais négatifs). -->

```{ .python .no-copy  title="Appeler une méthode"}
p1.subir_degats(10)
print(f'{p1.nom} a {p1.pv} PV restants.')
# affiche « Pikachu a 20 PV restants. »
print(p1.est_ko())  # affiche False

p3.attaquer(p1)  # Dracaufeu attaque Pikachu
print(p1.est_ko())  # affiche True
```

!!! note "Que vaut `self` ?"
    Lors de l'appel `p1.subir_degats(10)`, Python exécute en réalité `Pokemon.subir_degats(p1, 10)` : `self` vaut donc `p1`. De même, dans `p3.attaquer(p1)`, `self` vaut `p3` et `autre` vaut `p1`.

```{ .python .no-copy  title="Manipuler une liste d'objets"}
equipe = [p1, p2, p3]
for p in equipe:
    if not p.est_ko():
        print(p.nom)
# affiche « Salamèche » et « Dracaufeu »
```

