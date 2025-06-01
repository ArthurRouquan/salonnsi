---
title: 24-NSIJ1PO1-3
---

<div class="circle-ol" markdown>

1. 
```python
(
    participants['PHILIPSEN Jasper'],
    classement_general[participants['PHILIPSEN Jasper']],
    temps_etapes[participants['PINOT Thibaut']][3]
)
```

2. 
```python
def calcul_temps_total(d):
    total = 0
    for temps in temps_etapes[d]:
        total += temps
    return total
```

3. 
```python hl_lines="8 9 14"
classement = []

for numero_dossard in temps_etapes:
    element = (numero_dossard, calcul_temps_total(numero_dossard))
    classement.append(element)
    pos = len(classement) - 2

    while pos >= 0 and element[1] < classement[pos][1]:
        classement[pos + 1] = classement[pos]
        pos = pos - 1
        classement[pos + 1] = element

for i in range(len(classement)):
    classement_general[classement[i][0]] = i + 1
```

4. 
```python hl_lines="12 13 14"
tableau_final = []
difference_temps = 0
premier = True
for ligne in tableau_temps:
    coureur = [ligne[0]]
    coureur.append(ligne[1])
    if premier:
        temps_premier = ligne[2]
        coureur.append(temps_premier)
        premier = False
    else:
        difference_temps = ligne[2] - temps_premier
        coureur.append(difference_temps)
    tableau_final.append(coureur)
```

5. Une clé primaire doit permettre d’identifier chaque enregistrement **de manière unique**. Dans la table `Temps`, un coureur (représenté par `numDossard`) participe à plusieurs étapes, donc cet attribut seul n’est pas unique. De même, une étape (`numEtape`) concerne plusieurs coureurs.
   
    En revanche, le couple `(numDossard, numEtape)` est unique pour chaque ligne, car **un coureur n’a qu’un seul temps par étape**. Ce couple peut donc servir de clé primaire.
 
6. Cette requête renvoie **tous les noms des coureurs de l'équipe Cofidis**.

7. 
```sql
SELECT Date
FROM Etapes
WHERE Type = 'contre-la-montre';
```

8. 
```sql
SELECT directeurSportif
FROM Equipes
JOIN Coureurs ON Equipe = nomEquipe
WHERE nomCoureur = 'BARDET Romain';
```

9. La première requête provoque une erreur car elle tente d’insérer un temps pour l’étape 5 alors que cette étape n’existe pas encore dans la table `Etapes`. Or une clé étrangère doit obligatoirement faire référence à une clé primaire existante dans la table liée. Ici, **la première requête viole la contrainte d'intégrité référentielle**.

10. Il suffit d'**inverser l'ordre des deux requêtes**.

11.  
```sql
SELECT SUM(tempsRéalisé)
FROM Coureurs
JOIN Temps ON Temps.numDossard = Coureurs.numDossard
WHERE nomCoureur = 'BARDET Romain';
```

</div>
