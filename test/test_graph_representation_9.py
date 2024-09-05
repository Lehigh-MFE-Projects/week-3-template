import subprocess
import re
from student_code import part_1_graph 

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

# Test 9: Check part 1 graph
def test_part_1():
       graph=part_1_graph()
       assert type(graph)==list
       assert 't' not in graph[node_dict['a']]
       assert 'q' not in graph[node_dict['d']]