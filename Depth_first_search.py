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
    for j in adj_list[start_node][:]:
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