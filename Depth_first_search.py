import numpy as np

def DFS(v_array, iterator: int, edge_array):
    # iterator = int(iterator)
    v_array[iterator] = True
    neighbours_array = np.array([])
    for j in range(len(edge_array)):
        if edge_array[j, 0] == iterator + 1:
            neighbours_array = np.append(neighbours_array, edge_array[j, 1])
        elif edge_array[j, 1] == iterator + 1:
            neighbours_array = np.append(neighbours_array, edge_array[j, 0])
        # else:
        #     continue
    for j in neighbours_array:
        j = int(j)
        if v_array[j - 1] == False:
            DFS(v_array, j - 1, edge_array)
        # elif v_array[j - 1] == True:
        #     continue
    # return None

def connectivity(nodes_number, edge_array) -> int:
    connectivity_number = 0
    v_array = np.full(nodes_number, False, dtype=bool)
    for i, val in enumerate(v_array):
        if val == False:
            DFS(v_array, i, edge_array)
            connectivity_number += 1
        # else:
        #     continue
    return connectivity_number

def main():
    v, e = map(int, input().split())
    edge_array = np.zeros((e, 2))
    for i in range(e):
        edge_array[i, 0], edge_array[i, 1] = map(int, input().split())
    connectivity_number = connectivity(v, edge_array)
    print(connectivity_number)

if __name__ == "__main__":
    main()