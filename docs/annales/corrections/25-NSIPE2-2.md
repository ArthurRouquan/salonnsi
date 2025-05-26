---
title: 25-NSIPE2-2
---

<div class="circle-ol" markdown>

1. 
    * Exemple de **feuille** : $\small (\texttt{j},\ 1)$
    * La **racine** de l'arbre :  $\small (\texttt{ }-\texttt{j}-\texttt{f}-\texttt{e}-\texttt{l}-\texttt{i}-\texttt{p}-\texttt{t}-\texttt{a}-\texttt{u},\ 19)$

2. Le nœud correspondant au caractère $\texttt{p}$ se situe à 4 arêtes de la racine, donc sa profondeur est de **4**. Son code associé est $\texttt{1100}$.

3. Suivant cette compression, plus un caractère est fréquent, plus son code binaire associé est court, ce qui réduit la longueur totale du message compressé.

4. 
```python hl_lines="3 4 5 6 9"
class Noeud:
    def __init__(self, nom, nb_occu, fils_g, fils_d):
        self.nom = nom
        self.nb_occu = nb_occu
        self.fils_g = fils_g
        self.fils_d = fils_d

    def __str__(self):
        return '(' + self.nom + ',' + str(self.nb_occu) + ')'
```

5. 
```python hl_lines="2 4 7 8 10 11"
def liste_occurrences(chaine):
    dico = {}
    for c in chaine:
        if c in dico:
            dico[c] = dico[c] + 1
        else:
            dico[c] = 1
    liste_res = []
    for cle in dico:
        liste_res.append((cle, dico[cle]))
    return liste_res
```

6. 
```python hl_lines="3 5 7 8"
def tri_liste(liste_a_trier):
    liste_triee = []
    for i in range(0, len(liste_a_trier)):
        element = liste_a_trier[i]
        j = 0
        while j < len(liste_triee) and element[1] >= liste_triee[j][1]:
            j += 1
        liste_triee.insert(j, element)
    return liste_triee
```

7. 
```python
def conversion_en_noeuds(liste_tuples):
    return [Noeud(nom, nb_occu, None, None) for nom, nb_occu in liste_tuples]
```

    Ou plus simplement :

    ```python
    def conversion_en_noeuds(liste_tuples):
        liste_noeuds = []
        for nom, nb_occu in liste_tuples:
            liste_noeuds.append(Noeud(nom, nb_occu, None, None))
        return liste_noeuds
    ```

8. 
```python hl_lines="3 4 5"
def insere_noeud(noeud, liste_noeud):
    j = 0
    while j < len(liste_noeud) and noeud.nb_occu > liste_noeud[j].nb_occu:
        j += 1
    liste_noeud.insert(j, noeud)
```

9. 
```python hl_lines="2 6 7 8 9"
def construit_arbre(liste):
    while len(liste) > 1:
        noeud1 = liste.pop(0)
        noeud2 = liste.pop(0)
        nom_noeud_pere = noeud1.nom + "-" + noeud2.nom
        nb_occu_noeud_pere = noeud1.nb_occu + noeud2.nb_occu
        noeud_pere = Noeud(nom_noeud_pere, nb_occu_noeud_pere, noeud1, noeud2)
        insere_noeud(noeud_pere, liste)
    return liste[0]
```

10. Il s'agit d'un **dictionnaire** où chaque clé est un caractère et sa valeur associée son code binaire. Les clés et les valeurs sont des chaînes de caractères.

11. 
```python
def compresse(texte, dico_code):
    texte_compresse = ''
    for caractere in texte:
        texte_compresse += dico_code[caractere]
    return texte_compresse
```

</div>