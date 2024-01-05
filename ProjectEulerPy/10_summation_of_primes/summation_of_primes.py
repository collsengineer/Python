"""
The sum of the primes below 10 is:
    2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million (2000000).

"""


def main():
    N = 2000000
    primes_below_N = generate_prime_numbers(N)
    total = sum(primes_below_N)

    print(f"Summation of primes below {N} = {total}")


def generate_prime_numbers(N: int) -> list:
    primes: list = []
    for num in range(2, N):
        is_prime: bool = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes


if __name__ == "__main__":
    main()
