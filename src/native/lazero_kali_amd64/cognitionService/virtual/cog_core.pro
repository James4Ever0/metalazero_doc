%:- write("prolog\n").
%:- write("prolog is good"), halt.
% anything  substring anything
substr(String) --> ([_|_];[]), String,  ([_|_];[]).

% is X a substring of Y ?
substring(X,Y) :- phrase(substr(X),Y).
:- (string_to_list("happyBirth",X),substring("happy",X) -> write("success"); write("fail")), nl.
:- (string_to_list("happy",X),substring("happyBirth",X) -> write("success"); write("fail")), nl.
:- halt.
