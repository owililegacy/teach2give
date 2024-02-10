#Question 5: 
'''Reverse IntegerWrite a program that takes an integer as input and returns an integer with reversed digit
ordering.'''



def reverse_integer(num):
    # Convert the number to a string and handle the negative sign
    if num < 0:
        num_str = str(num)[1:]  # Exclude the negative sign
        reversed_num_str = '-' + num_str[::-1]  # Add the negative sign back after reversing
        return int(reversed_num_str)
    else:
        return int(str(num)[::-1])

num = int(input("Enter a number: "))
print("Reversed integer:", reverse_integer(num))
