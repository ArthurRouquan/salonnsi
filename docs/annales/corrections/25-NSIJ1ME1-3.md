---
title: 25-NSIJ1ME1-3
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ1ME1-2.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1ME1-3.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1ME1.pdf){ .md-button }
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Les deux seules adresses IP valides sont **(a)** et **(b)**.

2. **192.168.20.255** est l'adresse de diffusion du réseau du café 1.

3. En prenant en compte les 4 machines connectées et les 2 adresses réservées, il est encore possible de connecter $255 - 4 - 2 = \boxed{249}$ machines à ce réseau.

4. Puisque $8 = 2^3$, le numéro d'hôte peut s'écrire sur 3 bits, donc la longueur maximale du masque de sous-réseau est de $32 - 3 = \boxed{29}$ bits.

5. 
| Réseau destination | Interface de sorties | Prochain routeur | Nombre de sauts |
| :----------------: | :------------------: | :--------------: | :-------------: |
|    192.168.30.0    |    **172.16.4.1**    |  **172.16.4.2**  |      **1**      |
|     172.16.1.0     |    **172.16.3.1**    |  **172.16.3.2**  |      **1**      |

6. Depuis le routeur 2, le réseau du siège social (192.168.10.0) peut être atteint, avec un nombre minimal de sauts, en passant par le routeur 1 (route actuelle) ou par le routeur 3 (nouvelle route). Ainsi la ligne correspondante à cette destination dans sa table de routage peut être modifiée comme :

    | Réseau destination | Interface de sorties | Prochain routeur | Nombre de sauts |
    | :----------------: | :------------------: | :--------------: | :-------------: |
    |    192.168.10.0    |    **172.16.4.1**    |  **172.16.4.2**  |        2        |

7. 
| Réseau destination | Interface de sorties | Prochain routeur |
| :----------------: | :------------------: | :--------------: |
|       Autre        |    **172.16.3.1**    |  **172.16.3.2**  |

8. 
| Type de connexion |   Débit    |  Coût  |
| :---------------: | :--------: | :----: |
|     Ethernet      | 10 Mbit/s  |  100   |
|   Fast Ethernet   | 100 Mbit/s | **10** |
|   Fibre Optique   |  1 Gbit/s  | **1**  |

9. La route dont le coût est minimal est **R1 → R2 → R3 → R4** de coût $10 + 10 + 1 = \boxed{21}$.

10. L'appel `#!py ip_bin('192.168.20.12')` renvoie **`#!py '11000000.10101000.00010100.00001100'`**.

11. La dernière instruction sera exécutée si et seulement si les deux adresses IP `ip_1` et `ip_2` sont **égales**.

12. 
```python hl_lines="4 6 7"
def precede(ip_1, ip_2):
    for i in range(35):
        if ip_1[i] < ip_2[i]:
            return True
        elif ip_1[i] > ip_2[i]:
            return False
    return False
```

13. Dans la classe `Abr`, **`adresse_ip`** est un attribut et **`est_vide`** est une méthode.

14. 
```python
def est_vide(self):
    return self.adresse_ip == ''
```

15. Un Arbre Binaire de Recherche (ABR) est une structure de données particulièrement adaptée au maintien d'un ensemble de valeurs triées. En moyenne, les opérations d'insertion et de recherche s'effectuent en temps **logarithmique** par rapport au nombre d'éléments. Représenter une table de routage par un ABR permet ainsi d'effectuer avec efficience la recherche de la passerelle correspondant à une adresse IP, ainsi que sa mise à jour.

16. 
```python
def modifie(self, adresse_ip, interface, passerelle, cout):
    if self.est_vide():
        self.gauche = Abr('', '', '', 0)
        self.droite = Abr('', '', '', 0)
    self.adresse_ip = adresse_ip
    self.interface  = interface
    self.passerelle = passerelle
    self.cout       = cout
```

17.  
```python
elif precede(adresse_ip, self.adresse_ip):
```

</div>
