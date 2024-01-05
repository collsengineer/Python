#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def main():
    n = 600851475143

    print(largest_prime_factor_of(n))


def largest_prime_factor_of(n: int) -> int:
    i: int = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == "__main__":
    main()
