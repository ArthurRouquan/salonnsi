---
title: 24-NSIJ1PO1-1
---

<div class="circle-ol" markdown>

1. Le masque `255.255.255.0` réserve 8 bits pour le numéro d’hôte, donc on peut connecter au maximum $2^8 - 2 = \boxed{254}$ machines. On enlève bien les deux adresses réservées : celle du réseau et celle de diffusion générale.

2. $217 = 128 + 64 + 16 + 8 + 1 = \boxed{(11011001)_2}$

3. $(110010)_2 = 2 + 16 + 32 = \boxed{50}$

4. Avec le masque `255.255.255.0`, l’adresse réseau de `110.217.53.22` est `110.217.53.0`. Comme cela ne correspond pas à l’adresse du réseau pédagogie 2 `110.217.52.0`, **cette machine n’en fait pas partie**.


5. 
|     Destination     |      Passerelle       |    Interface     |
| :-----------------: | :-------------------: | :--------------: |
| `110.217.50.0` (P1) |        on-link        | `110.217.50.254` |
| `110.217.52.0` (P2) | `110.217.54.253` (R2) | `110.217.54.254` |
| `110.217.54.0` (AD) |        on-link        | `110.217.54.254` |
| `110.217.56.0` (VS) | `110.217.54.253` (R2) | `110.217.54.254` |

6. La table de routage est seulement modifiée pour la destination P2 :
   
    |     Destination     |      Passerelle       |    Interface     |
    | :-----------------: | :-------------------: | :--------------: |
    | `110.217.52.0` (P2) | `110.217.50.253` (R4) | `110.217.50.254` |

7. **Non**, car depuis R2, les chemins vers tous les réseaux restent optimaux, le nouveau routeur R4 ne permet d'établir de route plus courte.

8. L'appel de cette fonction sur deux sommets non reliés peut entraîner une **récursion infinie**. Par exemple, on peut considérer l'appel `rechercher(A, C)` pour le graphe suivant :

    ![](assets/24-NSIJ1PO1-1-Q8.svg){ .center-img }

    Cet appel appelle ensuite `recherche(A, B)` qui appelle `recherche(B, A)` qui appelle `recherche(A, B)` etc.

9.  Une solution serait de **marquer les sommets déjà visités**, on aboutirait alors à un parcours en profondeur classique.

</div>
