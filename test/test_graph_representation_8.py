import subprocess
import re
from student_code import part_5_graph 

# Test 3: Check for unhandled pylint style recommendations
def test_part_5():
       graph=part_5_graph()
       assert type(graph)==dict
       assert type(graph['a'])==dict
       assert graph['b']=={'e':3}