# Working with CFGs Assignment
## Functions
- `get_path_lengths(cfg, entry)`: Starts at entry and does BFS. It gives the shortest steps/edges to each reachable node. If a node is unreachable, it is not in the result.
- `reverse_postorder(cfg, entry)`: Does DFS from entry and gives the list the list in reverse postorder.
- `find_back_edges(cfg, entry)`: Finds edges that go back to an ancestor in the DFS stack. Helps spot cycles or back edges.
- `is_reducible(cfg, entry)`: Checks dominators. If every back edge's target overtakes its source, then the CFG is reducible. Otherwise, it's irreducible.
