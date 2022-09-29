import numpy as np
import collections

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = np.arange(nodes_number)
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def BFS(adjacency_list: dict, is_discovered: list, queue: collections.deque) -> list:
    if not queue:
        return
    v = queue.popleft()
    for u in adjacency_list[v]:
        if not is_discovered[u]:
            is_discovered[u] = True
            queue.append(u)
    BFS(adjacency_list, is_discovered, queue)


def calculate_distances(start_node: int, goal_node: int):
    return

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int,input().split())) for r in range(e))
    is_discovered = [False] * v
    queue = collections.deque()
    print(adjacency_list(v, edge_array))
    # print(adjacency_list(v, edge_array))

if __name__ == "__main__":
    main()