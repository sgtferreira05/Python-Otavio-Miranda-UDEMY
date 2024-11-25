""" This is an exemple module

This module contain functions and function documentation exemples.
The sum function is likely well-know to you.
"""
variable_1 = 1

def sum_(x: int|float, y: int|float) -> int|float:
    """ 
    sum x, y

    blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, 

    :param x: number 1
    :type x: int or float
    :param y: number 2
    :type y: int or float

    :return: A sum between x,y
    :type: int or float
    """
    return x + y

def times(
        x: int|float,
        y: int|float,
        z: int|float|None = None
) -> int|float:
    """ Times x, y and/or z
    Times x and y. If z is sent, times x, y and z.
    """
    if z is None:
        return x * y
    return x * y * z

variable_2 = 2
variable_3 = 3
variable_4 = 4