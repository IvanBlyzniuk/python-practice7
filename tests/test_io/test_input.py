import unittest
import os
import pandas as pd
from app.io.input import input_from_file, input_from_file_pandas
from app.io.output import output_to_file


class TestInputs(unittest.TestCase):

    def setUp(self):
        os.makedirs("./data", exist_ok=True)

    def test_input_from_txt(self):
        output_to_file("Hello world", "input.txt")
        text = input_from_file()
        self.assertEqual(text, 'Hello world')

    def test_input_from_wrong_extension(self):
        if os.path.isfile("./data/input.txt"):
            os.remove("./data/input.txt")
        output_to_file("Hello world", "input.csv")
        with self.assertRaises(FileNotFoundError):
            text = input_from_file()

    def test_input_from_nonexistent(self):
        if os.path.isfile("./data/input.txt"):
            os.remove("./data/input.txt")
        with self.assertRaises(FileNotFoundError):
            text = input_from_file()

    def test_input_from_csv_pandas(self):
        output_to_file("Hello,world\nline,2", "input_pandas.csv")
        actual = input_from_file_pandas()
        self.assertTrue((actual.columns == ["Hello", "world"]).all())

    def test_input_from_csv_pandas_wrong_extension(self):
        if os.path.isfile("./data/input_pandas.csv"):
            os.remove("./data/input_pandas.csv")
        output_to_file("Hello,world\nline,2", "input_pandas.txt")
        with self.assertRaises(FileNotFoundError):
            actual = input_from_file_pandas()

    def test_input_from_csv_pandas_nonexistent(self):
        if os.path.isfile("./data/input_pandas.csv"):
            os.remove("./data/input_pandas.csv")
        with self.assertRaises(FileNotFoundError):
            actual = input_from_file_pandas()


if __name__ == "__main__":
    unittest.main()
