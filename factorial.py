"""
Factorial Calculator
====================
Calculates the factorial of a non-negative integer entered by the user.

The factorial of n (written n!) is the product of all positive integers
from 1 to n. By definition, 0! = 1.

Example:
    Enter a non-negative integer: 5
    The factorial of 5 is 120.
"""

def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main() -> None:
    print("=" * 40)
    print("       Factorial Calculator")
    print("=" * 40)

    while True:
        user_input = input("\nEnter a non-negative integer: ").strip()

        # Validate input — must be a whole number, not a float or text
        try:
            n = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 5).")
            continue

        if n < 0:
            print("Please enter a non-negative integer (0 or greater).")
            continue

        break

    answer = factorial(n)
    print(f"\nThe factorial of {n} is {answer}.")

if __name__ == "__main__":
    main()
