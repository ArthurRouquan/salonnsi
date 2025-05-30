---
title: 24-NSIJ1AN1-3
---

<div class="circle-ol" markdown>

1. L'étudiante a choisi le séparateur `;`.

2. Le caractère `,` apparaît dans certains champs, par exemple `Allemagne, Italie, Japon`. On peut se passer du caractère `;` plus facilement.

3. 
```python
def charger(nom_fichier):
    with open(nom_fichier,'r') as fichier:
        donnees = list(csv.DictReader(fichier,delimiter=';'))
    return donnees
```

4. Le sujet contient ici une erreur. `time.sleep` est une fonction du module `time`, et non une méthode. Bien qu'on l'appelle via la syntaxe `time.sleep(...)`, elle n'est liée à aucun objet ou classe spécifique.

5. L'expression `#!py donnees[i]` renvoie un **dictionnaire**, donc de type `#!py dict` en Python.

6. 
```python
flashcard = charger('flashcards.csv')
d = choix_discipline(flashcard)
c = choix_chapitre(flashcard, d)
entrainement(flashcard, d, c)
```

7. 
```sql
INSERT INTO boite
VALUES (5, 'tous les huit jours', 15)
```

8. 
```sql
UPDATE flashcard
SET reponse = '7 décembre 1941'
WHERE id = 5;
```

9. 
```sql
SELECT DISTINCT lib
FROM discipline
```

10. 
```sql
SELECT chapitre.lib
FROM chapitre
JOIN discipline ON discipline.id = chapitre.id_disc
WHERE discipline.lib = 'histoire';
```

11. 
```sql
SELECT flashcard.id
FROM chapitre
JOIN flashcard  ON flashcard.id_ch = chapitre.id
JOIN discipline ON discipline.id   = chapitre.id_disc
WHERE discipline.lib = 'histoire';
```

12. 
```sql
DELETE FROM flashcard
WHERE id_boite = 3;
```
</div>