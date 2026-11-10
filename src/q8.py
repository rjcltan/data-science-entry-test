"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: It returns 3. The condition `n % 2 == 1` is true when a number
    leaves a remainder of 1 after dividing by 2, i.e. when it is ODD, so the
    function counts the odd numbers 1, 3 and 5 instead of the evens.

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
"""

def count_evens(numbers):
    """Return how many even numbers are in the list `numbers`."""
    count = 0
    for n in numbers:
        # An even number divides by 2 with no remainder, so check for 0
        # (the bug was checking for a remainder of 1, which means odd).
        if n % 2 == 0:
            count = count + 1
    return count


if __name__ == "__main__":
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))  # Expected: 4 (2, 4, 6, 8)


"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: It checks whether n divided by 2 leaves a remainder of 0, which
    means n is an even number.
"""
