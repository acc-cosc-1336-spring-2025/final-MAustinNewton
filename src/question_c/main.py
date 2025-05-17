from question_c import get_stock_list

def main():
    while True:
        print("\nMenu")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            stock_list = get_stock_list()
            if stock_list:
                print("\nStock Report\n")
                print(f"{'Company':<20} {'Symbol'}")
                print("-" * 30)
                for stock in stock_list:
                    print(f"{stock.get_company_name():<20} {stock.get_symbol()}")
            else:
                print("No stock data available.")
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()