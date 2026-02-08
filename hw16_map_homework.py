from math import isqrt 
import re
# - Map -
# A. Create a function that takes a list of numbers and uses the map() function to 
# double each number in the list.
def get_double_number(num):
    return num * 2

x = map(get_double_number, [3, 5, 4324])
print(list(x))

# B. Write a function that takes a list of temperatures in Celsius and uses map() 
# to convert them to Fahrenheit using the appropriate conversion formula.
def c_convert_f(c):
    return (c * 9/5) + 32

fahrenheit = map(c_convert_f, [34, 43.5, 10, 0, 100])
print(list(fahrenheit))

# C. Implement a function that takes a list of numbers and uses the map() function to 
def get_num_function(num):
    if int(num) > 90:
        return 90
    return num

result = map(get_num_function, [43, 90, 9034, 3434, 24, 92])
print(list(result))

# D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".
def greet(name):
    return f"Hello {name}"

name_greet = map(greet, ["Zaur", "Lale"])
print(list(name_greet))

# E. Create a function that takes a list of numbers and uses the map() function to generate a 
# power series for each number, up to a specified exponent.
def power_series(numbers, max_exp):
    return list(map(lambda x: [x**i for i in range(1, max_exp + 1)], numbers))
    
result = power_series([2, 5, 10], 3)
print(result)

# F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
# of the same index from both lists.
def concat_list(lst_1, lst_2):
    return list(map(lambda s: " ".join(s), zip(lst_1, lst_2)))

print(concat_list(["Salam", "Hello"], ["Aleykum", "World"]))

# G. Create a function that takes a list of floats and uses the map() function to round each float 
# to a specified number of decimal places.
def round_floats(values, decimals):
    return list(map(round, values, [decimals] * len(values)))

num_list = [2.293, 4.3662, 4.5354]
print(round_floats(num_list, 2))

# H. Write a function that takes a list of prices and uses map() to apply a discount percentage to each price.
def apply_discount(cost_list, disc_perc):
    return list(map(lambda p: p * (1 - disc_perc / 100), cost_list))

cost_list = [20, 235, 100]
discount = 10
print(apply_discount(cost_list, discount))

# I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
# a simple encryption algorithm

#           XXXXXXXX

# J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.
def count_vowels(word_list):
    vowels = "aeiouAEIOU"
    return list(map(lambda word: sum(1 for char in word if char in vowels), word_list))
word_list = ["apple", "banana", "Cherry", "Orange"]
print(count_vowels(word_list))

# K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.
def len_string(words):
    return list(map(lambda s: len(s), words))

print(len_string(["bir", "üç", "iki"]))

# - Filter -
# A. Create a function that takes a list of numbers and uses the filter() function to 
# return a new list containing only the even numbers.
numbers = [2, 3, 4, 5, 34, 7, 0, 343, 23.2, 64]

def filter_even_numbers(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False

result = list(
    filter(
        filter_even_numbers, 
        numbers
    )
)

print(result)

# B. Write a function that takes a list of numbers and uses the filter() function to 
# return a new list containing only the prime numbers.

def filter_prime_number(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

filtered = list(
    filter(
        filter_prime_number,
        numbers
    )
)

print(filtered)

# C. Implement a function that filters a list of strings to return a new tuple containing 
# only the words that are palindromes.
words = ["level", "python", "radar", "hello", "madam", "code"]

def filter_palindromes(word):
   return word == word[::-1]

result = tuple(
    filter(
        filter_palindromes,
        words
    )
)

print(result)

# D. Given a list of dictionaries representing employees and their salaries, use filter() 
# to create a new list of employees whose salary is above a specified threshold.
employees = [
    {"name": "Ali", "salary": 5000},
    {"name": "Leyla", "salary": 3000},
    {"name": "Bob", "salary": 7000},
    {"name": "Messi", "salary": 40_000_000}
]

threshold = 3000 

def salary_above_threshold(employee):
    return employee["salary"] > threshold

filtered_employees = list(filter(salary_above_threshold, employees))
print(filtered_employees)

# E. Write a function that takes a list of file names and filters it to return a new list 
# containing only files with a specified file extension.
file_names = ["text.py", "name.txt", "zaur.pdf", "exam.pdf", "django.jpg"]

def filter_extension(files, extension):
    return list(filter(lambda f: f.endswith(extension), files))

pdf_files = filter_extension(file_names, ".pdf")
print(pdf_files)  

# F. Create a function that takes a dictionary of student names and their corresponding grades, 
# and uses filter() to return a new dictionary containing only students who passed (grades above 
# a certain threshold).
grades = {
    "Sahil": 85, 
    "Zaur": 70, 
    "Vusal": 50, 
    "Leyla": 90
}

def passed_students(students, threshold):
    return dict(filter(lambda item: item[1] > threshold, students.items()))

passed = passed_students(grades, 60)
print(passed)

# G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
# filters it to return separate lists for each data type.
data = [1, 2.5, "hello", 3, "42", 4.0, True]

def filter_separate_by_type(data):
    integers = list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool),data))
    strings = list(filter(lambda x: isinstance(x, str), data))
    floats = list(filter(lambda x: isinstance(x, float), data))
    bools = list(filter(lambda x: isinstance(x, bool), data))

    return integers, strings, floats, bools


ints, strs, flts, bls = filter_separate_by_type(data)
print("int:", ints)

print("str:", strs)

print("float:", flts)

print("bool:", bls)

# H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
# of numbers based on the user-provided condition.
numbers = [1, 4, 5, 6, 10, 16, 19]
def filter_by_condition(numbers, condition):
    operator = condition[:2] if condition[:2] in ["<=", ">=", "==", "!="] else condition[0]
    value = int(condition[len(operator):].strip())
    
    def check(x):
        if operator == ">":
            return x > value
        elif operator == "<":
            return x < value
        elif operator == ">=":
            return x >= value
        elif operator == "<=":
            return x <= value
        elif operator == "==":
            return x == value
        elif operator == "!=":
            return x != value
        return False
    
    return list(filter(check, numbers))

print(filter_by_condition(numbers, "<= 10"))

# I. Write a function that takes a list of strings and filters it to return a new list containing 
# only strings that contain a specific substring.
words = ["apple", "banana", "grape", "apricot", "orange"]

def filter_by_substring(words, substring):
    return list(filter(lambda word: substring in word, words))

print(filter_by_substring(words, "an"))

# J. Implement a function that takes a list of strings and filters it to return a new list containing 
# strings with a specified character appearing a certain number of times.
words = ["apple", "banana", "grape", "apricot", "orange"]

def filter_by_char_count(words, char, count):
    return list(filter(lambda word: word.count(char) == count, words))

print(filter_by_char_count(words, "n", 2))

# K. Create a function that takes a list of integers and uses the filter() function to return a 
# new list containing only those numbers for which a specified mathematical function (e.g., square, 
# cube) yields a prime result.
numbers = [1, 4, 5, 6, 10]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def filter_by_prime_function(numbers, func):
    return list(filter(lambda x: is_prime(func(x)), numbers))

print(filter_by_prime_function(numbers, lambda x: x**3))
# GPT 

# L. Write a function that takes a list of date objects and filters it to return a new list containing 
# dates within a specified range.
years = ["1980", "1983", "2000", "2004", "2006", "2010"]

def filter_years_range(years, start_year, end_year):
    def check(y):
        y_int = int(y)
        return start_year <= y_int <= end_year
    return list(filter(check, years))

print(filter_years_range(years, 1980, 2004))

# M. Given a list of cities and their corresponding countries, use filter() to return a new list 
# containing cities from a specific country.
places = [
    {"city": "Paris", "country": "France"},
    {"city": "Lyon", "country": "France"},
    {"city": "Berlin", "country": "Germany"},
    {"city": "Munich", "country": "Germany"},
    {"city": "Baku", "country": "Azerbaijan"}
]

def filter_cities_country(places, country_name):
    def check(place):
        return place ["country"] ==  country_name
    
    filtered_places = filter(check, places)
    return [places["city"] for places in filtered_places]

print(filter_cities_country(places, "France"))

# N. Create a function that takes a list of product objects and uses the filter() function to return a 
# new list containing only available products.
products = [
    {"name": "Laptop", "price": 4000, "available": True},
    {"name": "Phone", "price": 2000, "available": False},
    {"name": "Tablet", "price": 1200, "available": True},
    {"name": "Watch", "price": 400, "available": False},
    {"name": "Car", "price": 13200, "available": True}
]

def filter_available_products(products):
    return list(filter(lambda p: p["available"] is True, products))

print(filter_available_products(products))

# O. Implement a function that takes a list and uses filter() to return a new list containing only 
# the unique elements.
data = [1, 2, 2, 3, 4, 3, 5, 1, "zaur", "mamed", "zaur", "salam", True, False, True, None]

def filter_unique_elements(data):
    seen = set()
    return list(filter(lambda d: d not in seen and not seen.add(d), data))

print(filter_unique_elements(data))
# P. Write a function that takes a list of words and filters it to return a new list containing only 
# anagrams of a specified word.
words = ["listen", "silent", "enlist", "google", "inlets", "banana"]

def filter_anagrams(words, target_word):
    target_sorted = sorted(target_word)
    return list(filter(lambda word: sorted(word) == target_sorted, words))

print(filter_anagrams(words, "etlisn"))

# Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
# specified range.
numbers = [10, 25, 30, 45, 50, 60, 53, 42, 31, 23, 12]
def filter_numbers_range(numbers, start, end):
    return list(filter(lambda x: start <= x <= end, numbers))

print(filter_numbers_range(numbers, 4, 54))

# R. Create a function that takes a list of strings and uses filter() to return a new list containing 
# only strings that match a specific regular expression.
words = ["apple", "banana", "123", "abc123", "xyz"]

def filter_regex(words, pattern):
    regex = re.compile(pattern)
    return list(filter(lambda word: regex.match(word), words))

pattern = r'^[a-z]+$' 
print(filter_regex(words, pattern))

# - Reversed -
# A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
# order of elements in the list.
numbers = [1, 2, 3, 4, 5]

def reverse_list(item):
    return list(reversed(item))

print(reverse_list(numbers))

# B. Create a function that takes a string and uses reversed() to reverse the characters in the string.
def reverse_string(text):
    return "".join(reversed(text))

print(reverse_string("ruaZ"))

# C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.
tpl = ("salam", 4, "3ewd", 4, 1)
def reverse_tuple(data):
    return tuple(reversed(data))

print(reverse_tuple(tpl))

# D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

print(reverse_words("Python is very powerful"))

# E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.
d = {"a": 1, 
     "b": 2, 
     "c": 3
}

def reverse_dict_order(data):
    return {key: data[key] for key in reversed(data)}

print(reverse_dict_order(d))

# F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list.


# G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.
# FIFO
from collections import deque

def reverse_queue(queue):
    queue.reverse()
    return queue

q = deque([1, 2, 3, 4])

print(reverse_queue(q))

# H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.
#LIFO
def reverse_stack(stack):
    return list(reversed(stack))

print(reverse_stack([1, 2, 4, 4]))

# I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
# indices, while keeping the elements at even indices unchanged.
def reverse_odd_indices(lst):
    odd_elements = [lst[i] for i in range(1, len(lst), 2)]
    reversed_odds = list(reversed(odd_elements))
    
    result = lst[:]
    odd_index = 0
    for i in range(1, len(lst), 2):
        result[i] = reversed_odds[odd_index]
        odd_index += 1

    return result

lst = [10, 20, 30, 40, 50, 60]
reverse_odd_indices(lst)

# J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.
def reverse_binary(binary_str):
    return "".join(reversed(binary_str))

print(reverse_binary("13"))

# K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.
def reverse_matrix_rows(matrix):
    return list(reversed(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(reverse_matrix_rows(matrix))

# L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
# separated by a specific delimiter.
def reverse_substrings(text, delimiter):
    parts = text.split(delimiter)
    reversed_parts = ["".join(reversed(part)) for part in parts]
    return delimiter.join(reversed_parts)

s = "ruaz-malas-nac"
print(reverse_substrings(s, "-"))

# - Sorted -
# A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
# the numbers sorted in ascending order.
numbers = [1, 3, 5, 64, 34, 54, 83, -4, 53, 0]

def sort_numbers_ascending(numbers):
    return sorted(numbers)

print(sort_numbers_ascending(numbers))

# B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
# the numbers sorted in descending order.
num = [1, 3, 5, 64, 34, 54, 83, -4, 53, 0]

def sort_numbers_descending(num):
    return sorted(num, reverse=True)

print(sort_numbers_descending(num))

# C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
# with the strings sorted by their lengths.
words = ["five", "four", "two", "three"]

def sort_strings_by_length(words):
    return sorted(words, key=len)

print(sort_strings_by_length(words))

# D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
# the tuples sorted based on their second element.
data = [(1, 3), (4, 1), (2, 2)]

def sort_tuples_by_second(data):
    return sorted(data, key=lambda x: x[1])

print(sort_tuples_by_second(data))

# E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
# with its items sorted by their values.
scores = {"Ali": 85, "Veli": 70, "Aysel": 90}

def sort_dict_by_value(scores):
    return dict(sorted(scores.items(), key=lambda item: item[1]))

print(sort_dict_by_value(scores))

# F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
# with the strings sorted in a case-insensitive manner.
words = ["Banana", "apple", "cherry", "Apricot"]

def sort_strings_case_insensitive(words):
    return sorted(words, key=str.lower)

print(sort_strings_case_insensitive(words))

# G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
# with the objects sorted based on a specified attribute.
# H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
# with the dates sorted in chronological order.
# I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
# the lists sorted based on the sum of their elements.
# J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
# the integers sorted based on the number of factors they have.
# K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
# the strings sorted based on their last characters.
# L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
# with the dictionaries sorted based on their keys.
# M. Sort the following list of strings alphabetically by the second letter:
# string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]

# Quiz.
# 1. What is the purpose of the filter() function in Python?
#     A) To remove elements from an iterable based on a given condition
#     B) To sort elements in an iterable
#     C) To modify elements in an iterable
#     D) To combine elements in an iterable

# 2. Which of the following data types can the filter() function be applied to?
#     A) Lists
#     B) Strings
#     C) Tuples
#     D) All of the above

# 3. What does the filter() function return?
#     A) A new iterable containing filtered elements
#     B) The original iterable with filtered elements
#     C) A list of filtered elements
#     D) A tuple of filtered elements

# 4. Which parameter does the filter() function take?
#     A) A filter function
#     B) An iterable
#     C) Both A and B
#     D) Neither A nor B

# 5. In the context of the filter() function, what does the filter function do?
#     A) Defines the condition for filtering elements
#     B) Specifies the data type of the iterable
#     C) Sorts the iterable elements
#     D) Combines the iterable elements

# 6. Which of the following statements is true about the filter() function?
#     A) The filter function can only return True or False
#     B) The filter function can return any data type
#     C) The filter function must return a boolean
#     D) The filter function is not required

# 7. What is the syntax for using the filter() function in Python?
#     A) filter(condition, iterable)
#     B) filter(iterable, condition)
#     C) filter(function, iterable)
#     D) filter(iterable, function)

# 8. When using the filter() function, what happens if the filter function returns False for an element?
#     A) The element is removed from the iterable
#     B) The element is included in the iterable
#     C) An error is raised
#     D) None of the above

# 9. Can the filter() function be used to filter elements based on multiple conditions?
#     A) Yes
#     B) No

# 10. In Python 3, what does the filter() function return by default?
#     A) A filter object
#     B) A list of filtered elements
#     C) A tuple of filtered elements
#     D) A set of filtered elements

# 11. What is the purpose of the map() function in Python?
#     A) To apply a given function to each item in an iterable
#     B) To filter elements from an iterable based on a given condition
#     C) To sort elements in an iterable
#     D) To combine elements in an iterable

# 12. Which of the following is an iterable that can be passed to the map() function?
#     A) Lists
#     B) Strings
#     C) Tuples
#     D) All of the above

# 13. What does the map() function return?
#     A) A new iterable containing transformed elements
#     B) The original iterable with transformed elements
#     C) A list of transformed elements
#     D) A tuple of transformed elements

# 14. What parameters does the map() function take?
#     A) A mapping function and an iterable
#     B) A single iterable
#     C) A single mapping function
#     D) A mapping function, followed by one or more iterables

# 15. In the context of the map() function, what does the mapping function do?
#     A) Defines the transformation to be applied to each element
#     B) Specifies the data type of the iterable
#     C) Sorts the iterable elements
#     D) Combines the iterable elements

# 16. Which of the following is true about the map() function?
#     A) The mapping function can return any data type
#     B) The mapping function must return a boolean
#     C) The mapping function is not required
#     D) The mapping function must return an integer

# 17. What is the syntax for using the map() function in Python?
#     A) map(mapping_function, iterable)
#     B) map(iterable, mapping_function)
#     C) map(function, iterable)
#     D) map(iterable, function)    

# 18. When using the map() function, what happens if the mapping function returns None for an element?
#     A) The element is removed from the iterable
#     B) The element remains unchanged in the iterable
#     C) An error is raised
#     D) None of the above

# 19. Can the map() function be used to transform elements from multiple iterables?
#     A) Yes
#     B) No

# 20. In Python 3, what does the map() function return by default?
#     A) A map object
#     B) A list of transformed elements
#     C) A tuple of transformed elements
#     D) A set of transformed elements

# 21. What is the purpose of the reversed() function in Python?
#     A) To reverse the order of elements in an iterable
#     B) To sort elements in an iterable
#     C) To remove elements from an iterable
#     D) To concatenate elements in an iterable

# 22. Which of the following is an iterable that can be passed to the reversed() function?
#     A) Lists
#     B) Strings
#     C) Tuples
#     D) All of the above

# 23. What does the reversed() function return?
#     A) A new iterable containing reversed elements
#     B) The original iterable with reversed elements
#     C) A list of reversed elements
#     D) A tuple of reversed elements

# 24. What parameter does the reversed() function take?
#     A) An iterable
#     B) A single element
#     C) A number
#     D) A mapping function

# 25. In the context of the reversed() function, what does "reversed elements" mean?
#     A) The elements are in the opposite order
#     B) The elements are sorted in ascending order
#     C) The elements are concatenated
#     D) The elements are multiplied

# 26. Which of the following is true about the reversed() function?
#     A) The reversed elements are returned as a list
#     B) The reversed elements are returned as a tuple
#     C) The reversed elements are returned as an iterator
#     D) The reversed elements are returned as a set

# 27. What is the syntax for using the reversed() function in Python?
#     A) reversed(iterable)
#     B) iterable.reversed()
#     C) reversed(function, iterable)
#    D) reversed(iterable, function)
# 8. When using the reversed() function, can it be applied to strings?
#    A) Yes
#    B) No
# 9. Can the reversed() function be used to reverse a dictionary?
#    A) Yes
#    B) No
# 0. In Python 3, what does the reversed() function return by default?
#    A) A reversed object
#    B) A list of reversed elements
#    C) A tuple of reversed elements
#    D) A set of reversed elements
# 1. What is the purpose of the sorted() function in Python?
#    A) To sort elements in an iterable and return a sorted list
#    B) To reverse the order of elements in an iterable
#     C) To remove elements from an iterable
#     D) To concatenate elements in an iterable

# 32. Which of the following is an iterable that can be passed to the sorted() function?
#     A) Lists
#     B) Strings
#     C) Tuples
#     D) All of the above
    
# 33. What does the sorted() function return?
#     A) A new iterable containing sorted elements
#     B) The original iterable with sorted elements
#     C) A list of sorted elements
#     D) A tuple of sorted elements

# 34. What parameters does the sorted() function take?
#     A) An iterable
#     B) A single element
#     C) A mapping function
#     D) A mapping function and an iterable

# 35. In the context of the sorted() function, what does "sorted elements" mean?
#     A) The elements are arranged in ascending order
#     B) The elements are arranged in descending order
#     C) The elements are multiplied
#     D) The elements are concatenated

# 36. Which of the following is true about the sorted() function?
#     A) The sorted elements are returned as a tuple
#     B) The sorted elements are returned as a set
#     C) The sorted elements are returned as an iterator
#     D) The sorted elements are returned as a list

# 37. What is the syntax for using the sorted() function in Python?
#     A) sorted(iterable)
#     B) iterable.sorted()
#     C) sorted(function, iterable)
#     D) sorted(iterable, function)

# 38. When using the sorted() function, can you specify a custom sorting order?
#     A) Yes, by providing a custom sorting function
#     B) No, the sorting order is always ascending
#     C) Yes, by providing a reverse parameter
#     D) No, the sorting order is always descending

# 39. Can the sorted() function be used to sort a dictionary based on its keys or values?
#     A) Yes
#     B) No

# 40. In Python 3, what does the sorted() function return by default?
#     A) A list of sorted elements
#     B) A sorted object
#     C) A tuple of sorted elements
#     D) A set of sorted elements
