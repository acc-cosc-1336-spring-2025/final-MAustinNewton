class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def stock_purchase_history():
    # Create stock instances
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    # Add to the dictionary
    stock_dict = {
        stock1.get_symbol(): stock1,
        stock2.get_symbol(): stock2,
        stock3.get_symbol(): stock3,
        stock4.get_symbol(): stock4,
        stock5.get_symbol(): stock5
    }

    # Printed output
    print("\nStock List:\n")
    print(f"{'Symbol':<10} {'Company Name'}")
    print("-" * 30)
    for symbol, stock in stock_dict.items():
        print(f"{symbol:<10} {stock.get_company_name()}")



def test_config():
    return True