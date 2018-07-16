#### File flow
1. `johnsons_rule.py`
	1. `console_input.py`
		1. `makespan_general.py`

#### classes
1. Error Class
	1. Sequence errors
		1. no. of elements in sequence don't match with the no. of jobs
		1. job is present in sequence but not in PT matrix 

#### functions
1. `apply_sequence` = a function that rearranges a matrix according to a sequence

#### things to do
1. use `raise`,`try`,`except` in raising errors
2. add ability to take weight as input for heurestic methods
3. use enumerate (`list.enum()`) with lists

#### game plan
Step 1: :red_circle: five algorithms (Johnsons rule, Palmer, CDS, etc...)

Step 2: :large_orange_diamond: django/flask application

Step 3: :red_circle: postgreSQL database

Step 4: :large_orange_diamond: login page and user accounts

Step 5: :large_orange_diamond: Login and see the stored data

Step 6: :black_circle: Apply an algorithm to the data and see the result

Step 7: :large_orange_diamond: Use some sort of graph to compare different algorithms
