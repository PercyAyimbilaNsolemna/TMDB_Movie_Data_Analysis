import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy

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

#Defines a function that calculates the profit
def calculateProfit(data:pd.DataFrame, revenueColumn: str, budgetColumn: str) -> pd.DataFrame:
    """
    Calculates the profit for every movie using the revenue and budget columns and creates a 
    new column to store the profits
    
    :Parameter:

    data    :   pandas DataFrame
            Data to be used for the profit calculation

    revenueColumn   :   str
                The name of the revenue column

    budgetColumn    :   str
                The name of the budget column

    
    :Return

    data    :   pandas DataFrame
            
    """
     # Validate columns exist
    for col in [revenueColumn, budgetColumn]:
        if col not in data.columns:
            print(f"Column '{col}' not found in DataFrame.")
            return data
        
    # Calculate profit and craete a new column to store the profit
    data["profit"] = data[revenueColumn] - data[budgetColumn]
    return data

def calculateROI(data: pd.DataFrame, revenueColumn: str, budgetColumn: str) -> pd.DataFrame:
    """
    Docstring for calculateROI
    
    :param data: Description
    :type data: pd.DataFrame
    :param revenueColumn: Description
    :type revenueColumn: str
    :param budgetColumn: Description
    :type budgetColumn: str
    :return: Description
    :rtype: DataFrame
    """
    # Validate columns exist
    for col in [revenueColumn, budgetColumn]:
        if col not in data.columns:
            print(f"Column '{col}' not found in DataFrame.")
            return data
        
    # Calculate profit and craete a new column to store the profit
    data["ROI"] = (data[revenueColumn] / data[budgetColumn]).round().astype(int)
    return data

#Defines a function that calculates central tendency (mean, mode and median of a given column)
def calculateCentralTendency(data: pd.DataFrame | DataFrameGroupBy, column: str, measure: str) -> pd.Series | str:
    """
    Docstring for calculateCentralTendency
    
    :param data: Description
    :type data: pd.DataFrame
    :param column: Description
    :type column: str
    :param measure: Description
    :type measure: str
    :return: Description
    :rtype: Series[Any]
    """

    # Determine which columns to check depending on input type
    if isinstance(data, DataFrameGroupBy):
        cols = data.obj.columns
    else:
        cols = data.columns

    # Validate column
    if column not in cols:
        return f"The column '{column}' is not in the DataFrame."

    # Fix measure argument
    measure = measure.lower()

    valid_measures = {"mean", "median", "mode"}

    if measure not in valid_measures:
        return f"Invalid measure '{measure}'. Must be one of: {valid_measures}"

    # Perform calculation
    return getattr(data[column], measure)()



#Defines a function that checks if a specific data exists in the dataFrame
def dataExist(data: pd.DataFrame, keyword: str) -> bool:
    """
    Docstring for dataExist
    
    :param data: Description
    :type data: pd.DataFrame
    :param keyword: Description
    :type keyword: str
    :return: Description
    :rtype: bool
    """

    cols = data.apply(lambda col: col.astype(str).str.contains(keyword, na=False).any())

    if len(cols[cols].index.tolist()) != 0:
        print(f"The columns that have such data is/are \n{cols[cols].index.tolist()}")
        return True
    else:
        print(f"None of the columns have the {keyword}")
        return False


def main():
    ...


if __name__ == "__main__":
    main()