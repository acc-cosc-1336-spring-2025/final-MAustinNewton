from question_d import get_most_likely_ancestor_consensus

def main():
    while True:
        dna_string1 = input("Enter a DNA string (9 to 16 characters): ").upper()
        if not (8 < len(dna_string1) <= 16):
            print("Invalid input. DNA string must be between 9 and 16 characters.")
            continue

        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").upper()
        if len(dna_string2) != 4:
            print("Invalid input. DNA substring must be exactly 4 characters.")
            continue

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        if result:
            print("Substring found at positions:", *result)
        else:
            print("Substring not found.")

        choice = input("Do you want to try again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
