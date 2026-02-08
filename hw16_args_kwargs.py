
# ===============================
# =   *args & **kwargs TASKS    =
# ===============================
# # EASY

# 1. Write a function that accepts any number of positional arguments and prints them.
def get_args(*args):
    print(args)

get_args(12, 213, "trump")

# 2. Write a function that sums all the numbers passed via *args.
def get_sum_args(*args: int) -> int:
    return sum(args)

print(get_sum_args(12, 232))

# 3. Create a function that multiplies all numbers using *args.
def multiply_args(*args: int) -> int:
    result = 1
    for x in args:
        result *= x
    return result

print(multiply_args(12, 4, 34, 0.1, 3))

# 4. Write a function that accepts any number of keyword arguments and prints them in key=value format.
def get_kwargs(**kwargs) -> dict:
    return kwargs

print(get_kwargs(color="blue", name=232))

# 5. Write a function that prints only the values from **kwargs.
def get_kwargs_value(**kwargs):
    print(kwargs.values())

get_kwargs_value(name=22, color=42)

# 6. Create a function that prints a greeting message using **kwargs with keys: name and age.
def greet(**kwargs):
    print(f"hello {kwargs['name']}, age - {kwargs['age']}")

greet(name="Zaur", age=20)

# 7. Write a function that combines *args and **kwargs and prints both.
def print_args_kwargs(*args, **kwargs):
    print(args, kwargs)

print_args_kwargs(33, 39238, name="zaur")

# 8. Write a function that checks if a specific key exists in **kwargs.
def check_kwargs(key, **kwargs) -> bool:
    return kwargs.get(key) is not None

print(check_kwargs("zaur", zar=3, zaur=34))

# 9. Create a function that returns the longest word passed in *args.
def get_longest_word(*args: str) -> str:
    if not args:
        return None
    return max(args, key=len)

print(get_longest_word("two", "three", "four"))

# 10. Create a function that prints a formatted address using **kwargs (e.g., street, city, zip).
def get_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

get_address(street="Nizami st", city="Baku", zip="AZ1000")

# # MEDIUM

# 11. Write a function that filters only even numbers from *args.
def filter_even_number(*args: int) -> list[int]:
    return list(filter(lambda num: num % 2 == 0, args))

print(filter_even_number(2, 3, 23, 24))

# 12. Create a function that returns a dictionary combining both *args (as values) and **kwargs.
# anlamadim 

# 13. Create a function that takes a default tax rate via **kwargs and applies it to all *args prices.
def tax_apply(*prices, **kwargs):
    tax_rate = kwargs.get("tax_rate", 0.9)
    taxed_prices = [price * (1 + tax_rate) for price in prices]
    return taxed_prices

print(tax_apply(100, 200, 345)) 

# 14. Write a function that accepts student scores via **kwargs and returns the average.
def get_average_student(**scores):
    return sum(scores.values()) / len(scores)

print(get_average_student(ali=50, omar=90, zaur=73, said=87))

# 15. Create a logger function that accepts *args as log messages and **kwargs for metadata (e.g., level, timestamp).
# anlamadim

# 16. Build a function that uses *args to take any strings and **kwargs for formatting options like upper=True, reverse=True.
def format_strings(*args: str, **kwargs: bool) -> list[str]:
    result = []

    for x in args:
        text = x

        if kwargs.get("upper"):
            text = text.upper()
            
        if kwargs.get("reverse"):
            text = text[::-1]

        result.append(text)

    return result

print(format_strings("malas", "ruaz", reverse=True, upper=True))

# 17. Create a function that finds the max of numbers from both *args and values in **kwargs.
def get_max(*args: float, **kwargs: float) -> float:
    num = []
    num.extend(args)
    num.extend(kwargs.values())

    if not num:
        raise ValueError("No number!")
    
    return max(num)

print(get_max(232, 243, 23, num1=323))

# 18. Write a function that accepts any number of named configurations (**kwargs) and validates that required keys exist.
def validate_config(**kwargs) -> bool:
    required_keys = ['jet', 'academy']
    return all(key in kwargs for key in required_keys)

print(validate_config(zaur=10, jet="pyhton", academy=23))

# 19. Write a decorator that uses *args and **kwargs to wrap and log function calls.

# 20. Implement a function that creates a formatted table where columns are defined via **kwargs and values via *args.

# # HARD

# 21. Create a class with a method that accepts *args for dynamic field names and **kwargs for their values.

# 22. Write a function that groups items passed via **kwargs based on data type.

# 23. Design a function that builds a nested dictionary structure from **kwargs with dot notation (e.g., 'user.name': 'Ali').

# 24. Write a function that recursively sums all numbers passed via nested **kwargs.

# 25. Create a dynamic API router simulator function where *args represent endpoints and **kwargs represent methods and handlers.
