def create_multiplication_table():
    table = []
    for i in range(1, 6):  # Rows: 1 to 5
        row = []
        for j in range(1, 11):  # Columns: 1 to 10
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    print("\nMultiplication Table:\n")
    for row in table:
        for num in row:
            print(f"{num:<4}", end='')  # Align output
        print()  # New line after each row
