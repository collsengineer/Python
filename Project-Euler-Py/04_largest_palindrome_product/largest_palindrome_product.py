#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A palindromic number reads the same both ways. 

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def main():
    # if n_digits_numbers == '2', it means, e.g 12 x 49, or 99 x 99.
    # if '3' = 124 x 245, etc...
    n_digits_numbers = "3"
    print(
        f"""Max palindrome product made of 2-digit numbers: {max_pal_product(n_digits_numbers)}"""
    )


def max_pal_product(n_digits: str) -> int:
    """It checks if the product is palindromic and returns the max value"""

    axb: list[int] = []

    if n_digits == "3":
        a_list_int: list[int] = [val for val in range(1, 1000)]
        b_list_int: list[int] = [val for val in range(1, 1000)]

        for i in a_list_int:
            for j in b_list_int:
                result = i * j
                axb.append(result)

    axb_str: list[str] = [str(i) for i in axb]
    axb_pal: list[str] = [i for i in axb_str if i == i[::-1]]
    axb_pal_int: list[int] = [int(i) for i in axb_pal]

    return max(axb_pal_int)


if __name__ == "__main__":
    main()
