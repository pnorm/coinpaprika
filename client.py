# Standard Python libraries
from datetime import date
import json
from typing import Dict, List, Union

# 3rd party libraries
import re
import requests
import sys


class Client:
    """Client allows us to fetch data from external CoinPaprika API"""

    def __init__(self, start: date = date(2020, 11, 1),
                 end: date = date(2021, 2, 28),
                 coin: str = "btc-bitcoin") -> None:
        self.BASE_URL = "https://api.coinpaprika.com/v1"
        self.coin = coin
        self.query_parameters = {
            "start": start,
            "end": end,
        }

    def _check_status_codes(self, response) -> bool:
        """Check response code. HTTP response status codes indicate whether a
        specific HTTP request has been successfully completed.
            Successful responses (200–299)
            Client errors (400–499)
            Server errors (500–599)
        """
        if re.match("^5[0-9]{2}$", str(response.status_code)):
            print("Can't fetch the data. The issue is on coinparprika's side.")
            sys.exit()
        elif re.match("^4[0-9]{2}$", str(response.status_code)):
            if response.status_code == 429:
                print("Breaking a request rate limit. Single IP address can \
send less than 10 requests per second")
            print("Invalid requests ")
            sys.exit()

    def get_historical_values(self) -> Union[List[Dict], None]:
        """
        Open/High/Low/Close values with volume and market_cap.
        Try/except block catches newtwork problems (e.g. DNS failure, refused
        connection etc.)
        Returns: List[Dict] or None (when connection problem occurs)
        """
        try:
            url = f"{self.BASE_URL}/coins/{self.coin}/ohlcv/historical"
            response = requests.get(url, self.query_parameters)
        except requests.exceptions.RequestException as e:
            print("Connection problem. Check arguments.")
        else:
            # print(f"Connection succeed for url:\n{response.url}")
            self._check_status_codes(response)
            return response.json()

    def get_coin_symbols(self) -> List[Dict[str, Union[str, int]]]:
        """
        Fetch all symbols.
        Returns List[Dict]
        """
        url = "https://api.coinpaprika.com/v1/coins"
        response = requests.get(url)
        return response.json()
