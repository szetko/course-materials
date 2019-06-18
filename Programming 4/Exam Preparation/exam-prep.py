# Write a list comprehension that uses double(x)  to generate numbers between 0-20 and returns a list of odd numbers


def double(x):
    return x * 2

# Write a map and lambda function that adds two list of numbers together and returns a single list of numbers


list_x = [20, 10, 62]
list_y = [23, 76, 34]

print(list())  # [45, 86, 96]

# Write __next__ code to get the desired output


class CountToFive():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        pass


count_to_five = CountToFive(1, 5)
print(list(count_to_five))  # [1, 2, 3, 4, 5]
