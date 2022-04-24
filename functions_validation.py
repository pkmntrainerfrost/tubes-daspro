def is_integer(object):

    try:
        integer = int(object)
    except:
        return False
    else:
        return True

def is_alphabet(string):

    for char in string:
        orde = ord(char)
        if not ((65<=orde<=90) or (97<=orde<=122)):
            return False

    return True