# Standard Python libraries
from copy import deepcopy
from datetime import date
from typing import Set, Dict

# local application imports
from client import Client
from historical_values import HistoricalValue


class Calculator:
    """Class Container which implements methods to calculate..."""

    def __init__(self, start_date: date, end_date: date, coin: str) -> None:
        self.historical_values = []
        # Creating instance of Client and fetching historical ohlcs
        self.client = Client(start_date, end_date, coin)
        ohlc = self.client.get_historical_values()
        # Converting list of dicts to list of objects with selected keys
        for o in ohlc:
            self.historical_values.append(HistoricalValue(o["time_close"],
                                                          o["close"]))

    def _group_data(self) -> Set:
        """
        Returns: set of unique, unsorted dates in string (Year-Month)
        """
        groups = {str(value.time_close.date())[:7] for value in
                  self.historical_values}
        return groups

    def calculate_average_price_by_month(self) -> Dict:
        """Calculate average price of currency by month for given period."""

        # Determining what groups are in historical_values
        groups = self._group_data()

        # Calculate average price by month
        average_price_by_month = {}
        for group in groups:
            sum = 0
            counter = 0
            for value in self.historical_values:
                if str(value.time_close)[:7] == group:
                    sum += value.close
                    counter += 1
            try:
                average_price_by_month[group] = sum / counter
            except ZeroDivisionError:
                print("ZeroDivisionError when calculating average price.")

        # Sorting dict by keys
        average_price_by_month = dict(sorted(average_price_by_month.items()))
        return average_price_by_month


def main():
    calc = Calculator(date(2020, 11, 1), date(2021, 2, 28), "btc-bitcoin")
    avg_prices = calc.calculate_average_price_by_month()

    # Priting dates and average prices
    print(f"Date \t Average Price ($)")
    for d, price in avg_prices.items():
        print(f"{d:8} {price:.5f}")


if __name__ == "__main__":
    main()
