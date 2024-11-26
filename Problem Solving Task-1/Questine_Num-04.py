Write a program that takes a string and returns the number of unique characters in it.

def count_unique_characters(input_string):
    unique_characters = set(input_string)
    return len(unique_characters)
input_string = "Guvi Geeks Network Private Limited"
print( count_unique_characters(input_string))



