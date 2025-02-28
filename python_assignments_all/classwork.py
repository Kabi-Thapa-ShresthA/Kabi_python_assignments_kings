#in and not in Operators 
#in Operator -> 

"""text = "python programming"
print("p" in text)
print("z" not in text)
print("Next")


list = [2,4,6,7,8,9]
list1 = [3,5,7,9]

for i in list:
    if i not in list1:
        print(i)
        print("Next")


i = 1
while i <= 5:
    print(i)
    i += 1
"""

#break and continue:

"""for i in range(100):
    if i == 50:
        break
    print(i)"""


"""for i in range(5):
    if i == 2:
        continue
    print(i**2)"""


# num1=int(input("Enter first number::"))
# num2=int(input("Enter second number"))
# num3=int(input("Enter third number"))

# if num1 >= num2:
#     if num1 >= num3:
#         print(num1,"is the largest number")
#     if num2 >= num1:
#         if num2 >= num3:
#             print(num2,"is the largest number")
# else:
#     print(num3,"is the largest number")



#WAP to print all the prime numbers between 1 to 20


# for num in range(20):
#     if num % 2 == 0:
#         print(num)



# for num in range(1, 21):  # Loop from 1 to 20
#     if num > 0:  # Prime numbers are greater than 1
#         for i in range(2, num):
#             if num % i == 0:
#                 break  # Not a prime number, exit the loop
#         else:
#             print(num)


#WAp to take a list of words as input and store the frequency of each word in dictionary


# list = [2,3,4,5,6,8,9,10]
# print(list)

# list[3] = 99
# print(list)  


# fruits = ["apple", " orange", "mango","grapes", "pineapple"]

# dict = {}

# for item in fruits:
#     dict[item] = item
#     print(fruits)
#     print("the dictionary goods are::", dict) 


# students = { "name" : "alice", "age" : 15, "course" : "physics"}

# for key , value in students.items():
#     print(f"{key} : {value}")


# words = input("Enter words separated by spaces: ").split()

# dict = {}

# for word in words:
#     dict[word] = dict.get(word, 0) + 1

# print("Word Frequency Dictionary:", dict)


# words = { "this","is","a","kitab"}

# for key , value in students.items():
#     print(f"{key} : {value}")


#week 4 tuesday

# try:
#     num = int(input("Enter a number: "))
#     divd = 15/num 
# # except ZeroDivisionError as e:
# except Exception as e: #handles every exception 
#     print("Error: ", e)
# else:
#     print("no eror occured")
# finally:
#     print("this will always run")


#syntaxError
# try:
#     eval("print(0/0)")
# except SyntaxError as e:
#     print(f"SyntaxError: {e}")


#typeError

# try:
#     result = '2' + 2
# except TypeError as e:
#     print(f"TypeError: {e}")

#IndexError
# try:
#     my_list = [1, 2, 3]
#     print(my_list[5]) #indexouotof bound
# except IndexError as e:
#     print(f"IndexError: {e}")


#keyError
#valueError
#FileNotfoundError

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None
    except Exception as e:
                    print(f"An error occurred: {e}")
                    return None

read_file("C:\\Users\\ACER\\OneDrive\\Desktop\\routine.txt")


