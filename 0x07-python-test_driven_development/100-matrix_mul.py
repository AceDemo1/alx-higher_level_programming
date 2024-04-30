#!/usr/bin/python3
"""

This module contains a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied
        m_b (list of lists of int/float): Matrix to be multiplied

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the outcome of the multiplication

    """

    if type(m_a) is not list:
       raise TypeError('m_a must be a list')
    if type(m_b) is not list:
       raise TypeError('m_b must be a list')
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    

    re = []
    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError('m_a must be a list of lists')
        ro = []
        for j in range(len(m_a[0])):
            el = 0
            for k in range(len(m_b)):
                if type(m_b[k]) is not list:
                    raise TypeError('m_b must be a list of lists')
                if not m_a[i][k]:
                    raise TypeError("each row of m_a must be of the same size")
                if not m_b[k][j]:
                    raise TypeError("each row of m_b must be of the same size")
                if type(m_a[i][k]) is not int and type(m_a[i][k]) is not float:
                    raise TypeError("m_a should contain only integers or floats")
                if type(m_b[k][j]) is not int and type(m_a[i][k]) is not float:
                    raise TypeError("m_b should contain only integers or floats")
                el += m_a[i][k] * m_b[k][j]
            ro.append(el)
        re.append(ro)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return re
