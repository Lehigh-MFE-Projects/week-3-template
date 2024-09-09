import pytest
import time

@pytest.fixture
def graph():
    from student_code import VersatileDigraph
    return VersatileDigraph()

def test_performance_add_edge(graph):
    graph.add_node("A")
    start_time = time.time()
    for i in range(1000):
        graph.add_edge("A", f"Node{i}", edge_weight=i)
    end_time = time.time()
    assert (end_time - start_time) < 0.1 # Ensure the operation is efficient
