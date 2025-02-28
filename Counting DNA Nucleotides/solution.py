def counting_dna_nucleotides(dna):
    a = dna.count('A')
    c = dna.count('C')
    g = dna.count('G')
    t = dna.count('T')
    return a, c, g, t

if __name__ == "__main__":
    with open('./data/rosalind_dna.txt', 'r') as f:
        dna = f.read().strip()
    print(' '.join(map(str, counting_dna_nucleotides(dna))))

    # Output to data file with bash
    # python3 solution.py > ./data/output.txt
    # cat ./data/output.txt
    