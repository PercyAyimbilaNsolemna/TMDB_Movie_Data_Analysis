
import pandas as pd

def convertNumeric(data: pd.DataFrame, columns: list, value: int) -> pd.DataFrame:
    """
    Rounds a numeric column to a specified value
    
    Parameters:

    data    :   pandas.DataFrame
            The pandas DataFrame to perform the modification on

    columns : list
            A list of the columns to perform the conversion on

    value   : int
            The value to round the data in the column to like 1000

    Return

    data    :   pandas.DataFrame
            Returns a pandas DataFrame which has been modified bsed on the given value and the 
            specified columns

    """

    for col in columns:
        if col in data.columns:
            # Scale the data in the column
            data[col] = data[col] / value
            data.rename(columns={col: f"{col}_musd"}, inplace=True)

        else:
            print(f"Column '{col}' not found, skipping.")

    return data

    


def main():
    ...


if __name__ == "__main__":
    main()