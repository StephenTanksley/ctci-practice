
"""
    PROBLEM: Given a string and a number, insert "%20" between the spaces in the string. 
    
    example: 
        input: "Mr John Smith   ", 13
        output: "Mr%20John%20Smith"
        
    SOLUTION: A possible naive solution would be to iterate through the string and check each character in sequence. If a character is a space, replace that character with "%20" before moving on to the next character.
    
    Possible problems:
        1) What if there's more than one space in a row in the string?
        2) What if 
"""


def urlify(string):
    rtn_string = ""
    url_nums = "%20"

    for char in string:
        if char == " ":
            rtn_string += url_nums
        else:
            rtn_string += char

    return rtn_string


print(urlify("Jacob Jones"))
