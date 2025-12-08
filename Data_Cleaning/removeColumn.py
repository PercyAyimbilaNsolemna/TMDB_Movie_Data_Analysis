import pandas as pd
import logging

def removeColumn(data: pd.DataFrame, columns: tuple) -> pd.DataFrame:
    """
    Creates a function that removes columns from a dataFrame
    
    :Parameters
    -----------
    data    :   DataFrame
            Pandas DataFrame to remov the columns from

    column(s)   : Tuple
            A tuple of the columns to be removed from the dataFrame

    :Return
    -------
    data    : Pandas DataFrame
            The pandas DataFrame excluding the columns in the tuple
    
    """
    
    # Parameters Validation
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input 'data' must be a pandas DataFrame.")

    if not isinstance(columns, tuple):
        raise TypeError("Columns must be provided as a tuple.")

    if data.empty:
        logging.warning("Provided DataFrame is empty. No columns removed.")
        return data.copy()

    if not columns:
        logging.warning("No columns provided for removal.")
        return data.copy()

    # Filter Columns 
    existing = set(data.columns)
    columns_to_remove = set(columns)

    valid_cols = list(columns_to_remove & existing)
    missing_cols = list(columns_to_remove - existing)

    # Logging missing and invalid columns
    if missing_cols:
        logging.warning(f"Columns not found and were skipped: {missing_cols}")

    if not valid_cols:
        logging.warning("No valid columns were found for removal.")
        return data.copy()

    # Remove Columns
    try:
        new_df = data.drop(columns=valid_cols, axis=1)
        return new_df

    except Exception as e:
        logging.error(f"Unexpected error while removing columns: {e}")
        return data.copy()

def main():
    data = pd.DataFrame({
        "id": [1, 2, 3],
        "title": ["A", "B", "C"],
        "year": [2020, 2021, 2022],
        "rating": [7.5, 8.0, 6.9]
    })

    new_data = removeColumn(data, columns=('rating',))

    print(new_data)

if __name__ == "__main__":
    main()
