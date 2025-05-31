---
title: 24-NSIJ2AN1-3
---

<div class="circle-ol" markdown>

1. Le masque `255.255.255.0` indique que les trois premiers octets de l'adresse IP correspondent à l'adresse réseau. Alice et Bob sont donc sur le réseau `192.168.1.0`. Une adresse valide pour Charlie pourrait être `192.168.1.3`, car elle n’est ni déjà attribuée, ni une adresse réservée, comme l’adresse du réseau (`.0`) ou l’adresse de diffusion (`.255`).

2. La liste de ces transactions est :

    ```python
    [
        Transaction('Alice', 'Charlie', 10),
        Transaction('Bob',   'Alice',   5)
    ]
    ```

3. Le bloc 0 correspond au tout premier bloc crée, il n'a donc pas de prédécesseur, ainsi son attribut `bloc_precedent` est `None`.

4. L'attribut `bloc_precedent` du bloc 1 doit contenir une référence vers le bloc 0.

5. 
```python
blockchain = Blockchain()

blockchain.tete = Bloc(
    [
        Transaction('Alice',   'Charlie', 50),
        Transaction('Charlie', 'Bob',     30)
    ],
    blockchain.tete)

blockchain.tete = Bloc(
    [
        Transaction('Bob',     'Charlie', 20),
        Transaction('Bob',     'Charlie', 20),
        Transaction('Charlie', 'Alice',   30)
    ],
    blockchain.tete)
```

6. À l'issue du bloc 2, Bob a un solde de 100 + 30 – 20 – 20 = **90 nsicoins**.

7. 
```python
def ajouter_bloc(self, liste_transactions):
    self.tete = Bloc(liste_transactions, self.tete)
```

8. L'adresse de **broadcast** ou de **diffusion générale** permet d'envoyer un paquet à l'ensemble du résau local. Il s'agit de la dernière adresse IP du réseau, à savoir ici `192.168.1.255`.

9. Le code à compléter contient plusieurs erreurs :

    * Ligne 2 : <s>`#!py self.precedent`</s> → `#!py self.bloc_precedent`
    * Ligne 6 : <s>`#!py bloc.liste_transactions`</s> → `#!py self.liste_transactions`
    * Ligne 6 : Il manque `:` à la fin de la boucle `#!py for`  

    ```python hl_lines="5 7 8 9 10"
    def calculer_solde(self, utilisateur):
        if self.bloc_precedent is None:  # cas de base
            solde = 0
        else:
            solde = self.bloc_precedent.calculer_solde(utilisateur)
            for transaction in self.liste_transactions:
                if transaction.expediteur == utilisateur:
                    solde = solde - transaction.montant
                elif transaction.destinataire == utilisateur:
                    solde = solde + transaction.montant
            return solde
    ```

10. Suivant la variable `blockchain` définit à la question 5, l'expression `#!py blockchain.tete.calculer_solde('Alice')` renvoie le solde actuel d'Alice.

11. Déterminer une valeur par recherche exhaustive signifie tester toutes les valeurs possibles, une par une, jusqu’à trouver celle qui satisfait une condition donnée (par exemple, ici, un hash commençant par `#!py '00'`).


12. Puisque le bloc 0 correspond au tout premier bloc crée, son attribut `bloc_precedent` vaut  `None`. Son attribut `hash_bloc_precedent` est initialisé par la méthode `donner_hash_precedent`, qui lui affecte la valeur `#!py '0'`.

13. Puisque le hash s'écrit sur 256 bits, il existe $2^{256} \approx 10^{77}$ hashs possibles.

14. 
```python hl_lines="4 5 6"
def minage_bloc(self):
    self.nonce = 0
    self.hash = self.calculer_hash()
    while self.hash[:2] != '00':
        self.nonce = self.nonce + 1
        self.hash = self.calculer_hash()
```

</div>
