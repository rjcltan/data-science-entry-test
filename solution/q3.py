def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # If the key is already present, show its original value before overwriting.
    if key in dct:
        print(dct[key])

    # Add the new key-value pair (or overwrite the existing value).
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
if __name__ == "__main__":
    # "name" is a new key, so it is simply added -> {"name": "Alice"}
    print(update_dictionary({}, "name", "Alice"))

    # "age" already exists, so 25 is printed first, then updated -> {"age": 26}
    print(update_dictionary({"age": 25}, "age", 26))
