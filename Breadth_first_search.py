import numpy as np

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = np.arange(nodes_number)
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def BFS(start_node: int, goal_node: int) -> list:
    return

# def calculate_distances():
#     return

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int,input().split())) for r in range(e))
    print(adjacency_list(v, edge_array))
    # print(adjacency_list(v, edge_array))

if __name__ == "__main__":
    main()