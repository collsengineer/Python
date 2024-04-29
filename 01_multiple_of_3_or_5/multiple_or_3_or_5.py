#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    range_of_numbers = 1000
    print(multiple_3_or_5(range_of_numbers))


def multiple_3_or_5(num: int) -> int:
    resulting_sum: list[int] = []

    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            resulting_sum.append(i)

    return sum(resulting_sum)



if __name__ == "__main__":
    main()
