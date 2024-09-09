import subprocess
import re
import pytest

@pytest.fixture
def graph():
    from student_code import VersatileDigraph
    return VersatileDigraph()

def test_add_edge(graph):
    graph.add_edge("A", "B", edge_name="edge1", edge_weight=5)
    assert graph.get_edge_weight("A", "B") == 5
