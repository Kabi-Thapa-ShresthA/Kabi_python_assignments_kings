# Write a function count_vowels(text) that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. The function should be case insensitive (i.e., treat uppercase and lowercase letters the same).

# def count_vowels(word):
#     count = 0

#     for char in word:
#         if(char in "aAeEiIoOuU"):
#             count = count + 1

#     return count

# word = str(input("Enter any anything it will count the vowels in it:"))
# count = count_vowels(word)

# print("The number of vowels in what you have entered are::", count)



# Write a function find_maximum(list1) that takes a list of numbers as input and returns the maximum number from the list. (Do not use the built-in max() function).

# def find_maximum(list):
#     maximum = list[0]
    
#     for number in list:
#         if (number > maximum):
#             maximum = number
            
#     return maximum

# list = [1,2,3,5,9,8,77,11,22,32,66,999,10]

# maximum = find_maximum(list)

# print("the maximum nuber from the list is::", maximum)





# Write a function multiplication_table(n) that takes a number n as input and prints the multiplication table of n from 1 to 10.

# multiplication_table(5)
# # Output:
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # ...
# # 5 x 10 = 50

def mul(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")  # Directly print the result

# Get user input and call the function
num = int(input("Enter a number: "))
mul(num)




# Write a function largest_word(sentence) that takes a sentence as input and returns the longest word in the sentence. If there are multiple words of the same length, return the first one that appears.
# Hint: Split the sentence into words using .split(), then compare the lengths of the words to find the longest one.
# largest_word("Python programming is awesome") 
# # Output: "programming"




# Write a function sum_of_list(numbers) that takes a list of numbers as input and returns the sum of all elements in the list. (Do not use the built-in sum() function).

# sum_of_list([1, 2, 3, 4, 5]) 
# # Output: 15



# Write a function to_title_case(sentence) that takes a sentence as input and returns the sentence in title case, where the first letter of each word is capitalized.

# to_title_case("hello world from python") 
# # Output: "Hello World From Python"

# Write a function is_palindrome(word) that takes a string as input and returns True if the word is a palindrome (reads the same forward and backward), otherwise returns False.

# is_palindrome("madam") 
# # Output: True 
# is_palindrome("hello") 
# # Output: False

# Write a function char_count(s) that takes a string as input and returns a dictionary where keys are the characters and values are their frequencies in the string.

# char_count("hello")  
# # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
