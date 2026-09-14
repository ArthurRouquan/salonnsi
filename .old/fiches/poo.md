---
title: POO
icon: material/puzzle
---

## Vocabulaire

| Terme            | Définition                                                                                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Classe**       | Modèle qui définit les **attributs** (données) et **méthodes** (fonctions) communes à tous les objets créés à partir d'elle. |
| **Objet**        | Instance concrète d'une classe. Il possède ses **propres valeurs d'attributs**.                                              |
| **Attributs**    | Données associées à un objet.                                                                                                |
| **Méthodes**     | Fonctions définies dans une classe, qui agissent spécifiquement sur les objets de cette classe.                              |
| **Constructeur** | Méthode spéciale appelée à la création d'un objet qui initialise ses attributs.                                              |

## Exemple

```{ .python .no-copy  title="Définir une classe"}
class Pokemon:
    def __init__(self, nom, attaque, pv_max):  # constructeur
        self.nom     = nom      # self.nom = attribut, nom = paramètre
        self.attaque = attaque
        self.pv_max  = pv_max
        self.pv      = pv_max   # paramètres ≠ attributs 
        
    def subir_degats(self, degats):  # méthode
        # self est l'objet de la classe sur lequel on applique la méthode.
        self.pv = self.pv - degats   # un attribut peut être modifié
        if self.pv < 0:
            self.pv = 0

    def est_ko(self):  # méthode
        return self.pv == 0
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
p3.pv_max = 200
```

</div>

```{ .python .no-copy  title="Appeler une méthode"}
p1.subir_degats(10)
print(f'{p1.nom} a {p1.pv} PV restants.')
# affiche « Pikachu a 20 PV restants. »
print(p1.est_ko())  # affiche False
```