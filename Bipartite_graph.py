def flatten(l):
    return [item for sublist in l for item in sublist]

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = [i + 1 for i in range(nodes_number)]
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def mod_DFS(adjacency_list: dict, start_node: int, color_array: list, is_discovered: list) -> list:
    is_discovered[start_node - 1] = True
    for i in adjacency_list[start_node]:
        if is_discovered[i - 1]:
            color_array[start_node - 1] = color_array[i - 1] + 1
            color_array[start_node - 1] %= 2
        else:
            color_array[i - 1] = color_array[start_node - 1] + 1
            color_array[i - 1] %= 2
            adjacency_list[start_node].pop(adjacency_list[start_node].index(i))
            adjacency_list[i].pop(adjacency_list[i].index(start_node))
            mod_DFS(adjacency_list, i, color_array, is_discovered)  
    return color_array

def edges_checker(adj_list: dict, color_array: list) -> bool:
    i = 1
    while len(flatten(adj_list.values())) != 0:
        if len(adj_list[i]) != 0:
            for j in adj_list[i][:]:
                if color_array[i - 1] == color_array[j - 1]:
                    return False
                adj_list[j].pop(adj_list[j].index(i))
                adj_list[i].pop(adj_list[i].index(j))
        i += 1            
    return True

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    color_array = [0] * v
    adj_list = adjacency_list(v, edge_array)
    is_discovered = [False] * v
    for i, val in enumerate(is_discovered):
        if not val:
            mod_DFS(adj_list, i + 1, color_array, is_discovered)
    if not edges_checker(adj_list, color_array):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()