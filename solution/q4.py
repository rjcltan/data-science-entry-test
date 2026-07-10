def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Slicing with a step of -1 walks the string backwards, producing the reverse.
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
if __name__ == "__main__":
    # "Hello World" reversed -> "dlroW olleH"
    print(string_reverse("Hello World"))

    # "Python" reversed -> "nohtyP"
    print(string_reverse("Python"))
