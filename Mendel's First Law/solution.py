import sys

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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python solution.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Get input file from command-line argument
    output_file = sys.argv[2]  # Get output file from command-line argument

    try:
        with open(input_file, 'r') as input_data:
            k, m, n = map(int, input_data.read().strip().split())
        
        result = mendel(k, m, n)

        with open(output_file, 'w') as output_data:
            output_data.write(str(result))

        print(result)  # Print to console for immediate feedback
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    