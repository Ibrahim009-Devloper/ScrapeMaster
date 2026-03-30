import pandas as pd
import re
import os

class clean_Amazon_data():
    dataset = pd.read_excel(".//Data//processed//Amazon_product.xlsx")

    def title_clean(text):
        word = str(text).split()
        if len(word) > 6:
            return "".join(word[:6]) + "..."
        return "".join(word)

    dataset["Title"] = dataset["Title"].apply(title_clean)

    dataset["Price"] = dataset["Price"].astype(str).str.extract(r"(\d+\.\d+|d+)").astype(float)

    dataset["Rating"] = dataset["Rating"].fillna("No Rating")
    dataset["Rating"] = dataset["Rating"].astype(str).str.extract(r"(\d+\.?\d+|d+)").astype(float)

    def clean_sales(value):
        value = str(value).lower()
        if "NAN" in value or "N/A" in value:
            return 0.0
        matching = re.search(r"(\d+\.?\d*)",value)
        if matching:
            nan = float(matching.group(1))
            if "k" in value:
                return nan*1000
            return nan
        return 0.0


    dataset["monthly sels"] = dataset["monthly sels"].apply(clean_sales)

    folder_path = "Data/Export_ready_data/Amazon_data"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # file_path = os.path.join(folder_path,"")
    dataset.to_csv(f"{folder_path}/Amazon_clean_data.csv")
    dataset.to_json(f"{folder_path}/Amazon_clean_data.json")
    dataset.to_excel(f"{folder_path}/Amazon_clean_data.xlsx")

if __name__=="__main__":
    clean_Amazon_data()