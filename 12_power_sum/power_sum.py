"""
   2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

   What's the sum of the digits of the number 2^1000?
"""


def main() -> None:
    # Calculate 2^1000
    power = pow(2, 1000)

    # Convert result to string and sum its digits
    digit_sum = sum(int(digit) for digit in str(power))

    print(f"Sum of digits of 2^1000: {digit_sum}")


if __name__ == "__main__":
    main()
