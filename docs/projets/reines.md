---
icon: lucide/chess-queen
---

# Le problème des reines

## Description

Comment placer $N$ reines sur un échiquier $N \times N$ **sans qu'aucune ne puisse en menacer une autre&nbsp;?**

![](assets/queens.jpg){ .rounded-img }
/// caption
Illustration de Samuel Velasco pour Quanta Magazine.
///

Une reine menace toutes les cases de sa **ligne**, de sa **colonne** et de ses deux **diagonales**. Deux reines ne doivent donc partager ni ligne, ni colonne, ni diagonale.

Pour $N = 8$, il existe 92 solutions. Pour $N = 2$ et $N = 3$, il n'en existe aucune.

Ce [problème](https://fr.wikipedia.org/wiki/Problème_des_huit_dames) se résout exactement comme le sudoku vu en cours&nbsp;: on fait un choix, on poursuit la résolution avec ce choix, on annule le choix. C'est du **backtracking** (retour sur trace).

## Rendu attendu

* Un **compte rendu** qui reprend les questions une par une, dans l'ordre, avec pour chacune la réponse (explication, pseudocode, tableau de mesures ou extrait de code selon la question).

* Un **fichier `.py`** contenant l'ensemble du code dans sa version finale&nbsp;: `#!py afficher`, `#!py est_compatible` et `#!py placer`. Le code doit s'exécuter sans erreur et chaque fonction doit être commentée.

## Représentation d'une solution

Puisque deux reines ne peuvent pas être sur la même ligne, une solution contient exactement une reine par ligne. On va donc construire la solution **ligne après ligne**&nbsp;: pour la ligne $0$, **on choisit la colonne où placer la reine**&nbsp;; puis pour la ligne $1$, on choisit sa colonne&nbsp;; et ainsi de suite jusqu'à la ligne $N - 1$.

<div class="sl-steps" start="1" markdown>
1. Avec cette façon de procéder, quelles sont les contraintes qu'il reste à vérifier à chaque choix&nbsp;?
</div>

On représente une solution (partielle ou complète) par une liste `#!py reines` de longueur $N$, où `#!py reines[i]` est la colonne de la reine de la ligne `#!py i`, et `#!py -1` si la ligne n'est pas encore remplie.

<div class="sl-steps" start="2" markdown>
2. Soit la solution suivante pour $N = 4$. Donner la liste `#!py reines` qui représente cette solution avec la représentation décrite ci-dessus.

    ```
    . R . .
    . . . R
    R . . .
    . . R .
    ```

3. Écrire la fonction `#!py afficher(reines)` qui affiche l'échiquier avec `R` pour une reine et `.` pour une case vide, comme ci-dessus.
</div>

## Résolution par backtracking

<div class="sl-steps" start="4" markdown>

4. Écrire la fonction `#!py est_compatible(reines, ligne, colonne)` qui renvoie `#!py True` si on peut placer une reine en `#!py (ligne, colonne)` sans qu'elle soit menacée par les reines déjà placées dans les lignes `#!py 0` à `#!py ligne - 1`.

    !!! info "Indice"
        Les cases `#!py (i, j)` et `#!py (k, l)` sont en diagonale si `#!py abs(i - k) == abs(j - l)`.

5. Écrire le pseudocode de la fonction `#!py placer(reines, ligne)` sur le modèle de `#!py remplir(grille)` vu en cours. Identifier clairement&nbsp;:

    - le ou les **cas de base**&nbsp;;
    - le **cas récursif**&nbsp;;
    - l'endroit où l'on **fait un choix** et celui où l'on **annule le choix**.

6. Traduire ce pseudocode en Python. La fonction doit simplement **afficher** chaque solution trouvée.

    ```python
    def placer(reines, ligne):
        # à compléter
    ```

    !!! info "Ça marche&nbsp;?"
        Vérifier le programme sur $N = 4$ (2 solutions), puis sur $N = 8$ (92 solutions).

7. Modifier la fonction pour qu'elle **renvoie le nombre de solutions** au lieu de les afficher.

</div>

## Expérimentation

<div class="sl-steps" start="8" markdown>

8. Ajouter une variable globale pour compter le nombre d'appels à `#!py placer`, remise à zéro avant chaque résolution.

9. Compléter le tableau suivant en mesurant le temps d'exécution avec `#!py time.perf_counter()`&nbsp;:

    /// html | div.center-table
    | Nombre de reines | Nombre de solutions | Nombre d'appels à `#!py placer` | Temps (s) |
    |:---:|:---:|:---:|:---:|
    | 4 | | | |
    | 5 | | | |
    | 6 | | | |
    | 7 | | | |
    | 8 | | | |
    | 9 | | | |
    | 10 | | | |
    | 11 | | | |
    | 12 | | | |
    ///

10. Tracer deux graphiques en fonction de $N$ : le nombre d'appels à `#!py placer`, et le temps d'exécution. Quelle est l'allure de ces courbes ? Que devient cette allure avec une échelle logarithmique sur l'axe vertical ?

11. Ajouter sur le graphique du nombre d'appels les courbes de $N^N$ et de $N!$. Que constate-t-on, et comment l'expliquer ?

12. Quel est le nombre maximal d'appels à `placer` en cours *en même temps* ?

</div>



