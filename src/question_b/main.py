from question_b import create_multiplication_table, display_multiplication_table

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        choice = input("\nDo you want to generate the table again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
