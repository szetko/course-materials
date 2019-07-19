# IN628 2019 Practical 12.1 - Functional Programming 1

from functools import reduce
'''
1.	Assume that a passing grade on an exam is 50. Write a single Python statement that accepts a 
list of exam scores and returns all the values that did not pass. Your code should be something like this:
'''

exam_scores = [65, 72, 41, 99, 32, 84]
did_not_pass  # = Write your code here
print(list(did_not_pass))  # [41, 32]

'''
2.	Use a single reduce expression to accept a list of strings and return the items of the list concatenated 
into a single string in the reverse order. Your code should be something like this:
'''

items = ['ab', 'cd', 'ef', 'gh']
reversed  # = reduce(Write your code here)
print(reversed)  # ghefcdab

'''
3.	Assume this string variable has been created:

star_wars = "A long time ago in a galaxy far far away"

Write a single python statement that returns all the words in the sentence which are four or more characters in 
length, in upper case. You can accomplish this all in a single exporession (no loops!). Your code should look like:

Hint: There is a built-in Python method which, when applied to a sentence, returns a sequence comprised of the words 
in the sentence (i.e. it splits on the space character and returns a sequence).
'''

star_wars = 'A long time ago in a galaxy far far away'
long_words  # = Write your code here
print(list(long_words))  # ['LONG', 'TIME', 'GALAXY', 'AWAY']

'''
4.	You are writing an application to compute scores for a Quiz Night. You want a flexible scoring algorithm to allow 
fair competition between teams composed of adults and teams composed of children. For Adult teams, the score is defined 
as 10 points for each correct answer minus 1 point for each incorrect answer. Child teams get 15 points per correct answer 
and lose 1/2 point for each incorrect answer. Build your scoring application using idiomatic Python. Your main logic should 
be a single function that will compute either the child team score or the adult team score, based on an input flag. Here 
is a fragment from my solution:
'''

quiz_scorer  # = Write your code here
adult_score = quiz_scorer(8, 2, False)
child_score = quiz_scorer(8, 2, True)
print(adult_score)  # 78
print(child_score)  # 119.0
