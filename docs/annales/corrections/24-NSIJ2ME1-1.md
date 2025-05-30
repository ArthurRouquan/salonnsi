---
title: 24-NSIJ2ME1-1
---

<div class="circle-ol" markdown>

1. **Non**, l'attribut `Nom_artiste` ne peut pas être utilisé comme clé primaire dans la relation `CD`, car il ne permet pas d'identifier de manière unique un album, en effet un artiste peut en composer plusieurs.

2. 
| `Nom_artiste` |
| :-----------: |
|   Nightwish   |
|  The Rasmus   |

3. 
| `CD.Annee` |
| :--------: |
|    1986    |
|    2001    |
|    1986    |

1. 
```sql
UPDATE CD
SET Annee = 2000
WHERE Titre_album = 'Wishmaster';
```

5. 
```sql
SELECT Titre_album
FROM CD
JOIN Rangement ON Rangement.id_album  = CD.id_album
JOIN Artiste   ON Artiste.Nom_artiste = CD.Nom_artiste
WHERE Style = 'Metal'
    AND Numero_etagere = 1;
```

6. Il faut d’abord supprimer l’album dans la table `Rangement` car il y est référencé. Ensuite, on peut le supprimer de la table `CD`. Enfin, si l’artiste n’a plus d’album, on peut aussi le retirer de la table `Artiste`. La requête pour supprimer l’album de la table `CD` :

    ```sql
    DELETE FROM CD
    WHERE Titre_album = 'Dead Letters';
    ```

7. Un algorithme de chiffrement symétrique utilise **une seule et même clé** pour chiffrer et déchiffrer les messages.

8. Un algorithme de chiffrement asymétrique repose sur **deux clés différentes** : une clé publique pour chiffrer, et une clé privée pour déchiffrer.

9. Bob génère deux clés d'un chiffrement asymétrique et partage publiquement sa clé de chiffrement. Sa clé de déchiffrement reste privée. Le serveur utilise alors la clé publique de Bob pour chiffrer la clé C et l'envoie à Bob. Seul Bob peut alors la déchiffrer, car il est le seul à connaître sa clé de déchiffrement.

</div>