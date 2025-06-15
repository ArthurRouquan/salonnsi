---
title: 24-NSIJ2JA1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ2JA1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2JA1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2JA1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. **Non**, la clé primaire doit pouvoir identifier de manière unique chaque entrée. Or, certaines chansons paratagent un même titre, comme Showbiz.

2. 
|        `titre`         |         `album`          |
| :--------------------: | :----------------------: |
| Welcome too the Jungle | Appetite for Destruction |

3. 
```sql
SELECT titre
FROM Chanson
WHERE album = 'Showbiz'
ORDER BY titre;
```

4. 
```sql
INSERT INTO Chanson
VALUES (10, 'Megalomania', 'Hullabaloo', 'Muse');
```

5. 
```sql
UPDATE Chanson
SET titre = 'Welcome to the Jungle'
WHERE id = 7;
```

6. Cette séparation en plusieurs tables permet d'éviter la **redondance** des données (par exemple, ne pas répéter le nom du groupe à chaque chanson).

7. L'attribut `id_album` est une clé étrangère qui met en relation la table `Chanson` avec la table `Album`.

8. Le schéma relationnel de la base de données :

    * <tt style="font-size: .85em">Chanson(<u>id</u>: INT, titre: TEXT, #id_album: INT)</tt>
    * <tt style="font-size: .85em">Album(<u>id</u>: INT, année: INT, #id_groupe: INT)</tt>
    * <tt style="font-size: .85em">Groupe(<u>id</u>: INT, nom: TEXT)</tt>

9. 
```sql
SELECT Album.titre
FROM Chanson
JOIN Album ON Album.id = Chanson.id_album
WHERE Chanson.titre = 'Showbiz';
```

10.  
```sql
SELECT Chanson.titre, Album.titre
FROM Chanson
JOIN Album  ON Album.id  = Chanson.id_album
JOIN Groupe ON groupe.id = Album.id_groupe
WHERE Groupe.nom = 'Muse';
```

11.  La requête renvoie le nombre d'albums réalisés par le groupe Muse présents dans la base de données.

12.  
```python hl_lines="2 3"
assert ordre_lex('', 'a') == True
assert ordre_lex('b', 'a') == False
assert ordre_lex('aaa', 'aaba') == True
```

13.  
```python hl_lines="10 12 14"
def ordre_lex(mot1, mot2):
    if mot1 == '':
        return True
    elif mot2 == '':
        return False
    else:
        c1 = mot1[0]
        c2 = mot2[0]
        if c1 < c2:
            return True
        elif c1 > c2:
            return False
        else:
            return ordre_lex(mot1[1:], mot2[1:])
```

14. 
```python
def ordre_lex2(mot1, mot2):
    for i in range(min(len(mot1), len(mot2))):
        if mot1[i] < mot2[i]:
            return True
        if mot1[i] > mot2[i]:
            return False
    return len(mot1) <= len(mot2)
```

</div>
