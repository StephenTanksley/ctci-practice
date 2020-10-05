"""
    PROBLEM: Given two strings, write a method to decide if one is a permutation of the other.

    SOLUTION: First off - what is the definition of a permutation?

    A permutation of a string is where all of the characters are the same, but the order is not the same.

    A naive approach might be to use one string to populate a set. Then, using the second string, check whether each character in that string exists in the set.

    This approach would be O(N) time complexity with O(N) space complexity. The set would take up N amount of space. 

    THINGS TO CONSIDER:

    1) What if the strings are not the same length?
        1a) They can't be an exact permutation if they're different lengths.

    2) What if there are non-character punctuation marks?
        2a) That would remove 

"""


def is_permutation(string_1, string_2):
    pass
