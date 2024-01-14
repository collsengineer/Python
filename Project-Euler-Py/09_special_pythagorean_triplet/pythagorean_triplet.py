"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

            a² + b² = c²

for example:

            3² + 4² = 9 + 16 = 25 = 5²

There's exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""


def main():
    d = 1000
    product = pythagorean_triplet_product(d)

    print(f"Product abc: {product}")


def pythagorean_triplet_product(d: int) -> int:
    """a + b + c = d"""

    for a in range(1, d):
        for b in range(a, d - a):
            c = d - a - b
            if a * a + b * b == c * c:
                product: int = a * b * c
                break

    return product


if __name__ == "__main__":
    main()
