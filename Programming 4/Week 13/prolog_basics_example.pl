lectures(john, programming_1).
lectures(jane, programming_2).
lectures(james, programming_3).

is_digesting(X, Y) :- just_ate(X, Y).
is_digesting(X, Y) :- just_ate(X, Z), is_digesting(Z, Y).
just_ate(mosquito, john(blood)).
just_ate(frog, mosquito).
just_ate(stork, frog).

% Facts
word_and_letters(apple, a, p, p, l, e).
word_and_letters(amber, a, m, b, e, r).
word_and_letters(eagle, e, a, g, l, e).
word_and_letters(raise, r, a, i, s, e).

% Rules
crossword_solution(V1, V2, H1, H2) :-
    word_and_letters(V1, UL, _, _, _, LL),
    word_and_letters(H1, UL, _, _, _, UR),
    word_and_letters(V2, UR, _, _, _, LR),
    word_and_letters(H2, LL, _, _, _, LR),
    V1 \= H1.

% Facts
has(john, peanut).
owns(john, pet(dog, peanut)).

owns(john, pet(dog, X)).

% facts
soprano(anne).
soprano(barbara).
alto(caitlin).
tenor(dominic).
baritone(edgar).
alto(fred).

% Rules
upper_voice(S) :- soprano(S).
upper_voice(S) :- tenor(S).
lower_voice(S) :- alto(S).
lower_voice(S) :- baritone(S).
duet(S1, S2) :- upper_voice(S1), lower_voice(S2).

/* 
% ?- duet(S1, S2).

S1 = anne
S2 = caitlin ? ;

S1 = anne
S2 = edgar ? ;

S1 = barbara
S2 = caitlin ? ;

S1 = barbara
S2 = edgar ? ;

S1 = dominic
S2 = caitlin ? ;

S1 = dominic
S2 = edgar
*/