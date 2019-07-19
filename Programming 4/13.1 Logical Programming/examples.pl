has(john, peanut).
owns(john, pet(dog, peanut)).
owns(john, pet(dog, X)). 

lectures(john, programming_1).
lectures(jane, programming_2).
lectures(james, programming_3).

studies(cam, programming_1).
studies(pam, programming_2).
studies(sam, programming_3).

teaches(Lecturer, Student) :- 
    lectures(john, programming_1), studies(cam, programming_1).
teaches(Lecturer, Student) :- 
    lectures(jane, programming_2), studies(pam, programming_2).
teaches(Lecturer, Student) :- 
    lectures(james, programming_3), studies(sam, programming_3).

% | ?- lectures(james, programming_3). % yes
% | ?- lectures(james, programming_2). % no

soprano(anne).
soprano(barbara).
alto(caitlin).
tenor(dominic).
baritone(edgar).
alto(fred).

upper_voice(S) :- soprano(S).
upper_voice(S) :- tenor(S).
lower_voice(S) :- alto(S).
lower_voice(S) :- baritone(S).
duet(S1, S2) :- upper_voice(S1), lower_voice(S2).

% ?- duet(S1, S2).

% S1 = anne
% S2 = caitlin ? ;

% S1 = anne
% S2 = edgar ? ;

% S1 = barbara
% S2 = caitlin ? ;

% S1 = barbara
% S2 = edgar ? ;

% S1 = dominic
% S2 = caitlin ? ;

% S1 = dominic
% S2 = edgar

has_enough_credits('John').
hires_regalia('John').
knows_csharp('Jane').
knows_java('Jane').

will_graduate(Student) :- has_enough_credits(Student), hires_regalia(Student). 
can_code(Person) :- knows_csharp(Person) ; knows_java(Person).

% Can also be written as:
can_code(Person) :- knows_csharp(Person).
can_code(Person) :- knows_java(Person).

member(5, [2, 4, 6]). % no
member(4, [2, 4, 6]). % yes

length([2, 4, 6], L). % L = 3

permutation([X, Y, Z], [2, 4, 6]).

% X = 2
% Y = 4
% Z = 6 ? ;

% X = 2
% Y = 6
% Z = 4 ? ;

% X = 4
% Y = 2
% Z = 6 ? ;

% X = 6
% Y = 2
% Z = 4 ? ;

% X = 4
% Y = 6
% Z = 2 ? ;

% X = 6
% Y = 4
% Z = 2 ? ;

is_digesting(X, Y) :- just_ate(X, Y).
is_digesting(X, Y) :- just_ate(X, Z), is_digesting(Z, Y).
just_ate(mosquito, john(blood)).
just_ate(frog, mosquito).
just_ate(stork, frog).

% | ?- is_digesting(X, Y).

% X = mosquito
% Y = john(blood) ? ;

% X = frog
% Y = mosquito ? ;

% X = stork
% Y = frog ? ;

% X = frog
% Y = john(blood) ? ;

% X = stork
% Y = mosquito ? ;

% X = stork
% Y = john(blood) ? ;

word_and_letters(apple, a, p, p, l, e).
word_and_letters(amber, a, m, b, e, r).
word_and_letters(eagle, e, a, g, l, e).
word_and_letters(raise, r, a, i, s, e).

crossword_solution(V1, V2, H1, H2) :-
    word_and_letters(V1, UL, _, _, _, LL),
    word_and_letters(H1, UL, _, _, _, UR),
    word_and_letters(V2, UR, _, _, _, LR),
    word_and_letters(H2, LL, _, _, _, LR),
    V1 \= H1.

% | ?- crossword_solution(V1, V2, H1, H2).

% H1 = amber
% H2 = eagle
% V1 = apple
% V2 = raise ? ;

% H1 = apple
% H2 = raise
% V1 = amber
% V2 = eagle ? 

