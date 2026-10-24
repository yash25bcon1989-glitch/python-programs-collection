# Python Programs Collection

A collection of three beginner-friendly Python programs with input validation, created as part of a B.Tech Computer Science Engineering assignment.

## Programs

| # | File | Description |
|---|------|-------------|
| 1 | `factorial.py` | Calculates the factorial of a non-negative integer entered by the user. |
| 2 | `fibonacci.py` | Prints the Fibonacci sequence for a user-entered number of terms. |
| 3 | `struct-to-dict.py` | Demonstrates converting structured student data into a Python dictionary using a dataclass. |

## Requirements

- **Python 3.9 or later** (uses type hints like `list[int]`)

No external libraries are required — all three programs use only the Python standard library.

## How to Run

Open a terminal in this folder and run any program with:

```bash
python factorial.py
python fibonacci.py
python struct-to-dict.py
```

Each program will prompt you for input. Type your answer and press Enter.

## Program Details

### 1. factorial.py

Calculates the factorial of a non-negative integer using an iterative loop.

- Validates that input is a whole number (rejects decimals and text).
- Rejects negative numbers.
- Returns `1` for `0` (by definition, `0! = 1`).

**Example output:**

```
========================================
       Factorial Calculator
========================================

Enter a non-negative integer: 5

The factorial of 5 is 120.
```

### 2. fibonacci.py

Generates the first `n` terms of the Fibonacci sequence.

- Validates that input is a whole number.
- Rejects zero and negative numbers.
- Handles the edge case of a single term (prints just `0`).

**Example output:**

```
========================================
    Fibonacci Sequence Generator
========================================

Enter the number of terms: 7

Fibonacci sequence (7 terms):
0  1  1  2  3  5  8
```

### 3. struct-to-dict.py

Demonstrates converting structured student data into a Python dictionary.

Python does not have C-style `struct` types. This program uses a `dataclass` (the modern Python equivalent) to hold student fields, then converts it to a plain dictionary using two methods so you can see how each works:

1. **`dataclasses.asdict()`** — the standard-library helper that auto-converts any dataclass.
2. **Manual conversion** — building the dictionary field by field to show the logic behind it.

Both methods produce identical results, which the program verifies at the end.

- Validates that the name is not empty.
- Validates that the roll number is a non-negative integer.
- Validates that marks are a number between 0 and 100.

**Example output:**

```
========================================
   Structure to Dictionary Converter
========================================

Python has no C-style struct, so we use a dataclass to hold structured data, then convert it to a dictionary.

Enter student name: Yash Sharma
Enter roll number: 42
Enter marks: 87.5

Student (structured):
    Student(name='Yash Sharma', roll_number=42, marks=87.5)

Converted to dictionary (asdict):
    {'name': 'Yash Sharma', 'roll_number': 42, 'marks': 87.5}

Converted to dictionary (manual):
    {'name': 'Yash Sharma', 'roll_number': 42, 'marks': 87.5}

Both methods produce identical dictionaries.
```

## File Structure

```
python-programs-collection/
├── factorial.py
├── fibonacci.py
├── struct-to-dict.py
└── README.md
```

## Author

Yash Sharma — B.Tech Computer Science Engineering (AI & ML specialization)
