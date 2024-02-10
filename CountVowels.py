#Question 6: Count Vowels
'''Write a program that counts the number of vowels in a sentence.'''


def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    seen_vowels = set()  # Using a set to store unique vowels encountered

    for char in sentence:
        if char in vowels and char.lower() not in seen_vowels:
            count += 1
            seen_vowels.add(char.lower())

    print("Number of unique vowels:", count)

sentence = input("Enter the sentence: ")
count_vowels(sentence)
