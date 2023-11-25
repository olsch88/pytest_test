try:  # normal version
    from lib import imported_function
except (ImportError, ModuleNotFoundError):  # for pytest
    from .lib import imported_function


def use_import():
    imported_function()


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


if __name__ == "__main__":
    print(read_file("real_data.txt"))
