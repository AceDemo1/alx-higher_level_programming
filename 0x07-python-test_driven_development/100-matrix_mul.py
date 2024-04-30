#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
       raise TypeError('m_a must be a list')
    if type(m_b) is not list:
       raise TypeError('m_b must be a list')
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    re = []
    for i in range(len(m_a)):
        ro = []
        for j in range(len(m_a[0])):
            el = 0
            for k in range(len(m_b)):
                if not m_a[i][k]:
                    raise TypeError("each row of m_a must be of the same size")
                if not m_b[k][j]:
                    raise TypeError("each row of m_b must be of the same size")
                if type(m_a[i][k]) is not int:
                    raise TypeError("m_a should contain only integers or floats")
                if type(m_b[k][j]) is not int:
                    raise TypeError("m_b should contain only integers or floats")
                el += m_a[i][k] * m_b[k][j]
            ro.append(el)
        re.append(ro)
    return re
