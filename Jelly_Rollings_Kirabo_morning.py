# tkinter learn
# create a simple calculator program  to calculate (add, subtract, multiply,divide) with GUI interface
# make the title of the calculator program window with your name e.g. Jelly calculator
import tkinter as tk


def add():
    number1 = float(entry_number1.get())
    number2 = float(entry_number2.get())
    result = number1 + number2
    label_result.config(text="Result: " + str(result))


def subtract():
    number1 = float(entry_number1.get())
    number2 = float(entry_number2.get())
    result = number1 - number2
    label_result.config(text="Result: " + str(result))


def multiply():
    number1 = float(entry_number1.get())
    number2 = float(entry_number2.get())
    result = number1 * number2
    label_result.config(text="Result: " + str(result))


def divide():
    number1 = float(entry_number1.get())
    number2 = float(entry_number2.get())
    if number2 != 0:
        result = number1 / number2
        label_result.config(text="Result: " + str(result))
    else:
        label_result.config(text="Error: Division by zero")


# Create the main window
window = tk.Tk()
window.title("Kirabo Jelly Rollings Simple Calculator")

# Create entry fields for numbers
label_number1 = tk.Label(window, text="Enter first Number :")
label_number1.pack()
entry_number1 = tk.Entry(window)
entry_number1.pack()

label_number2 = tk.Label(window, text="Enter second Number :")
label_number2.pack()
entry_number2 = tk.Entry(window)
entry_number2.pack()

# Create buttons for operations
button_add = tk.Button(window, text="Add", command=add)
button_add.pack()

button_subtract = tk.Button(window, text="Subtract", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(window, text="Multiply", command=multiply)
button_multiply.pack()

button_divide = tk.Button(window, text="Divide", command=divide)
button_divide.pack()

# Create label for displaying result
label_result = tk.Label(window, text="Result:")
label_result.pack()

# Start the main loop
window.mainloop()


# Morning class work
"""a = 15
b = 9
# greater than
if a > b:
    print("a is greater than b")
    print(a > b)
# less than
if a < b:
    print("a is less than b")
    print(a < b)
# greater or equal to
if a >= b:
    print("a is greater or equal to b")
    print(a >= b)
# less than or equal
if a <= b:
    print("a is less than or equal to b")
    print(a <= b)
# equal to
if a == b:
    print("a is  equal to b")
    print(a == b)
# not equal
if a != b:
    print("a is not equal to b")
    print(a != b)
# less than or equal to
print(a <= b)

# logical operators
a = True
b = False
# logical AND
if a and b:
    print(a and b)
    # logical OR
    print(a or b)
    # logical NOT
    print(not a)
    print(not b)
# assignment operator
# compound operators
a = 5
# add and assign
a += 5
print(a)
# subtract and assign
b = 18
b -= 9
print(b)
# exponential and assign
f = 2
f **= 3
print(f)
# membership assignment operators
cars = ["bmw", "jeep", "tesla", "toyota"]
if 'jeep' in cars:
    print("it exists in list")
    print('raum' in cars)
# identity operators
x = 10
y = 10
print(x is y)
print(x is not y)
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
# bitwise operators are used to perform bits in form of binary number
# bitwise AND(&)
# bitwise OR(|)
# bitwise XOR(^)
# bitwise NOT(~) flips numbers
# bitwise LEFT SHIFT(<<)
# bitwise RIGHT SHIFT(>>)
a = 10
b = 20

print(a & b)
print(a | b)
print(a ^ b)
print(~ b)
print(~ a)
print(a << b)
print(a >> b)"""
