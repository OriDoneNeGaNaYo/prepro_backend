import os 
import pandas as pd 
import numpy as np

from typing import List
from pathlib import Path


FILE_LOCATION: str = f"{Path(os.getcwd())}/data"


def city_extract(filename: str) -> List[str]:
    data: np.ndarray = pd.read_csv(f"{FILE_LOCATION}/{filename}").values
    
    return [j for i in data for j in i]


def preprocessing(filename: str, csv_file: city_extract, drop_column: str, compare: str) -> pd.DataFrame:
    data = pd.read_csv(f"{FILE_LOCATION}/{filename}").drop(columns=[drop_column])
    dd: List[pd.DataFrame] = [data[data[compare] == i] for i in csv_file]
    data_concat = pd.concat(dd) 
       
    return data_concat
    

def main() -> None:
    filename: str = "gyoung.csv"
    filename2: str = "english_korea_busstop.csv"
    
    ja = city_extract(filename=filename)
    jb = preprocessing(filename2, ja, "ename", "city")
    print(jb)


main()
