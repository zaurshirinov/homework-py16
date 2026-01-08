# Homework Assignment: Introduction to Classes in Python

# Instructions:
# Create a Python program with two classes that model real-world objects. 
# Each class should have attributes, methods, and a main program that demonstrates 
# their functionality. Follow the steps below to complete the assignment.

# Class 1: Person

# Create a class named Person with the following attributes and methods:

# Attributes:

# name (str) - The name of the person.
# age (int) - The age of the person.

# Methods:

# greeting(self) - A method that prints a greeting message using the person's name.
# sleep(self) - A method that prints a message indicating that the person is going to sleep.

class Person:
    """
    Represents a person with a name and age.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self):
        """
        Prints a greeting message using the person's name.
        """
        print(f"Salam {self.name}.")
    
    def sleep(self):
        """
        Prints a message indicating that the person is going to sleep.
        """
        print(f"{self.name} is going to sleep.")

# Class 2: Animal

# Create a class named Animal with the following attributes and methods:

# Attributes:

# name (str) - The name of the animal.
# age (int) - The age of the animal.
# color (str) - The color of the animal
# Methods:

# eat(self) - A method that prints a message indicating that the animal is going to eat.
# run(self) - A method that prints a message indicating that the animal is running.

class Animal:
    """
    Represents an animal with a name, age, and color.
    """
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        """
        Prints a message indicating that the animal is going to eat.
        """
        print(f"{self.name} will eat soon.")

    def run(self):
        """
        Prints a message indicating that the animal is running.
        """
        print(f"{self.name} is running.")
         
# Main Program:
if __name__ == "__main__":
    # Create a Person object
    person1 = Person("Zaur", 19)
    person1.greeting()
    person1.sleep()

    print()  # Empty line for clarity

    # Create an Animal object
    animal1 = Animal("Kedo", 2, "Brown tabby with white.")
    animal1.eat()
    animal1.run()

# Write a main program that demonstrates the use of the Person and Animal classes. 
# Create instances of both classes and use their methods to show their behavior. 
# For example, create a person and an animal, set their attributes, and call 
# their appropriate methods for each of them.

# Ensure that your program is well-documented and follows best practices for Python 
# code formatting and style.

# Quiz.
# 1. What is a class in Python?
#     a) A class is a built-in function.
#     b) A class is an instance of an object.
#     c) A class is a blueprint for creating objects.
#     d) A class is a reserved keyword in Python.

# c)

# 2. In Python, which keyword is used to define a class?
#     a) class
#     b) define
#     c) struct
#     d) object

# a)

# 3. How do you create an instance of a class in Python?
#     a) By using the new keyword.
#     b) By calling the class as a function.
#     c) By using the instance keyword.
#     d) By using the class name followed by parentheses.

# b) & d)

# 4. Which of the following statements is true regarding attributes in a class?
#     a) Attributes are methods defined within a class.
#     b) Attributes are used to create instances of a class.
#     c) Attributes are variables that store data in a class.
#     d) Attributes are not allowed in Python classes.

# c)

# 5. Which keyword is used to access the attributes and methods of a class instance?
#     a) access
#     b) use
#     c) this
#     d) dot (.)
    
# d)

# 6. How do you create an instance of a class in Python?
#     a) By using the new keyword.
#     b) By calling the class as a function.
    
# b)

# 7. Which of the following statements is true regarding attributes in a class?
#     a) Attributes are methods defined within a class.
#     b) Attributes are variables that store data in a class.
    
# b)

# 8. What is an "object" in the context of classes?
#     a) An instance of a class.
#     b) A Python module.
#     c) A function

# a)

# 9. What is the relationship between a class and an object in Python?
#     a) A class is an instance of an object.
#     b) An object is an instance of a class.
    
# b)

# 10. What are "attributes" in a class?
#     a) Functions defined within a class.
#     b) Variables that store data within a class.
    
# b)

# 11. In Python, how do you define a class?
#     a) By using the class keyword followed by the class name and a colon.
#     b) By using the def keyword followed by the class name and a colon.

# a)