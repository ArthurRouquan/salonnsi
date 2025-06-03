---
title: 24-NSIG11BIS-3
---

<div class="circle-ol" markdown>

1. `#!py print(tab_trace[-1][1])`

2. 
```python hl_lines="6 7 8"
def creation_trace(tab_trace):
    trace = []
    for enregistrement in tab_trace:
        pt = {}
        pt['lat'] = float(enregistrement[0])
        pt['lon'] = float(enregistrement[1])
        pt['alt'] = int(enregistrement[2])
        pt['tsp'] = int(enregistrement[3])
        trace.append(pt)
    return trace
```

3. 
```python
def valeurs_altitude(trace):
    return [enregistrement['alt'] for enregistrement in trace]
```

4. 
```python
def denivele(altitudes):
    positif = negatif = 0
    for i in range(len(altitudes) - 1):
        difference = altitudes[i + 1] - altitudes[i]
        if difference > 0:
            positif += difference
        else:
            negatif -= difference
    return positif, negatif
```

5. 
```python
def asc_desc(trace):
    tascension = tdescente = tplat = 0
    for i in range(len(trace) - 1):
        dt = trace[i + 1]['tsp'] - trace[i]['tsp']
        da = trace[i + 1]['alt'] - trace[i]['alt']
        if da > 0:
            tascension += dt
        elif da < 0:
            tdescente += dt
        else:
            tplat += dt
    return tascension, tdescente, tplat
```

6. 
```python
from math import cos, sin, acos, radians

def distance(p1: dict, p2: dict) -> float:
    RAYON_TERRE = 6371000
    latA, lonA = radians(p1['lat']), radians(p1['lon'])
    latB, lonB = radians(p2['lat']), radians(p2['lon'])
    return RAYON_TERRE * acos(
        sin(latA) * sin(latB) +
        cos(latA) * cos(latB) * cos(lonA - lonB)
    )
```

7. 
```python
from math import sqrt  # square root, racine carrée

def distance_precise(p1: dict, p2: dict) -> float:
    dx = distance(p1, p2)
    dy = p2['alt'] - p1['alt']
    return sqrt(dx * dx + dy * dy)
```

8. 
|   `lieu`   | `dist` |
| :--------: | :----: |
| Mont Blanc |  21.3  |
| Mont Blanc |  171   |

9. 
```sql
SELECT id, lieu
FROM trails
WHERE dist > 50;
```

10. 
```sql
SELECT lieu, dist
FROM trails
WHERE denivele_p != denivele_n;
```

11. 
```sql
SELECT SUM(dist)
FROM trails
WHERE denivele_p > 1000;
```

</div>
