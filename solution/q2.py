def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Walk the list by index so each matching element can be replaced in place.
    for index, value in enumerate(lst):
        if value == find_val:
            lst[index] = replace_val
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
if __name__ == "__main__":
    # Every 2 is replaced with 5 -> [1, 5, 3, 4, 5, 5]
    print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))

    # Every "apple" is replaced with "orange" -> ["orange", "banana", "orange"]
    print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
