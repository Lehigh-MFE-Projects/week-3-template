import subprocess
import re
from student_code import part_2_graph 

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

# Test 5: Check part 2 graph
def test_part_2():
       graph=part_2_graph()
       assert type(graph)==list
       assert 'n' not in graph[node_dict['a']]
       assert 'm' not in graph[node_dict['a']]