# coding=utf-8
"""
Utility helpers for text, string
"""
import re

TCVN3TAB = [
    "À", "Á", "Â", "Ã", "È", "É", "Ê", "Ì", "Í", "Ò",
    "Ó", "Ô", "Õ", "Ù", "Ú", "Ý", "à", "á", "â", "ã",
    "è", "é", "ê", "ì", "í", "ò", "ó", "ô", "õ", "ù",
    "ú", "ý", "Ă", "ă", "Đ", "đ", "Ĩ", "ĩ", "Ũ", "ũ",
    "Ơ", "ơ", "Ư", "ư", "Ạ", "ạ", "Ả", "ả", "Ấ", "ấ",
    "Ầ", "ầ", "Ẩ", "ẩ", "Ẫ", "ẫ", "Ậ", "ậ", "Ắ", "ắ",
    "Ằ", "ằ", "Ẳ", "ẳ", "Ẵ", "ẵ", "Ặ", "ặ", "Ẹ", "ẹ",
    "Ẻ", "ẻ", "Ẽ", "ẽ", "Ế", "ế", "Ề", "ề", "Ể", "ể",
    "Ễ", "ễ", "Ệ", "ệ", "Ỉ", "ỉ", "Ị", "ị", "Ọ", "ọ",
    "Ỏ", "ỏ", "Ố", "ố", "Ồ", "ồ", "Ổ", "ổ", "Ỗ", "ỗ",
    "Ộ", "ộ", "Ớ", "ớ", "Ờ", "ờ", "Ở", "ở", "Ỡ", "ỡ",
    "Ợ", "ợ", "Ụ", "ụ", "Ủ", "ủ", "Ứ", "ứ", "Ừ", "ừ",
    "Ử", "ử", "Ữ", "ữ", "Ự", "ự", "Ỳ", "ỳ", "Ỵ", "ỵ",
    "Ỷ", "ỷ", "Ỹ", "ỹ"
]

UNICODETAB = [
    "À", "Á", "Â", "Ã", "È", "É", "Ê", "Ì", "Í", "Ò",
    "Ó", "Ô", "Õ", "Ù", "Ú", "Ý", "à", "á", "â", "ã",
    "è", "é", "ê", "ì", "í", "ò", "ó", "ô", "õ", "ù",
    "ú", "ý", "Ă", "ă", "Đ", "đ", "Ĩ", "ĩ", "Ũ", "ũ",
    "Ơ", "ơ", "Ư", "ư", "Ạ", "ạ", "Ả", "ả", "Ấ", "ấ",
    "Ầ", "ầ", "Ẩ", "ẩ", "Ẫ", "ẫ", "Ậ", "ậ", "Ắ", "ắ",
    "Ằ", "ằ", "Ẳ", "ẳ", "Ẵ", "ẵ", "Ặ", "ặ", "Ẹ", "ẹ",
    "Ẻ", "ẻ", "Ẽ", "ẽ", "Ế", "ế", "Ề", "ề", "Ể", "ể",
    "Ễ", "ễ", "Ệ", "ệ", "Ỉ", "ỉ", "Ị", "ị", "Ọ", "ọ",
    "Ỏ", "ỏ", "Ố", "ố", "Ồ", "ồ", "Ổ", "ổ", "Ỗ", "ỗ",
    "Ộ", "ộ", "Ớ", "ớ", "Ờ", "ờ", "Ở", "ở", "Ỡ", "ỡ",
    "Ợ", "ợ", "Ụ", "ụ", "Ủ", "ủ", "Ứ", "ứ", "Ừ", "ừ",
    "Ử", "ử", "Ữ", "ữ", "Ự", "ự", "Ỳ", "ỳ", "Ỵ", "ỵ",
    "Ỷ", "ỷ", "Ỹ", "ỹ"
]

TCVN3_PATTERN = re.compile("|".join(TCVN3TAB))
UNICODE_PATTERN = re.compile("|".join(UNICODETAB))

TCVN3_REPLACES_DICT = dict(zip(TCVN3TAB, UNICODETAB))
UNICODE_REPLACES_DICT = dict(zip(UNICODETAB, TCVN3TAB))


def tcvn3_to_unicode(tcvn3str: str, default='') -> str:
    """
    Convert TCVN3 to Unicode
    :param tcvn3str: source string
    :param default: default value if fail
    :return: result string
    """
    try:
        return TCVN3_PATTERN.sub(lambda m: TCVN3_REPLACES_DICT[m.group(0)], tcvn3str)
    except:
        return default


def unicode_to_tcvn3(unicodestr: str, default='') -> str:
    """
    Convert Unicode string into TCVN3 string
    :param unicodestr: source string
    :param default: default value if fail
    :return: result string
    """
    try:
        return UNICODE_PATTERN.sub(lambda m: UNICODE_REPLACES_DICT[m.group(0)], unicodestr)
    except:
        return default
