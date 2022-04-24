
def is_empty_string(string):

    for char in string:
        if char != " ":
            return False

    return True

def remove_delimiter(string):

    new_string = ""

    try:
        float = float(string)
    except:
        for char in string:
            if char != "." and char != ",":
                new_string += char
        return new_string
    else:
        return string