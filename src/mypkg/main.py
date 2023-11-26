# this works for the script but not with pytest
from .lib import imported_function


def use_import():
    imported_function()


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


if __name__ == "__main__":
    print(read_file("./src./mypkg/real_data.txt"))
