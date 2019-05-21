from functools import reduce

x = 3


def side_effect():
    global x
    x = 5


side_effect()
print(x)


def repeat_word(word):
    return word * 2


def repeat_word_again(word):
    return word * 2


repeat = repeat_word('Hello')
repeat_again = repeat_word_again(repeat)

print(repeat)  # HelloHello
print(type(repeat_word))  # <class 'function'>
print(repeat_again)  # HelloHelloHelloHello
print(type(repeat_word_again))  # <class 'function'>


def repeat_word_six_times(worker, word):
    for _ in range(6):
        output = worker(word)
        print(output)


repeat_word_six_times(repeat_word, 'Hello')

'''
HelloHello
HelloHello
HelloHello
HelloHello
HelloHello
HelloHello
'''


def odd_characters_only(word):
    return word[1::2]


repeat_word_six_times(odd_characters_only, 'Hello')


def good_and_bad_worker(sucess_worker, error_worker, word):
    if (len(word) > 10):
        res = error_worker(word)
    else:
        res = sucess_worker(word)
    return res


success_output = good_and_bad_worker(repeat_word, odd_characters_only, 'Hello')
print(success_output)  # HelloHello
error_output = good_and_bad_worker(
    repeat_word, odd_characters_only, 'HelloHelloHello')
print(error_output)  # elHloel


def return_a_func(n, word):
    if (n == 0):
        return repeat_again(word)
    else:
        return odd_characters_only(word)


print(return_a_func(str(0), 'Hello'))
print(return_a_func(1, 'HelloHelloHello'))


def cel_to_fah(temp):
    return temp * (9/5) + 32


temps = [0, 37, 20, 180]
fah_temps = map(cel_to_fah, temps)
print(list(fah_temps))

# [32.0, 98.60000000000001, 68.0, 356.0]


def is_long_animal(animal):
    return len(animal) > 5


animals = ['chicken', 'cow', 'goat', 'sheep']
long_animals = filter(is_long_animal, animals)
print(list(long_animals))  # ['chicken']

count_long_animal_letters = map(len, filter(is_long_animal, animals))
print(list(count_long_animal_letters))  # [7]


def multiply(o1, o2):
    return o1 * o2


lambda o1, o2: o1 * o2

nums = [1, 3, 5, 7]
mult_nums = reduce(multiply, nums)
# 1 * 3 = 3
# 3 * 5 = 15
# 15 * 7 = 105
print(mult_nums)


def lambda_output(x): return x * 3


print(lambda_output(3))


def show_three_times(worker):
    for i in range(3):
        print(worker(i))


show_three_times(lambda_output)  # 0, 3, 6

what_will_this_be = filter(lambda x: not x % 2 == 0, range(20))
print(list(what_will_this_be))
result = reduce(lambda o1, o2: o1 + o2,
                filter(lambda x: not x % 2 == 0, range(20)))
print(result)  # 100


def mult_five():
    five = 5

    def mult(arg):
        return arg * five
    return mult


closure = mult_five()
print(closure(1))  # 5
print(closure(2))  # 10
