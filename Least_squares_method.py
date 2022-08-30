from array import array
import numpy as np

def get_an_array(n, m):
    array = np.zeros((n, m + 1), dtype=float)
    for i in range(n):
        array[i] = [float(item) for item in input().split()]
    return array


def main():
    n, m = map(int, input().split())
    full_array = get_an_array(n, m)
    coeff_array = np.delete(full_array, -1, axis=1)
    f_array = full_array[:, [-1]]

if __name__ == "__main__":
    main()