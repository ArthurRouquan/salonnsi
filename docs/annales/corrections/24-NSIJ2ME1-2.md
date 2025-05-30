---
title: 24-NSIJ2ME1-2
---

<div class="circle-ol" markdown>

1. 
```python
class Marchandise:
    def __init__(self, p: int, v: int) -> None:
        assert v > 0
        self.prix = p
        self.volume = v
```

2. `#!py m1 = Marchandise(20, 7)`

3. 
```python
def ratio(self) -> float:
    return self.prix / self.volume
```

4. 
```python
def prixListe(tab: list) -> int:
    total = 0
    for marchandise in tab:
        total += marchandise.prix
    return total
```

5. Les combinaisons possibles respectant la contrainte de capacité de 100 litres : 
   
    |    Combinaison    | Volume total | Prix total |
    | :---------------: | :----------: | :--------: |
    |    $\{ m_1 \}$    |     20L      |    40€     |
    |    $\{ m_2 \}$    |     70L      |    210€    |
    |    $\{ m_3 \}$    |     40L      |    160€    |
    |    $\{ m_4 \}$    |     50L      |    50€     |
    | $\{ m_1,\ m_2 \}$ |     90L      |  **250€**  |
    | $\{ m_1,\ m_3 \}$ |     60L      |    200€    |
    | $\{ m_1,\ m_4 \}$ |     70L      |    90€     |
    | $\{ m_3,\ m_4 \}$ |     90L      |    210€    |

    La combinaison optimale qui maximise le prix est donc $\{ m_1,\ m_2 \}$.

6.  L'algorithme précédent est un algorithme **glouton**.

7. 
```python hl_lines="6 7 8"
def tri(tab: list) -> None:
    n = len(tab)
    for i in range(1, n):
        marchandise = tab[i]
        j = i - 1
        while j >= 0 and marchandise.ratio() > tab[j].ratio():
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = marchandise
```

8. La fonction `tri` est un **tri par insertion** dont le coût temporel est **quadratique** $O(n^2)$ dans le pire des cas.

9. 
```python hl_lines="5 6 7 8 9"
def charge(tab: list, volume: int) -> list:
    tri(tab)
    chargement = []
    n = len(tab)
    for marchandise in tab:
        if marchandise.volume >= volume:
            chargement.append(marchandise)
            volume -= marchandise.volume
    return chargement
```

10. 
```python hl_lines="2 3 8 9 11 13"
def chargeOptimale(tab: list, v_restant: int, i: int) -> list:
    if i >= len(tab):
        return []
    else:
        if tab[i].volume > v_restant:
            return chargeOptimale(tab, v_restant, i + 1)
        else:
            option1 = chargeOptimale(tab, v_restant, i + 1)
            option2 = [tab[i]] + chargeOptimale(tab, v_restant - tab[i].volume, i + 1)
            if prixListe(option1) > prixListe(option2):
                return option1
            else:
                return option2
```

</div>