import pandas as pd
import json

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        self._process_data()
        return self.data

    def _process_data(self):
        # Convert 'Purchase History' JSON-like strings to structured data
        def parse_history(history):
            dates = []
            categories = []
            if pd.notna(history):
                if isinstance(history, str):
                    try:
                        history_json = json.loads(history)
                        if isinstance(history_json, list):
                            for entry in history_json:
                                dates.append(entry.get("Date") or entry.get("Purchase Date"))
                                categories.append(entry.get("Category") or entry.get("Product Category"))
                        elif isinstance(history_json, dict):
                            dates.append(history_json.get("Purchase Date"))
                            categories.append(history_json.get("Product Category"))
                    except json.JSONDecodeError:
                        pass
            return dates, categories
        
        # Apply parsing and create new columns for purchase dates and categories
        self.data['Purchase Dates'], self.data['Purchase Categories'] = zip(*self.data['Purchase History'].apply(parse_history))