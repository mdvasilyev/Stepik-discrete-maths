def permutation(n, k=None):
    pool = tuple(n)
    n = len(pool)
    k = n if k is None else k
    if k > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - k, -1))
    yield tuple(pool[i] for i in indices[:k])
    while n:
        for i in reversed(range(k)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:k])
                break
        else:
            return

def main():
    n, k = map(int, input().split())
    for p in permutation(range(n), k):
        for i, _ in enumerate(p):
            print(p[i], end=' ')
        print()
    
if __name__ == "__main__":
    main()