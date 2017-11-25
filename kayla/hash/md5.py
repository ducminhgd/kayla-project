import hashlib


def md5(data, salt='', upper_case=False):
    """
    Hash data into MD5 string
    :param data: data to be hashed
    :param salt: salt string added in the end of data
    :param upper_case: cast hashed string into upper case
    :return: md5 hashed string
    """
    if not isinstance(salt, str):
        salt = str(salt)
    md5_string = hashlib.md5(data + salt).hexdigest()
    if upper_case:
        md5_string = md5_string.upper()
    return md5_string


def md5_verify(sign, data, salt=None, upper_case=False):
    """
    Verify a md5 sign
    :param sign: md5 string
    :param data: data to verify
    :param salt: salt if any
    :param upper_case: sign is uppercase or not 
    :return: True or False
    """
    expected_sign = md5(data, salt, upper_case)
    return sign == expected_sign
