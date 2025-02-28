#Write a Python program to ask the user to enter a decimal number (float). Convert it into an integer and a string. Display all three values (original float, integer, and string) using string formatting.
number = float(input("Enter any number in decimal:: "))

print("Original Float:", number)
print("Converted to integer", int(number))
print("Coonverted to string", str(number))




#Write a Python program to ask the user for their full name. Extract the first letter of the first and last name using string slicing and display the initials in uppercase.
first_name = str(input("Enter your first name::"))
middle_name = str(input("Enter your middle name::"))
last_name = str(input("Enter your last name::"))



first_name = first_name[0].upper() + first_name[1:].lower() if first_name else ""
middle_name = middle_name[0].upper() + middle_name[1:].lower() if middle_name else ""
last_name = last_name[0].upper() + last_name[1:].lower() if last_name else ""


print("Your full name is ", first_name + " " + middle_name + " " + last_name + ".")


initials1 = first_name[0].upper()
initials2 = middle_name[0].upper()
initials3 = last_name[0].upper()

print("Your initials are::", initials1 + " " + initials2 + " " + initials3 )


#Write a Python program that takes a string input from the user and uses string slicing to reverse it. Print the reversed string.
name = str(input("Enter a word:: "))

print("The word is:", name[: : -1])



#Write a Python program that asks the user to enter a word and a starting index. Extract and print the substring from that index to the end using string slicing.
word = input("Enter any word::")
starting_index = int(input("Enter the starting index::"))

output = word[starting_index:]

print("Substring from index ", starting_index, "is : ", output)



#Write a Python program that asks the user to enter an email address. Extract and print the domain name (part after @) using string slicing.
email = str(input("Enter your email address::"))

index = email.index("@")
domain = email[index + 1:]

print(email)
print("Domain::", domain)


#Write a Python program that takes a word as input. Swap its first and last character using string slicing and display the new word.
word = input("Enter any word::")

replace = word[-1] + word[1:-1] + word[0]
print(replace)