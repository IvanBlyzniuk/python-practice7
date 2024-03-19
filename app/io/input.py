import pandas as pd


def input_from_console():
    """
    Reads some input from console and returns it as a string

    Returns:
        str. The string that was inputted in console
    """
    return input()


def input_from_file():
    """
    Reads some input from file named "input.txt" located in "data" directory using default python capabilities

    Returns:
        str. The text that was present inside the file
    """
    with open('./data/input.txt') as file:
        file_content = file.read()
        return file_content


def input_from_file_pandas():
    """
    Reads some input from file named "input_pandas.csv" located in "data" directory using pandas library
    and converts it into a DataFrame

    Returns:
        DataFrame. The data that was present inside the file
    """
    return pd.read_csv('./data/input_pandas.csv')
