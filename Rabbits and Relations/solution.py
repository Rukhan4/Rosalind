import sys

def rabbits(n, k):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return rabbits(n-1, k) + k * rabbits(n-2, k)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python solution.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Get input file from command-line argument
    output_file = sys.argv[2]  # Get output file from command-line argument

    try:
        with open(input_file, 'r') as data:
            dna = data.read().strip()
            n, k = map(int, dna.split())

        result = rabbits(n, k)

        with open(output_file, 'w') as output_data:
            output_data.write(str(result))

        print(result)  # Print to console for immediate feedback
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)