#Leilani Luna
#CS 4390 
import pytest
from cfg_utils import (
    get_path_lengths, reverse_postorder,
    find_back_edges, is_reducible
)
#Test Cases
def test_shortest_paths_only_reachable():
    cfg = {"A": ["B"], "B": [], "X": ["Y"], "Y": []}
    d = get_path_lengths(cfg, "A")
    assert d == {"A": 0, "B": 1}

def test_rpo_includes_all_reachable_once():
    cfg = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["E"],
        "E": []
    }
    rpo = reverse_postorder(cfg, "A")
    assert set(rpo) == {"A", "B", "C", "D", "E"}
    assert len(rpo) == 5
    assert rpo[0] == "A" 

def test_back_edges_and_reducible_true():
    cfg = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
    }
    backs = find_back_edges(cfg, "A")
    assert ("C", "A") in backs
    assert is_reducible(cfg, "A") is True

def test_irreducible_multiple_entry_cycle():
    cfg = {
        "A": ["B", "C"],
        "B": ["D", "C"],
        "C": ["D", "B"],
        "D": []
    }
    assert is_reducible(cfg, "A") is False