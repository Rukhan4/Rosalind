import sys

def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python solution.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Get input file from command-line argument
    output_file = sys.argv[2]  # Get output file from command-line argument

    try:
        with open(input_file, 'r') as data:
            dna = data.read().strip()

        result = transcribe_dna_to_rna(dna)

        with open(output_file, 'w') as output_data:
            output_data.write(result)

        print(result)  # Print to console for immediate feedback
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)