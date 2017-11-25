import collections
import json


def sort_by_key(ori_dict):
    ordered_dict = collections.OrderedDict(sorted(ori_dict.items()))
    return ordered_dict
