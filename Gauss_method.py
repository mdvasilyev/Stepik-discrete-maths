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
    for i in range(n - 1):              # i stands for major line for calculating coefficients
        for k in range(n - i):          # k stands for lines below
            if k == 0:
                coefficient = 0
            else:
                coefficient = array[k + i, i] / array[i, i]
            for j in range(m + 1):      # j stands for elements in each line
                array[k + i, j] = array[k + i, j] - coefficient * array[i, j]
    return array

def main():
    n, m = map(int, input().split())
    array = get_an_array(n, m)
    new_array = first_elimination(array, n, m)
    print(new_array)

if __name__ == "__main__":
    main()