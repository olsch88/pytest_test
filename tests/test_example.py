import os
import sys
import pathlib

# # adding project path to sys path according to https://stackoverflow.com/a/38231766
# TEST_DIR = pathlib.Path(__file__)
# PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
# print(TEST_DIR.parent.parent)
# sys.path.insert(0, TEST_DIR.parent.parent / "src")


from src.main import read_file
import pytest


# def test_simple():
#     assert None == main()


def test_read_file():
    text = read_file("./tests/test_data.txt")  # doesn't work
    # text = read_file("test_data.txt")  # doesn't work

    assert text == "Some test data"
