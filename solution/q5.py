def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # num is divisible by divisor when the remainder of the division is zero.
    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
if __name__ == "__main__":
    # 10 divided by 2 leaves no remainder -> True
    print(check_divisibility(10, 2))

    # 7 divided by 3 leaves a remainder of 1 -> False
    print(check_divisibility(7, 3))
