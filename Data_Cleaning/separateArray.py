import pandas as pd
import ast
import numpy as np

def separateArray(data: pd.DataFrame, columns: dict, separator: str=" | ") -> pd.DataFrame:
    """
    Converts JSON-like array columns into pipe (|) separated strings.

    Example:
    Input:
        [{'id': 12, 'name': 'Adventure'}, {'id': 28, 'name': 'Action'}]

    Output:
        'Adventure|Action'

    Parameters
    ----------
    data : pd.DataFrame
        Input DataFrame

    columns : dictionary
        Columns that contain JSON-like arrays (list of dicts) as key value pair with keys being
        columns to extract and values being keys to use to extract values in the list 

    Returns
    -------
    pd.DataFrame
        Transformed DataFrame
    """
     # Apply transformation to each column
    for col, key in columns.items():
        if col in data.columns:
            data[col] = data[col].apply(lambda value: extract_key(value, key, separator))
        else:
            print(f"Column '{col}' not found in dataset. Skipping.")

    return data


def extract_key(value, key, separator):
    """
    Extracts values for the specified keys and separate them with a Pipe (|)
    
    :Parameters
    value   :   array of dicts
            Array containing dictionary items with details of that field

    key :  string
            Key to use to extract the value in the dictionary in that particular cell

    Returns:
    --------
    The values separated with a Pipe (|)
    """
    
    # Safe NaN handling
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return np.nan

    try:
        # Convert string → list
        if isinstance(value, str):
            value = ast.literal_eval(value)

        # Ensure correct type
        if not isinstance(value, list):
            return np.nan

        # Extract values using dynamic key
        values = [item.get(key) for item in value if isinstance(item, dict) and key in item]

        return separator.join(map(str, values)) if values else np.nan

    except Exception:
        return np.nan


def main():
    sampleData = pd.DataFrame({
        "title": ["Merlin"],
        "genre": [[
                    {
                    "id": 12,
                    "name": "Adventure"
                    },
                    {
                    "id": 28,
                    "name": "Action"
                    },
                    {
                    "id": 878,
                    "name": "Science Fiction"
                    }
                ]],
        "production companies": [[
                                    {
                                    "id": 420,
                                    "logo_path": "/hUzeosd33nzE5MCNsZxCGEKTXaQ.png",
                                    "name": "Marvel Studios",
                                    "origin_country": "US"
                                    },
                                    {
                                    "id": 430,
                                    "logo_path": "/hUzeosd33nzE5MCNsZxCGEKTXaQ.png",
                                    "name": "Navel Studios",
                                    "origin_country": "Africa"
                                    }
                                ]]
    })

    modifiedData = separateArray(sampleData, columns={"genre":"name", "production companies":"origin_country"})

    print(modifiedData)


if __name__ == "__main__":
    main()