"""
    PROBLEM: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

    SOLUTION: Off the top of my head, I want to find a way of comparing the two strings one to one. To that end, I could initialize a loop to run through both strings and compare each character as I come into contact with it.

        1) If the characters match, we move on to the next set of characters.
        2) If the characters don't match, we can increment a counter.
        3) If the counter == 1 at the end of the string, we can return True.
        4) If the counter is > 1, we have more than one required edit and should return False.
        
        SUB PROBLEMS: 
            1) What if the strings are the same? We can check this at the beginning. if str_1 == str_2, return False.
            2) What if the strings are not the same length? If the length of one string is more than 1 character more or less, return False.

"""


def one_away(str_1, str_2):
    pass


print(one_away("something", "someting"))
