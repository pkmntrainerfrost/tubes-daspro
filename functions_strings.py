def is_empty_string(string):

    for char in string:
        if char != " ":
            return False

    return True