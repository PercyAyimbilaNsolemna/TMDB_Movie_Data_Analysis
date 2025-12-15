import ast
import pandas as pd
import numpy as np

def extractData(value, columnKey, columnValue, separator):
    if pd.isna(value):
        return np.nan

    # Handle stringified lists (from CSV)
    if isinstance(value, str):
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return np.nan

    if not isinstance(value, list):
        return np.nan

    directors = [
        person.get("name")
        for person in value
        if isinstance(person, dict) and person.get(columnKey) == columnValue
    ]

    return separator.join(directors) if directors else np.nan

def extractColumnData(data: pd.DataFrame, 
                      column: str, 
                      columnName: str,
                      columnKey: str ,
                      columnValue: str,
                      separator: str = ", ") -> pd.DataFrame:
    data[columnName] = data[column].apply(
                                            lambda value: 
                                            extractData(value, columnKey, columnValue, separator)
                                        )
    
    return data


def main():
    ...


if __name__ == "__main__":
    main()
