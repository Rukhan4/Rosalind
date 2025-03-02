def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complemented_dna = ''.join([complement[base] for base in dna])
    reverse_complement = complemented_dna[::-1]
    return reverse_complement


if __name__ == "__main__":
    with open('data/rosalind_revc.txt', 'r') as data:
        dna = data.read().strip()
        print(reverse_complement(dna))
    
    with open('data/output.txt', 'w') as output_data:
        output_data.write(reverse_complement(dna))





    # Output to data file with bash
    # python3 solution.py > ./data/output.txt
    # cat ./data/output.txt