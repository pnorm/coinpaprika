# Standard Python libraries
from datetime import datetime
from typing import Dict


# local application imports


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
    pass


if __name__ == "__main__":
    main()
