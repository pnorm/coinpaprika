# Standard Python libraries
from datetime import datetime, date
from pprint import pprint
from typing import Dict

# local application imports
from client import Client


class HistoricalValue:
    """Converts Python dict to Python object."""

    def __init__(self, time_close: str, close: float) -> None:
        self.time_close = datetime.strptime(time_close[:10], "%Y-%m-%d")
        self.close = close

    def __repr__(self):
        return f"<Date: {self.time_close.date()}, Price: {self.close}>"

    def __eq__(self, other):
        return self.close == other.close

    def __ne__(self, other):
        return self.close != other.close

    def __gt__(self, other):
        return self.close > other.close

    def __lt__(self, other):
        return self.close < other.close

    def __ge__(self, other):
        return self.close >= other.close

    def __le__(self, other):
        return self.close <= other.close

    def to_dict(self) -> Dict:
        """Converts HistoricalValue object to dict."""
        return {
            "Date": str(self.time_close.date()),
            "Price": self.close
        }

def main():
    # Testing
    client = Client()
    ohlc = client.get_historical_values()

    # Converts to HistoricalValue objects
    historical_values = []
    for o in ohlc:
        historical_values.append(HistoricalValue(o["time_close"], o["close"]))
    pprint(historical_values)

    # Convert to dicts
    list_of_dicts = []
    for value in historical_values:
        list_of_dicts.append(value.to_dict())
    pprint(list_of_dicts)

if __name__=="__main__":
    main()
