import pytest

@pytest.fixture
def graph():
    from student_graph import VersatileDigraph
    return VersatileDigraph()

def test_print_graph(graph, capsys):
    graph.add_node("A", 10)
    graph.add_edge("A", "B", edge_weight=5, edge_name="edge1")
    graph.print_graph()
    captured = capsys.readouterr()
    assert "Node A with value 10" in captured.out
    assert "Edge from A to B with weight 5 and name edge1" in captured.out
