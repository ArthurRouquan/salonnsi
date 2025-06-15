---
title: 25-NSIJ2JA1-2
---

<!--NAVIGATION_START-->
<div class="center-button" markdown>
[:material-arrow-left:](25-NSIJ2JA1-1.md){ .md-button .nav-button }
[:fontawesome-solid-file-pdf: &nbsp; Énoncé](../exercices/25-NSIJ2JA1-2.pdf){ .md-button }
[:fontawesome-solid-file-pdf: &nbsp; Sujet](../sujets/25-NSIJ2JA1.pdf){ .md-button }
[:material-arrow-right:](25-NSIJ2JA1-3.md){ .md-button .nav-button }
</div>
<!--NAVIGATION_END-->

<div class="circle-ol" markdown>

1. Ce type de programme est un **ordonnanceur**.

2. Un processus est dans un des états suivants : **Prêt**, **Élu** ou **Bloqué**.

3. La structure la plus adaptée serait une **file** (proposition **2**). En effet, on souhaite modéliser ici une *file* d'attente des processus, où le premier processus arrivé est le premier servi (élu).

4. 
```python hl_lines="2 3 4"
class Processus:
    def __init__(self, PID, priorite, temps_CPU):
        self.priorite = priorite
        self.PID = PID
        self.temps_utilisation = 0
        self.temps_CPU = temps_CPU
```

5. 
| Cycle | Processus élu | `liste_files`            |
| :---: | :-----------: | :----------------------- |
|   0   |       –       | `[[P3, P2, P1], [], []]` |
|   1   |     `P1`      | `[[P3, P2], [], []]`     |
|   2   |     `P2`      | `[[P3], [P1], []]`       |
|   3   |     `P3`      | `[[], [P2, P1], []]`     |
|   4   |     `P3`      | `[[], [P2, P1], []]`     |
|   5   |     `P1`      | `[[], [P2], [P3]]`       |

6.  
Lorsqu'un processus est élu, sa priorité diminue de 1 à chaque cycle. Ainsi, après seulement 5 cycles d'exécution, la priorité d'un long processus qui nécessite 1000 cycles pour terminer, sera de 5. Or, dans la situation où de nouveaux processus très courts apparaissent sans cesse avec une priorité inférieure ou égale à 4, il ne pourra plus jamais être réélu. **Ce long processus ne se termine donc jamais, car ces courts processus toujours plus prioritaires l'empêchent d'être réélu.**

7. Grâce à ce mécanisme, lorsqu'un long processus attend trop longtemps (au-delà de `Max_Temps`), il voit sa priorité remonter à chaque cycle d'attente, possiblement jusqu'à être mis dans la file la plus prioritaire. Il peut ainsi redevenir prioritaire face aux nouveaux processus plus courts et se faire réélire. Tout processus se termine donc en temps fini.

8. 
```python
def meilleur_priorite(liste_files):
    for i in range(len(liste_files)):
        if liste_files[i]:  # si la liste est non-vide
            return i
    return None
```

9. 
```python
def prioritaire(liste_files):
    i = meilleur_priorite(liste_files)
    if i is None:
        return None
    else:
        return liste_files[i].pop()
```

10. La question n'indique pas explicitement si la fonction `gerer` effectue un cycle ou une simulation complète. Je suppose ici une simulation complète.

    === "Version fidèle"

        ```python
        def gerer(p, liste_files):
            while True:
                if p is None:  # si aucun processus élu
                    p = prioritaire(liste_files)
                    if p is None:  # aucun processus en attente
                        return
                else:
                    if p.temps_utilisation == p.temps_CPU:
                        p = None
                    else:
                        print(f'Exécution de P{p.PID}')
                        p.temps_utilisation += 1
                        i = meilleur_priorite(liste_files)
                        if i is not None and i <= p.priorite:
                            p.priorite += 1
                            if p.priorite == len(liste_files):
                                liste_files.append([p])  # création d'une nouvelle file de priorité
                            else:
                                liste_files[p.priorite].insert(0, p)
                            p = prioritaire(liste_files)
                        else:
                            p.priorite += 1
        ```

    === "Version simplifiée"

        ```python
        def gerer(p, liste_files:
            while p and p.temps_utilisation < p.temps_CPU or (p := prioritaire(liste_files)):
                print(f'Exécution de P{p.PID}')
                p.temps_utilisation += 1
                p.priorite += 1
                if (i := meilleur_priorite(liste_files)) is not None and i < p.priorite:
                    if p.priorite == len(liste_files):
                        liste_files.append([])
                    liste_files[p.priorite].insert(0, p)
                    p = prioritaire(liste_files)
        ```

</div>
