%S="hello world".
%Word="world".
%Ok = string:str(S, Word) > 0.
main2() ->
	S="hello world",
	Word="nope",
	Ok = string:str(S, Word) > 0,
	io:format(Ok).

main(String) ->
	main2(),
	S="hello world",
	Word="world",
	Ok = string:str(S, Word) > 0,
	io:format(Ok).
	%io:format("hello world").
