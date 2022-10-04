from collections import deque

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

def necessity_checker(adjacency_list: dict) -> bool:
    for i in adjacency_list:
        if len(adjacency_list[i]) == 0 or len(adjacency_list[i]) % 2 != 0:
            return False
    return True

def join_all_cycles(start_node: int, adj_list: dict) -> list:
    true_false_adj_list = {}
    for i in adj_list:
        true_false_adj_list[i] = [False] * len(adj_list[i])
    queue = deque()
    queue.append(start_node)
    path = [start_node]
    while False in flatten(list(true_false_adj_list.values())):
        cur_node = queue.popleft()
        for i, x in enumerate(adj_list[cur_node]):
            if true_false_adj_list[cur_node][i] == False:
                true_false_adj_list[cur_node][i] = True
                true_false_adj_list[x][adj_list[x].index(cur_node)] = True
                path.append(adj_list[cur_node][i])
                queue.append(adj_list[cur_node][i])
                break
    return path

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    adj_list = adjacency_list(v, edge_array)
    if not necessity_checker(adj_list):
        print("NONE")
    else:
        print(join_all_cycles(1, adj_list))

if __name__ == "__main__":
    main()