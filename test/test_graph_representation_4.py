import subprocess
import re
import pytest

@pytest.fixture
def graph():
    from student_graph import VersatileDigraph
    return VersatileDigraph()

def test_add_node(graph):
'''Test adding node'''
    graph.add_node("A", 10)
    assert graph.get_node_value("A") == 10
