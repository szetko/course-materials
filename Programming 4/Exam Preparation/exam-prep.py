# Write a list comprehension that uses double(x) to generate numbers between 0-20 and returns the following list of numbers


def double(x):
    return x * 2


double_odd = [double(x) for x in range(20) if not x % 2 == 0]
print(double_odd)

# Write a map and lambda function that adds two list of numbers together and returns a single list of numbers


list_x = [20, 10, 62]
list_y = [23, 76, 34]

print(list(map(lambda x, y: x + y, list_x, list_y)))   # [45, 86, 96]

# Write __next__ code to get the desired output


class CountToFive():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.min += 1
        if (self.min > self.max):
            raise StopIteration
        else:
            return self.min


count_to_five = CountToFive(1, 5)
print(list(count_to_five))  # [1, 2, 3, 4, 5]

# Write count_to_ten(min, max) code to get the desired output


def count_to_ten(min, max):
    while min < max:
        yield min
        min += 1


nums_to_10 = [n for n in count_to_ten(1, 11)]
print(nums_to_10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sample_str = 'Hello 12345 World'
numbers = []
for x in sample_str:
    if x.isdigit():
        numbers.append(x)

print("IsDigit" + str(numbers))

is_digit = [x for x in sample_str if x.isdigit()]
print(is_digit)

nums = [1, 2, 3, 4]
numbers = []
for n in nums:
    numbers.append(n**2)
print(numbers)

x = [n**2 for n in nums]
print(x)

longWords = map(lambda x: x, filter(lambda x: x.isdigit(), sample_str))
# longWords = map(lambda x: x.isdigit(),  sample_str)
print(list(longWords))
