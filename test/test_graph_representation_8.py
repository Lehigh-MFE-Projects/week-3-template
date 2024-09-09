import pytest

@pytest.fixture
def graph():
    from student_code import VersatileDigraph
    return VersatileDigraph()

def test_edge_name_uniqueness(graph):
    graph.add_edge("A", "B", edge_name="edge1")
    with pytest.raises(ValueError):
        graph.add_edge("A", "C", edge_name="edge1")
