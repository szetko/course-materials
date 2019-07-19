# Single-line comment
=begin
    Multi-line comment
=end

# Get input
puts 'Enter your first number:'
first_num = gets.to_i
puts 'Enter your second number:'
second_num = gets.to_i
sum = first_num + second_num
puts "#{first_num} + #{second_num} = #{sum}"

# Arithmetic operators
puts "6 + 4 = #{(6 + 4)}"
puts "6 - 4 = #{(6 - 4)}"
puts "6 * 4 = #{(6 * 4)}"
puts "6 / 4 = #{(6 / 4)}"
puts "6 % 4 = #{(6 % 4)}"

# Basic I/O
TEXT_FILE_NAME = 'example.txt'
write_handler = File.new(TEXT_FILE_NAME, 'w')
write_handler.puts('Hello world').to_s
write_handler.close
read_handler = File.read(TEXT_FILE_NAME)
puts read_handler

# Conditional
# - comparison: == != < > <= >=
# - logical: && || ! and or not

puts 'Enter your age:'
age = gets.to_i
if (age < 18)
    puts 'You aren\'t legal'
else
    puts 'You are legal'
end

# Unless
unless age >= 18
    puts 'You aren\'t legal'
else 
    puts 'You are legal'
end

# Case
puts 'Enter greeting:'
greeting = gets.chomp
case greeting
when 'French', 'french'
    puts 'Bonjour'
when 'Spanish', 'spanish'
    puts 'Hola'
else
    puts 'Hello'
end

# Ternary
puts (age < 18) ? 'You aren\'t legal' : 'You are legal'

# Loop do
x = 1
loop do
    x += 1
    next unless (x % 2) == 0
    puts x
    break if x >= 10
end

# While loop
x = 1
while x <= 10
    x += 1
    next unless (x % 2) == 0
    puts x
end

# Until loop
x = 1
until x >= 10
    x += 1
    next unless (x % 2) == 0
    puts x
end

# For loop
nums = [1, 2, 3, 4, 5]
for n in nums
    puts n
end

# Each loop
animals = ['chicken', 'cow', 'goat', 'sheep']
animals.each do |a|
    puts a
end

# Functions
def add_nums(num_one, num_two)
    return num_one.to_i + num_two.to_i
end

puts add_nums(3, 4)

# Classes
class Animal
    def initialize
        puts 'Initialising'
    end

    def set_name(new_name) 
        @name = new_name
    end

    def get_name
        @name
    end
end

dog = Animal.new
dog.set_name('Sophie')
puts dog.get_name

class Dog
    def initialize
        puts 'Initialising'
    end

    attr_accessor :name

    def bark
        return 'Woof!'
    end
end

dog = Dog.new
dog.name = 'Sophie'
puts dog.name
puts dog.bark()

# Modules
module Sound
    def growl
        return "Grrrrrr!"
    end
end

# Inheritance
class Poodle < Dog
    include Sound

    def initialize
        puts 'Initialising'
    end

    def bark
        return 'Woooof!'
    end
end

poodle = Poodle.new
poodle.name = 'Charlie'
puts poodle.name
puts poodle.bark()
puts poodle.growl()

# Polymorphism
class Shape    
    def size=(size)
        @size = size
    end

    def size
        @size
    end

    def calculate_area(shape_type)
        shape_type.calculate_area
    end
end

class Circle < Shape
    def calculate_area
        return Math::PI * (size / 2) * (size / 2)
    end
end

class Square < Shape
    def calculate_area
        return size * size
    end
end

class Triangle < Shape
    def calculate_area
        return 0.5 * (size * 2) * size
    end
end

circle = Circle.new
square = Square.new
triangle = Triangle.new
circle.size = 5
square.size = 5
triangle.size = 5
puts circle.calculate_area()
puts square.calculate_area()
puts triangle.calculate_area()


