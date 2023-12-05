def read_file(filename=""):
    """Print the contents of a UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
