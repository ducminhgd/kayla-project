# coding=utf-8
"""
Utility helpers for text, string
"""
import re

TCVN3TAB = "¸µ¶·¹©ÊÇÈÉË¨¾»¼½Æ®ÐÌÎÏÑªÕÒÓÔÖÝ×ØÜÞãßáâä«èåæçé¬íêëìîóïñòô­øõö÷ùýúûüþ¸µ¶·¹¢ÊÇÈÉË¡¾»¼½Æ§ÐÌÎÏÑ£ÕÒÓÔÖÝ×ØÜÞãßáâä¤èåæçé¥íêëìîóïñòô¦øõö÷ùýúûüþ"
TCVN3TAB = [ch for ch in TCVN3TAB]

UNICODETAB = "áàảãạâấầẩẫậăắằẳẵặđéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶĐÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
UNICODETAB = [ch for ch in UNICODETAB]

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
