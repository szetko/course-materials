'''
Indexing example
'''

sequence_of_chars = "abcde"

print(sequence_of_chars[0])  # a
print(sequence_of_chars[1])  # b
print(sequence_of_chars[2])  # c
print(sequence_of_chars[3])  # d
print(sequence_of_chars[4])  # e

print(sequence_of_chars[-1])  # e
print(sequence_of_chars[-2])  # d
print(sequence_of_chars[-3])  # c
print(sequence_of_chars[-4])  # b
print(sequence_of_chars[-5])  # a

'''
Slicing examples
'''

print(sequence_of_chars[0:2])  # ab
print(sequence_of_chars[2:5])  # cde

longer_sequence_of_chars = "abcdefghij"

print(longer_sequence_of_chars[-4:-1])  # ghi
print(longer_sequence_of_chars[-6:-4])  # ef
print(longer_sequence_of_chars[1:-4])  # bcdef

sequence_of_digits = "0123456789"

print(sequence_of_digits[-1:-4])

print(sequence_of_digits[:-4])  # 012345
print(sequence_of_digits[-4:])  # 6789

print(sequence_of_digits[:-4:2])
print(sequence_of_digits[::-1])  # 9876543210

array_of_types = ['Grayson', 1, False]
array_of_types[0] = 'Graeme'
print(array_of_types)

print(array_of_types)
print(type(array_of_types[0]), type(
    array_of_types[1]), type(array_of_types[2]))

list_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
list_of_months[0:3] = ['J', 'F', 'M']
first_six_months = list_of_months[:-1]
print(first_six_months)

'''
Tuple example
'''
list_of_months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul')
for i in list_of_months:
    print(i)

'''
Dictionary example
'''
transport = {1: "bike", 2: "bike", 3: "bus"}
print(transport.get(1))  # bike
print(2 in transport)  # True
print(4 in transport)  # False
transport[4] = "horse"
print(4 in transport)  # True

'''
Class example
'''


class Cat:

    species = "Burmese"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        print("meow")

    def describe(self):
        print("My name is", self.name, "and I am a", self.breed, "cat")


if __name__ == "__main__":
    cat1 = Cat('Grayson', 'Persian')
    cat1.sound()
    cat1.describe()
