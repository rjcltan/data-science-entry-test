def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Validate that both inputs are numeric (int or float) before swapping.
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Tuple unpacking swaps the values using only x and y (no temp variable).
    x, y = y, x
    print(f"x = {x}, y = {y}")


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
if __name__ == "__main__":
    # "Apple" is not numeric, so swap() returns -1 instead of printing.
    print(swap("Apple", 10))

    # Both values are numeric, so swap() prints "x = 17, y = 9".
    swap(9, 17)
