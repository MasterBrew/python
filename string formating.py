#!/bin/python3

'''

       # Reference : https://realpython.com/python-f-strings/
         - Format strings different ways ..
         - Be conventional and consistent!
'''

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"



'''

# Make a function that returns input in lowercase
def call_myfunction(input):
    print("### Called myfunction() ##")
    # Use Methode .lower() on input variable
    return input.lower()

name = "Eric Idle"
print(name)
print(f"#This is Formatted around This body ( {call_myfunction(name)} ) # ")

name = "Bob"
age = "68"

# print("Hello " + name + " How are you today?")
print("Hello ", name, " Guess its okay at age", age, "?")

name, age = "Batman", 55
# How to Use %-formatting
print("Hello %s your %s\n" % (name, age))

name, age = "BadGirl", 18
# How To Use str.format()
print("Hello, {}. You are {}.\n".format(name, age))

name, age = "Robin of the Forest", 37
# f-Strings: A New and Improved Way to Format Strings in Python
print(f"1.Hello, {name}. You are {age}.")

name, age = "Mr x", "Unknown"
print(F"2.Hello, {name}. You are {age}.")

'''