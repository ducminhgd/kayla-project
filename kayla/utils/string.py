import six


def xor(str_1, str_2, *args):
    """
    XOR 2 or more strings,
    :param str_1: first string
    :param str_2: second string
    :param args: more strings
    :return: 
    """
    str_result = xor_2_str(str_1, str_2)
    for add_str in args:
        str_result = xor_2_str(str_result, add_str)
    return str_result


def xor_2_str(str_1, str_2):
    """
    XOR 2 strings together, the result string has length of the longest string
    :param str_1: first string
    :param str_2: second string
    :return: result string
    """
    len_1 = len(str_1)
    len_2 = len(str_2)
    if len_1 > len_2:
        str_2 = rpad(str_2, '\0', len_1)
    else:
        str_1 = rpad(str_1, '\0', len_2)
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str_1, str_2))


def lpad(orig, char, length):
    """
    Pad more character to the left of original string to have enough length.
    If original string length is longer than expected string, there is no change
    :param orig: original string
    :param char: filling character
    :param length: expected length of result string
    :return: Padded string or original string
    """
    if six.PY2:
        src_len = len(orig)
        missing_len = length - src_len
        if missing_len > 0:
            orig = '{}{}'.format((missing_len * char), orig)
    else:
        orig = str(orig).ljust(length, char)
    return orig


def rpad(orig, char, length):
    """
    Pad more character to the right of original string to have enough length.
    If original string length is longer than expected string, there is no change
    :param orig: original string
    :param char: filling character
    :param length: expected length of result string
    :return: Padded string or original string
    """
    if six.PY2:
        src_len = len(orig)
        missing_len = length - src_len
        if missing_len > 0:
            orig = '{}{}'.format(orig, (missing_len * char))
    else:
        orig = str(orig).rjust(length, char)
    return orig


def replace(orig, position, char):
    """
    Replace a character in string by position
    :param orig: origin string
    :param position: position to be replaced
    :param char: character to replace
    :return:
    """
    str_len = len(orig)
    if position < 0 or position > str_len - 1:
        return orig

    # Method 1
    # orig = list(orig)
    # orig[position] = char
    # return ''.join(orig)

    # Method 2 - Faster
    return orig[:position] + char + orig[position + 1:]
