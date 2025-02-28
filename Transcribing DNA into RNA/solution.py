def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')


if __name__ == "__main__":
    with open('./data/rosalind_rna.txt', 'r') as f:
        dna = f.read().strip()

    rna = transcribe_dna_to_rna(dna)
    print(rna)
    with open('./data/output.txt', 'w') as f:
        f.write(rna)

    # Output to data/output.txt
    # python3 solution.py > ./data/output.txt
    # cat ./data/output.txt