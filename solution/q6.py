def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Scan the list from the start, stopping at the first negative number.
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1

    # The loop finished without finding a negative number.
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
if __name__ == "__main__":
    # -1 appears before -2, so -1 is returned.
    print(find_first_negative([3, 5, -1, 7, -2, 8]))

    # The list has no negative numbers -> "No negatives"
    print(find_first_negative([2, 10, 7, 0]))
