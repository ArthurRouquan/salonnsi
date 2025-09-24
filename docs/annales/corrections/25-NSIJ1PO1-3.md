---
title: 25-NSIJ1PO1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ1PO1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1PO1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1PO1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
```python
gen_mdp(8, True, True, False)
```

2. 
```python
minuscules = [chr(i) for i in range(97, 123)]
majuscules = [chr(i) for i in range(65, 91)]
caracteres_speciaux = [chr(i) for i in range(33, 48)] + \ 
                      [chr(i) for i in range(58, 65)]
```

3. 
```python
jeu_caracteres = []
if cont_min:
    jeu_caracteres += minuscules
if cont_maj:
    jeu_caracteres += majuscules
if cont_spe:
    jeu_caracteres += caracteres_speciaux
```

4. 
```python
mot_de_passe += jeu_caracteres[randint(0, n - 1)]
```

5. Le mot de passe est généré en choisissant chaque caractère de manière aléatoire parmi les caractères autorisés. Cela n'assure pas que le mot de passe contiendra **au moins une minuscule et un caractère spécial**, comme exigé.

6. Le mot de passe étant une **clé primaire** dans la table `compte`, il doit être **unique**. Il est donc impossible d’avoir deux comptes avec le même mot de passe.

7. 
```sql
SELECT url
FROM site;
```

8. 
```sql
UPDATE compte
SET mot_de_passe = 'yhTS?d@UTJe'
WHERE mot_de_passe = '@rDfohpj!&';
```

9. 
```sql
SELECT id_site
FROM compte
WHERE renouvellement < '2024-03-20';
```

1.  Le format AAAA-MM-JJ permet une **comparaison lexicographique** entre les dates (comme pour l'ordre alphabétique).

2.  
```sql
SELECT utilisateur, mot_de_passe
FROM compte
JOIN site ON site.id = compte.id_site
WHERE nom_site = 'Votremailp'
ORDER BY renouvellement;
```

1.  Alice pourrait avoir plusieurs comptes pour un même site donné, la sépération en deux tables permet ainsi d'éviter des **redondances**.

2.  
```python
chiffrement('gestionnaire.db', '../Perso/secret.db', '../Perso/cle')
```

1.  
|      Binaire      |   Hexadécimal   |
| :---------------: | :-------------: |
| <tt>10100011</tt> |   <tt>A3</tt>   |
| <tt>01011001</tt> |   <tt>59</tt>   |
| <tt>11111010</tt> | <tt>**FA**</tt> |

1.  On dresse une table de vérité :

    |    $a$     |    $b$     |  $a ⊕ b$   | $(a ⊕ b) ⊕ b$ |
    | :--------: | :--------: | :--------: | :-----------: |
    | <tt>0</tt> | <tt>0</tt> | <tt>0</tt> |  <tt>0</tt>   |
    | <tt>0</tt> | <tt>1</tt> | <tt>1</tt> |  <tt>0</tt>   |
    | <tt>1</tt> | <tt>0</tt> | <tt>1</tt> |  <tt>1</tt>   |
    | <tt>1</tt> | <tt>1</tt> | <tt>0</tt> |  <tt>1</tt>   |

    Les colonnes $a$ et $(a ⊕ b) ⊕ b$ sont identiques, ce qui vérifie la propriété.

2.  Le chiffrement est **symétrique**, car la même clé de chiffrement sert à déchiffrer. En effet, la question précédente indique qu'il suffit d'appliquer l'opération OU exclusif entre le fichier chiffré et la clé pour obtenir le fichier clair.

3.  Les droits actuels (`-rw-r--r--`) permettent à tous les utilisateurs du système de **lire le fichier chiffré**, ce qui constitue un risque. Alice devrait restreindre ces droits en retirant l'accès au groupe et aux autres utilisateurs, par exemple avec la commande :
    ```sh
    chmod og-r /home/Perso/secret.db
    ```

4.  
    * **P1** : Alice respecte cette recommandation, car chaque mot de passe est unique pour un site donné, comme indiqué à la question 6.
    * **P2** : La fonction de génération doit être améliorée pour garantir la présence d’au moins un caractère de chaque type requis, comme expliqué à la question 5.
    * **P3** : Les mots de passe d'Alice sont vulnérables. ILs sont stockés en clair sur son ordinateur, et les permissions du fichier ont de grandes changes d'être mal configurées.
    * **P4** : Le gestionnaire de mots de passe qu'elle a conçu elle-même peut comporter des vulnérabilités. La cybersécurité étant un domaine complexe, il est recommandé d’utiliser un outil plus éprouvé.


</div>
