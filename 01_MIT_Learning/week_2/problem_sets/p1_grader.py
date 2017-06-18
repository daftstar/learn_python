# ################# INSTRUCTIONS ############################

# A regular polygon has n number of sides.
# Each side has length s.

# Area of regular polygon is:
#         0.25 * n * s^2
#         _______________
#         tan (pi / n)

# Perimeter of polygon is length of boundary of region

# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter
# of the regular polygon.

# The function returns the sum, rounded to 4 decimal places.

############################################################
from math import tan, pi


def polysum(n, s):
    """
    n = integer value for number of sides
    s = integer value for length of sides

    Expected Result:
    Area of Polygon + Squared Perimeter of Polygon,
    rounded to 4 decimal places

    """

    def area_polygon(n, s):
        numerator = .25 * n * (s ** 2)
        denominator = tan(pi/n)

        area = numerator / denominator
        return (area)

    def perimeter_polygon(n, s):
        perimeter = n * s
        return (perimeter)

    polysum_pt1 = area_polygon(n, s)
    polysum_pt2 = perimeter_polygon(n, s) ** 2

    rounded_polysum = round(polysum_pt1 + polysum_pt2, 4)
    return (rounded_polysum)


