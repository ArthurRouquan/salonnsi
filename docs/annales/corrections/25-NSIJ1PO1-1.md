---
title: 25-NSIJ1PO1-1
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-home:](../index.md/#sujets-2025){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ1PO1-1.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ1PO1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ1PO1-2.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. 
|  Destination  |   Prochain saut   | Distance |
| :-----------: | :---------------: | :------: |
| R<sub>2</sub> |   R<sub>2</sub>   |    0     |
| R<sub>3</sub> |   R<sub>2</sub>   |    1     |
| R<sub>4</sub> | **R<sub>4</sub>** |  **0**   |
| R<sub>5</sub> | **R<sub>5</sub>** |  **0**   |
| R<sub>6</sub> | **R<sub>5</sub>** |  **1**   |

2. La route est **LAN<sub>1</sub> → R<sub>1</sub> → R<sub>5</sub> → R<sub>6</sub> → Internet**.

3. 
|  Destination  |   Prochain saut   | Distance |
| :-----------: | :---------------: | :------: |
| R<sub>2</sub> |   R<sub>2</sub>   |    10    |
| R<sub>3</sub> | **R<sub>2</sub>** |  **11**  |
| R<sub>4</sub> | **R<sub>2</sub>** |  **12**  |
| R<sub>5</sub> | **R<sub>2</sub>** |  **13**  |
| R<sub>6</sub> | **R<sub>2</sub>** |  **14**  |

4. La route est **LAN<sub>1</sub> → R<sub>1</sub> → R<sub>2</sub> → R<sub>3</sub> → R<sub>4</sub> → R<sub>5</sub> → R<sub>6</sub> → Internet**.

5. La route est **LAN<sub>1</sub> → R<sub>1</sub> → R<sub>5</sub> → R<sub>6</sub> → Internet** de distance **101**.

6. 
|        Machine        |      Masque       |        Réseau         | Réseau (décimal) |
| :-------------------: | :---------------: | :-------------------: | :--------------: |
|   <tt>11000000</tt>   | <tt>11111111</tt> |   <tt>11000000</tt>   |       192        |
|   <tt>10101000</tt>   | <tt>11000000</tt> | **<tt>10000000</tt>** |     **128**      |
| **<tt>00000001</tt>** | <tt>00000000</tt> | **<tt>00000000</tt>** |      **0**       |
| **<tt>01100100</tt>** | <tt>00000000</tt> | **<tt>00000000</tt>** |      **0**       |

7. 
|      Réseau       |      Masque       |      Complément       |       Broadcast       | Broadcast (décimal) |
| :---------------: | :---------------: | :-------------------: | :-------------------: | :-----------------: |
| <tt>11000000</tt> | <tt>11111111</tt> | **<tt>00000000</tt>** | **<tt>11000000</tt>** |       **192**       |
| <tt>10000000</tt> | <tt>11000000</tt> | **<tt>00111111</tt>** | **<tt>10111111</tt>** |       **191**       |
| <tt>10000000</tt> | <tt>00000000</tt> | **<tt>11111111</tt>** | **<tt>11111111</tt>** |       **255**       |
| <tt>10000000</tt> | <tt>00000000</tt> | **<tt>11111111</tt>** | **<tt>11111111</tt>** |       **255**       |

8.  * L'adresse du réseau LAN<sub>1</sub> : **172.16.0.0**
    * L'adresse de broadcast : **172.16.255.255**
    * le nombre total d'adresses disponibles : 2<sup>16</sup> – 2 = **65534**.

9. 
```python hl_lines="6 7"
def masquer(self, masque: str) -> str:
    tmp = []
    ip = self.octets()
    crible = IPv4(masque).octets()
    for i in range(4):
        tmp.append(str(ip[i] & crible[i]))
    return '.'.join(tmp)
```

10. 
```python hl_lines="8 9"
def adresse_suivante(self, adresse_max: str) -> str:
    assert self.adresse < adresse_max
    liste_courante = self.octets()
    liste_suivante = list()
    retenue = 1
    for index in range(4):
        somme = liste_courante[3 - index] + retenue
        valeur, retenue = somme % 256, somme // 256
        liste_suivante = [str(valeur)] + liste_suivante
    return '.'.join(liste_suivante)
```


</div>
