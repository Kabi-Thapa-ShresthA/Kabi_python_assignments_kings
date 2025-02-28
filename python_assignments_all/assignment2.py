# Task 1: Print numbers but skip numbers divisible by 5, stop if number > 50

def process_numbers(numbers):
    for num in numbers:
        if num > 50:
            break
        if num % 5 == 0:
            continue
        print(num)

# Example usage
numbers = [3, 10, 15, 22, 33, 45, 51, 60]
process_numbers(numbers)

# Task 2: Check password strength
import re

def check_password_strength(password):
    if len(password) < 6 or password.isalpha():
        return "Weak"
    elif len(password) >= 6 and re.search(r'\d', password) and re.search(r'[a-zA-Z]', password):
        if len(password) >= 8 and re.search(r'[@#$%&]', password):
            return "Strong"
        return "Moderate"
    return "Weak"

# Example usage
password = input("Enter a password: ")
print("Password Strength:", check_password_strength(password))

# Task 3: Reverse every alternate word in a string
def alternate_reverse(sentence):
    words = sentence.split()
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]
    return " ".join(words)

# Example usage
sentence = "Python is an amazing programming language"
print(alternate_reverse(sentence))

# Task 4: Find duplicate words and count occurrences
def word_frequencies(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return {word: count for word, count in freq.items() if count > 1}

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
print(word_frequencies(words))

# Task 5: Book availability check
books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10,
}

def check_book_availability():
    book_name = input("Enter the book name: ")
    if book_name not in books:
        print("Unavailable")
        return
    while True:
        try:
            copies = int(input("Enter number of copies: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    if books[book_name] >= copies:
        print("Available")
    else:
        print("Partially Available")

# Example usage
check_book_availability()

# Task 6: Count word frequency in a dictionary
def count_word_frequency(words):
    freq = {}
    for word in words:
        word_lower = word.lower()
        freq[word_lower] = freq.get(word_lower, 0) + 1
    return freq

# Example usage
words_list = ["This", "is", "good", "is"]
print(count_word_frequency(words_list))
