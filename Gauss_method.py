import numpy as np

def get_an_array(n, m):
    array = np.zeros((n, m + 1))
    for i in range(n):
        array[i] = [float(item) for item in input().split()]
    return array

def remove_last_column(array):
    array = np.delete(array, -1, axis=1)
    return array

def first_elimination(array, n, m):
    new_array = array
    for i in range(n):
        if i == 0:
            coefficient = 0
        else:
            coefficient = array[i, i - 1] / array[i - 1, i - 1]
        for j in range(m + 1):
            new_array[i, j] = array[i, j] - coefficient * array[i - 1, j]
    return new_array

def main():
    n, m = map(int, input().split())
    array = get_an_array(n, m)
    new_array = first_elimination(array, n, m)
    print(array)
    print(new_array)

if __name__ == "__main__":
    main()