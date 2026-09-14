
# Sujet 26-NSIJ2AN1


* Sujet complet
* Exercice 1
* Exercice 2
* Exercice 3



## Exercice 1

*Cet exercice porte sur l’architecture matérielle, les systèmes d’exploitation, et les structures de données linéaires en Python.*

Un système d’exploitation permet d’exécuter plusieurs applications à la fois en donnant l’impression qu’elles fonctionnent simultanément. En réalité, le système répartit le temps de calcul du processeur entre les différents processus, de sorte qu’ils s’exécutent chacun à leur tour très rapidement.

Chaque application peut être représentée par un ou plusieurs processus, gérés par le système d’exploitation. Même si un seul processus utilise réellement le processeur à un instant donné, cette alternance rapide donne l’impression que tout s’exécute en même temps. Lorsque le système interrompt un processus pour en exécuter un autre, on parle de *préemption*.

### Partie A


<div class="sl-steps" markdown>

1. Recopier et compléter le schéma ci-dessous avec les termes suivants&nbsp;: «&nbsp;élu&nbsp;», «&nbsp;prêt&nbsp;», «&nbsp;bloqué&nbsp;», «&nbsp;élection&nbsp;», «&nbsp;blocage&nbsp;», «&nbsp;déblocage&nbsp;».


    ![](assets/26-NSIJ2AN1-1.1.svg){ .center-img }
    /// caption
    Figure 1. États d’un processus.
    ///

    ??? success "Solution"
        ![](assets/26-NSIJ2AN1-1.1C.svg){ .center-img }

</div>

On peut imaginer, par exemple, une application de streaming musical qui se compose de trois processus&nbsp;:

* le processus P1 gère l’interface utilisateur et interagit avec les composants visibles&nbsp;: listes de morceaux, boutons de lecture-pause, etc.&nbsp;;
* le processus P2 assure le téléchargement de la musique et l’écrit dans une mémoire cache locale&nbsp;;
* le troisième processus P3, qu’on pourrait appeler lecteur audio, assure le
décodage audio et envoie le flux de données au système pour lecture.

Voici une situation de fonctionnement&nbsp;:

* l’utilisateur décide de mettre l’application en arrière-plan, cachant ainsi l’interface utilisateur&nbsp;;
* le processus P2 attend un accès à la carte WIFI pour recharger des données&nbsp;;
* le processus P3 décode de la musique et l’envoie au système.

<div class="sl-steps" start="2" markdown>
2. Indiquer l’état de chacun des trois processus P1, P2 et P3 dans cette situation.

    ??? success "Solution"
        * P1 est **bloqué**&nbsp;;
        * P2 est **bloqué**&nbsp;;
        * P3 est **élu**.

3. Expliquer, de façon générale, quand est-ce qu’un interblocage de processus peut survenir.

    ??? success "Solution"
        L'interblocage est une situation où plusieurs processus sont bloqués, chacun attendant une ressource détenue par un autre, aboutissant à un blocage mutuel et permanent.
</div>

On considère plusieurs ressources dont un processeur graphique (GPU), un microphone (MIC), une caméra (CAM) et un processeur dédié au calcul (CAL). On suppose que chacune de ces ressources ne peut être utilisée que par un seul processus à la fois.

On considère de plus quatre processus nommés P1, P2, P3 et P4. Le tableau suivant récapitule les ressources utilisées par chacun des quatre processus, dans l’ordre où chacun des processus les demande&nbsp;:

<div class="center-table" markdown>
| P1 | P2 | P3 | P4 |
|:---:|:---:|:---:|:---:|
| demander MIC | demander CAL | demander CAM | demander GPU |
| demander CAL | demander MIC | libérer CAM | demander CAL |
| libérer CAL | libérer MIC | demander CAL | demander CAM |
| libérer MIC | libérer CAL | demander MIC | libérer CAM |
| demander CAM | demander CAM | libérer MIC | libérer CAL |
| demander GPU | libérer CAM | libérer CAL | demander MIC |
| libérer CAM | | demander GPU | libérer GPU |
| libérer GPU | | libérer GPU | libérer MIC |
</div>

<div class="sl-steps" start="4" markdown>

4. Les processus s’exécutent de manière concurrente. Justifier qu’une situation d’interblocage peut se produire.

    ??? success "Solution"
        La situation où&nbsp;:

        * P1 détient MIC et attend CAL
        * P2 détient CAL et attend MIC

        est une situation d'interblocage.



5. Expliquer l’intérêt d’utiliser une machine équipée de plusieurs processeurs plutôt qu’une machine équipée d’un seul processeur.

    ??? success "Solution"
        Sur un processeur (à cœur unique), les processus s'exécutent en alternance&nbsp;: un seul processus est élu à la fois, les autres attendent.
        
        Sur une machine multi-processeur, plusieurs processus peuvent s'exécuter véritablement en parallèle, un par processeur, à condition qu'ils n'entrent pas en concurrence pour une autre ressource partagée. Cela réduit les temps d'attente.




6. Décrire un avantage et un inconvénient des systèmes sur puces, tels que ceux utilisés dans les smartphones.

    ??? success "Solution"

        * **Avantage**&nbsp;: les composants (CPU, RAM etc.) étant sur la même puce, les échanges de données sont plus rapides (débit et latence).
        * **Inconvénient**&nbsp;: en cas de panne, on ne peut pas remplacer un seul composant, il faut changer toute la puce.

</div>

### Partie B

On s’intéresse à un ordonnanceur de type tourniquet (round-robin), dans lequel une durée appelée *quantum* est fixée à 2 ms. Chaque processus, lorsqu’il est défilé de la file d’attente, s’exécute sur le processeur pour une durée au plus égale au *quantum*&nbsp;:

* s’il termine son exécution avant ou à la fin du quantum, un autre processus est défilé de la file d’attente, et celui-ci bénéficie d’un nouveau quantum pour s’exécuter.

* s’il n’a pas terminé son exécution, il est mis en queue de la file d’attente.

De plus, d’autres processus peuvent être ajoutés à la file d’attente au fur et à mesure qu’ils arrivent.

On considère quatre processus nommés P1, P2, P3 et P4. Le tableau suivant donne les informations temporelles les concernant.

<div class="center-table" markdown>
| Processus | Instant d'arrivée | Temps d'exécution total |
|:---------:|:-----------------:|:-----------------------:|
| P1 | 0 ms | 6 ms |
| P2 | 1 ms | 4 ms |
| P3 | 3 ms | 5 ms |
| P4 | 5 ms | 3 ms |
</div>

<div class="sl-steps" start="7" markdown>

7. Recopier et compléter le chronogramme suivant en indiquant quel processus utilise le processeur à chaque instant, de 0 ms à la fin de l’exécution de tous les processus. À titre d’exemple, on a déjà indiqué sur le chronogramme que le processus P1 s’exécute entre les instants 0 ms et 2 ms. De plus on a indiqué sous l’axe du temps les instants d’arrivée des quatre processus.

    ![](assets/26-NSIJ2AN1-1.7.svg)
    /// caption
    Figure 2. Chronogramme à compléter.
    ///

    ??? success "Solution"
        ![](assets/26-NSIJ2AN1-1.7C.svg){ .center-img }
</div>

On souhaite modéliser en Python le comportement de l’algorithme du tourniquet. Chaque processus est représenté par un dictionnaire contenant les clés `#!py 'nom'`, `#!py 'arrivee'` et `#!py 'temps'`, ayant pour valeurs correspondantes le nom (de type `#!py str`), l’instant d’arrivée (de type `#!py int`) et le temps d’exécution restant en millisecondes (de type `#!py int`).

On définit donc ci-dessous quatre variables `P1`, `P2`, `P3` et `P4` représentant les quatre processus considérés ci-avant.

```python
P1 = {'nom': 'P1', 'arrivee': 0, 'temps': 6}
P2 = {'nom': 'P2', 'arrivee': 1, 'temps': 4}
P3 = {'nom': 'P3', 'arrivee': 3, 'temps': 5}
P4 = {'nom': 'P4', 'arrivee': 5, 'temps': 3}
```

Le quantum est fixé à 2 ms grâce à une variable `quantum` (de type `#!py int`).

De plus, on suppose qu’on dispose d’une implémentation de file en Python à travers les fonctions suivantes&nbsp;:

* `creer_file_vide` qui ne prend aucun paramètre et qui renvoie une file vide&nbsp;;
* `est_vide` qui prend en paramètre une file et qui renvoie un booléen indiquant si cette file est vide&nbsp;;
* `enfiler` qui prend en paramètres une file et un élément et qui modifie la file en y ajoutant cet élément en queue (la valeur de retour est `#!py None`)&nbsp;;
* `defiler` qui prend en paramètre une file, qui modifie cette file en enlevant son élément en tête et qui renvoie cet élément.


<div class="sl-steps" start="8" markdown>

8. Donner les instructions qui permettent de créer une file `fp` contenant les processus `P1`, `P2`, `P3` et `P4`, classés par ordre d’arrivée, le premier arrivé étant en tête de la file.

    ??? success "Solution" 
        ```python
        fp = creer_file_vide()
        enfiler(fp, P1)
        enfiler(fp, P2)
        enfiler(fp, P3)
        enfiler(fp, P4)
        ```
</div>

On souhaite créer une fonction `execute_un_processus` qui réalise une étape de l’algorithme du tourniquet. Plus précisément cette fonction prend en paramètres une file de processus non vide `file_d_attente` et un instant `t` donnant le début de cette étape. Elle extrait de la file le processus à exécuter, puis le remet si besoin dans la file d’attente avec le temps d’exécution restant. De plus cette fonction renvoie l’instant auquel cette étape se termine, qui est soit la fin de l’exécution du processus, soit la fin du quantum.

<div class="sl-steps" start="9" markdown>
9. Recopier et compléter le code de la fonction `execute_un_processus` ci-dessous.

    ```python
    def execute_un_processus(file_d_attente, t):
        processus = defiler(file_d_attente)
        if processus['temps'] ... quantum:
            processus['temps'] = ...
            ...
            return t + ...
        else:
            return t + ...
    ```

    ??? success "Solution" 

        ```python
        def execute_un_processus(file_d_attente, t):
            processus = defiler(file_d_attente)
            if processus['temps'] > quantum:
                processus['temps'] -= quantum
                enfiler(file_d_attente, processus)
                return t + quantum
            else:
                return t + processus['temps']
        ```
</div>

On se place maintenant dans le cas où tous les processus sont déjà arrivés, autrement dit tous les processus à traiter sont dans la file que l’on prend en entrée. On ne tiendra donc pas compte des temps d’arrivée dans la suite. On souhaite créer une fonction `execute_tous_processus` qui prend en paramètre une file de processus, qui simule le comportement de l’algorithme du tourniquet sur ces processus jusqu’à les avoir tous complètement exécutés, et qui renvoie à quel instant se termine la dernière de ces exécutions. On suppose que l’exécution de ces processus commence à partir de l’instant 0.


<div class="sl-steps" start="10" markdown>
10. Recopier et compléter le code de la fonction `execute_tous_processus` ci-dessous.

    ```python
    def execute_tous_processus(file_d_attente):
        t = 0
        while ...
            t = ...
        return t
    ```

    ??? success "Solution" 

        ```python
        def execute_tous_processus(file_d_attente):
            t = 0
            while not est_vide(file_d_attente):
                t = execute_un_processus(file_d_attente, t)
            return t
        ```
</div>

## Exercice 2

*Cet exercice porte sur la programmation Python en général, la programmation orientée objet en particulier et la structure de données d’arbre.*

La WTA (Women’s Tennis Association) est l’instance dirigeante du tennis professionnel international féminin, responsable de l’organisation du circuit « WTA Tour » et de l’établissement des classements mondiaux des joueuses. Dans cet exercice, on ne considère que des matchs de tennis en simple, c’est-à-dire des matchs qui opposent uniquement deux joueuses.

### Partie A

On dispose d’une classe `Joueuse` pour modéliser une joueuse de tennis professionnelle du circuit WTA.

```python
class Joueuse:
    def __init__(self, nom, prenom, pays, age, point):
        """nom, prenom et pays sont de type str, age et point de type int"""
        self.nom = nom
        self.prenom = prenom
        self.pays = pays
        self.age = age
        self.point = point  # nombre de points WTA
        self.victoire = 0  # nombre de victoires
        self.defaite = 0  # nombre de défaites
```

<div class="sl-steps" start="1" markdown>
1. Instancier l’objet `pegula` de la classe `Joueuse` qui modélise la joueuse Pegula Jessica de nationalité américaine (`#!py "USA"`), âgée de 29 ans et ayant 6101 points WTA.

    ??? success "Solution" 

        ```python
        pegula = Joueuse('Pegula', 'Jessica', 'USA', 29, 6101)
        ```
</div>

On considère les objets déjà instanciés `gauff`, `paloni`, `sabalenka` et `swiatek` de la classe `Joueuse` représentant respectivement les joueuses&nbsp;:

* Gauff Coco, américaine, âgée de 20 ans et ayant 6063 points WTA&nbsp;;
* Paloni Marta, espagnole, âgée de 23 ans et ayant 4843 points WTA&nbsp;;
* Sabalenka Aryna, biélorusse, âgée de 25 ans et ayant 10541 points WTA&nbsp;;
* Swiatek Iga, polonaise, âgée de 22 ans et ayant 7470 points WTA.

<div class="sl-steps" start="2" markdown>
2. Recopier et compléter le code ci-après de la méthode `ajouter_victoire` de la classe `Joueuse` permettant d’ajouter une victoire à la joueuse en question ainsi qu’une défaite à son adversaire objet de la classe `Joueuse`.

    ```python
    def ajouter_victoire(self, adversaire):
        ...
        ...
    ```

    ??? success "Solution" 
        ```python
        def ajouter_victoire(self, adversaire):
            self.victoire += 1
            adversaire.defaite += 1
        ```
</div>

Lors de la finale du dernier tournoi des masters Marta Paloni a été battue par Iga Swiatek.

<div class="sl-steps" start="3" markdown>
3. Écrire une instruction utilisant la méthode `ajouter_victoire` pour prendre en compte l’issue de ce match.

    ??? success "Solution" 
        ```python
        swiatek.ajouter_victoire(paloni)
        ```
</div>

On souhaite classer les joueuses à l’aide de leurs points WTA. Pour cela il est possible en Python redéfinir l’opérateur de comparaison `#!py <` (strictement inférieur) pour les objets de la classe `Joueuse` en utilisant les points WTA. Ainsi on obtient par exemple&nbsp;:

```python
>>> swiatek < paloni
False
>>> swiatek < sabalenka
True
```

On utilise une liste Python pour stocker des objets de la classe `Joueuse`,

```python
liste_joueuses = [swiatek, gauff, paloni, sabalenka, pegula]
```

que l’on souhaite trier dans l’ordre croissant des points WTA. Pour cela on choisit le tri par insertion dont le code est donné ci-dessous&nbsp;:

```python
def tri_insertion(liste):
    for i in range(1, len(liste)):
    j = i
    while j > 0 and liste[j] < liste[j - 1]:
        # échange les valeurs liste[j] et liste[j-1]
        liste[j], liste[j - 1] = liste[j - 1], liste[j]
        j = j - 1
```

<div class="sl-steps" start="4" markdown>
4. Préciser, sans justifier, le coût temporel du tri par insertion d’une liste de $n$ éléments dans le pire des cas.

    ??? success "Solution"
        $O(n^2)$
</div>

On détaille les étapes du tri par insertion appliqué à la liste `liste_joueuses` dans le tableau ci-dessous, où chaque ligne correspond à un échange entre deux éléments de la liste.

<div class="center-table" markdown>
| Étape | Contenu de `liste_joueuses` |
|:-----:|:---------------------------:|
| 0 | `#!py [swiatek, gauff, paloni, sabalenka, pegula]` |
| 1 | `#!py [gauff, swiatek, paloni, sabalenka, pegula]` |
| ... | ... |
</div>

<div class="sl-steps" start="5" markdown>
5. Recopier et compléter le tableau ci-dessus en ajoutant autant de lignes que nécessaires.

    ??? success "Solution"
        | Étape | Contenu de `liste_joueuses` |
        |:-----:|:---------------------------:|
        | 0 | `#!py [swiatek, gauff, paloni, sabalenka, pegula]` |
        | 1 | `#!py [gauff, swiatek, paloni, sabalenka, pegula]` |
        | 2 | `#!py [gauff, paloni, swiatek, sabalenka, pegula]` |
        | 3 | `#!py [paloni, gauff, swiatek, sabalenka, pegula]` |
        | 4 | `#!py [paloni, gauff, swiatek, pegula, sabalenka]` |
        | 5 | `#!py [paloni, gauff, pegula, swiatek, sabalenka]` |
</div>

Un match de tennis se déroule en plusieurs sets, et chaque set en plusieurs *jeux*. Ayant fixé qui est la joueuse 1 et qui est la joueuse 2, on peut décrire l’issue d’un set à l’aide d’un couple d’entier&nbsp;: le premier entier donne le nombre de jeux gagnés par la joueuse 1 lors de ce set, le second le nombre de jeux gagnés par la joueuse 2 lors de ce set. Le score d’un match est alors décrit par une liste de tuples.

Par exemple, en mai 2024, Swiatek affronte Sabalenka en finale du tournoi «&nbsp;WTA 1000&nbsp;» de Madrid. Ce match s’est déroulé en 3 sets&nbsp;: 7-5, 4-6, 7-6. Swiatek remporte donc la finale 2 sets à 1. La liste de tuples représentant le score de ce match est `#!py [(7,5), (4,6), (7,6)]`.

Aucun cas d’égalité n’est possible.

Pour automatiser la gestion des tournois on crée une classe `Match`.

```python
class Match:
    def __init__(self, intitule, joueuse1, joueuse2):
        self.intitule = intitule
        self.joueuse1 = joueuse1
        self.joueuse2 = joueuse2
        self.gagnante = None
        self.perdante = None
        self.score = None
```

Cette classe est constituée de :

* `self.intitule`, un intitulé du match sous la forme d’une chaîne de
caractères&nbsp;;
* `self.joueuse1` et `self.joueuse2` représentant les deux joueuses, deux
objets de la classe `Joueuse`&nbsp;;
* `self.gagnante` et `self.perdante` représentant la joueuse victorieuse
respectivement la joueuse perdante deux objets de la classe `Joueuse`&nbsp;;
* `self.score` représentant le score du match sous la forme d’une liste de
tuples d’entiers.

Au terme d’un match une fois que le score est connu, on souhaite pouvoir le saisir à l’aide de la méthode `resultat_match(self, score)` de la classe `Match`. Cette méthode prend en paramètre un score sous la forme de liste de tuple de deux entiers et&nbsp;:

* enregistre le score du match&nbsp;;
* détermine la gagnante et la perdante en comptant le nombre de set(s) gagné(s) par chaque joueuse&nbsp;;
* ajoute une victoire à la joueuse gagnante et une défaite à la joueuse perdante.


Par exemple, pour créer un objet `finale_mad_24` représentant le match Swiatek vs Sabalenka décrit précédemment, on utilise les deux instructions suivantes.

```python
# instanciation de la finale Madrid 2024
finale_mad_24 = Match('finale Madrid 24', swiatek, sabalenka)
# mise-à-jour du score du match
finale_mad_24.resultat_match([(7, 5), (4, 6), (7, 6)])
```

<div class="sl-steps" start="6" markdown>
6. Recopier et compléter le code de la méthode `resultat_match` de la classe `Match`. On ajoutera autant de lignes que nécessaire.

    ```python
    def resultat_match(self, score):
        self.score = score
        nb_set_joueuse1 = 0
        nb_set_joueuse2 = 0
        # code incomplet
    ```

    ??? success "Solution" 

        ```python
        def resultat_match(self, score):
            self.score = score

            nb_set_joueuse1 = 0
            nb_set_joueuse2 = 0
            for j1, j2 in score:
                if j1 > j2:
                    nb_set_joueuse1 += 1
                else:
                    nb_set_joueuse2 += 1

            if nb_set_joueuse1 > nb_set_joueuse2:
                self.gagnante = self.joueuse1
                self.perdante = self.joueuse2
            else:
                self.gagnante = self.joueuse2
                self.perdante = self.joueuse1

            self.gagnante.ajouter_victoire(self.perdante)
        ```
</div>

### Partie B

Afin de pouvoir modéliser chaque tour d’un tournoi de tennis à partir des quarts de finale uniquement, on décide d’utiliser un arbre binaire.

![](assets/26-NSIJ2AN1-2.7.svg){ .center-img }
/// caption
Figure 1. Tournoi de tennis.
///

<div class="sl-steps" start="7" markdown>
7. Justifier qu’un tournoi de tennis peut effectivement être modélisé à l’aide d’un arbre binaire.

    ??? success "Solution"

        Dans ce tournoi, chaque match oppose exactement 2 joueurs&nbsp;: le gagnant d'un match devient le fils gauche ou droit du match suivant. Chaque nœud a donc exactement 2 fils, ce qui correspond à la définition d'un arbre binaire. 
</div>

On décide d’implémenter un arbre binaire à l’aide de la classe `Arbre` ci-dessous :

```python
class Arbre:
    def __init__(self, racine, gauche, droit):
    self.racine = racine
    self.gauche = gauche
    self.droit = droit
```

où `self.racine` est un objet de la classe `Match`, `self.gauche` et `self.droit`, des objets de la classe `Arbre`.

Dans le cas du tournoi de Madrid 2025 on connaît les matchs du tournoi à partir des
quarts de finale, où `pilar`, `inie`, `jabeur` sont des objets de la classe `Joueuse` :

```python
# quarts de finale
Q1 = Match('Quart de finale 1', gauff, pilar)
Q2 = Match('Quart de finale 2', paloni, inie)
Q3 = Match('Quart de finale 3', pegula, sabalenka)
Q4 = Match('Quart de finale 4', swiatek, jabeur)
# demi-finale
D1 = Match('Demi-finale 1', None, None)
D2 = Match('Demi-finale 2', None, None)
# finale
F = Match('Finale', None, None)
```

* La première demi-finale `D1` verra s’affronter les joueuses victorieuses des quarts de finales `Q1` et `Q2`.
* La seconde demi-finale `D2` verra s’affronter les joueuses victorieuses des quarts de finales `Q3` et `Q4`.
* La finale `F` verra s’affronter les joueuses victorieuses des demi-finales `D1` et `D2`.

<div class="sl-steps" start="8" markdown>
8. Instancier la variable `tournoi` de la classe `Arbre` représentant ce tournoi depuis les quarts de finale en passant par les demi-finales jusqu’à la finale.

    ??? success "Solution"
        ```python
        tournoi = Arbre(
            F,
            Arbre(D1, Arbre(Q1, None, None), Arbre(Q2, None, None)),
            Arbre(D2, Arbre(Q3, None, None), Arbre(Q4, None, None)),
        )
        ```
</div>

Dès qu’un match est joué, et donc dès que la gagnante est connue, on souhaite mettre à jour le match du tour suivant. Par exemple le premier quart de finale `Q1` s’est terminé sur le score de 6-4, 7-5, en faveur de la joueuse `gauff`. Elle participera donc en tant que `joueuse1` au premier match des demi-finales `D1`.

```python
Q1.resultat_match([(6, 4), (7, 5)])
```

<div class="sl-steps" start="9" markdown>
9. Compléter l’instruction suivante afin de mettre à jour dans `tournoi` la première joueuse de la première demi-finale comme étant `gauff`.

    ```python
    tournoi. ... = gauff
    ```

    ??? success "Solution"
        ```python
        tournoi.gauche.racine.joueuse1 = gauff
        ```
</div>

Cette façon de mettre à jour le tournoi n’est pas satisfaisante, on souhaite automatiser cette tâche à l’aide d’une méthode `mise_a_jour` de la classe `Arbre` qui parcourt l’arbre et dès que l’on rencontre un match dont la gagnante est connue, on la fait passer au tour suivant si ce n’est pas déjà fait. Cette méthode doit être récursive.

<div class="sl-steps" start="10" markdown>
10. Rappeler ce qu’est un programme récursif.

    ??? success "Solution"
        Un programme récursif est un programme qui s'appelle lui-même.

11. Recopier et compléter les lignes 6, 7, 13, 14 et 16 du code ci-dessous de la méthode `mise_a_jour` permettant de compléter automatiquement les matchs du tournoi en les mettant à jour à partir des résultats des matchs des tours précédents.

    ```python linenums="1"
    def mise_a_jour(self):
        """Met à jour les matchs de l'arbre"""
        if self.racine.joueuse1 is None:
            if self.gauche is not None:
                # mise à jour si gagnante à gauche
                if ...
                    ... = self.gauche.racine.gagnante
                else:
                    self.gauche.mise_a_jour()
        if self.racine.joueuse2 is None:
            if self.droit is not None:
                # mise à jour si gagnante à droite
                if ...
                    ... = self.droit.racine.gagnante
                else:
                    ...
    ```

    ??? success "Solution"

        ```python
        def mise_a_jour(self):
            """Met à jour les matchs de l'arbre"""
            if self.racine.joueuse1 is None:
                if self.gauche is not None:
                    # mise à jour si gagnante à gauche
                    if self.gauche.racine.gagnante is not None:
                        self.racine.joueuse1 = self.gauche.racine.gagnante
                    else:
                        self.gauche.mise_a_jour()
            if self.racine.joueuse2 is None:
                if self.droit is not None:
                    # mise à jour si gagnante à droite
                    if self.droit.racine.gagnante is not None:
                        self.racine.joueuse2 = self.droit.racine.gagnante
                    else:
                        self.droit.mise_a_jour()
        ```
</div>


## Exercice 3

*Cet exercice porte sur les bases de données relationnelles, le langage SQL et la programmation Python, en particulier les dictionnaires.*

Un club d'athlétisme organise une compétition de course à pied sur route. Deux épreuves sont proposées&nbsp;: une course de 5 km et une course de 10 km.

### Partie A&nbsp;: Bases de données

Dans cet exercice, on pourra utiliser les clauses du langage SQL pour&nbsp;:

* construire des requêtes d'interrogation à l'aide de `#!sql SELECT`, `#!sql FROM`, `#!sql WHERE` (avec les opérateurs logiques `#!sql AND` et `#!sql OR`), `#!sql JOIN ... ON`&nbsp;;
* construire des requêtes d'insertion et de mise à jour à l'aide de `#!sql UPDATE`, `#!sql INSERT` et `#!sql DELETE`&nbsp;;
* affiner les recherches à l'aide de `#!sql DISTINCT` et `#!sql ORDER BY`&nbsp;;
* réaliser des agrégations à l'aide de `#!sql COUNT`.

Le club souhaite gérer les inscriptions et les résultats de cette compétition à l'aide d'une base de données informatique constituée de deux tables&nbsp;: `#!sql coureur` et `#!sql epreuve`. Le schéma relationnel de cette base de données est représenté ci-dessous. Sur ce schéma, les clés primaires de chacune des tables sont soulignées et les clés étrangères sont précédées du symbole #.

![](assets/26-NSIJ2AN1-3.1.svg){ .center-img }
/// caption
Figure 1. Schéma de la base de données.
///

Chaque coureur ne peut participer qu'à une seule épreuve.

**Relation `coureur`**

L'identifiant du coureur est son numéro de dossard. Ce numéro est automatiquement incrémenté d'une unité à chaque nouvel enregistrement. Les autres champs doivent être saisis par l'organisateur lorsqu'il reçoit les bulletins d'inscription des coureurs. La codification du sexe est «&nbsp;H&nbsp;» pour les hommes et «&nbsp;F&nbsp;» pour les femmes. Les temps sont exprimés en secondes et sont initialisés avec la valeur 0.

<div class="center-table" markdown>
| `num_dossard` | `nom` | `prenom` | `annee` | `sexe` | `id_epreuve` | `temps` |
|:-----------:|:---:|:------:|:-----:|:----:|:----------:|:-----:|
| 1 | DA SILVA | José | 1980 | H | 1 | 0 |
| 2 | HANG LI | Léo | 2005 | H | 2 | 0 |
| 3 | BODIANE | Lola | 2000 | F | 2 | 0 |
| 4 | BRELET | Sandra | 1972 | F | 1 | 0 |
</div>
///caption
Extrait de la table `coureur`
///


**Relation `epreuve`**

Cette relation contient actuellement deux enregistrements, l'organisateur prévoyant d'ajouter de nouvelles distances dans le futur. La distance est exprimée en km et le prix de l'inscription en euros. Le champ `#!sql horaire` donne l'heure de départ de la course.

<div class="center-table" markdown>
| `id_epreuve` | `distance` | `horaire` | `prix` | `juge_arbitre` |
|:----------:|:--------:|:-------:|:----:|:------------:|
| 1 | 5 | 10 | 10 | GAVEAU Philippe |
| 2 | 10 | 11 | 20 | BOULA Awa |
</div>
///caption
Extrait de la table `epreuve`
///

<div class="sl-steps" markdown>

1. Expliquer le choix de `#!sql num_dossard` comme clé primaire pour la relation `#!sql coureur`.

    ??? success "Solution"
        Le numéro de dossard est automatiquement incrémenté ; il est donc unique pour chaque coureur et peut distinguer sans ambiguïté chaque enregistrement de la table.

2. Décrire ce que donne la requête SQL suivante&nbsp;:

    ```sql
    SELECT nom, prenom
    FROM coureur
    ORDER BY nom;
    ```

    ??? success "Solution"
        Cette requête renvoie le nom et le prénom de tous les coureurs inscrits dans la table `coureur` triés par ordre alphabétique croissant du nom.

3. Écrire une requête SQL permettant d'établir le nom et prénom de toutes les femmes inscrites à la compétition.

    ??? success "Solution"
        ```sql
        SELECT nom, prenom
        FROM coureur
        WHERE sexe = 'F';
        ```

4. Écrire une requête SQL permettant de connaître le nombre total d'inscrits à la compétition.

    ??? success "Solution"
        ```sql
        SELECT COUNT(*)
        FROM coureur;
        ```

</div>

L'organisateur reçoit le bulletin d'inscription contenant les informations suivantes&nbsp;:

!!! quote ""
    Nom : REMY ; Prénom : Patrice <br>
    Civilité : homme <br>
    Course : 5 km <br>
    Année de naissance : 1973

<div class="sl-steps" start="5" markdown>

5. Écrire une requête SQL permettant d'insérer ce participant dans la base.

    ??? success "Solution"
        ```sql
        INSERT INTO coureur (nom, prenom, annee, sexe, id_epreuve, temps)
        VALUES ('REMY', 'Patrice', 1973, 'H', 1, 0);
        ```
        `id_epreuve = 1` correspond à la course de 5 km. Le `num_dossard` est auto-incrémenté et n'est donc pas à saisir.

</div>

Le coureur dont le numéro de dossard est le 137 s'est blessé quelques jours avant l'épreuve, il ne pourra pas participer à la course.

<div class="sl-steps" start="6" markdown>

6. Écrire une requête SQL qui permettra à l'organisateur de supprimer son inscription de la base de données.

    ??? success "Solution"
        ```sql
        DELETE FROM coureur
        WHERE num_dossard = 137;
        ```

</div>

Le coureur dont le numéro de dossard est le 256 a oublié sur quelle épreuve (5 km ou 10 km) il s'est inscrit. Il contacte l'organisateur pour qu'il lui rappelle la distance qu'il devra parcourir ainsi que l'horaire de son départ.

<div class="sl-steps" start="7" markdown>

7. Écrire une requête SQL permettant de lui fournir ces informations.

    ??? success "Solution"
        ```sql
        SELECT epreuve.distance, epreuve.horaire
        FROM coureur
        JOIN epreuve ON coureur.id_epreuve = epreuve.id_epreuve
        WHERE coureur.num_dossard = 256;
        ```

</div>

Lorsque les coureurs franchissent la ligne d'arrivée, le juge arbitre note leur numéro de dossard et leur temps de course (en secondes) sur une feuille de pointage. Voici un extrait d'une telle feuille&nbsp;:

<div class="center-table" markdown>
| dossard | temps |
|:-------:|:-----:|
| 57 | 1242 |
| 72 | 1845 |
| 183 | 1284 |
| 2 | 1285 |
</div>

Les temps de tous les coureurs ayant été enregistrés, on souhaite afficher le classement général de la catégorie *Master Femme* pour la course de 10 km. Cette catégorie regroupe les coureuses nées avant 1986.

<div class="sl-steps" start="8" markdown>

8. Écrire une requête SQL renvoyant le numéro de dossard, le nom, le prénom et le temps de course de ces participantes classées par temps de course croissant.

    ??? success "Solution"
        ```sql
        SELECT num_dossard, nom, prenom, temps
        FROM coureur
        JOIN epreuve ON coureur.id_epreuve = epreuve.id_epreuve
        WHERE sexe = 'F' AND annee < 1986 AND distance = 10
        ORDER BY coureur.temps;
        ```

</div>

### Partie B&nbsp;: Programmation Python

Émilie, fille de l'organisateur et élève en classe de terminale spécialité NSI propose de réaliser une étude pluriannuelle des performances accomplies.

Pour enregistrer les informations elle crée pour chaque type de course un *dictionnaire de performances*. Les clés d'un tel dictionnaire sont les années où ce type de course a eu lieu. La valeur associée à une année est la liste des meilleurs temps réalisés dans chacune des six catégories suivantes (dans cet ordre).

* Junior homme (JH) et Junior femme (JF)&nbsp;: moins de 18 ans&nbsp;;
* Sénior homme (SH) et Sénior femme (SF)&nbsp;: de 18 à 40 ans&nbsp;;
* Master homme (MH) et Master femme (MF)&nbsp;: plus de 40 ans.

Par exemple, le dictionnaire ci-dessous enregistre les performances pour les courses de 5 km. Il indique par exemple qu'en 2024 le meilleur temps réalisé dans la catégorie junior femme (JF) est de 1010 s, et celui dans la catégorie master homme (MH) de 1022 s.

```python
dict_perf_5km = {
    2022: [1020, 1050, 900, 1000, 1018, 1040],
    2023: [1010, 1048, 1100, 1024, 1080, 1108],
    2024: [1012, 1010, 1000, 1036, 1022, 1098],
    2025: [998, 1028, 1000, 959, 1002, 980],
}
```

<div class="sl-steps" start="9" markdown>

9. Donner la valeur de l'expression `#!py dict_perf_5km[2025][2]`.

    ??? success "Solution"
        `#!py 1000`
</div>

En 2026, pour la course de 5 km, les meilleurs temps réalisés dans chaque catégorie sont les suivants&nbsp;:

<div class="center-table" markdown>
| JH | JF | SH | SF | MH | MF |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 1004 | 1016 | 1000 | 1140 | 1023 | 1024 |
</div>
/// caption
Résultats par catégories - 2026
///

<div class="sl-steps" start="10" markdown>

10. Écrire l'instruction permettant d'ajouter ces informations dans le dictionnaire `dict_perf_5km`.

    ??? success "Solution"
        ```python
        dict_perf_5km[2026] = [1004, 1016, 1000, 1140, 1023, 1024]
        ```

11. Écrire le code de la fonction `scratch` qui prend en paramètres un dictionnaire de performances `dico` et une année `annee`, et qui renvoie le meilleur temps (toutes catégories confondues) de cette année. On suppose que `annee` est une clé présente dans `dico`.

    On n'utilisera pas les fonctions natives `#!py min` et `#!py max` de Python.

    Par exemple, l'appel `#!py scratch(dict_perf_5km, 2024)` renvoie `#!py 1000`.

    ??? success "Solution"
        ```python
        def scratch(dico, annee):
            mini = dico[annee][0]
            for temps in dico[annee]:
                if temps < mini:
                    mini = temps
            return mini
        ```

</div>

Émilie propose maintenant la fonction suivante&nbsp;:

```python
def mystere(dico, cat):
    categories = ['JH', 'JF', 'SH', 'SF', 'MH', 'MF']
    s = 0
    nb = 0
    for i in range(len(categories)):
        if cat == categories[i]:
            i_cat = i
    for annee in dico.keys():
        s = s + dico[annee][i_cat]
        nb = nb + 1
    return s / nb
```

<div class="sl-steps" start="12" markdown>

12. Indiquer la valeur affectée à la variable `i_cat` au cours de l'appel `#!py mystere(dict_perf_5km, 'SH')`.

    ??? success "Solution"
        `#!py i_cat = 2` car `#!py 'SH'` est à l'indice 2 dans la liste `#!py ['JH', 'JF', 'SH', 'SF', 'MH', 'MF']`

</div>

Un appel du type `#!py mystere(dict_perf_5km, 'SG')` pose problème car `#!py 'SG'` n'est pas une catégorie répertoriée.

<div class="sl-steps" start="13" markdown>

13. Indiquer quel sera le message d'erreur renvoyé à la console parmi les choix suivants&nbsp;:

    * `"expected an indented block"`&nbsp;;
    * `"takes 2 positionnals arguments but 3 were given"`&nbsp;;
    * `"local variable 'i_cat' referenced before assignement"`&nbsp;;
    * `"list index out of range"`.

    ??? success "Solution"
        `"local variable 'i_cat' referenced before assignment"`

        Comme `#!py 'SG'` n'est pas une catégorie répertoriée, la condition `#!py cat == categories[i]` n'est jamais vraie : la variable `#!py i_cat` n'est donc jamais assignée. Quand Python tente d'y accéder dans la seconde boucle, il lève cette erreur.

14. Proposer une assertion à ajouter entre la ligne 2 et la ligne 3 pour indiquer une éventuelle faute de saisie par un message à l'utilisateur du script.

    ??? success "Solution"
        ```python
        assert cat in categories, f"Catégorie '{cat}' invalide. Les catégories valides sont : {categories}"
        ```

15. Indiquer le résultat de l'appel `#!py mystere(dict_perf_5km, 'SH')`.

    ??? success "Solution"
        La fonction effectue la moyenne des temps pour la catégorie `#!py 'SH'`. Elle renvoie donc `#!py (900 + 1100 + 1000 + 1000) / 4 = 1000.0`.
</div>

Émilie souhaiterait disposer d'une fonction `records` prenant en paramètre un dictionnaire de performances et renvoyant la liste des meilleurs temps enregistrés pour chaque catégorie et toutes années confondues. Par exemple, l'appel `#!py records(dict_perf_5km)` devrait renvoyer `#!py [998, 1010, 900, 959, 1002, 980]`. On suppose que les temps enregistrés pour les différentes catégories et les différentes années n'excèdent jamais 24 h.

<div class="sl-steps" start="16" markdown>

16. Écrire le code de la fonction `records`.

    ??? success "Solution"
    
        ```python
        def records(dico):
            meilleurs = [24 * 60 * 60] * 6
            for annee in dico:
                for i in range(6):
                    if dico[annee][i] < meilleurs[i]:
                        meilleurs[i] = dico[annee][i]
            return meilleurs
        ```

</div>
