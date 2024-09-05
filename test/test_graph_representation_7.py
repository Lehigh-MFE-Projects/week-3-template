import subprocess
import re
from student_code import part_4_graph 

# Test 3: Check for unhandled pylint style recommendations
def test_part_4():
       graph=part_4_graph()
       assert type(graph)==dict
       assert type(graph['a'])==set
       assert graph['a']=={'a','b','e'}