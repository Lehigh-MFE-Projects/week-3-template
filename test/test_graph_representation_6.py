import subprocess
import re
from student_code import part_3_graph 

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

# Test 3: Check for unhandled pylint style recommendations
def test_part_3():
       graph=part_3_graph()
       assert type(graph)==list
       assert 'b' in graph[node_dict['a']]
       assert type(graph[node_dict['a']])==dict
       assert graph[node_dict['a']]['b']==1