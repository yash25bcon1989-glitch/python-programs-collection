"""
Fibonacci Sequence Generator
============================
Prints the Fibonacci sequence for a user-entered number of terms.

The Fibonacci sequence starts with 0 and 1. Every subsequent number is
the sum of the two numbers before it:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Example:
    Enter the number of terms: 7
    Fibonacci sequence (7 terms):
    0  1  1  2  3  5  8
"""


def fibonacci(n: int) -> list[int]:
    """Return a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def main() -> None:
    print("=" * 40)
    print("    Fibonacci Sequence Generator")
    print("=" * 40)

    while True:
        user_input = input("\nEnter the number of terms: ").strip()

        try:
            n = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 7).")
            continue

        if n <= 0:
            print("Please enter a positive integer (1 or greater).")
            continue

        break

    sequence = fibonacci(n)
    print(f"\nFibonacci sequence ({n} {'term' if n == 1 else 'terms'}):")
    print("  ".join(str(num) for num in sequence))


if __name__ == "__main__":
    main()
