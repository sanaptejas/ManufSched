<style type="text/css">
.create {background-color: #00FF00;}
.action {background-color: #FFFF00;}
</style>
<!---
<span class="action">Action</span>
<span class="create">Create</span>
-->

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
Step 1: <span class="create">Create</span> five algorithms (Johnsons rule, Palmer, CDS, etc...)

Step 2: <span class="create">Create</span> django/flask application

Step 3: <span class="create">Create</span> postgreSQL database

Step 4: <span class="create">Create</span> login page and user accounts

Step 5: <span class="action">Action</span> Login and see the stored data

Step 6: <span class="action">Action</span> Apply an algorithm to the data and see the result

Step 7: <span class="create">Create</span> Use some sort of graph to compare different algorithms
