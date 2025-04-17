---
title: Architecture matérielle
icon: octicons/cpu-16
---

## Architecture de Von Neumann

![](assets/neumann.svg)


Le **cycle** d'une machine séquentielle se répète jusqu'à l'arrêt de la machine :

<div class="no-bullet" markdown>
* :material-numeric-1-circle: &nbsp; Le processeur **récupère** l'instruction à exécuter en mémoire.
* :material-numeric-2-circle: &nbsp; Le processeur **décode** et **exécute** l'instruction.
* :material-numeric-3-circle: &nbsp; Le processeur passe à l'instruction suivante et ainsi de suite.
</div>

Un programme est une suite d'**instructions** en code machine, c'est-à-dire une suite d’octets que le processeur décode puis exécute.

## Processus

### Création et états d'un processus

* Quand un programme est lancé, un processus est créé par le système d'exploitation. Un processus contient :
    <div class="no-bullet" markdown>
    * :material-file-code: &nbsp; Les **instructions** du programme à exécuter (chargées en mémoire).
    * :fontawesome-solid-memory: &nbsp; Un **espace mémoire** réservé.
    * :fontawesome-solid-hard-drive: &nbsp; Des droits d’accès à certaines **ressources** (fichiers, périphériques…).
  
    </div>

* Un **processus** peut être démarré au démarrage du système, par l'utilisateur, par un périphérique ou par un autre processus appelé **parent**.

* Chaque processus possède un **identifiant unique (PID)** et celui de son parent (PPID). Cela permet de structurer les processus en arbre. Si un processus parent se termine, tous ses processus enfants (et leur descendance) sont également arrêtés.

* Un processeur n’exécute qu’une seule instruction à la fois, donc un seul processus à la fois. Pour donner l'illusion de simultanéité d'exécution, les processus se partagent le processeur à tour de rôle. Ainsi, un processus peut donc se trouver dans différents **états** :

    ![](assets/processus-etats.svg){ .center-img }

### Commandes UNIX relatifs aux processus

=== ":material-camera-enhance: &nbsp; `ps`"

    `ps` affiche **un cliché instantané** des processus en cours d'exécution. Les options `-ef` permet d'afficher tous les processus avec informations détaillées.

    ![](assets/ps.png){ width="600px" .center-img }

=== ":material-monitor-eye: &nbsp; `top`"

    `top` affiche **en temps réel** les processus actifs et leur consommation ﬂsystème (CPU, mémoire...).

    ![](assets/top.png){ width="600px" .center-img }


=== ":material-skull: &nbsp; `kill`"

    `kill <PID>` **termine** le processus identifié par son PID. L'option `-9` permet de forcer l’arrêt immédiat du processus, sans lui laisser la possibilité de se terminer de manière contrôlée.

    ![](assets/kill.png){ width="600px" .center-img }


### Ordonnancement des processus

L'**ordonnanceur** est un programme du système d’exploitation qui choisit le processus à élire, l’interrompt si nécessaire, et définit le temps processeur (mesuré en cycles) qui lui est alloué. Pour cela, il peut appliquer différentes **stratégies d’ordonnancement**, selon des critères comme la priorité des processus, leur durée estimée, leur ordre d’arrivée, un partage équitable du temps etc. Voici quelques stratégies d'ordonnancement pour les quatre processus suivants :

![](assets/ordonnancements.svg)

### Interblocage (deadlock)

L'**interblocage** est une situation où plusieurs processus sont bloqués, chacun attendant une ressource détenue par un autre, aboutissant à un blocage mutuel et infini.

<div class="slideshow" markdown>
  <button class="nav prev">:material-arrow-left-circle:</button>
  <div class="slides">
    <img src="../assets/interblocage/01.svg" class="slide">
    <img src="../assets/interblocage/02.svg" class="slide">
    <img src="../assets/interblocage/03.svg" class="slide">
    <img src="../assets/interblocage/04.svg" class="slide">
    <img src="../assets/interblocage/05.svg" class="slide">
    <img src="../assets/interblocage/06.svg" class="slide">
    <img src="../assets/interblocage/07.svg" class="slide">
    <img src="../assets/interblocage/08.svg" class="slide">
    <img src="../assets/interblocage/09.svg" class="slide">
    <img src="../assets/interblocage/10.svg" class="slide">
    <img src="../assets/interblocage/11.svg" class="slide">
    <img src="../assets/interblocage/12.svg" class="slide active">
  </div>
  <button class="nav next">:material-arrow-right-circle:</button>
  <div class="dots">
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot"></span>
    <span class="dot active"></span>
  </div>
</div>