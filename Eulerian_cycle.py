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
    queue = deque()
    queue.append(start_node)
    path = [start_node]
    discarded_nodes = []
    while len(flatten(list(adj_list.values()))) != 0:
        cur_node = queue.popleft()
        if len(adj_list[cur_node]) == 0:
            discarded_nodes.append(path.pop(-1))
            cur_node = path[-1]
        for i, x in enumerate(adj_list[cur_node]):
            path.append(adj_list[cur_node][i])
            queue.append(adj_list[cur_node][i])
            adj_list[cur_node].pop(i)
            adj_list[x].pop(adj_list[x].index(cur_node))
            break
    discarded_nodes = list(reversed(discarded_nodes))
    for i in range(len(discarded_nodes)):
        path.append(discarded_nodes[i])
    return path

def check_coincidence(l: list) -> list:
    if l[0] == l[-1]:
        l.pop(-1)
    return l

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    adj_list = adjacency_list(v, edge_array)
    if not necessity_checker(adj_list):
        print("NONE")
    else:
        euler_cycle = join_all_cycles(1, adj_list)
        print(check_coincidence(euler_cycle))

if __name__ == "__main__":
    main()