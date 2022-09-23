from math import factorial
import numpy as np

def number_of_combinations(k, n):
    return factorial(n) / (factorial(k) * factorial(n - k))

def recurrence(k, n):
    sum = 0
    i = k - 1
    while i <= n - 1:
        sum += number_of_combinations(k - 1, i)
        i += 1
    return sum

def all_combinations(k, n):
    elements = np.arange(k, dtype=int)
    while True:
        for i in range(k):
            print(elements[i], end=' ')
        print()
        m = -1
        for i in range(k - 1, -1, -1):
            if elements[i] <= n - k + i - 1:
                m = i
                elements[i] += 1
                break
        if m == -1:
            break
        for j in range(m + 1, k):
            elements[j] = elements[j - 1] + 1
    
    

def main():
    k, n = map(int, input().split())
    all_combinations(k, n)

if __name__ == "__main__":
    main()