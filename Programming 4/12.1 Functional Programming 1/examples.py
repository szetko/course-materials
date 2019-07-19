from functools import reduce


def repeat_word(word):
    return word * 2


def repeat_word_again(word):
    return word * 2


repeat = repeat_word('Hello')
repeat_again = repeat_word_again(repeat)

print(type(repeat_word))  # <class 'function'>
print(type(repeat_word_again))  # <class 'function'>
print(repeat)  # HelloHello
print(repeat_again)  # HelloHelloHelloHello


def repeat_word_six_times(worker, word):
    for _ in range(6):
        output = worker(word)
        print(output)


repeat_word_six_times(repeat_word, 'Hello')

# HelloHello
# HelloHello
# HelloHello
# HelloHello
# HelloHello
# HelloHello


def odd_characters_only(word):
    return word[1::2]


repeat_word_six_times(odd_characters_only, 'Hello')


def odd_characters_only(word):
    return word[1::2]


def good_and_bad(success_worker, error_worker, word):
    if (len(word) < 10):
        worker = success_worker(word)
    else:
        worker = error_worker(word)
    return worker


success = good_and_bad(repeat_word, odd_characters_only, 'Hello')
error = good_and_bad(repeat_word, odd_characters_only, 'HelloHello')

print(success)  # HelloHello
print(error)  # elHlo


def return_a_func(n, word):
    if (n == 0):
        return repeat_word(word)
    else:
        return odd_characters_only(word)


func_one = return_a_func(0, 'Hello')
func_two = return_a_func(1, 'HelloHelloHello')

print(func_one)  # HelloHello
print(func_two)  # elHloel


def cel_to_fah(temp):  # Map example
    return temp * (9 / 5) + 32


temps = [0, 37, 20, 180]
fah_con = map(cel_to_fah, temps)

print(list(fah_con))  # [32.0, 98.60000000000001, 68.0, 356.0]


def is_long_animal(animal):  # Filter example
    return len(animal) > 5


animals = ['chicken', 'cow', 'goat', 'sheep']
long_animals = filter(is_long_animal, animals)

print(list(long_animals))

# Map and filter example
count_long_animals_letters = map(len, filter(is_long_animal, animals))

print(list(count_long_animals_letters))  # [7]


def multiply(num_one, num_two):  # Reduce example
    return num_one * num_two


nums = [1, 3, 5, 7]
mult_nums = reduce(multiply, nums)

# 1 * 3 = 3
# 3 * 5 = 15
# 15 * 7 = 105
print(mult_nums)  # 105


def mult_five():  # Partials/closure example
    five = 5

    def mult(arg):
        return arg * five

    return mult


closure = mult_five()

print(closure(1))  # 5
print(closure(2))  # 10

# Lambda
lambda num_one, num_two: num_one * num_two

times_three = lambda x: x * 3

print(times_three(3)) # 9

def show_three_times(worker):
    for i in range(3):
        print(worker(i))

show_three_times(times_three)
# 0
# 3
# 6

# Lambda and filter example
guess = filter(lambda x: not x % 2 == 0, range(20))

what_is_the_output = filter(lambda x: not x % 2 == 0, range(20))

# Lambda and reduce example
what_is_the_output_two = reduce(
    lambda x, y: x + y, filter(lambda z: not z % 2 == 0, range(20)))

print(list(what_is_the_output))
print(what_is_the_output_two)  # 100
