def bin_to_hex(binary_string, min_width=0):
    """
    Convert binary string into hex string
    :param binary_string: binary string
    :param min_width: width of hex string
    :return:
    """
    return '{0:0{width}x}'.format(int(binary_string, 2), width=min_width)


def hex_to_bin(hex_string, min_width=0):
    """
    Convert hex string into binary string
    :param hex_string: hex string
    :param min_width: binary of hex string
    :return:
    """
    return '{0:0{width}b}'.format(int(hex_string, 16), width=min_width)


def zero_lpad(number, length):
    """
    Fill 0 on the left of number
    :param number: number to be padded
    :param length: length of result string
    :return:
    """
    return '{number:0>{length}}'.format(number=number, length=length)

def zero_rpad(number, length):
    """
    Fill 0 on the right of number
    :param number: number to be padded
    :param length: length of result string
    :return:
    """
    return '{number:0<{length}}'.format(number=number, length=length)
