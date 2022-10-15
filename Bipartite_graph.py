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
    pred = start_node
    for i in adjacency_list[start_node]:
        if not is_discovered[i - 1]:
            color_array[i - 1] = color_array[pred - 1] + 1
            color_array[i - 1] %= 2
            adjacency_list[pred].pop(adjacency_list[pred].index(i))
            adjacency_list[i].pop(adjacency_list[i].index(pred))
            mod_DFS(adjacency_list, i, color_array, is_discovered)  
    return color_array

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    color_array = [0] * v
    adj_list = adjacency_list(v, edge_array)
    is_discovered = [False] * v
    start_node = 1
    mod_DFS(adj_list, start_node, color_array, is_discovered)
    while False in is_discovered:
        next_node = -1
        for i in adj_list:
            if is_discovered[i - 1] == True and len(adj_list[i]) != 0:
                next_node = i
                break
        else:
            for i in adj_list:
                if len(adj_list[i]) != 0:
                    next_node = i
                    break
        mod_DFS(adj_list, next_node, color_array, is_discovered)
    print(color_array)

if __name__ == "__main__":
    main()