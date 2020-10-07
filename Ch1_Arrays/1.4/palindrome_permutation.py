"""
    PROBLEM: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

    SOLUTION: Offhand, it seems very inefficient to generate every possible permutation of the string. If the string were very long, that would take a long time. There are some characteristics of palindromes which give us an easier way to solve the problem.

    1) A palindrome needs to be the same forwards and backwards.
    2) A palindrome therefore will have mostly even counts of characters. 
    3) If the palindrome string's length is an odd number, there should be only 1 unique character in it and that's the middle character.

    THEREFORE -- We could iterate through the string to create a hashmap with counts of each character. In our hashmap, we can then check to see if the values of each entry are odd or even. 
    
    1) If all of our character counts are even, it's a permutation of a palindrome. 
    2) If all of our character counts ...except one... are even, it's a permutation of a palindrome.
    3) If more than one character count is an odd number, it is not a permutation of a palindrome.

    PSEUDOCODE: 

    create hash table
    create counter to keep track of the number of odd numbers.

    for character in string:
        if character isn't in the hash table:
            add it to the hash table with a count of 1.
        if it IS in the hash table:
            add 1 to the counter.

    Once we've evaluated the string, check the hash table's values. If the value is even, move on. If the value is odd, we increment our counter. Once we have checked all the values, we can look at our counter to determine if the string is a palindrome permutation or not. 

    EDIT: We can do this whole operation with a single set. If a character isn't in the set, add it. If it is in the set, remove it. Iterate through the string adding and removing characters until we get to the end. If the length of the set is <= 1, we're golden. Otherwise, it isn't a palindrome.

"""

# HASH TABLE IMPLEMENTATION
# def palindrome_permutation(string):
#     counter = 0
#     table = {}

#     # Populate the table with the characters in the string.
#     for char in string:
#         if char not in table:
#             table[char] = 1
#         else:
#             table[char] += 1

#     # Check the values in the table. If the value for the character's count is odd, increase the counter by 1.
#     for _, value in table.items():
#         if value % 2 > 0:
#             counter += 1

#     # If the counter is greater than or equal to 2, that means that the string absolutely cannot be a palindrome because there's more than 1 character with an odd number of repetitions.
#     if counter >= 2:
#         return False

#     # Assuming that we make it through all of those checks and nothing returns false, we return True.
#     return True


def palindrome_permutation(string):
    string_set = set()

    for char in string:
        if char not in string_set:
            string_set.add(char)
        else:
            string_set.remove(char)

    print(string_set)
    if len(string_set) >= 2:
        return False
    else:
        return True


print(palindrome_permutation("at"))
