import os

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    stock_list = []

    # Ensure the file path works no matter where you run the script from
    file_path = os.path.join(os.path.dirname(__file__), "stock_file.dat")

    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(" ", 1)
                if len(parts) == 2:
                    symbol, company_name = parts
                    stock = Stock(symbol, company_name)
                    stock_list.append(stock)
    except FileNotFoundError:
        print("stock_file.dat not found at:", file_path)

    return stock_list
