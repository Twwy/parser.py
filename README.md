parser.py
-----------

It may be the smallest parser in python.

# INPUT
	python test.py xxx -a 1 -b 2 2 4 -t 
# DATA IN PARSER
	data: {"default":["xxx"], "a":["1"], "b":["2","2","4"], "t":[]}

# USAGE

 	import parser
	parser.load()
	a = parser.read("a")       # 1
	b = parser.read("b")       # 2
	b1 = parser.readList("b")  # ["2","2","4"]
	c = parser.read()          # xxx
	d = parser.read("b","a")   # 2
	e = parser.read("e")       # None
	t = parser.read("t")       # ""



