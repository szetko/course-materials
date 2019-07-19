import requests
import json
import unittest
import math
import timeit

nums = [1, 2, 3, 4]
squares = []
for n in nums:
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16]

squares = map(lambda n: n ** 2, nums)
print(list(squares))  # [1, 4, 9, 16]

squares = [n ** 2 for n in nums]
print(squares)  # [1, 4, 9, 16]

count_by_ten = [10, 20, 30, 40, 50]
output = [x + 5 for x in count_by_ten]
output_two = map(lambda x: x + 5, count_by_ten)

print(output)  # [15, 25, 35, 45, 55]
print(list(output_two))  # [15, 25, 35, 45, 55]

# Performance example


def squares(i):
    squares = []
    for n in range(i):
        squares.append(n ** 2)
    return squares


def squares_lc(i):
    return [n ** 2 for n in range(i)]


print(timeit.timeit('squares(50)',
                    'from __main__ import squares',
                    number=100_000))  # 1.95 seconds
print(timeit.timeit('squares_lc(50)',
                    'from __main__ import squares_lc',
                    number=100_000))  # 1.68 seconds

# Conditional filtering
even_nums = [x for x in range(20) if x % 2 == 0]
powers_of_two = [math.pow(2, x) for x in range(10) if x % 2 == 0]

print(even_nums)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(powers_of_two)  # [1.0, 4.0, 16.0, 64.0, 256.0]


def remove_vowels(input):
    vowels = ['a', 'i', 'e', 'o', 'u']
    consonants = ''
    for i in range(len(input)):
        if (input[i] not in vowels):
            consonants += input[i]
    return consonants


days_of_the_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
no_vowels = [remove_vowels(d) for d in days_of_the_week]

# ['Mndy', 'Tsdy', 'Wdnsdy', 'Thrsdy', 'Frdy', 'Strdy', 'Sndy']
print(no_vowels)

# Nested list comprehension
two_d_arr = [[item for item in range(5)] for row in range(3)]

print(two_d_arr)  # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

# Side effects
set_of_nums = [print(n ** 2) for n in range(10) if n % 2 == 1]

print(set_of_nums)

# Iterator


class Sentence:
    def __init__(self, input):
        self.word_list = input.split()
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.current_index >= len(self.word_list)):
            self.current_index = 0
            raise StopIteration
        current_word = self.word_list[self.current_index]
        self.current_index += 1
        return current_word


if __name__ == '__main__':
    sentence = Sentence('Hello my name is John')
    for s in sentence:
        print(s)
    word_sentence = [w for w in sentence]
    word_count = [len(w) for w in sentence]
    print(word_sentence)  # ['Hello', 'my', 'name', 'is', 'John']
    print(word_count)  # [5, 2, 4, 2, 4]

# Built-in iter
x = iter([1, 2, 3])
print(x)  # <list_iterator object at 0x10739e710>
print(x.__next__())  # 1
print(x.__next__())  # 2
print(x.__next__())  # 3
# print(x.__next__())  # StopIteration

# Infinite iterator


class PowerOfTwo:
    def __init__(self):
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_power = 2 ** self.power
        self.power += 1
        return current_power


if __name__ == '__main__':
    iteration = PowerOfTwo()
    for perfect_power in iteration:
        print(perfect_power)
        if perfect_power > 2000:
            break

# Generator


def generate_birthday_months():
    yield 'Jan'
    yield 'Feb'
    yield 'Mar'
    yield 'May'


birthday = generate_birthday_months()
for m in birthday:
    print(m)

# print(birthday.__next__())  # Jan
# print(birthday.__next__())  # Feb


# Yield in for loop
def birthday_months():
    months = ['Jan', 'Feb', 'Mar', 'Apr']
    for m in months:
        yield m


capitalise_months = [m.upper() for m in birthday_months()]
print(capitalise_months)  # ['JAN', 'FEB', 'MAR', 'APR']

# Generator expression
nums = [1, 2, 3, 4, 5]
squared_nums = (n ** 2 for n in nums)
# print(len(squared_nums))  # TypeError: object of type 'generator' has no len()
# print(squared_nums[0])  # TypeError: 'generator' object is not subscriptable
print(list(squared_nums))  # [1, 4, 9, 16, 25]
print(list(squared_nums))  # []

# Infinite generator


def power_of_two_generator():
    exponent = 0
    while True:
        yield 2 ** exponent
        exponent += 1


for i in power_of_two_generator():
    print(i)

# List comprehension - unit test

BASE_URL = 'https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false'


class TestAssurity(unittest.TestCase):
    def test_description_and_tagline(self):
        req = requests.get(BASE_URL)
        json = req.json()
        charities = json.get('Charities', [])
        self.assertTrue(any((c['Description'] == 'Plunket') and (
            'well child health services' in c['Tagline']) for c in charities))


if __name__ == '__main__':
    unittest.main()
