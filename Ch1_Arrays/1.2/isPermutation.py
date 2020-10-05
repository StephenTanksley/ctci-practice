"""
    PROBLEM: Given two strings, write a method to decide if one is a permutation of the other.

    SOLUTION: First off - what is the definition of a permutation?

    A permutation of a string is where all of the characters are the same, but the order is not the same.

    A naive approach might be to use one string to populate a set. Then, using the second string, check whether each character in that string exists in the set.

    This approach would be O(N) time complexity with O(N) space complexity. 
    
    The set would take up N amount of space where N is the length of the string. This approach assumes that the strings are of equal length.

    THINGS TO CONSIDER:

    1) What if the strings are not the same length?
        1a) They can't be an exact permutation if they're different lengths.

    2) What if both strings are the same?
        2a) That means it wouldn't be a permutation.

"""


def is_permutation(string_1, string_2):

    # Edge case #1 - If the strings provided are the same.
    if string_1 == string_2:
        print("This is the same string, not a permutation.")
        return False

    # Edge case #2 - If the strings are different lengths.
    if len(string_1) != len(string_2):
        return False

    string_set = set(string_1)

    for char in string_2:
        if char not in string_set:
            return False

    return True


print(is_permutation("rats", "rats"))
