import pandas as pd

def convertDataType(data: pd.DataFrame, columns: dict) -> pd.DataFrame:
    """
    Cast a pandas object to a specified datatype
    
    Parameters
    ----------
    data    :   pandas DataFrame
            The data to perform the datatype casting on

    columns :   dict
            A dictionary that contains the name of the column to be casted as the key and the value
            as the datatype to be casted to

    Return:
    -------
    data    :   pandas DatFrame

    """
    # Apply data type casting on each of the columns
    for col, dtype in columns.items():

        if col not in data.columns:
            print(f"Column '{col}' not found. Skipping.")
            continue

        try:
            # Numeric types
            if dtype in ["int", "int64", "float", "float64"]:
                data[col] = pd.to_numeric(data[col], errors="coerce")

            # Datetime types
            elif "datetime" in str(dtype):
                data[col] = pd.to_datetime(data[col], errors="coerce")

            # Boolean
            elif dtype == bool:
                data[col] = data[col].astype("boolean")

            # string, category, object
            else:
                data[col] = data[col].astype(dtype, errors="ignore")

        except Exception as e:
            print(f"Could not convert column '{col}' to {dtype}: {e}")

    return data




def main():
    s = pd.DataFrame(
        {
            "Scores": [23.7, 46, 80, "at"],
            "date_str": ['2023-01-01', '2023-01-02','2024-01-02', 'at']
        }
    )
    #ms = convertDataType(s, {"Scores" : "int"})

    s['date_str'] = pd.to_datetime(s["date_str"], errors="coerce")

    print(s)
    


if __name__ == "__main__":
    main()