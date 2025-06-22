---
title: 25-NSIJ2ME1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ2ME1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ2ME1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ2ME1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Le message <tt style="font-size: .95em">LIBRE</tt>, chiffré à l'aide de la clé <tt style="font-size: .95em">EYQMT</tt>, donne le résultat <tt style="font-size: .95em">**PGRDX**</tt>.

    ```
        11 (L)    8 (I)    1 (B)   17 (R)    4 (E)   message
    +    4 (E)   24 (Y)   16 (Q)   12 (M)   19 (T)   masque
    =   15       32       17       29       23       masque + message
    =   15 (P)    6 (G)   17 (R)    3 (D)   23 (X)   masque + message mod 26
    ```

2. 
```python
def indice(L, element):
    for i in range(len(L)):
        if L[i] == element:
            return i
```

3. 
```python
def lettres_vers_indices(chaine):
    return [indice(alphabet, c) for c in chaine]
```

4.  
```python hl_lines="8 10 12"
def chiffrement(msg, cle):
    assert len(cle) >= len(msg), 'impossible'
    indices_msg = lettres_vers_indices(msg)
    indices_cle = lettres_vers_indices(cle)
    n = len(msg)
    indices_msg_chiffre = []
    for k in range(n):
        ind = indices_msg[k] + indices_cle[k]
        if ind >= 26:
            ind = ind - 26
        indices_msg_chiffre.append(ind)
    msg_chiffre = indices_vers_lettres(indices_msg_chiffre)
    return msg_chiffre
```

5. L'appel lève ici l'erreur `#!py AssertionError` (avec le message `#!py 'impossible'`) car l'assertion en début de fonction n'est pas vérifiée, la longueur de la clé n'est pas ici au moins égale à longueur du texte.

6. On peut d'abord déduire la somme masque + message et enfin le message clair : 
   
    ```
         1 (B)   17 (R)    0 (A)   21 (V)   14 (O)   message
    +    5 (F)   21 (V)    4 (E)    8 (I)   19 (T)   masque
    =    6       38        4       29       33       masque + message
    =    6 (G)   12 (M)    4 (E)    3 (D)    7 (H)   masque + message mod 26
    ```

    Le message clair est <tt style="font-size: .95em">**BRAVO**</tt>.

7. Les indices du message clair sont obtenues en soustrayant les indices du message chiffré par les indices du masque, modulo 26. Il suffit ensuite de convertir ces indices en caractères pour obtenir le message clair.


8. 
```python hl_lines="8 9 10 11"
def dechiffrement(msg, cle):
    assert len(cle) >= len(msg), 'impossible'
    indices_msg = lettres_vers_indices(msg)
    indices_cle = lettres_vers_indices(cle)
    n = len(msg)
    indices_msg_dechiffre = []
    for k in range(n):
        ind = indices_msg[k] - indices_cle[k]
        if ind < 0:
            ind = ind + 26
        indices_msg_dechiffre.append(ind)
    msg_dechiffre = indices_vers_lettres(indices_msg_dechiffre)
    return msg_dechiffre
```

9. Un algorithme de chiffrement symétrique utilise **une seule et même clé** pour chiffrer et déchiffrer un message. À l'inverse, un algorithme de chiffrement asymétrique repose sur **deux clés distinctes** :
    * une clé publique pour chiffrer le message, librement diffusée,
	* une clé privée pour le déchiffrer, conservée secrète.

10. Comme Alice a chiffré le message avec la clé publique de Bob, seul Bob peut le déchiffrer **en utilisant sa clé privée**. 

11. **Une personne malveillante peut intercepter l'échange de clés.** Par exemple, lorsque Bob envoie sa clé publique à Alice, l'attaquant peut la remplacer par la sienne. Alice chiffre alors son message avec cette fausse clé, permettant à l'attaquant de le déchiffrer, de le lire ou le modifier, puis de le re-chiffrer avec la vraie clé publique de Bob. Ce dernier, ne se doutant de rien, pense que le message vient d'Alice. C'est une **attaque de l'homme du milieu**.

12. Le protocole HTTPS sécurise les communications entre deux hôtes sur un réseau en combinant chiffrement asymétrique et symétrique. Le serveur envoie sa clé publique accompagnée d'un **certificat d'authenticité** délivré par une autorité de confiance, que le client vérifie pour s'assurer de l'identité du serveur. Il chiffre ensuite une clé symétrique temporaire avec cette clé publique. Le serveur la déchiffre avec sa clé privée, et toute la communication qui suit utilise cette clé symétrique.

13. Le chiffrement asymétrique requiert **un plus grand temps de calcul** que le chiffrement symmétrique. HTTPS l'utilise juste pour échanger une clé symétrique, qui sert ensuite à chiffrer efficacement la communication.

14. **Marc a mal saisi l'adresse IP de Bob** : il a tapé <tt style="font-size: .95em">192.168.100.115</tt> au lieu de <tt style="font-size: .95em">192.168.**110**.115</tt>. Cette adresse erronée ne fait pas partie de son réseau local. Comme l'erreur affichée n'est pas « destination inaccessible », cela signifie qu'une passerelle est bien configurée sur le réseau de Marc, et que la machine a tenté d'envoyer les paquets vers un autre réseau. Aucun hôte ne répondant à cette adresse, tous les paquets ont été perdus.

15. Ce masque s'écrit <tt style="font-size: .95em">**255.255.255.224**</tt> en notation décimale.

16. Ce sous-réseau réserve 5 bits pour le numéro d'hôte. En excluant les deux adresses réservées, le nombre total d'adresses IPv4 utilisables est de $2^5 - 2 = \boxed{30}$.

17. $134 = 128 + 4 + 2 = \boxed{(10000110)_2}$

18. On suppose que Zoé utilise également le masque <tt style="font-size: .95em">255.255.255.224</tt> :

    * L'adresse <tt style="font-size: .95em">192.168.110.115</tt> n'est donc pas sur son sous-réseau, car <tt style="font-size: .95em">115 = 0b**<span class="red-text">011</span>**10011</tt>.

    * L'adresse <tt style="font-size: .95em">192.168.110.153</tt> appartient au même sous-réseau que celui de Zoé, car <tt style="font-size: .95em;">153 = 0b**<span class="green-text">100</span>**11001</tt>.

    Si aucune passerelle n’est configurée, **seule la commande 2 peut aboutir**.

</div>
