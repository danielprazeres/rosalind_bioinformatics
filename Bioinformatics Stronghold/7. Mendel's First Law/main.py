def mendels_first_law(k, m, n):
    # Total de organismos
    total = k + m + n

    # Probabilidades de seleção e cruzamento
    prob_AA_AA = (k / total) * ((k - 1) / (total - 1)) * 1  # 100% dominante
    prob_AA_Aa = (k / total) * (m / (total - 1)) * 1 * 2  # 100% dominante (x2 para considerar ambas as ordens)
    prob_AA_aa = (k / total) * (n / (total - 1)) * 1 * 2  # 100% dominante (x2 para considerar ambas as ordens)
    prob_Aa_Aa = (m / total) * ((m - 1) / (total - 1)) * 0.75  # 75% dominante
    prob_Aa_aa = (m / total) * (n / (total - 1)) * 0.5 * 2  # 50% dominante (x2 para considerar ambas as ordens)
    prob_aa_aa = (n / total) * ((n - 1) / (total - 1)) * 0  # 0% dominante

    # Soma todas as probabilidades
    return prob_AA_AA + prob_AA_Aa + prob_AA_aa + prob_Aa_Aa + prob_Aa_aa + prob_aa_aa


k, m, n = 24, 19, 25
print(round(mendels_first_law(k, m, n), 5))