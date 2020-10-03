"""
    PROBLEM: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
    
    Naive solution: Implement a hashmap as a counter. Loop over the string to add elements to a hashmap, then run a loop to check characters against the keys in the hashmap. If a character is already in the hashmap, return false (not all of the characters in the string are unique). Otherwise, return true.


"""


def is_unique(string):
    table = {}

    for char in string:
        if char not in table:
            table[char] = 1
        else:
            table[char] += 1

    for char in string:
        if table[char] > 1:
            return False
    return True
