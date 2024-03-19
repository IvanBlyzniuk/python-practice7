

def output_to_console(text):
    """
    Outputs the given text to the console

    Args:
        text (str): the text that needs to be outputted
    """
    print(text)


def output_to_file(text, file_name):
    """
    Outputs the given text to the file named using file_name argument located in "data" directory
    using default python capabilities

    Args:
        text (str): the text that needs to be outputted
        file_name (str): filename
    """
    with open(f'./data/{file_name}', mode='w') as file:
        file.write(text)


def output_to_file_pandas(data, file_name):
    """
    Outputs the given data to the file named using file_name argument located in "data" directory using pandas library

    Args:
        data (DataFrame): the data that needs to be outputted
        file_name (str): filename
    """
    data.to_csv(f'./data/{file_name}')
