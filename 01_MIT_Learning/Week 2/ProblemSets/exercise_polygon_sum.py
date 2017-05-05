"""
INSTRUCTIONS:

A regular polygon has 'n' number of sides. Each side has length 's'.
* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon

Write a function called 'polysum' that takes 2 arguments, 'n' and 's'.
    This function should sum the area
    and square of the perimeter of the regular polygon.

    n = number of sides
    s = length of each side

    The function returns the sum, rounded to 4 decimal places.
"""


# IMPORT SELECTIVE FUNCITONS FROM MATH MODULE

from math import tan
from math import pi


# DISCRETE FUNCTIONS TO HANDLE EACH TYPE OF CALCULATION

def area_polygon(n, s):
    """
    This function calculates the area of a regular polygon.
    var n = integer or float value
    var s = integer or float value.
    """
    area = (0.25 * n * (s ** 2)) / tan(pi/n)
    return area


def perimeter_polygon(n, s):
    """
    This function calculates the perimeter of a regular polygon.
    var n, s = integer or float value
    """
    perimeter = n * s
    return (perimeter)


def polysum(n, s):
    """
    This function adds the area of the polygon to the square of it's perimeter.
    var n, s = integer or float value
    """
    part_1 = area_polygon(n, s)
    part_2 = (perimeter_polygon(n, s) ** 2)
    polysum_value = part_1 + part_2

    return (round(polysum_value, 4))  # returns value rounded to 4 decimals


print (polysum(14, 3))
