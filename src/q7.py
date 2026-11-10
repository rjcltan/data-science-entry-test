"""
Question 7 — Python: Read and Predict Output  [Short Answer — Write Code]

AI tools can write code for you. This question checks something more important:
can you READ code and work out what it does? Do NOT run the code first. Read
it and predict the output by hand. (You may run it afterwards to check.)

------------------------------------------------------------------
Snippet 1
------------------------------------------------------------------

    numbers = [3, 8, 1, 9, 4]
    total = 0
    for n in numbers:
        if n > 4:
            total = total + n
    print(total)

(a) What does this print? Write the exact value.

    Answer: 17

    Working: go through the list one number at a time.
      3 > 4? no  -> total stays 0
      8 > 4? yes -> total = 0 + 8 = 8
      1 > 4? no  -> total stays 8
      9 > 4? yes -> total = 8 + 9 = 17
      4 > 4? no (4 is not greater than 4) -> total stays 17

(b) In one sentence, describe in plain English what this loop computes.

    Answer: It adds up only the numbers in the list that are strictly
    greater than 4 (here 8 + 9) and prints that sum.

------------------------------------------------------------------
Snippet 2
------------------------------------------------------------------

    def greet(name="world"):
        return "Hello, " + name + "!"

    print(greet())
    print(greet("Ada"))

(c) Write the two lines this program prints, in order.

    Answer:
    Line 1: Hello, world!
    Line 2: Hello, Ada!

    greet() is called with no argument, so name uses its default value
    "world"; greet("Ada") passes "Ada", which replaces the default.
"""


# Check the predictions by running the snippets (python3 src/q7.py).
if __name__ == "__main__":
    # Snippet 1: sum the numbers greater than 4
    numbers = [3, 8, 1, 9, 4]
    total = 0
    for n in numbers:
        if n > 4:
            total = total + n
    print(total)  # 17

    # Snippet 2: function with a default argument
    def greet(name="world"):
        return "Hello, " + name + "!"

    print(greet())       # Hello, world!
    print(greet("Ada"))  # Hello, Ada!
