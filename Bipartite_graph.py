def main():
    v, e = map(int, input().split())
    edge_array = np.zeros((e, 2))
    for i in range(e):
        edge_array[i, 0], edge_array[i, 1] = map(int, input().split())
    print(edge_array)

if __name__ == "__main__":
    main()