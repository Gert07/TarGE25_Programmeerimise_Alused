"""Math exercises."""
from math import remainder
import math

from numpy.ma.core import multiply


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = float(num_a / num_b)
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi ** radius
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    return round(triangle_area, 0)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b**2 - 4*a*c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a**2+b**2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c**2 - a**2)
    return b

if __name__ == '__main__':
    addition_result, difference =  sum_and_difference(5, 6)
    assert addition_result == 11
    assert difference == -1

    float_division_result = float_division (6,2)
    assert 2.99 < float_division_result < 3.01

    integer_division_result = integer_division(10,2)
    assert isinstance(integer_division_result, int)
    assert integer_division_result == 5

    multiply_numbers, power, remainder = powerful_operations(4,5)
    assert multiply_numbers == 20
    assert power == 4 ** 5
    assert remainder == 4

    find_average_result = find_average(5, 9)
    assert find_average_result == 7

    circle_area_result = area_of_a_circle(5)
    assert circle_area_result == round(math.pi ** 5, 2)
