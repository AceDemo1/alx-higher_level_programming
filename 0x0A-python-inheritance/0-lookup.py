#!/usr/bin/python3
"""
A function that returns the list of available attributes and methods
of an object
"""
def lookup(obj):
    """ Returns a list of attributes and methods of an object. 
    Args: obj: The object to inspect. 
    Returns: A list of strings representing the attributes and methods of the object. 
    """
    return list(dir(obj))
