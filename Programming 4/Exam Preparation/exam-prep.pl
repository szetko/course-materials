% male(james1).
% male(charles1).
% male(charles2).
% male(james2).
% male(george1).

% female(catherine).
% female(elizabeth).
% female(sophia).

% parent(charles1, james1).
% parent(elizabeth, james1).
% parent(charles2, charles1).
% parent(catherine, charles1).
% parent(james2, charles1).
% parent(sophia, elizabeth).
% parent(george1, sophia).

% % Knowledge base
% likes(mary, food).
% likes(mary, wine).
% likes(john, wine).
% likes(john, mary).

% likes(mary, food). % yes
% likes(john, wine). % yes
% likes(john, food). % no

lecturer(john).
lecturer(X) :- has_degree(X), can_teach(X).
has_degree(jane).
is_smart(grayson).
is_smart(jane).
can_teach(jane).
has_degree(X) :- is_smart(X).

lecturer(grayson).
has_degree(jane).
lecturer(X).
has_degree(X).
