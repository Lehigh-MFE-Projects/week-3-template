import subprocess
import re
from student_code import part_1_graph 

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

# Test 4: Check part 1 graph
def test_part_1():
       graph=part_1_graph()
       assert type(graph)==list
       assert 'b' in graph[node_dict['a']]
       assert 'c' not in graph[node_dict['d']]