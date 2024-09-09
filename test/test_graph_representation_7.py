import pytest

@pytest.fixture
def graph():
    from student_code import VersatileDigraph
    return VersatileDigraph()

def test_add_edge_with_new_nodes(graph):
    graph.add_edge("A", "B", edge_weight=5)
    assert set(graph.get_nodes()) == {"A", "B"}
