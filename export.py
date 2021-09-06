# Standard libraries
import json
import os
from datetime import date

# 3rd party libraries
import pandas as pd

# local application imports
from client import Client


class Export:
    def __init__(self, start: date, end: date, coin: str, filename: str,
                 filepath: str = "data/"):
        self.filename = filename
        self.filepath = filepath
        self.coin = coin
        self.client = Client(start, end, coin)
        self.response = self.client.get_historical_values()

    def _subset_columns(self) -> pd.DataFrame:
        df = pd.json_normalize(self.response)
        df = df[['time_close', 'close']]
        df['time_close'] = df['time_close'].apply(lambda x: x[:10])
        df.columns = ['Date', 'Price']
        return df

    def to_csv(self):
        """Converts data to csv file."""
        filename = f"{self.coin}_{self.filename}.csv"
        relative_path = os.path.join(self.filepath, filename)
        absolute_path = os.path.join(os.getcwd(), relative_path)
        df = self._subset_columns()
        try:
            df.to_csv(absolute_path, index=False)
        except Exception as e:
            print(e)
        else:
            print("Data successfully saved to the CSV file.")

    def to_json(self):
        """Converts data to json file."""
        filename = f"{self.coin}_{self.filename}.json"
        relative_path = os.path.join(self.filepath, filename)
        absolute_path = os.path.join(os.getcwd(), relative_path)
        df = self._subset_columns()
        filtered_data = df.to_dict('records')
        try:
            with open(absolute_path, 'w', encoding='utf-8') as file:
                json.dump(filtered_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
        else:
            print("Data successfully saved to the JSON file")
