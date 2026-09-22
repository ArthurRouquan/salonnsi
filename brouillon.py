from random import randint


def fusionner(A, B):
    F = []
    while A and B:
        L = A if A[-1] > B[-1] else B  # copie de référence
        F.append(L.pop())
    F.reverse()
    return A + B + F


def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    m = len(tab) // 2
    return fusionner(tri_fusion(tab[:m]), tri_fusion(tab[m:]))


for _ in range(10):
    t = [randint(1, 99) for _ in range(10)]
    print(tri_fusion(t), tri_fusion(t) == sorted(t))
