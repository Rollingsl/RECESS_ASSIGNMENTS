# EXCEPTION HANDLING
"""
 Exception handling in Python allows you to handle and manage errors that may occur during the
  execution of your program.
Different types of exceptions in python:
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence
 types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or
input,
such as trying to convert a string to an integer when the string does not represent a valid integer.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong
 type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
AttributeError: This exception is raised when an attribute or method is not found on an object,
such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due
 to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code.

"""
# Try and Except Statement

x = ["Jelly", "Rollings", "Kirabo", "Joanath"]
try:
    print("1st element = %d" % (x[0]))
    # Throws error since there are only 3 elements in array
    print("8th element = %d" % (x[7]))

except:
    print("8th element doesnt exist")


# example 2
# Program to handle multiple errors with one except statement
def fun(x):
    if x < 5:
        # throws ZeroDivisionError for a = 3
        y = x / (x - 3)

    # throws NameError if x >= 5
    print("y = ", y)


try:
    fun(5)
    fun(8)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("error occured and solved")


# Try with Else Clause
# Program to depict else clause with try-except
def divide(x, y):
    try:
        z = (x / y)
    except ZeroDivisionError:
        print("syntax error")
    else:
        print(z)


divide(9, 0)
divide(20, 10)

# Finally Keyword
try:
    j = 8 // 0
    print(j)

# handles zero division exception
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    # this block is always executed regardless of exception generation.
    print('This is always executed')


# user defined exceptions
"""you can define your own custom exceptions by creating
 a new class that inherits from the built-in Exception class or any of its subclasses.
 Here's an example of how you can define and use a custom exception:"""

class UserDefined(Exception):
    pass


def divide(x, y):
    if y == 0:
        raise UserDefined("Error: Division by zero!")
    return x / y


try:
    answer = divide(2, 0)
    print("The answer is:", answer)

except UserDefined as e:
    print(str(e))

finally:
    print("This will always be excuted.")


# Example
class InvalidInputError(Exception):
    def __init__(self, invalid_value):
        self.invalid_value = invalid_value

    def __str__(self):
        return f"invalid_value: {self.invalid_value}"


def is_valid():
    pass


def process_input(invalid_value):
    if not is_valid():
        raise InvalidInputError(invalid_value)


try:
    invalid_value = "Thief"
    process_input(invalid_value)

except InvalidInputError as e:
    print(str(e))

# FILE HANDLING
"""
>File handling in Python refers to the process of working with files, including reading from and writing to them.
 It enables programmers to manipulate files stored on a computer's file system, allowing them to store and retrieve data as needed.
  Python provides built-in functions and modules that make file handling straightforward and efficient.
Opening a file: To work with a file, you need to open it first. The open() function is used to open a file and returns a file object. 
File modes:
>'r': Read mode (default). The file is opened for reading.
>'w': Write mode. The file is opened for writing, and if it doesn't exist, a new file is created. If it exists, its contents are truncated.
>'a': Append mode. The file is opened for writing, and if it doesn't exist, a new file is created. If it exists, new data is appended to the end.
>'x': Exclusive creation mode. The file is opened for writing, but only if it doesn't already exist.
>'b': Binary mode. Used in combination with other modes, it opens the file in binary mode.
>'t': Text mode (default). Used in combination with other modes, it opens the file in text mode.
>Reading from a file: Once a file is open in read mode, you can read its contents using methods like read(), readline(), or readlines(). read() reads the entire file, readline() reads a single line, and readlines() reads all lines and returns them as a list.
>Writing to a file: When a file is open in write mode, you can write data to it using the write() method. You can write strings or use a loop to iterate over a collection of data and write each item to the file.
>Appending to a file: If a file is open in append mode, you can use the write() method to append data to the end of the file.
>Closing a file: After you finish working with a file, it's essential to close it using the close() method. Closing a file ensures that all data is written, and system resources are freed.
>Context managers: Python provides a convenient way to work with files using context managers. You can use the with statement to open a file, and it automatically takes care of closing the file when you're done, even if an exception occurs.
>File handling operations: Python's os module provides functions for file-related operations such as renaming files, deleting files, checking file existence, getting file information, and more
"""

# write to a file
# Open the file in write mode
file = open('Jelly.txt', 'w')
# Write  to the file
file.write('God is good,\n')
file.write('He loves us all.')
# Close the file
file.close()


# read  from a file
# Open the file in read mode
file = open('Jelly.txt', 'r')
# Read from the file
note = file.read()
print(note)
# Close the file
file.close()


# appending to a file
# Open the file in append mode
file = open('Jelly.txt', 'a')
# Append content to the file
file.write('\nSalvation came through Mary.')
# Close the file
file.close()

# using context managers
# The file is automatically closed outside the 'with' block
# Open the file using a context manager
with open('Jelly.txt', 'r') as file:
    # Read the file content
    value = file.read()
    print(value)


# Handling exceptions in files
try:
    # Open the file in read mode
    with open('Rollings.txt', 'r') as file:
        # Read
        input = file.read()
        print(input)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("denied access.")
except Exception as e:
    print(f"An error occurred: {e}")

# using the os module
import os

# Rename a file
# os.rename('copy.txt', 'new_copy.txt')
# Delete a file
# os.remove('delete.txt')
# Check if a file exists
if os.path.exists('check.txt'):
    print("File exists!")
else:
    print("File does not exist.")
# Get file information
file_info = os.stat('Jelly.txt')
print(f"File size is: {file_info.st_size} bytes")
print(f"Last modified: {file_info.st_mtime}")

# using the with statement
# Specify the file path
file_path = 'Jelly.txt'
try:
    # Open the file in write mode using a context manager
    with open(file_path, 'w') as file:
        # Write  to the file
        file.write('God sent his only son\n')
        file.write('To forgive us')
    print(f"notes written to '{file_path}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
