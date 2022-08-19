import numpy as np

def get_an_array(n, m):
    a = np.zeros((n, m + 1))
    for i in range(n):
        a[i] = [float(item) for item in input().split()]
    return a

def main():
    n, m = map(int, input().split())
    array = get_an_array(n, m)
    print(array)

if __name__ == "__main__":
    main()