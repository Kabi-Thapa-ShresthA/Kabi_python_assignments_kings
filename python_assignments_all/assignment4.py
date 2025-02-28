# 1. Write a Python function read_file_content(file_path) that takes the path of a text file as input and returns its content as a string.

def read_file_content(file_path):
  
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


# 2. Write another function write_to_file(file_path, content) that takes a file path and a string content as input and writes the content to the file.

def write_to_file(file_path, content):
    
    with open(file_path, 'w') as file:
        file.write(content)


# 3. Write a function find_longest_word(file_path) that reads a text file and returns the longest word in the file.

def find_longest_word(file_path):
    
    content = read_file_content(file_path)
    words = content.split()
    return max(words, key=len) if words else ""


# 4. Write a function check_file_empty(file_path) that takes a file path as input and returns True if the file is empty, and False otherwise.

def check_file_empty(file_path):
    
    return len(read_file_content(file_path).strip()) == 0


# 5. Write a function reverse_file_content(file_path) that reads a text file and writes its content in reverse order to a new file named reversed.txt.

def reverse_file_content(file_path):
    
    content = read_file_content(file_path)
    reversed_content = content[::-1]
    write_to_file('reversed.txt', reversed_content)


# 6. Write a Python function convert_to_uppercase that:
#    - Accepts a list of strings.
#    - Uses a lambda function inside map() to convert all strings in the list to uppercase.
#    - Returns the list of uppercase strings.

def convert_to_uppercase(strings):
    
    return list(map(lambda s: s.upper(), strings))


# 7. Write a Python function filter_even_length_words that:
#    - Accepts a list of strings.
#    - Uses a lambda function inside the filter() function to return only words that have an even length.

def filter_even_length_words(words):
    #Filters and returns words with even lengths.
    return list(filter(lambda w: len(w) % 2 == 0, words))


# 8. Write a function process_file_with_lambda that:
#    - Takes a file name as input.
#    - Reads each line from the file and uses a lambda function to convert each word in the line to uppercase.
#    - Writes the processed lines back to the file.

def process_file_with_lambda(file_path):
    """Converts each word in the file to uppercase and writes back to the file."""
    lines = read_file_content(file_path).splitlines()
    processed_lines = [' '.join(map(lambda w: w.upper(), line.split())) for line in lines]
    write_to_file(file_path, '\n'.join(processed_lines))



