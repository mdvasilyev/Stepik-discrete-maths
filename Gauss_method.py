import numpy as np

def get_an_array(n, m):
    number_of_elements = n * (m + 1)
    a = np.array([])
    for i in range(number_of_elements):
        x = int(input())
        a.append(x)
    return a

def main():
    n, m = map(int, input().split())
    print(get_an_array(n, m))

if __name__ == "__main__":
    main()