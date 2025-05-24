---
title: 25-NSIJ1AN1-1
---

<!-- <div class="center-button" markdown>
[:material-arrow-left-circle:](){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1AN1-1.pdf){ .md-button }
[:material-arrow-right-circle:](25-NSIJ1AN1-2.md){ .md-button }
</div> -->

<div class="circle-ol" markdown>

1. En suivant l'arbre de décision, le végétal correspondant à cette description est un **sorbier**.

2. En suivant l'arbre de décision, la feuille correspondante à cette description est vide, **on ne peut donc pas identifier ce végétal**.

3. 
```python
arbre_2 = Noeud(
    'Simples ?',
    Feuille_resultat([]),
    Noeud(
        'Alternées ?',
        Noeud(
            'Bord denté ?',
            Feuille_resultat(['Sorbier']),
            Feuille_resultat(['Robinier', 'Noyer'])
        ),
        Feuille_resultat([]),
    )
)
```

1. 
```python
class Noeud:
    # ...
    def est_resultat(self):
        return False
```

1. 
```python
class Feuille_resultat:
    # ...
    def est_resultat(self):
        return True
```

1. 
```python
class Feuille_resultat:
    # ...
    def nb_vegetaux(self):
        return len(self.vegetaux)
```

1. 
```python
class Noeud:
    # ...
    def nb_vegetaux(self):
        return self.sioui.nb_vegetaux() + self.sinon.nb_vegetaux()
```

1. 
```python
class Feuille_resultat:
    # ...
    def liste_questions(self):
        return []
```

1. 
```python
class Noeud:
    # ...
    def liste_questions(self):
        return [self.question] + self.sioui.liste_questions() + self.sinon.liste_questions()
```

1.  
```python
def est_bien_renseigne(dico_vegetal, arbre):
    questions = arbre.liste_questions()
    for question in dico_vegetal:
        if question not in questions:
            return False
    return True
```

1.  
```python
def identifier_vegetaux(arbre, dico_vegetal)
    while not arbre.est_resultat():
        if dico_vegetal[arbre.question]:
            arbre = arbre.sioui
        else:
            arbre = arbre.sinon
    return arbre.vegetaux 
```

</div>