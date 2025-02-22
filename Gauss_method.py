import numpy as np

def get_an_array(n, m):
    array = np.zeros((n, m + 1), dtype=float)
    for i in range(n):
        array[i] = [float(item) for item in input().split()]
    return array

def remove_last_column(array):
    return np.delete(array, -1, axis=1)

def first_elimination(array, n, m):
    if n > m:
        ref_number = m
    else:
        ref_number = n
    for i in range(ref_number - 1):        # i stands for major line for calculating coefficients
        if array[i, i] == 0:
            coeff_array = array[:, [i]]
            good_index = np.transpose(np.nonzero(coeff_array))[:, [0]][-1][0]
            array[[i, good_index]] = array[[good_index, i]]
        else:
            pass
        for k in range(ref_number - i):             # k stands for lines below
            if k == 0:
                coefficient = 0
            else:
                coefficient = array[k + i, i] / array[i, i]
            for j in range(i, m + 1):      # j stands for elements in each line
                array[k + i, j] = array[k + i, j] - coefficient * array[i, j]
    return array

def decision(full_rank, rank, number_of_variables):
    need_output = False
    if full_rank != rank:
        print('NO')
    elif full_rank == rank and rank < number_of_variables:
        print('INF')
    elif full_rank == rank and rank == number_of_variables:
        need_output = True
        print('YES')
    return need_output
        
def back_substitution(eliminated_full_array, m):
    variables = np.zeros(m)
    for i in range(m - 1, -1, -1):
        if i == m - 1:
            variables[i] = eliminated_full_array[i, m] / eliminated_full_array[i, i]
        else:
            sum = 0
            for j in range(m - 1, i, -1):
                sum = sum + variables[j] * eliminated_full_array[i, j]
            variables[i] = (eliminated_full_array[i, m] - sum) / eliminated_full_array[i, i]
    return variables

def main():
    n, m = map(int, input().split())    # n - number of equations, m - number of variables
    array = get_an_array(n, m)
    eliminated_full_array = first_elimination(array, n, m)
    eliminated_array = np.delete(eliminated_full_array, -1, axis=1)
    full_rank = np.linalg.matrix_rank(eliminated_full_array)
    rank = np.linalg.matrix_rank(eliminated_array)
    need_output = decision(full_rank, rank, m)
    if need_output == True:
        variables = back_substitution(eliminated_full_array, m)
        for i in range(m):
            print(variables[i], end=' ')

if __name__ == "__main__":
    main()