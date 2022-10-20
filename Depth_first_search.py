def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = [i + 1 for i in range(nodes_number)]
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def DFS(is_discovered: list, start_node: int, adj_list: dict):
    is_discovered[start_node - 1] = True
    for j in adj_list[start_node]:
        if not is_discovered[j - 1]:
            adj_list[start_node].pop(adj_list[start_node].index(j))
            adj_list[j].pop(adj_list[j].index(start_node))
            DFS(is_discovered, j, adj_list)

def connectivity(nodes_number: int, adj_list: dict) -> int:
    connectivity_number = 0
    is_discovered = [False] * nodes_number
    for i, val in enumerate(is_discovered):
        if not val:
            DFS(is_discovered, i + 1, adj_list)
            connectivity_number += 1
    return connectivity_number

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    adj_list = adjacency_list(v, edge_array)
    connectivity_number = connectivity(v, adj_list)
    print(connectivity_number)

if __name__ == "__main__":
    main()


# def DFS(v_array, iterator: int, edge_array):
#     v_array[iterator] = True
#     neighbours_array = []
#     for j in range(len(edge_array)):
#         if edge_array[j, 0] == iterator + 1:
#             neighbours_array.append(edge_array[j, 1])
#         elif edge_array[j, 1] == iterator + 1:
#             neighbours_array.append(edge_array[j, 0])
#     for j in neighbours_array:
#         j = int(j)
#         if not v_array[j - 1]:
#             DFS(v_array, j - 1, edge_array)


# def main():
#     v, e = map(int, input().split())
#     edge_array = np.zeros((e, 2))
#     for i in range(e):
#         edge_array[i, 0], edge_array[i, 1] = map(int, input().split())
#     connectivity_number = connectivity(v, edge_array)
#     print(connectivity_number)
