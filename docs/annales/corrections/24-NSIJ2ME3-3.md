---
title: 24-NSIJ2ME3-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](24-NSIJ2ME3-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/24-NSIJ2ME3-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/24-NSIJ2ME3.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2024){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Une adresse IPv4 est composée de **4 octets**.

2. Les adresses IP des serveurs :
    * `Serveur_web`, la 1ère adresse IP du réseau, est `172.16.0.1`.
    * `Serveur_BDD`, la 2ème adresse IP du résau, est `172.16.0.2`.

3. La commande `ping` permet de tester la **connectivité** entre deux hôtes sur un réseau.
   
4. Le poste `PC_A1` est mal configuré. La passerelle par défaut `192.168.0.254` n’est pas accessible car elle n’est pas dans le même sous-réseau que le poste (`192.168.1.0`). Il suffit de modifier sa passerelle en `192.168.1.254`, conformément au schéma.

5. Les paquets suivent le chemin **<tt>PC_A1</tt> → Routeur <tt>A</tt> → Routeur <tt>B</tt> → Routeur <tt>C</tt> → Routeur <tt>D</tt> → <tt>Serveur_impression</tt>**.

6. Les paquets suivent le chemin **<tt>PC_A1</tt> → Routeur <tt>A</tt> → Routeur <tt>B</tt> → Routeur <tt>C</tt>** et n'arrivent donc pas à destination.

7. Table de routage du routeur C :

    |     Destination      |                    Prochain saut                     |               Métrique               |
    | :------------------: | :--------------------------------------------------: | :----------------------------------: |
    | <tt>172.16.0.0</tt>  |                  <tt>10.0.2.2</tt>                   |                  2                   |
    | <tt>192.168.0.0</tt> |                  <tt>10.0.2.2</tt>                   |                  2                   |
    | <tt>192.168.1.0</tt> | <span class="blue-text"><tt>**10.0.2.2**</tt></span> | <span class="blue-text">**2**</span> |
    | <tt>192.168.2.0</tt> | <span class="blue-text"><tt>**10.0.3.2**</tt></span> | <span class="blue-text">**1**</span> |
    | <tt>192.168.3.0</tt> | <span class="blue-text"><tt>**10.0.4.2**</tt></span> | <span class="blue-text">**1**</span> |
    |  <tt>10.0.0.0</tt>   |                  <tt>10.0.2.2</tt>                   |                  1                   |
    |  <tt>10.0.1.0</tt>   | <span class="blue-text"><tt>**10.0.2.2**</tt></span> | <span class="blue-text">**1**</span> |
    |  <tt>10.0.2.0</tt>   |                          —                           |                  —                   |
    |  <tt>10.0.3.0</tt>   |                          —                           |                  —                   |
    |  <tt>10.0.4.0</tt>   |                          —                           |                  —                   |
    |  <tt>10.0.5.0</tt>   | <span class="blue-text"><tt>**10.0.3.2**</tt></span> | <span class="blue-text">**1**</span> |
    |   <tt>0.0.0.0</tt>   |                  <tt>10.0.2.2</tt>                   |                  2                   |

8. Les paquets suivent le chemin **<tt>PC_A1</tt> → <tt>A</tt> → <tt>B</tt> → <tt>C</tt> → <tt>D</tt> → <tt>Serveur_impression</tt>**.

9. La liaison entre les routeurs C et D offrant un faible débit de 10 Mb/s, il serait ainsi préférable d’emprunter l’itinéraire C → D → E, où chaque liaison bénéficie d’un débit supérieur de 1 Gb/s.

10. Après la coupure de la liaison C–D, les lignes suivantes de la table du routeur C sont ainsi modifiées :

    |     Destination      |   Prochain saut   | Métrique |
    | :------------------: | :---------------: | :------: |
    | <tt>192.168.2.0</tt> | <tt>10.0.4.2</tt> |    2     |
    |  <tt>10.0.5.0</tt>   | <tt>10.0.4.2</tt> |    1     |

    Les paquets suivent alors le nouveau chemin <tt>PC_A1</tt> → <tt>A</tt> → <tt>B</tt> → <tt>C</tt> → <tt>E</tt> → <tt>D</tt> → <tt>Serveur_impression</tt>.

11. 
```sql
SELECT titre_parution FROM parution;
```

12.  La requête renvoie le numéro de parution et le numéro des pages écrites en Arial 12, classés par ordre croissant de numéro de parution.

13. 
```sql
SELECT num_image, titre_image, poids
FROM image 
WHERE poids > 1000;
```

14.  Cette requête renvoie les numéros de parution contenant au moins une image dont le titre comporte le mot « Appolo ». Un même numéro de parution peut apparaître plusieurs fois si plusieurs images correspondantes y sont associées.

15. Cette requête ajoute l’image portant le numéro 2923 à la relation <tt>image</tt>. Son titre est « Volcans du massif central », ses dimensions sont de 400×400 pixels et son poids est de 1430 Ko. Aucune description n'est renseignée.

16. 
```sql
INSERT INTO texte
VALUES (2754, 'Vulcania', 'Parc d''attraction', 250);
```

17. Cette requête supprime le texte portant le numéro 2034 de la relation <tt>texte</tt>.

18. 
```sql
DELETE FROM comporte_texte
WHERE num_texte = 2034;
```

</div>