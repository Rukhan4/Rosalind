def mendel(k, m, n):
    # Let AA = homozygous dominant
    # Let Aa = heterozygous
    # Let aa = homozygous recessive
    pop_size = k + m + n

    AA_AA = k/pop_size * (k-1)/(pop_size-1)
    AA_Aa = 2 * (k / pop_size) * (m / (pop_size-1))
    AA_aa = 2 * (k / pop_size) * (n / (pop_size-1))
    Aa_Aa = (m / pop_size) * ((m-1) / (pop_size-1)) * 3/4 # 3/4 gives dominant allele
    Aa_aa = 2 * (m / pop_size) * (n / (pop_size-1)) * 1/2 #1/2 gives dominant allele

    #print(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa)
    return AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa
