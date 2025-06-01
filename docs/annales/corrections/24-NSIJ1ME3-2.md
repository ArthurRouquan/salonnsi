---
title: 24-NSIJ1ME3-2
---

<div class="circle-ol" markdown>

1. P2 est connecté au réseau L1 constitué de P1 et R1. Comme P1 a pour adresse IP `192.168.1.10`, on en déduit que le routeur R1 est connecté au réseau via l'interface 1 `192.168.1.1/24`. Donc une adresse possible pour P2 est `192.168.1.2`.

2. D'après le tableau, on déduit que R9 est connecté à R7 via le réseau `192.168.16.0` et à R8 via le réseau `192.168.17.0`. On déduit de sa dernière interface restante, l'adresse réseau de L2, à savoir `192.168.18.0`. Puisque le numéro d'hôte s'écrit sur 32 – 24 = 8 bits, alors il existe $2^8 - 3 = \boxed{253}$ adresses IP disponibles pour P3 et P4. On enlève bien les trois adresses réservées : celle du réseau, celle de diffusion générale et celle du routeur.

3. 
```python
G = {
    'R1': ['R2', 'R3', 'R4', 'R6'],
    'R2': ['R1', 'R3', 'R5'],
    'R3': ['R1', 'R2', 'R5', 'R6'],
    'R4': ['R1', 'R6'],
    'R5': ['R2', 'R3', 'R6', 'R7'],
    'R6': ['R1', 'R3', 'R4', 'R5', 'R7', 'R8'],
    'R7': ['R5', 'R6', 'R8', 'R9'],
    'R8': ['R6', 'R7', 'R9'],
    'R9': ['R7', 'R8']
}
```

4. 
| Destination |   Suivant    | Nombre de sauts |
| :---------: | :----------: | :-------------: |
|     R2      |      R2      |        1        |
|     R3      |      R3      |        1        |
|     R4      |      R4      |        1        |
|     R5      | R2 / R3 / R6 |        2        |
|     R6      |      R6      |        1        |
|     R7      |      R6      |        2        |
|     R8      |      R6      |        2        |
|     R9      |      R6      |        3        |

5. Le paquet suit la route **P1 → R1 → R6 → R7 ou R8 → R9 → P3** et effectue donc **4 sauts** selon le protocole RIP (4 routeurs traversés).

6. 
```python
M = [
    [0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0] 
]
```

7. 
```python hl_lines="3 5 6"
def degre(MATRICE):
    d = []
    for ligne in MATRICE:
        cpt = 0
        for v in ligne:
            cpt = cpt + v
        d.append(cpt)
    return d
```

8. L'appel `#!py degre(M)` renvoie `#!py [4, 3, 4, 2, 4, 6, 4, 3, 2]`.

9. Le graphe est connexe et possède deux sommets de degré impair, R2 et R8, donc il admet une chaîne eulérienne. Ainsi le robot peut parcourir l'ensemble du réseau en empruntant chaque fibre optique une et une seule fois.

10. On calcule au préalable le coût pour chaque bande passante :

    | Bande passante |             Coût              |
    | :------------: | :---------------------------: |
    |   10 Mbit/s    | $10^8 / (10 \cdot 10^6) = 10$ |
    |   50 Mbit/s    | $10^8 / (50 \cdot 10^6) = 2$  |
    |   100 Mbit/s   | $10^8 / (100 \cdot 10^6) = 1$ |

    Ainsi le paquet suit la route **P1 → R1 → R2 → R5 → R6 → R7 → R9 → P3** pour un coût total de $1 + 1 + 1 + 1 + 2 = \boxed{6}$.
</div>
