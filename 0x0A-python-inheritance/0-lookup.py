#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj (object): The object to inspect.

    Returns:
    - list: List of available attributes and methods.
    """
    return dir(obj)
