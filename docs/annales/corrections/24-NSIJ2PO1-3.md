---
title: 24-NSIJ2PO1-3
---

<div class="circle-ol" markdown>

1. Les chemins possibles sont **R4 → R8 → R1 → R2** et **R4 → R8 → R7 → R2**.

2. Table des coûts du routeur R2 :
   
    | Destination | Coût  |
    | :---------: | :---: |
    |     R1      |   1   |
    |     R3      |   3   |
    |     R4      |   3   |
    |     R5      |   2   |
    |     R6      |   3   |
    |     R7      |   1   |
    |     R8      |   2   |
    |     R9      |   2   |

3. Le coût d'une liaison FTTH est de $\frac{10^8}{10 \cdot 10^9} = 10^{-2} = \boxed{0.01}$ .

4. Le chemin pris est **R4 → R8 → R9 → R1 → R2**.

5. La requête retourne le nom et le prénom des patients dont le numéro de sécurité sociale commence par 1.
6. 
```sql
SELECT num_SS
FROM hospitalisation
WHERE service = 'orthopédique'
AND date >= '2023-01-01' -- SQL utilise plutôt le format YYYY-MM-DD
AND date < '2024-01-01';
```

1. 
```sql
SELECT type, date
FROM patient AS p
JOIN examen  AS e ON e.num_SS = p.num_SS
WHERE nom LIKE 'Beaujean' AND prenom LIKE 'Emma';
```

1. 
```sql
SELECT p.nom, p.prenom
FROM patient      AS p
JOIN consultation AS c ON c.num_SS     = p.num_SS
JOIN medecin      AS m ON m.id_medecin = c.id_medecin
WHERE m.nom LIKE 'Arnos' AND m.prenom LIKE 'Pierre';
```

1. 
```python hl_lines="2 10 12 14"
def mdp_fort(mdp):
    if len(mdp) < 12:
        return False
    majuscules = 0
    chiffres = 0
    symboles = 0
    for caractere in mdp :
        if caractere.isupper():
            majuscules += 1
        if caractere.isdigit():
            chiffres += 1
        if caractere in liste_symboles:
            symboles += 1
    if majuscule < 2 or chiffres < 2 or symboles < 2:
        return False
    return True
```

1.   
```python hl_lines="9 13-19"
def creation_mdp(n, nbr_m, nbr_c, nbr_s):
    mdp = ''
    caracteres = 'abcdefghijklmnopqrstuvwxyz' + \
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' + \
                 '#@!?%<>=€$+-*/&'
    majuscules = 0
    chiffres = 0
    symboles = 0
    while len(mdp) < n or majuscules < nbr_m or chiffres < nbr_c or symboles < nbr_s:
        # la variable 'c' contient un caractère
        # choisi aléatoirement dans la variable 'caracteres'
        c = choice(caracteres)
        if c.isupper():
            majuscules += 1
        if c.isdigit():
            chiffres += 1
        if c in liste_symboles:
            symboles += 1
        mdp = mdp + c
    return mdp
```

1.   
```python hl_lines="5 6 15 16 18"
def recherche_mot(mdp):
    mot = transforme(mdp)
    trouve = []
    i = 0
    while i < len(mot):
        if mot[i].isdigit(): # si le caractère est un chiffre
            i = i + 1
        elif mot[i] in liste_symboles:
            i = i + 1
        else:
            # si le caractère est une lettre, on prend les
            # lettres qui la suivent jusqu'au moment où
            # on trouve un chiffre ou un symbole
            chaine = ''
            while mot[i].isalpha():
                chaine = chaine + mot[i]
                i = i + 1
            trouve.append(chaine)
    return trouve
```

1.  
```python
def mdp_extra_fort(mdp):
    for chaine in recherche_mot(mdp):
        if chaine in dicoFR and len(chaine) >= 4:
            return False
    return mdp_fort(mdp)  # si on renvoie True, une chaine vide serait extra fort
```

</div>