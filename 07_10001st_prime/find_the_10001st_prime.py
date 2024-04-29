#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


def main():
    # Init the range
    start = 2
    # Limit the range
    end = 1000000

    primes = primes_from(start, end)

    # Nth position of the target prime
    n = 10001

    # Getting prime number and its position or index.
    searched_prime, at_position = get_by_index(n, primes)

    print(f"Prime: {searched_prime} at position: {at_position}")


def primes_from(start: int, end: int) -> list:
    primes: list = []

    for i in range(start, end + 1):
        flag: int = 0

        if i < 2:
            continue
        if i == 2:
            primes.append(2)
            continue

        for x in range(2, i):
            if i % x == 0:
                flag = 1
                break

        if flag == 0:
            primes.append(i)

    return primes


def get_by_index(position: int, primes: list) -> tuple[int, int]:
    target_prime: int
    target_position: int

    for index in range(primes[0], len(primes) + 1):
        if index == position:
            target_prime = primes[index - 1]
            target_position = index
            break

    return target_prime, target_position


if __name__ == "__main__":
    main()
