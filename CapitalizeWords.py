#Question 4: Capitalize Words
'''Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.'''


def capitalize_words(s):
    output = s.title()
    return print(output)

s=input("Enter the words")
capitalize_words(s)