---
title: 24-NSIJ2JA1-2
---

<div class="circle-ol" markdown>

1. L'expression est **mal parenthéséee** : <tt markdown style="font-size: .85em"><span class="green-text">[</span>2 * <span class="green-text">(</span>i + 1<span class="green-text">)</span> - 3<span class="red-text hl-red" markdown>**)**</span> for i in range<span class="green-text">(</span>3, 10<span class="green-text">)]</span></tt>

2. 
```python
# évite de se répéter pour la question 3
def compte_caracteres(txt, caracteres):
    compteur = 0
    for caractere in txt:
        if caractere in caracteres:
            compteur += 1
    return compteur

def compte_ouvrante(txt):
    return compte_caracteres(txt, '({[')
```

3. 
```python
def compte_fermante(txt):
    return compte_caracteres(txt, ')}]')
```

4. 
```python
def bon_compte(txt):
    return compte_ouvrante(txt) == compte_fermante(txt)
```

5. Par exemple, `#!py bon_compte('](')` renvoie `True` alors que l'expression `#!py ']('` n'est pas bien parenthésée.

6. 
```python hl_lines="9 14"
class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return len(self.contenu) == 0

    def empiler(self, elt):
        self.contenu.append(elt)

    def depiler(self):
        if self.est_vide():
            return "La pile est vide."
        return self.contenu.pop()
```

7. Pour un caractère de la chaîne, l'algorithme effectue $O(1)$ comparaisons. Ainsi, pour une chaîne de $n$ caractères, il effectue $\boxed{O(n)}$ comparaisons. Le nombre précis de comparaisons dépend totalement de l'implémentation.

8. 
```python
def est_bien_parenthesee(chaine):
    COUPLE = {'(': ')', '[': ']', '{': '}'}
    pile = Pile()
    for c in chaine:
        if c in '([{':
            pile.empiler(c)
        elif c in ')]}':
            if pile.est_vide() or c != COUPLE[pile.depiler()]:
                return False
    return pile.est_vide()
```

</div>
