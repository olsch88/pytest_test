from src.main import read_file, use_import

# def test_simple():
#     assert None == main()


def test_read_file():
    text = read_file("./tests/test_data.txt")  # does work
    # text = read_file("test_data.txt")  # doesn't work

    assert text == "Some test data"
