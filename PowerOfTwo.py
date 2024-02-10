#Question 3: Power of Two
'''Write a program that takes an integer as input and returns true if the input is a power of two'''


def isPowerOfTwo(n):
    
    if n <= 0:
        return print('False')
    while n > 1:
        if n%2!=0:
            return print('False')
        n=n//2
    return print('True')
    
n = int(input("Enter a number:"))
isPowerOfTwo(n)