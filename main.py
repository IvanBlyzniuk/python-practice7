import app.io.input as my_input
import app.io.output as my_output


def main():
    from_console = my_input.input_from_console()
    from_file = my_input.input_from_file()
    from_file_pandas = my_input.input_from_file_pandas()

    inputs = [from_console, from_file, from_file_pandas]
    for input_data in inputs:
        my_output.output_to_console(input_data)

    my_output.output_to_file(from_console, "output_console.txt")
    my_output.output_to_file(from_file, "output_file.txt")
    my_output.output_to_file(from_file_pandas.to_string(), "output_pandas.csv")

    my_output.output_to_file_pandas(from_file_pandas, "output_pandas.csv")


if __name__ == "__main__":
    main()
