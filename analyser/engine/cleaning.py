import re
import pandas as pd
import numpy as np
from typing import List, Union, Optional


class CleanData:
    def drop_columns(self, data: pd.DataFrame,
                     cols_to_drop: List[str],
                     ) -> None:
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

        data.drop(columns=existing_cols, inplace=True)

    # Cleaning up number of appearances.

    def appearances_fix(self, data: Union[pd.Series, pd.DataFrame],
                        col_name: Optional[str] = None) -> None:
        """
        The default appearances is showed in multiple ways.
            1. For Players with no substitute appearance the apps are shown as 30.
            2. For Players with substitute appearance the apps are shown as 30 (15).

        Args:
            data (Union[pd.Series, pd.DataFrame]): The Appearances data.
        """

        if type(data) == pd.DataFrame:
            if col_name is None:
                raise Exception("Provide the column name which contains \
                                the appearances data.")
            data = data[col_name]

        data[col_name] = data[col_name].str.extract(
            r'(\d+)\s*(?:\((\d+|\-)\))?').fillna(0).astype(int)

    def unit_values_to_numeric(self, df: pd.DataFrame, col_names: List[str]) -> None:
        """
        Clear out unit values and convert to numeric.
        Dataframe is edited in place.

        Args:
            df (pd.DataFrame): Dataset.
            col_names (List[str]): Names of column with unit values.
        """

        for column in col_names:
            if df[column].dtype != 'O':
                continue
            df[column] = df[column].str.extract('(\d+)').astype(float)

    def detect_percentage_columns(self, df: pd.DataFrame) -> List[str]:
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

    def convert_percentage_to_numeric(self, df: pd.DataFrame) -> None:
        """
        The percentage values to nums.

        Args:
            df (pd.DataFrame): Dataset.
        """

        percentage_cols = self.detect_percentage_columns(df)

        for column in percentage_cols:
            df.loc[:, column] = pd.to_numeric(
                df[column].str.strip('%'), errors='coerce').fillna(0) / 100

    # Handling NAN data.
    def get_nan_percentage(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        The percentage of null values in the dataset per column.

        Args:
            df (pd.DataFrame): Dataset.

        Returns:
            pd.DataFrame: Dataframe containing columns and their % of nul values.
        """

        return pd.DataFrame(
            ((df.isna().sum()) / len(df)) * 100
        )

    def fill_na(self, df: pd.DataFrame):
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

    def wages_str_to_num(self, input_str: str) -> float:
        """
        Extracting the Wage from string.
        eg. "Â£400 p/w" -> 400.0
        """
        if input_str is np.NaN:
            return 0

        match = re.search(r'\d+(\.\d+)?', input_str)

        if match:
            number = match.group()
            return number
        return input_str

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the dataframe and returns clean.
        """

        self.drop_columns(df, cols_to_drop=[
            'Ability', 'Injury Risk',
            'SHP', 'CON', 'Fatigue',
            'Position Selected',
            "Potential",
            'Overall Happiness'])
        # self.appearances_fix(df, 'Apps')
        df['Wage'] = df['Wage'].apply(lambda wage: self.wages_str_to_num(wage))
        self.unit_values_to_numeric(
            df, col_names=['Height', 'Distance', 'Dist/90'])
        self.convert_percentage_to_numeric(df)
        df = self.fill_na(df)

        return df
