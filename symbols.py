# Standard Python libraries
import os
import pickle
import sys
from typing import Union

# local application imports
from client import Client


def fetch_symbols() -> None:
    """
    Fetching symbols from API, when it's already in the data/ directory
    then reads file.
    """
    client = Client()

    filename = "symbols.pkl"
    fullpath = os.path.join(os.getcwd(), "data")

    if filename not in os.listdir(fullpath):
        print("Fetching symbols from external API...")
        coins = client.get_coin_symbols()
        symbols = [coin["id"] for coin in coins]
        with open(os.path.join("data", filename), "wb") as file:
            pickle.dump(symbols, file)


def check_if_symbol_available(symbol: str) -> Union[bool, None]:
    """Check if coin symbol passed as an argument is available."""
    if symbol != 'btc-bitcoin':
        with open(os.path.join("data", "symbols.pkl"), "rb") as file:
            symbols = pickle.load(file)
        if symbol in symbols:
            return True
        else:
            print("Sorry, we don't have that coin.")
            sys.exit()


def main():
    pass


if __name__ == "__main__":
    main()
