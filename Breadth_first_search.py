from collections import deque
from turtle import distance

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = [i for i in range(nodes_number)]
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def BFS(nodes_number: int, adjacency_list: dict, start_node: int, goal_node: int, distance: list) -> bool:
    queue = deque()
    is_discovered = [False for _ in range(nodes_number)]
    distance = [10e6 for _ in range(nodes_number)]
    is_discovered[start_node] = True
    distance[start_node] = 0
    queue.append(start_node)
    while not queue:
        v = queue.popleft()
        for u in adjacency_list[v]:
            if not is_discovered[u]:
                is_discovered[u] = True
                distance[u] += 1
                queue.append(u)
                if adjacency_list[u] == goal_node:
                    return True
    return False

def calculate_distance(nodes_number: int, adjacency_list: dict, start_node: int, goal_node: int, distance: list):
    if not BFS(nodes_number, adjacency_list, start_node, goal_node, distance):
        print("Given start node and goal node are not connected")
    else:
        for i in range(nodes_number):
            print(distance[i], end=' ')

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    distance = [0 for _ in range(v)]
    print(adjacency_list(v, edge_array))
    for i in range(2):
        calculate_distance(v, adjacency_list(v, edge_array), 0, i, distance)

if __name__ == "__main__":
    main()