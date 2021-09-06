def validate_length(data_string):
    """
    Raise ValueError if data_string is not exactly six values
    """
    try:
        if len(data_string) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(data_string)}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False
    print("Length is valid!")
    return True


def convert_to_int(data_string):
    """
    Convert all string values to integer.
    Raise ValueError if data_string cannot be converted to Int
    """
    try:
        values_as_int = [int(value) for value in data_string]
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False
    print("Data is valid!")
    return values_as_int
