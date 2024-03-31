from typing import List, Union, Optional
import pandas as pd

# Dropping columns.

def drop_columns(data: pd.DataFrame,
                 cols_to_drop: List[str],
                ) -> Union[None, pd.DataFrame]:
    """
    given a list of columns names  that need to be dropped from the dataframe.
    Passing Inplace as true will change the dataframe inplace instead of 
    returning new dataframe.

    Args:
        data (pd.DataFrame): The dataframe you want to remove columns from.
        cols_to_drop (List[str]): Names of columns you want to drop.
    Returns:
        Union[None, pd.DataFrame]: depending on inplace flag None or a new 
                                   dataframe is returned.

    """
    if type(data) == pd.Series:
        return "Please Upload Dataframe! Series is not compatible."
    existing_cols = data.columns.intersection(cols_to_drop)

    data = data.drop(columns=existing_cols)

    return data


## Cleaning up number of appearances.
def appearances_fix(data: Union[pd.Series, pd.DataFrame],
                    col_name: Optional[str] = None) -> pd.DataFrame:
    """
    The default appearances is showed in multiple ways.
        1. For Players with no substitute appearance the apps are shown as 30.
        2. For Players with substitute appearance the apps are shown as 30 (15).

    Args:
        data (Union[pd.Series, pd.DataFrame]): The Appearances data.

    Returns:
        pd.DataFrame: appearances divided in columns 
                      "Appearances" and "Substitute Appearances".
    """

    if type(data) == pd.DataFrame:
        if col_name is None:
            raise Exception("Provide the column name which contains \
                            the appearances data.")
        data = data[col_name]

    return data.str.extract(r'(\d+)\s*(?:\((\d+|\-)\))?').fillna(0).astype(int)

def unit_values_to_numeric(df: pd.DataFrame, col_names: List[str]) -> None:
    """
    Clear out unit values and convert to numeric.
    Dataframe is edited in place.

    Args:
        df (pd.DataFrame): Dataset.
        col_names (List[str]): Names of column with unit values.
    """

    for column in col_names:
        df[column] = df[column].str.extract('(\d+)').astype(float)


def detect_percentage_columns(df: pd.DataFrame) -> List[str]:
    """
    Get the columns which values have '%'.

    Args:
        df (pd.DataFrame): Dataset.

    Returns:
        List[str]: names of columns
    """

    percentage_columns: List[str] = []

    for column in df.columns:
        if df[column].dtype == "O":
            if df[column].str.match(r'\b\d+\s*%').any():
                percentage_columns.append(column)

    return percentage_columns


def convert_percentage_to_numeric(df: pd.DataFrame) -> None:
    """
    The percentage values to nums.

    Args:
        df (pd.DataFrame): Dataset.
    """

    for column in df.columns:
        df.loc[:, column] = pd.to_numeric(df[column].str.strip('%'), errors='coerce'
                                          ).fillna(0) / 100

    return df

## Handling NAN data.
def get_nan_percentage(df: pd.DataFrame) -> pd.DataFrame:
    """
    The percentage of null values in the dataset per column.

    Args:
        df (pd.DataFrame): Dataset.

    Returns:
        pd.DataFrame: Dataframe containing columns and their % of nul values.
    """

    return  pd.DataFrame(
                ((df.isna().sum()) / len(df)) * 100
    )


def fill_na(df: pd.DataFrame):
    """
    The percentage of null values in the dataset per column.

    Args:
        df (pd.DataFrame): Dataset.
    """

    df[df.select_dtypes(include=['float']).columns] = df.select_dtypes(
        include=['float']
    ).fillna(0.0)

    df[df.select_dtypes(include=['int64']).columns] = df.select_dtypes(
        include=['int64']
    ).fillna(0)

    df[df.select_dtypes(include=['object']).columns] = df.select_dtypes(
        include=['object']
    ).fillna("Unknown")

    return df