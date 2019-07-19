# Imperative example
total = 0
num_one = 5
num_two = 10
num_three = 15
total = num_one + num_two + num_three

# Functional example
x = [1, 2, 3, 4, 5]


def square(num):
    return num * num


print(list(map(square, x)))  # [1, 4, 9, 16, 25]

a = 'Hello'
b = 0
c = 0.0
d = True
e = 3+1j

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'complex'>

# Arithmetic operators
x = 11
y = 2

print('x + y =', x + y)  # x + y = 11
print('x - y =', x - y)  # x - y = 9
print('x * y =', x * y)  # x * y = 22
print('x / y =', x / y)  # x / y = 5.5
print('x % y =', x % y)  # x % y = 1
print('x // y =', x // y)  # x // y = 5
print('x ** y =', x ** y)  # x ** y = 121

# Comparison operators
x = 10
y = 12

print('x > y is', x > y)  # x > y is False
print('x < y is', x < y)  # x < y is True
print('x == y is', x == y)  # x == y is False
print('x != y is', x != y)  # x != y is True
print('x >= y is', x >= y)  # x >= y is False
print('x <= y is', x <= y)  # x <= y is True

# Logical operators
x = True
y = False

print('x and y is', x and y)  # x and y is False
print('x or y is', x or y)  # x or y is True
print('not x is', not x)  # not x is False

# Special operators - identity and membership
a = 5
b = 5
c = 'Hello'
d = 'Hello'
e = [1, 2, 3]
f = [1, 2, 3]

print(a is not b)  # False
print(c is d)  # True
print(e is f)  # False

x = 'Hello world'
y = {1: 'a', 2: 'b'}

print('H' in x)  # True
print('hello' not in x)  # True
print(1 in y)  # True
print('a' in y)  # False

# Implicit type conversion
num_int = 123
num_float = 1.23
num = num_int + num_float

print(type(num_int))  # <class 'int'>
print(type(num_float))  # <class 'float'>
print(num)  # 124.23
print(type(num))  # <class 'float'>

# Explicit type conversion
num_int = 123
num_float = 1.23
num = num_int + num_float
num = int(num)

print(type(num_int))  # <class 'int'>
print(type(num_float))  # <class 'float'>
print(num)  # 124
print(type(num))  # <class 'int'>

# Flow of control - if statements
x = int(input("Please enter an integer: "))
if x < 50:
    print('x is less than 50')
elif x > 50:
    print('x is greater than 50')
else:
    print('x is equal to 50')

# Flow of control - for statements
animals = ['cat', 'dog', 'goldfish']
for a in animals:
    print(a, len(a))

# cat 3
# dog 3
# goldfish 8

# Functions


def hello_world():
    print('Hello world')


hello_world()

# String functions
my_str = 'Hello, my name is John Doe'

print(my_str)  # Hello, my name is John Doe
print(my_str.upper())  # HELLO, MY NAME IS JOHN DOE
print(my_str.lower())  # hello, my name is john doe
print(my_str.title())  # Hello, My Name Is John Doe
print(my_str.replace('John', 'Jane'))  # Hello, my name is Jane Doe
