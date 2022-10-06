from collections import deque

def flatten(l):
    return [item for sublist in l for item in sublist]

def remove_overlap(l: list) -> list:
    if l[0] == l[-1]:
        l.pop(-1)
    return l

def adjacency_list(nodes_number: int, edge_array: list) -> dict:
    nodes_array = [i + 1 for i in range(nodes_number)]
    adjacency_array = {}
    for node in nodes_array:
        adjacency_array[node] = []  
    for u, v in edge_array:
        adjacency_array[u].append(v)
        adjacency_array[v].append(u)
    return adjacency_array

def check_necessity(adjacency_list: dict) -> bool:
    for i in adjacency_list:
        if len(adjacency_list[i]) == 0 or len(adjacency_list[i]) % 2 != 0:
            return False
    return True

def pave_a_path(start_node: int, adj_list: dict, path: list) -> list:
    queue = deque()
    queue.append(start_node)
    cur_node = start_node
    while bool(queue):
        pred = cur_node
        cur_node = queue.popleft()
        for i, x in enumerate(adj_list[cur_node]):
            path.append(adj_list[cur_node][i])
            queue.append(adj_list[cur_node][i])
            adj_list[cur_node].pop(i)
            adj_list[x].pop(adj_list[x].index(cur_node))
            break
    if len(flatten(list(adj_list.values()))) != 0:
        adj_list[cur_node].append(pred)
        adj_list[pred].append(cur_node)
    return path, adj_list

def check_path(path: list, nodes_number: int, adj_list: dict):
    nodes_array = [i + 1 for i in range(nodes_number)]
    for i in nodes_array:
        for j in adj_list[i]:
            if i in path and j not in path:
                start_node = j
                return start_node
    return False

def add_a_cycle(cur_node: int, path: list, adj_list: dict) -> list:
    index = path.index(cur_node)
    queue = deque()
    queue.append(cur_node)
    while bool(queue):
        index += 1
        cur_node = queue.popleft()
        for i, x in enumerate(adj_list[cur_node]):
            path.insert(index, adj_list[cur_node][i])
            queue.append(adj_list[cur_node][i])
            adj_list[cur_node].pop(i)
            adj_list[x].pop(adj_list[x].index(cur_node))
            break
    return path

def main():
    v, e = map(int, input().split())
    edge_array = list(tuple(map(int, input().split())) for _ in range(e))
    adj_list = adjacency_list(v, edge_array)
    if not check_necessity(adj_list):
        print("NONE")
    else:
        start_node = 1
        path = [start_node]
        euler_cycle, adj_list = pave_a_path(1, adj_list, path)
        euler_cycle = remove_overlap(euler_cycle)
        while len(euler_cycle) != e:
            euler_cycle = remove_overlap(euler_cycle)
            if type(check_path(euler_cycle, v, adj_list)) == bool:
                break
            else:
                start_node = check_path(euler_cycle, v, adj_list)
                pave_a_path(start_node, adj_list, euler_cycle)
        for i in euler_cycle:
            print(i, end=' ')

if __name__ == "__main__":
    main()