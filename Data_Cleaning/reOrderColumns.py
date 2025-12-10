
import pandas as pd

def reOrderColumns(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Reorders the columns in a DataFrame according to the list provided.
    Columns in the list but not in the DataFrame are ignored.
    Columns in the DataFrame but not in the list are appended at the end.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame to reorder.

    columns : list
        The list of column names specifying the desired order.

    Returns
    -------
    pd.DataFrame
        DataFrame with reordered columns.
    """
    # Keep only columns that exist in the DataFrame
    existing_cols = [col for col in columns if col in data.columns]

    # Add any remaining columns that were not specified in the list
    remaining_cols = [col for col in data.columns if col not in existing_cols]

    # Reorder
    return data[existing_cols + remaining_cols]



def main():
    ...

if __name__ == "__main__":
    main()