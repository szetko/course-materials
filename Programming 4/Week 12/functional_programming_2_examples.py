from unicodedata import name
import math
import timeit
import requests
import json
import unittest

# Imperative-style
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)  # [1, 4, 9, 16]

# Map and lambda
numbers = [1, 2, 3, 4]
squares = map(lambda n: n**2, numbers)
print(squares)  # <map object at 0x108b3e4a8>
print(list(squares))  # [1, 4, 9, 16]

# List comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16]

# Another lc and map example
count_by_tens = [10, 20, 30, 40, 50]
result = [x+5 for x in count_by_tens]
print(result)  # [15, 25, 35, 45, 55]

result2 = map(lambda x: x+5, count_by_tens)
print(list(result2))  # [15, 25, 35, 45, 55]


def squares(n):  # Performance example
    result = []
    for numbers in range(n):
        result.append(numbers*numbers)
    return result


def squares_comprehension(n):
    return [numbers*numbers for numbers in range(n)]


print(timeit.timeit("squares(50)", "from __main__ import squares", number=1_000_000))
print(timeit.timeit("squares_comprehension(50)",
                    "from __main__ import squares_comprehension", number=1_000_000))

even_nums = [x for x in range(20) if x % 2 == 0]
print(even_nums)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

powers_of_two = [math.pow(2, x) for x in range(10) if x % 2 == 0]
print(powers_of_two)  # [1.0, 4.0, 16.0, 64.0, 256.0]


def remove_the_vowel(input):
    vowels = ['a', 'i', 'e', 'o', 'u']
    consonants = ''
    for i in range(len(input)):
        if (input[i] not in vowels):
            consonants += input[i]
    return consonants


days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
no_vowels = [remove_the_vowel(d) for d in days_of_the_week]
# ['Mndy', 'Tsdy', 'Wdnsdy', 'Thrsdy', 'Frdy', 'Strdy', 'Sndy']
print(no_vowels)

val = [[item for item in range(5)] for row in range(3)]
print(val)  # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]


class Sentence:
    def __init__(self, input):
        self.word_list = input.split()
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.current_index >= len(self.word_list)):  # No more words to return
            self.current_index = 0
            raise StopIteration  # Exits the method
        current_word = self.word_list[self.current_index]
        self.current_index += 1
        return current_word


sentence = Sentence('Hello my name is Grayson')
for s in sentence:
    print(s)

word_sentence = [w for w in sentence]
word_count = [len(w) for w in sentence]
print(word_sentence)  # ['Hello', 'my', 'name', 'is', 'Grayson']
print(word_count)  # [5, 2, 4, 2, 7]


class PowerOfTwo:

    def __init__(self):
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_power = 2 ** self.power
        self.power += 1
        return current_power


infinite_iter = PowerOfTwo()
for perfect_power in infinite_iter:
    print(perfect_power)
    if perfect_power > 2000:
        break

x = iter([1, 2, 3])
print(x)  # <list_iterator object at 0x10c994780>
print(x.__next__())  # 1
print(x.__next__())  # 2
print(x.__next__())  # 3
# print(x.__next__())  # StopIteration


def generate_birthday_months_yield():
    yield 'Jan'
    yield 'Feb'
    yield 'Apr'
    yield 'May'


birthday = generate_birthday_months_yield()
print(birthday.__next__())  # Jan
print(birthday.__next__())  # Feb

for m in generate_birthday_months_yield():
    print(m)


def generate_birthday_months():
    months = ['Jan', 'Feb', 'Mar', 'Apr']
    for m in months:
        yield m


capitalise_months = [m.upper() for m in generate_birthday_months()]
print(capitalise_months)


def power_of_two_generator():
    exponent = 0
    while True:
        yield 2 ** exponent
        exponent += 1


for i in power_of_two_generator():
    print(i)
    if i > 2000:
        break


def decorator_func(func):
    def wrapper():
        func()
    return wrapper


@decorator_func
def hello_world():
    print("Hello world")


hello_world()


chars = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(chars)


BASE_URL = 'https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false'


class TestAPI(unittest.TestCase):
    def test_description_and_tagline(self):
        req = requests.get(BASE_URL)
        json = req.json()
        charities = json.get('Charities', [])
        self.assertTrue(any((c['Description'] == 'Plunket') and (
            'well child health services' in c['Tagline']) for c in charities))


if __name__ == '__main__':
    unittest.main()

nums = [1, 2, 3, 4, 5]
squared_nums = (n ** 2 for n in nums)
print(len(squared_nums))  # TypeError: object of type 'generator' has no len()
print(squared_nums[0])  # TypeError: 'generator' object is not subscriptable
print(list(squared_nums))  # [1, 4, 9, 16, 25]
print(list(squared_nums))  # []

set_of_nums = [print(n**2) for n in range(10) if n % 2 == 1]
print(set_of_nums)
