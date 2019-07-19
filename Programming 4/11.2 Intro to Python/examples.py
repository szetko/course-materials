# Basic indexing
sequence = "abcde"

print(sequence[0])  # a
print(sequence[1])  # b
print(sequence[2])  # c
print(sequence[3])  # d
print(sequence[4])  # e
print(sequence[-1])  # e
print(sequence[-2])  # d
print(sequence[-3])  # c
print(sequence[-4])  # b
print(sequence[-5])  # a

# Index slicing
sequence = "abcde"

print(sequence[0:2])
print(sequence[2:5])

# Negative index slicing
longer_sequence = "abcdefghijk"

print(longer_sequence[-4:-1])
print(longer_sequence[-6:-4])
print(longer_sequence[1:-4])
print(longer_sequence[-1:-1])

# Ommiting an index
sequence_of_digits = "123456789"

print(sequence_of_digits[:-4])  # 12345
print(sequence_of_digits[-4:])  # 6789

# Step
print(sequence_of_digits[:-4:2])
print(sequence_of_digits[::-1])  # 987654321

# Lists
types = ['John', 1, False]
types[0] = 'Jane'

print(types)  # ['Jane', 1, False]

# Tuples
months = (
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
)

for m in months:
    print(m)

# Dictionaries
transportation = {
    1: 'bike',
    2: 'car',
    3: 'bus'
}

print(transportation.get(1))  # bike
print(2 in transportation)  # True
print(4 in transportation)  # False
transportation[4] = 'horse'
print(4 in transportation)  # True

# Classes


class Cat:
    species = 'Burmese'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        print('Meow')

    def describe(self):
        print('Name:', self.name, '\nBreed:', self.breed)


if __name__ == '__main__':
    cat1 = Cat('John', 'Persian')
    cat1.sound()
    cat1.describe()

# Meow
# Name: John
# Breed: Persian
