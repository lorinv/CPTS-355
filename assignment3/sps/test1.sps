/fact {
	dictz
	begin
	/n exch def
		n 2 lt
		{1}
		{n -1 add fact n mul }
	ifelse
	end
}def
5 fact =
