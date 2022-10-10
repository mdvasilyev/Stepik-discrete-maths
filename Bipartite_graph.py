from collections import deque

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = [i + 1 for i in range(nodes_number)]
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

# def DFS(v_array: list, iterator: int, edge_array: list) -> None:
#     v_array[iterator] = True
#     neighbours_array = np.array([])
#     for j in range(len(edge_array)):
#         if edge_array[j, 0] == iterator + 1:
#             neighbours_array = np.append(neighbours_array, edge_array[j, 1])
#         elif edge_array[j, 1] == iterator + 1:
#             neighbours_array = np.append(neighbours_array, edge_array[j, 0])
#     for j in neighbours_array:
#         j = int(j)
#         if not v_array[j - 1]:
#             DFS(v_array, j - 1, edge_array)

def DFS(adjacency_list: dict, nodes_number: int, start_node: int, color_array: list) -> list:
    queue = deque()
    queue.append(start_node)
    is_discovered = [False] * nodes_number
    is_discovered[start_node - 1] = True
    counter = 1
    while len(queue) != 0:
        cur_node = queue.popleft()
        for i in adjacency_list[cur_node]:
            if not is_discovered[i - 1]:
                is_discovered[i - 1] = True
                color_array[i - 1] = counter % 2
                queue.append(i)
                break
        counter += 1
    return color_array

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    color_array = [0] * v
    adj_list = adjacency_list(v, edge_array)
    print(DFS(adj_list, v, 1, color_array))

if __name__ == "__main__":
    main()