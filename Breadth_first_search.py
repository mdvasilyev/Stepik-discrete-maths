from collections import deque

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = [i for i in range(nodes_number)]
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def BFS(adjacency_list: dict, nodes_number: int, start_node: int) -> list:
    distances = [0 for _ in range(nodes_number)]
    is_discovered = [False for _ in range(nodes_number)]
    queue = deque()
    queue.append(start_node)
    is_discovered[start_node] = True
    while len(queue) != 0:
        current_node = queue.popleft()
        for i in adjacency_list[current_node]:
            if not is_discovered[i]:
                is_discovered[i] = True
                distances[i] = distances[current_node] + 1
                queue.append(i)
    return distances

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    for _, x in enumerate(BFS(adjacency_list(v, edge_array), v, 0)):
        print(x, end=' ')

if __name__ == "__main__":
    main()