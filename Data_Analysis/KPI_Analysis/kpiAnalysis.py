import pandas as pd

#Defines a function that returns the dataFrame ordered in ascending order based on the given column
def rankColumn(data: pd.DataFrame, column: str, order: str) -> pd.DataFrame:
    """
    Ranks movies using the column nad the order provided
    
    :Parameters

    data    :   pandas DataFrame
            The dataFrame to perform the operation on

    column  : str
            The column to use to rank the movies or the data

    order   :   str
            How to arrange the movies or data in the dataFrame. Asc or Desc

    :Return
    data    :   pandas DataFrame
            The ranked pandas DataFrame

        
    """
    ...

def rankColumn(data: pd.DataFrame, column: str, order: str = "asc") -> pd.DataFrame:
    """
    Ranks movies using a specified column and order.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to rank.

    column : str
        Column name to rank by.

    order : str
        Sorting order: 'asc' or 'desc'.

    Returns
    -------
    pd.DataFrame
        Ranked DataFrame.
    """

    # Validate column
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    # Validate order input and sets it to ascending if the value is not valid
    order = order.lower()
    if order not in ["asc", "desc"]:
        order = "asc"

    # Sort
    data.sort_values(
        by=column,
        ascending=(order == "asc"),
        na_position="last",
        inplace=True
    )

    # Reset index for a clean rank
    data.reset_index(drop=True, inplace=True)

    return data


def main():
    ...


if __name__ == "__main__":
    main()