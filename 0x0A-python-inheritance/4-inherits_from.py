#!/usr/bin/python3
"""4-inherits_from:
    fucntions:
        inherits_from
"""


def inherits_from(obj, a_class):
    """check if obj inherits from a_class"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
