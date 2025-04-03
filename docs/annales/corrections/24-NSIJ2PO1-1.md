---
title: 24-NSIJ2PO1-1
---

<div class="circle-ol" markdown>

1. Le plus court chemin est **Mp → Ar → Ax → Nc** de longueur 80 + 76 + 176 = **332** km.
   
2. Les deux chemins possibles sont :
    * **Mp → Ar → Ax → Nc**
    * **Mp → Ar → Mr → Nc**

3. 
```python
G = {
    'Av': ['Mr', 'Ni', 'Ax'],
    'Ni': ['Av', 'Ar', 'Mp'],
    'Mp': ['Ni', 'Ar'],
    'Ar': ['Mr', 'Mp', 'Ax', 'Mr'],
    'Mr': ['Av', 'Ar', 'Ax', 'To', 'Nc'],
    'Ax': ['Av', 'Ar', 'Mr', 'To', 'Nc', 'Di'],
    'To': ['Mr', 'Nc', 'Ax'],
    'Nc': ['Mr', 'To', 'Ax', 'Di'],
    'Di': ['Nc', 'Ax']
}
```

1. LIFO signifie ***Last In First Out*** (dernier entré, premier sorti) et FIFO signifie ***First In First Out*** (premier entré, premier sorti).

2. La structure de file est une structure de type **FIFO**.

3. `#!py parcours(G, 'Av')` renvoie `#!py ['Av', 'Mr', 'Ni', 'Ax', 'Ar', 'To', 'Nc', 'Mp', 'Di']`.

4. La fonction `parcours` est un **parcours en largeur**.

5. 
```python hl_lines="5 12 13"
def distance(graphe, sommet):
    f = creerFile()
    enfiler(f, sommet)
    visite = [sommet]
    distances = {sommet: 0}
    while not estVide(f):
        s = defiler(f)
        for v in graphe[s]:
            if not (v in visite):
                visite.append(v)
                enfiler(f, v)
                distances[v] = distances[s] + 1
    return distances
```

1.  `#!py distance(G, 'Av')` renvoie `#!py {'Av': 0, 'Mr': 1, 'Ni': 1, 'Ax': 1, 'Ar': 2, 'To': 2, 'Nc': 2, 'Mp': 2, 'Di': 2}`.

2.  
```python
def parcours2(G, s):
    p = creerPile()
    empiler(p, s)
    visite = []  # erreur du sujet
    while not estVide(p):
        x = depiler(p)
        if x not in visite:
            visite.append(x)
            for v in G[x]:
                empiler(p, v)
    return visite
```

1.  `parcours2` est un **parcours en profondeur** itératif, ainsi `#!py parcours2(G, 'Av')` peut renvoyer `#!py ['Av', 'Ax', 'Di', 'Nc', 'To', 'Mr', 'Ar', 'Mp', 'Ni']`.

</div>
