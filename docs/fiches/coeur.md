---
title: Programmes à connaître
icon: material/language-python
---

## Général

=== "Échanger le contenu de deux variables" 

    ```{.python .no-copy}
    copie = a
    a = b
    b = copie
    ```

=== "En une ligne" 

    ```{.python .no-copy}
    a, b = b, a  # création d'un tuple (b, a) puis déballage
    ```

## Listes

=== "Parcours par indice" 

    ```{.python .no-copy title="Complexité $O(n)$"}
    for i in range(len(tab)):
        print(i, tab[i])
    ```

=== "Parcours par élément" 

    ```{.python .no-copy title="Complexité $O(n)$"}
    for valeur in tab:
        print(valeur)
    ```

<span></span>

=== "Somme"

    ```{.python .no-copy title="Complexité $O(n)$"}
    def somme(tab):
        total = 0
        for valeur in tab:
            total = total + valeur
        return total
    ```

=== "Moyenne"

    ```{.python .no-copy title="Complexité $O(n)$"}
    def moyenne(tab):
        total = 0
        for valeur in tab:
            total = total + valeur
        return total / len(tab)
    ```

=== "Moyenne pondérée"

    ```{.python .no-copy title="Complexité $O(n)$"}
    def moyenne_ponderee(notes, coeffs):
        total = 0
        total_coeffs = 0
        for i in range(len(tab)):
            total += notes[i] * coeffs[i]
            total_coeffs += coeffs[i]
        return total / total_coeffs
    ```

=== ":octicons-terminal-16:"

    ```{.pycon .console .no-copy title="Complexité $O(n)$"}
    >>> tab = [12, 21, 37, 42]
    >>> somme(tab)
    112
    >>> moyenne(tab)
    28.0
    >>> moyenne_ponderee(tab, [1, 1, 1, 2])
    30.8
    ```

<span></span>

=== "Recherche linéaire" 

    ```{.python .no-copy title="Complexité $O(n)$"}
    def rechercher(tab, x):
        """ Renvoie True si x est présent dans tab, False sinon. """
        for valeur in tab:
            if valeur == x:
                return True
        return False
    ```

    L'expression `#!py rechercher(tab, x)` est équivalent à `x in tab`.

=== "Indice" 

    ```{.python .no-copy title="Complexité $O(n)$"}
    def rechercher_indice(tab, x):
        """ Renvoie l'indice de la 1ère occurence de x s'il est présent dans tab, None sinon. """
        for i in range(len(tab)):
            if tab[i] == x:
                return i
        return None
    ```

=== "Tous les indices" 

    ```{.python .no-copy title="Complexité $O(n)$"}
    def rechercher_indices(tab, x):
        """ Renvoie tous les indices où apparaît x dans tab. """
        indices = []
        for i in range(len(tab)):
            if tab[i] == x:
                indices.append(i)
        return indices
    ```

=== "Nombre d'occurences" 

    ```{.python .no-copy title="Complexité $O(n)$"}
    def compter(tab, x):
        """ Renvoie le nombre d'occurences de x dans tab. """
        compteur = 0
        for valeur in tab:
            if valeur == x:
                compteur += 1
        return compteur
    ```

=== ":octicons-terminal-16:"

    ```{.pycon .console .no-copy}
    >>> tab = [12, 42, 21, 37, 42]
    >>> rechercher(tab, 42)
    True
    >>> rechercher_indice(tab, 42)
    1
    >>> rechercher_indices(tab, 42)
    [1, 4]
    >>> compter(tab, 42)
    2
    ```

<span></span>

=== "Minimum"

    ```{.python .no-copy title="Complexité $O(n)$"}
    def minimum(tab):
        """ Renvoie le minimum de tab. """
        mini = tab[0]  # minimum courant
        for valeur in tab:
            if valeur < mini:
                mini = valeur
        return mini
    ```

=== "Indice"

    ```{.python .no-copy title="Complexité $O(n)$"}
    def indice_minimum(tab):
        """ Renvoie le 1er indice du minimum de tab. """
        m = 0  # indice du minimum courant
        for i in range(len(tab)):
            if tab[i] < tab[m]:
                m = i
        return m
    ```

=== "Tous les indices"

    ```{.python .no-copy title="Complexité $O(n)$"}
    def indices_minimum(tab):
        """ Renvoie les indices où apparaît le minimum de tab. """
        indices = [0] # indices du minimum courant
        for i in range(len(tab)):
            if tab[i] < indices[m]:
                indices = [i]
            elif tab[i] == indices[m]:
                indices.append(i)
        return indices
    ```

=== ":octicons-terminal-16:"

    ```{.pycon .console .no-copy}
    >>> tab = [21, 37, 7, 42, 7]
    >>> minimum(tab)
    True
    >>> minimum_indice(tab)
    2
    >>> minimum_indices(tab)
    [2, 4]
    ```

<span></span>

=== "Tri par sélection"

    ```{.python .no-copy title="Complexité $O(n^2)$"}
    def tri_selection(tab):
        for i in range(len(tab) - 1):
            # Détermine l'indice du minimum à partir de l'indice i
            m = i
            for j in range(i + 1, len(tab)):
                if tab[j] < tab[m]:
                    m = j
            # Échange le contenu de tab[i] et tab[m]
            tab[i], tab[m] = tab[m], tab[i] 
    ```

=== "Tri par insertion"

    ```{.python .no-copy title="Complexité $O(n^2)$"}
    def tab_insertion(tab):
        for i in range(len(tab)):
            valeur = tab[i]  # valeur à insérer
            # Décale tant que la valeur précédent est plus grand
            j = i
            while j > 0 and tab[j] > valeur:
                tab[j] = tab[j - 1]
                j -= 1
            tab[j] = valeur  # insertion
    ```

=== "Tri fusion"

    ```{.python .no-copy title="Complexité $O(n \log n)$"}
    def fusionner(A, B):
        """ Fusionne deux listes triées en une seule liste triée. """
        F = []
        a, b = 0, 0  # indices pour parcourir A et B
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                F.append(A[a])
                a += 1
            else:
                F.append(B[b])
                b += 1
    
        return F + A[a:] + B[b:]  # ajoute les éléments restants

    def tri_fusion(tab):
        if len(tab) == 1:  # cas de base
            return tab
        m = len(tab) // 2
        G, D = tab[:m], tab[m:]              # Étape 1. Diviser
        G, D = tri_fusion(G), tri_fusion(D)  # Étape 2. Régner 
        return fusionner(G, D)               # Étape 3. Combiner
    ```

<span></span>

=== "Recherche dichotomique"

    ```{.python .no-copy title="Complexité $O(\log n)$"}
    def dichotomie(tab, x):
        """ Recherche l'élément x dans la liste triée tab par dichotomie
            et retourne son indice s'il existe, None sinon. """
        i, j = 0, len(tab) - 1  # indices de la fenêtre de recherche
        while i <= j:  # tant qu'il reste des éléments à tester
            m = (i + j) // 2
            if tab[m] == x:
                return m
            elif tab[m] < x:
                i = m + 1
            else:
                j = m - 1
        return None
    ```

=== "Version récursive"

    ```{.python .no-copy title="Complexité $O(\log n)$"}
    def dichotomie_bornes(tab, x, i, j):
        if i > j:  # cas de base, si la fenêtre de recherche est vide
            return None
        m = (i + j) // 2
        if tab[m] == x:
            return m
        elif tab[m] < x:
            return dichotomie_bornes(tab, x, m + 1, j)
        else:
            return dichotomie_bornes(tab, x, i, m - 1)

    def dichotomie(tab, x):
        return dichotomie_bornes(tab, x, 0, len(tab) - 1)
    ```

=== ":octicons-terminal-16:"

    ```{.pycon .console .no-copy}
    >>> dichotomie([12, 21, 37, 42], 37)
    2
    >>> dichotomie([12, 21, 37, 42], 90)
    None
    ```

## Chaînes

Une chaîne de caractères est une **liste** de caractères, tous les algorithmes précédents peuvent s'y appliquer.

## Dictionnaires

=== "Parcours par clé" 

    ```{.python .no-copy}
    for cle in dico:
        print(cle)
    ```

=== "Parcours par valeur" 

    ```{.python .no-copy}
    for valeur in dico.values():
        print(valeur)
    ```

=== "Parcours par clé et valeur" 

    ```{.python .no-copy}
    for cle, valeur in dico.items():
        print(cle, valeur)
    ```

<span></span>

=== "Utilisation comme compteur" 

    ```{.python .no-copy}
    def compter(tab):
        compteurs = {}
        for valeur in tab:
            if valeur in tab:
                compteurs[valeur] += 1
            else:
                compteurs[valeur] = 1
        return compteurs
    ```
