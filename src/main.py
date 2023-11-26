# this works for the script but not with pytest
from lib import imported_function

# this works fot pytest, but not with the script
from .lib import imported_function


def use_import():
    imported_function()


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


if __name__ == "__main__":
    print(read_file("real_data.txt"))
