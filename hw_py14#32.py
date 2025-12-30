import os
import math
import datetime

# PYTHON FUNCTIONS BASIC HOMEWORK - 80 PRACTICAL TASKS
# =======================================================

# DESCRIPTION:
# This homework focuses on fundamental Python function concepts including:
# - Basic function creation with parameters and return values
# - String manipulation and list operations
# - Conditional logic and mathematical operations
# - Default parameters and multiple return values
# - Docstrings and documentation
# - Date/time operations
# - Financial calculations
# - File path operations

# The tasks progress from simple function creation to more complex operations,
# helping master the core concepts of Python functions.

# TASKS:
# ======

# BASIC FUNCTION OPERATIONS (1-20)
# ================================

# 1. Write a function that takes a name as a parameter and prints "Hello, <name>".
def greet(name):
    print(f"Hello {name}")

greet("Eldar")

# 2. Write a function that takes two numbers and prints their sum.
def calculate_two_num(num_1: int, num_2: int):
    print(num_1 + num_2)

calculate_two_num(25, 44)

# 3. Write a function that takes two numbers and returns their sum.
def return_two_num(num_1: int, num_2: int) -> int:
    return num_1 + num_2

print(return_two_num(15, 16))

# 4. Write a function that returns the string "Python is fun!".
def show_python_message() -> str:
    return "Python is fun!"

print(show_python_message())

# 5. Write a function that takes a string and returns it in uppercase.
def convert_uppercase(text: str) -> str:
    return text.upper()

print(convert_uppercase("salam"))

# 6. Write a function that takes a string and returns it in lowercase.
def convert_lowercase(text: str) -> str:
    return text.lower()

print(convert_lowercase("salam"))

# 7. Write a function that takes two strings and concatenates them.
def concatenate(text_1: str, text_2: str) -> str:
    return text_1 + text_2

print(concatenate("Salam", "Eldar"))

# 8. Write a function that takes a number and returns its square.
def calculate_square(num: int) -> float:
    return math.pow(num, 2)

print(calculate_square(7))

# 9. Write a function that takes a list and prints each item.
def print_items(lst: list): 
    for item in lst:
        print(item)

print_items(["Salam", "Eldar", 1, 2, 3])

# 10. Write a function that takes a list of numbers and returns their sum.
def sum_list(num_list: list) -> int:
    return sum(num_list)

print(sum_list([15, 16]))

# 11. Write a function that takes a list and returns its length.
def return_len_list(lst: list) -> int:
    return len(lst)

print(return_len_list(["Salam", "Eldar"]))

# 12. Write a function that takes a list and returns the first element.
def return_first_element(lst: list) -> str:
    return lst[0]

print(return_first_element(["Salam", "Eldar"]))

# 13. Write a function that takes a list and returns the last element.
def return_last_element(lst: list) -> str:
    return lst[-1]

print(return_last_element(["Salam", "Eldar"]))

# 14. Write a function that returns True if a list is empty, False otherwise.
def check_empty_list(lst: list) -> bool:
    if lst == []:
        return True
    else:
        return False
    
print(check_empty_list(["Salam"]))

# 15. Write a function that takes a list and a value, and returns True if the value exists in the list.

# 16. Write a function that takes a list and returns it reversed (without using reverse()).
def reversed_list(lst: list) -> list:
    return lst[: : -1]

print(reversed_list(["Eldar", "Salam"]))

# 17. Write a function that returns the maximum of three numbers.
def check_maximum(num_1: int, num_2: int, num_3: int) -> int:
    return max(num_1, num_2, num_3)

print(check_maximum(5, 13, 22))

# 18. Write a function that takes a list of strings and returns them joined with spaces.
def list_string(lst: list[str]) -> str:
    return " ".join(lst)

print(list_string("salam"))

# 19. Write a function that takes a number and checks if it is even.
def check_even_number(number: int) -> bool:
    return number % 2 == 0 

print(check_even_number(6))

# 20. Write a function that takes a number and checks if it is odd.
def check_odd_number(number: int) -> bool:
    return number % 2 != 0

print(check_odd_number(6))


# CONDITIONAL LOGIC & MATHEMATICS (21-40)
# ========================================

# 21. Write a function that takes an age and returns "Adult" if age >= 18 else "Minor".
def check_age(age: int) -> str:
    return "Adult" if age >= 18 else "Minor"

print(check_age(19))

# 22. Write a function that takes a temperature in Celsius and returns Fahrenheit.
def calculate_fahrenheit(C: int) -> float:
    return C * 9 / 5 + 32

print(calculate_fahrenheit(42))

# 23. Write a function that takes a temperature in Fahrenheit and returns Celsius.
def calculate_celsius(F: int) -> float:
    return (F - 32) * 5 / 9

print(calculate_celsius(107))

# 24. Write a function that takes a number and returns "Positive", "Negative", or "Zero".
def check_number(number: int) -> str:
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-(-1)))

# 25. Write a function that takes two numbers and returns the larger one.
def check_large_number(num_1: int, num_2: int) -> int:
    return num_1 if num_1 > num_2 else num_2

print(check_large_number(59, 69))

# 26. Write a function that takes two numbers and returns the smaller one.
def check_small_number(num_1: int, num_2: int) -> int:
    return num_1 if num_1 < num_2 else num_2

print(check_small_number(31, 41))

# 27. Write a function that returns the absolute value of a number.
def return_absolute_value(number: int) -> int:
    return abs(number)

print(return_absolute_value(-31))

# 28. Write a function that returns the last character of a string.
def return_last_char(string: str) -> str:
    return string[-1]

print(return_last_char("Python"))

# 29. Write a function that takes a string and returns its length.
def get_string_length(text: str) -> int:
    return len(text)

print(get_string_length("hello"))

# 30. Write a function that takes a string and returns True if it contains the word "Python".
def check_contain_python(text: str) -> bool:
    return "Python" in text

print(check_contain_python("I love Python programming"))

# 31. Write a function that counts vowels in a string.
def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in "aeiou")

print(count_vowels("Python Programming"))

# 32. Write a function that takes a sentence and returns it split into words.
def split_word(sentence: str) -> list:
    return sentence.split()

print(split_word("I love Pyhton!"))

# 33. Write a function that capitalizes the first letter of a string.
def capitalize_letter(text: str) -> str:
    return text[0].upper() + text[1:]

print(capitalize_letter("hello Python"))

# 34. Write a function that returns the title-cased version of a string.
def title_case(text: str) -> str:
    return text.title()

print(title_case("hello python I LOVE YOU"))

# 35. Write a function that removes spaces from a string.
def remove_spaces(text: str) -> str:
    return text.replace(" ", "")

print(remove_spaces("S A L A M"))

# 36. Write a function that replaces all commas with semicolons in a string.
def remove_semicolon(text: str) -> str:
    return text.replace(",", ";")

print(remove_semicolon(", , , , , , "))
# 37. Write a function that counts how many times "a" appears in a string.
def count_a(text: str) -> int:
    return text.count("a")

print(count_a("1a 2a 3a 4a "))

# 38. Write a function that checks if a string is empty.
def is_empty(text: str) -> bool:
    return text == ""

print(is_empty(()))

# 39. Write a function with a default parameter "guest" for name, and print "Welcome <name>".
def greet(name: str = "guest"):
    print(f"Welcome {name}")

greet("Zaur")

# 40. Write a function with three default parameters (city, country, age).
def show_info(city: str = "Baku", country: str = "Azerbaijan", age: int = 0):
    print(f"City: {city}, Country: {country}, Age: {age}")

show_info()

# DEFAULT PARAMETERS & MENU (41-44)
# ==================================

# 41. Write a function that prints today's menu with default "Pizza".
def print_menu(menu="Pizza"):
    print(f"Today's menu: {menu}")

print_menu()

# MULTIPLE RETURN VALUES (45-60)
# ===============================

# 42. Write a function that returns both min and max of a list.
def get_min_max(lst: list) -> tuple:
    return min(lst), max(lst)

print(get_min_max([1, 2, 3, 4]))

# 43. Write a function that returns both uppercase and lowercase version of a string.
def get_upper_lower(text: str) -> tuple:
    return text.upper(), text.lower()

print(get_upper_lower("Salam"))

# 44. Write a function that returns both length and reversed version of a string.
def get_length_reverse(text: str) -> tuple:
    return len(text), text[::-1]

print(get_length_reverse("New Year."))

# 45. Write a function that returns both square and cube of a number.
def get_square_cube(n: int) -> tuple:
    return n**2, n**3

print(get_square_cube(3))

# 46. Write a function that returns name and age together in a tuple.
def get_name_age(name: str, age: int) -> tuple:
    return name, age

print(get_name_age("Zaur", 20))

# 47. Write a function that returns first and last item of a list.
def get_first_last(items: list) -> tuple:
    return items[0], items[-1]

print(get_first_last([1, 3, 12, -1]))

# 48. Write a function that returns True/False and explanation string.
def check_positive(number: int) -> tuple:
    if number > 0:
        return True, "Number is positive"
    return False, "Number is not positive"

print(check_positive(-3))

# 49. Write a function that takes 2 numbers and returns sum and difference.
def return_sum_difference(a: int, b: int) -> tuple:
    return a + b, a - b

print(return_sum_difference(4, 7))

# 50. Write a function that returns (username, email) dictionary.
def user_info(username: str, email: str) -> dict:
    return {
        "username": username,
        "email": email
    }

print(user_info("zaur", "shiriov@dsf"))

# 51. Write a function that returns multiple values packed in a dict.
def get_student_data(name: str, age: int, grade: float) -> dict:
    return {
        "name": name,
        "age": age,
        "grade": grade
    }

print(get_student_data("Zaur", 20, 2))


# DOCSTRINGS (52-53)
# ==================

# 52. Write a function with a docstring that explains what it does.
def return_sum_difference(a: int, b: int) -> tuple:
    """Takes two numbers and returns their sum and difference."""
    return a + b, a - b

print(return_sum_difference(4, 7))

# 53. Write a function with parameters and include a docstring for them.
def user_info(username: str, email: str) -> dict:
    """Stores user information in a dictionary."""
    return {
        "username": username,
        "email": email
    }

print(user_info("zaur", "shiriov@dsf"))


# DATE & TIME OPERATIONS (54-63)
# ==============================

# 54. Write a function that prints the current year.
def get_current_year():
    current_year = datetime.datetime.now().year
    print(current_year)

get_current_year()

# 55. Write a function that prints the current day of week.
def get_week_day():
    current_week_day = datetime.datetime.now().strftime("%A")
    print(current_week_day)

get_week_day()

# 56. Write a function that prints the current time.
def get_current_time():
    current_time = datetime.datetime.now()
    print(current_time)

get_current_time()

# 57. Write a function that returns current date as string.
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

print(get_current_date())

# 58. Write a function that returns current month as string.
def get_current_month():
    return datetime.datetime.now().strftime("%B")  

print(get_current_month())

# 59. Write a function that prints today's date in "YYYY-MM-DD".
def get_todays_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

print(get_current_date())

# 60. Write a function that takes a datetime and returns only the year.
def get_only_year():
    return datetime.datetime.now().date()

print(get_only_year())

# 61. Write a function that takes a datetime and returns only the month.
def get_only_month():
    return datetime.datetime.now().month

print(get_only_month())

# 62. Write a function that takes a datetime and returns only the day.
def get_only_day():
    return datetime.datetime.now().day

print(get_only_day())

# 63. Write a function that returns today's date and time as dictionary.
def get_current_datetime_dict():
    now = datetime.datetime.now()
    return {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second
    }

print(get_current_datetime_dict())

# FINANCIAL CALCULATIONS (64-73)
# ===============================

# 64. Write a function that takes a price and returns price with VAT (add 18%).
def calculate_price_with_vat(price: int) -> float:
    VAT_RATE = 0.18
    return round(price * (1 + VAT_RATE), 2)

print(calculate_price_with_vat(9932))

# 65. Write a function that takes a salary and returns yearly salary.
def calculate_yerly_salary(monnthly_salary: int) -> int:
    return monnthly_salary * 12

print(calculate_yerly_salary(450))

# 66. Write a function that takes a bill amount and tip percent, returns total.

# 67. Write a function that takes a discount percent and price, returns final price.
def calculate_discounted_price(price: int, discount_percent: int) -> float:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return round(final_price, 2)   

print(calculate_discounted_price(59, 17))

# 68. Write a function that takes a list of prices and returns total.
def calculate_total_prices(prices_list: list[float]) -> float:
    return sum(prices_list)

print(calculate_total_prices([24.9, 44.5, 32, 98, 93]))

# 69. Write a function that applies a fixed discount (default 10%) to a price.
def calculate_discounted_price(price: int, discount_percent=10) -> float:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return round(final_price, 2)  

print(calculate_discounted_price(100))

# 70. Write a function that takes a balance and expense, and returns remaining balance.
def calculate_remaning_balance(balance: float, expense: float) -> float:
    return balance - expense

print(calculate_remaning_balance(543.8, 233.4))

# 71. Write a function that formats a number as currency string.
def get_format_currency(amount: float) -> float:
    return f"${amount:,.1f}"

print(get_format_currency(2964))

# 72. Write a function that takes hours worked and rate, returns salary.

# 73. Write a function that takes prices and tax percent, returns total.
def calculate_total_with_tax(prices_list: list[int], tax_percent: int) -> float:
    subtotal = sum(prices_list)
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount

    return round(total, 2)

print(calculate_total_with_tax([120, 35, 55], 20))

# FILE OPERATIONS (74-80)
# ========================

# 74. Write a function that takes a filename and prints it.
def print_filename(filename: str):
    print(filename)

print_filename("example.txt")

# 75. Write a function that takes a filename and returns its extension.
def get_filename_extension(filename: str) -> str:
    return filename.split(".")[-1]


print(get_filename_extension("main.py"))

# 76. Write a function that takes a path and returns only the filename.
def get_filename_path(path: str) -> str:
    return os.path.basename(path) 
    # return path.split("/")[-1] 

print(get_filename_path("/home/user/documents/example.txt"))

# 77. Write a function that takes a filename and returns True if ends with ".txt".
def check_file_extension(filename: str) -> bool:
    if filename.split(".")[-1] == "txt":
        return True
    return False

print(check_file_extension("main.txt"))

# 78. Write a function that takes a filename and adds ".bak" extension.
def add_bak_extension(filename: str) -> str:
    return filename + ".bak"

print(add_bak_extension("main.py"))

# 79. Write a function that takes a file content string and counts lines.

# def count_lines_in_file(filename: str) -> int:
#     with open(filename, "r") as file: 
#         return len(file.readlines())


# print(count_lines_in_file("index.py")) 

# 80. Write a function that takes filename and returns it uppercased.
def get_uppercase_filename(filename: str) -> str:
    return filename.upper()


print(get_uppercase_filename("example.txt")) 
# REQUIREMENTS:
# =============

# - All functions must be properly defined with def keyword
# - Use descriptive function names following Python naming conventions
# - Include appropriate parameters and return statements
# - Test all functions with different inputs
# - For docstring tasks, use triple quotes and explain purpose, parameters, and return values
# - Handle edge cases appropriately
# - Use meaningful variable names

# BONUS CHALLENGES:
# =================

# - Add type hints to function parameters and return values
# - Include error handling for invalid inputs
# - Create unit tests for each function
# - Optimize functions for performance
# - Add logging for debugging purposes 
