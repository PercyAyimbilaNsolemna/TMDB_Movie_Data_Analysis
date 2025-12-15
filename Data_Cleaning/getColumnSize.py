import ast
import pandas as pd
import numpy as np

def convertCastData(value):
    if pd.isna(value):
        return 0

    # If value was read from CSV → string
    if isinstance(value, str):
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return 0

    # Ensure it's a list
    if isinstance(value, list):
        return len(value)

    return 0

def getColumnSize(data: pd.DataFrame, column: str, columnName: str) -> pd.DataFrame:
    data[columnName] = data[column].apply(convertCastData)
    return data

def main():
    ...



if __name__ == "__main__":
    main()



