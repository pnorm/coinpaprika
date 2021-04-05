# Standard Python libraries
from copy import deepcopy
from datetime import date
from typing import Set, Dict

# local application imports
from client import Client
from historical_values import HistoricalValue


class Calculator:
    """
    Class which implements methods to calculate average price by month and to
    find longest consecutive increase.
    """

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

    def find_longest_consecutive_increase(self) -> Dict:
        """
        Finds longest consecutive increase for a given historical data.
        Returns: Dict
        """
        previous_value = self.historical_values[0]
        initial_dict = {
                "Dates": [],
                "Price Increase": 0,
                "Num_days": 0
            }
        temp_dict = deepcopy(initial_dict)
        longest_increasing = deepcopy(temp_dict)

        # I assume first value is not increasing.
        for actual_value in self.historical_values:
            # Determining if value is greater than previous
            if actual_value > previous_value:
                # Price increase
                temp_increase = actual_value.close - previous_value.close
                # Longest consecutive increase saved to dictionary
                temp_dict["Dates"].append(actual_value.time_close)
                temp_dict["Price Increase"] += temp_increase
                temp_dict["Num_days"] += 1
                if longest_increasing["Num_days"] < temp_dict["Num_days"]:
                    longest_increasing = deepcopy(initial_dict)
                    longest_increasing = temp_dict.copy()
            else:
                # Reset temporary dict
                temp_dict = deepcopy(initial_dict)
            # Remember value for later use
            previous_value = actual_value

        return longest_increasing


def main():
    calc = Calculator(date(2020, 11, 1), date(2021, 2, 28), "btc-bitcoin")
    avg_prices = calc.calculate_average_price_by_month()

    # Priting dates and average prices
    print(f"Date \t Average Price ($)")
    for d, price in avg_prices.items():
        print(f"{d:8} {price:.5f}")

    # Longest consecutive increasing period
    longest = calc.find_longest_consecutive_increase()

    print(f""" <<< Longest consecutive period was from \
{longest["Dates"][0].date()} to {longest["Dates"][-1].date()} with \
increase of ${round(longest["Price Increase"], 2)} >>>""")


if __name__ == "__main__":
    main()
