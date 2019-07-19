# IN628 2019 Practical 12.2 - Functional Programming 2

'''
1.	In the lecture PowerPoint we saw this function, which accepts a string input and
returns a string consisting of only the consonants from the input:
'''


def remove_vowels(input):
    vowels = ['a', 'i', 'e', 'o', 'u']
    consonants = ''
    for i in range(len(input)):
        if (input[i] not in vowels):
            consonants += input[i]
    return consonants


'''
The function as written is not "good" Python. It has a very imperative style, and fails to use
those Python features that would allow it to be written more succinctly.

Rewrite the function so that it uses a list comprehension instead of a for loop to produce the
correct output string. Hint: you may need to use some additional Python operations including "not in" and "join".
'''

# Write your code here

'''
2.	We used remove_vowels to process a list of strings, like this:
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
no_vowels = [remove_vowels(d) for d in week_days]

which produces['Mndy', 'Tsdy', 'Wdnsdy', 'Thrsdy', 'Frdy'].

In idiomatic Python, we can achieve the same result without writing the remove_vowels function. That is,
you can perform the entire list processing with only three statements, with this structure:
'''

vowels = ['a', 'i', 'e', 'o', 'u']
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
no_vowels  # = Write your code here
print(no_vowels)  # ['Mndy', 'Tsdy', 'Wdnsdy', 'Thrsdy', 'Frdy']

'''
3.	We have seen the syntax for adding a conditional filter to a list comprehension to select only a
subset of elements from the original list. However, one might also want to add conditional logic to
the "expression" part of the list comprehension. For example, one might want to process a list of numbers
such that positive numbers in the list are doubled, but negative numbers are replaced with 0.

That is, for example: [11, -17, 42, 8, -12, 9] => [22, 0, 84, 16, 0, 18]

To achieve this, the "expression" part of the list comprehension needs to be conditional: "if x is greater
than 0 apply this expression to x, otherwise apply this other expression to x". Write a Python list comprehension
to produce the functionality described above(use neither loops nor named functions). You will need to consult a
Python manual or other reliable reference to find the correct syntax for this extension of the list comprehension.
'''

# Write your code here

'''
4.	You are to define and exercise an iterable class FlashCards. This class accepts a list of string on construction.
When "next" is called on an instance of FlashCards, it returns a randomly selected element from its list(repetition allowed).

Here is an example of my solution being used:
'''

# Write your code here

german_words = FlashCards(
    ['die Kuh', 'der Hund', 'die Katze', 'das Pferd', 'die Ente'])

for i in range(5):
    print(next(german_words))
    # der Hund
    # die Katze
    # die Kuh
    # die Kuh
    # das Pferd

'''
5.	Write and test a generator function that accepts a list of string and when iterated over, returns the list
in reverse. Note that, for extra Python succinctness, it is possible to implement this without creating any kind
of local index variable in the generator function.

Here is an example of my solution being used:
'''

# Write your code here

reverse_animals = list_reverser(
    ['antelope', 'burro', 'cheetah', 'donkey', 'elephant'])

for a in reverse_animals:
    print(a)
    # elephant
    # donkey
    # cheetah
    # burro
    # antelope

'''
6.	Using the generator you wrote in problem 5, write a list comprehension to return only the elements of the list that have 
7 or more characters. Do not first create a variable from the generator(i.e. like reverse_animals, above), just call your 
list_reverser generator function inside the list comprehension to generate the sequence. 

Using the same set of words as in problem 5, my list comprehension returns: ['elephant', 'cheetah', 'antelope']
'''

# Write your code here

'''
7.	Using the generator function you wrote in problem 5, do the following:
    a.	Create a variable from your generator(like reverse_animals, above).
    b.	Use a for-in loop to print it out(again as in problem 5).
    c.	Run the list comprehension you wrote in problem 6, using the variable from step 7a as the sequence.
    d.	What happens?
    e.	Why?

What do you need to do so that you can use a variable in the list comprehension but get the correct result?
'''

# Write your code here
