from math import factorial
import numpy as np
import itertools

def number_of_combinations(k, n):
    res = factorial(n) / (factorial(k) * factorial(n - k))
    return res

def recurrence(k, n):
    sum = 0
    i = k - 1
    while i <= n - 1:
        summand = number_of_combinations(k - 1, i)
        sum = sum + summand
        i += 1
    return sum

def all_combinations(k, num_of_elements):
    elements = np.arange(k)
    print(elements)
    checker = -1
    for i in range(-1, 1, -1):
        if elements[i] <= num_of_elements - k + i + 1:
            elements[i] = elements[i] + 1
            for j in range(i, k):
                elements[i] = elements[i - 1] + 1
        else:
            break
    
    

def main():
    k, n = map(int, input().split())
    array = array_filler(k, recurrence(k, n))
    for i in itertools.combinations(np.arange(3), 2):
        print(i, end=' ')
    print(array)
    print(recurrence(k, n))

if __name__ == "__main__":
    main()