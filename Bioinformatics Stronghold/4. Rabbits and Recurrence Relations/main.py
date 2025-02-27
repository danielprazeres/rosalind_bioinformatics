def rabbits(n, k):
    F1, F2 = 1, 1  # Valores iniciais para os primeiros meses

    for _ in range(n -2):
        F1, F2 = F2, F1 * k + F2

    return F2

n, k = 29, 5
print(rabbits(n, k))