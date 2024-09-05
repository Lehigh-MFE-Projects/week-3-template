import subprocess
import re
import pytest

@pytest.fixture
def graph():
    from student_graph import VersatileDigraph
    return VersatileDigraph()

def test_add_edge(graph):
    graph.add_edge("A", "B", edge_name="edge1", edge_value=5)
    assert graph.get_edge_wt("A", "B") == 5
