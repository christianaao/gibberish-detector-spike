def txt_convert(text_file="queries.txt"):
    """
    Function to convert text file to list data type

    Args:

        takes a string of text file name. If none is given, will default to queries.txt

    Returns:

        list of strings from text file
    """
    with open(text_file, "r") as file:
        a = file.read().splitlines()

    print(type(a), a)


txt_convert("queries-fuzzy.txt")
