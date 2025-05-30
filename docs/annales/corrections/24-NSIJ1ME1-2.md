---
title: 24-NSIJ1ME1-2
---

<div class="circle-ol" markdown>

1. Un SGBD permet d'assurer la **cohérence** des données (en évitant les doublons ou incohérences) et leur **sécurité** (en contrôlant les accès et en protégeant contre les pertes ou modifications non autorisées).

2. En suivant le protocole RIP, un paquet du bureau №1 vers le prestataire suit la route **B → E → A**.

3. En suivant le protocole OSPF, un paquet du bureau №2 vers le prestataire pourrait suivre l'une deux routes :
    
    * **C → I → G → F → D → A**
    * **C → I → H → F → D → A**

    Ces deux routes partagent le même coût, à savoir 0.1 + 1 + 0.1 + 0.1 + 1 = **2.3**.

4. Puisque l'attribut `id_client` permet d'identifier de manière unique un client, elle peut être choisie comme clé primaire.

5. Une clé étrangère est un attribut qui fait référence à une clé primaire d'une autre relation, permettant ainsi de les lier. Dans la base de données de l'exercice :
   
    * La clé étrangère `id_client` de la relation `reservations` fait référence à la clé primaire `id_client` de la relation `clients`.
    * La clé étrangère `nom_croisiere` de la relation `reservations` fait référence à la clé primaire `nom` de la relation `croisieres`.
    * Les clés étrangères `escale_1`, `escale_2`, `escale_3` et `escale_4` de la relation `croisieres` font référence à la clé primaire `nom` de la relation `villes`.

6. L’erreur s’explique par le fait qu’au moins une de ces nouvelles villes n’est pas présente dans la relation `villes`. Or, une clé étrangère doit obligatoirement faire référence à une clé primaire existante. Une solution serait d'ajouter au préalable ces villes dans la relation `villes` avant d'effectuer la requête d'insertion.

7. 
    * La première requête permet d’obtenir l’identifiant (`id`) de Jean Barc à partir de la table `clients`.
    * La seconde requête utilise cet identifiant pour récupérer les identifiants des réservations de Jean Barc depuis la table `reservations`.

8. 
```sql
SELECT id_reservation
FROM clients
JOIN reservations ON reservations.id_client = clients.id_client
WHERE nom = 'Barc'
    AND prenom = 'Jean'
    AND date_naissance = '1972/06/29'
    AND pays = 'Allemagne';
```

9. 
```sql
UPDATE reservations
SET nom_croisiere = 'Croisière Puerto'
WHERE id_reservation = 20456;
```

10. 
```sql
SELECT nom, prenom, date_naissance
FROM clients
JOIN reservations ON reservations.id_client = clients.id_client
WHERE  nom_croisiere = 'Croisière Puerto'
    OR nom_croisiere = 'Croisière Piano';
```
</div>