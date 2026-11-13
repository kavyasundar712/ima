import pandas as pd
from pathlib import Path

BASE_DIR =Path(__file__).resolve().parent

class IncidentRepo:
    def __init__(self):
        self.file_path=BASE_DIR / "files" / "tickets.csv"

    def get_all(self):
        return pd.read_csv(self.file_path)

    def append(self, incident: dict):
        df=pd.DataFrame([incident])
        df.to_csv(self.file_path, mode="a",index=False)

class FaqRepo:
    def __init__(self):
        self.file_path=BASE_DIR / "files" / "faq.csv"
    
    def get_all(self):
        return pd.read_csv(self.file_path)
    
