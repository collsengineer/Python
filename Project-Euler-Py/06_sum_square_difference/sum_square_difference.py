#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The sum of the squares of the first ten natural numbers is:

        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

        (1 + 2 + ... + 10)^2 = 55^2 = 3025


Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is:

        3025 - 385 = 2640


Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum"""


def main():
    first_natural_numbers = 100
    print(sum_square_difference_of(first_natural_numbers))


def sum_square_difference_of(natural_numbers: int) -> int:
    sum_squares: int = sum([i**2 for i in range(1, natural_numbers + 1)])
    squares_sum: int = sum([i for i in range(1, natural_numbers + 1)]) ** 2
    sum_square_diff: int = squares_sum - sum_squares

    return sum_square_diff


if __name__ == "__main__":
    main()
