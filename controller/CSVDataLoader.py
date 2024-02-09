import pandas as pd

class CSVDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        return pd.read_csv(self.file_path)
