#Leilani Luna 
#CS 4390
from collections import deque

def get_path_lengths(cfg, entry):
    #Compute shortest path for entry node to every node
    nodes = set(cfg)
    for succs in cfg.values():
        nodes.update(succs)
    if entry not in nodes:
        return {}

    dist = {entry: 0}
    q = deque([entry])

    #breadth-first search
    while q:
        u = q.popleft()
        for v in cfg.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def reverse_postorder(cfg, entry):
    #RPO for CFG
    nodes = set(cfg)
    for succs in cfg.values():
        nodes.update(succs)
    if entry not in nodes:
        return []

    visited = set()
    post = []

    #depth-first
    def dfs(u):
        if u in visited:
            return
        visited.add(u)
        for v in cfg.get(u, []):
            dfs(v)
        post.append(u)

    dfs(entry)
    return list(reversed(post))


def find_back_edges(cfg, entry):
    #Find back edges
    nodes = set(cfg)
    for succs in cfg.values():
        nodes.update(succs)
    if entry not in nodes:
        return []

    back_edges = []
    visited = set()
    onstack = set()

    #depth-first
    def dfs(u):
        visited.add(u)
        onstack.add(u)
        for v in cfg.get(u, []):
            if v not in visited:
                dfs(v)
            elif v in onstack:
                back_edges.append((u, v))
        onstack.remove(u)

    dfs(entry)
    return back_edges


def is_reducible(cfg, entry):
    #Determine if reducible
    nodes = set(cfg)
    for succs in cfg.values():
        nodes.update(succs)
    if entry not in nodes:
        return True 

    #get preds
    preds = {n: set() for n in nodes}
    for u, succs in cfg.items():
        for v in succs:
            preds[v].add(u)

    #get dominator
    dom = {n: set(nodes) for n in nodes}
    dom[entry] = {entry}
    changed = True
    while changed:
        changed = False
        for n in nodes:
            if n == entry:
                continue
            if preds[n]:
                new = set(nodes)
                for p in preds[n]:
                    new &= dom[p]
            else:
                new = set(nodes)
            new.add(n)
            if new != dom[n]:
                dom[n] = new
                changed = True

    for u, v in find_back_edges(cfg, entry):
        if v not in dom[u]:
            return False
    return True
