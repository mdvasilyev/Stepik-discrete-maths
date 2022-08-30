import numpy as np

def get_an_array(n, m):
    array = np.zeros((n, m + 1), dtype=float)
    for i in range(n):
        array[i] = [float(item) for item in input().split()]
    return array

def target_array(initial_array, initial_f, n, m):
    coeff_array = np.zeros((m, m))
    f_array = np.zeros((m, 1))
    for i in range(m):
        for j in range(m):
            coeff_array[i, j] = np.dot(initial_array[:, i], initial_array[:, j])
    for i in range(m):
        f_array[i] = np.dot(initial_f.reshape(n), initial_array[:, i])
    final_array = np.hstack((coeff_array, f_array))
    return final_array

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
    n, m = map(int, input().split())
    full_array = get_an_array(n, m)
    coeff_array = np.delete(full_array, -1, axis=1)
    f_array = full_array[:, [-1]]
    final_array = target_array(coeff_array, f_array, n, m)
    eliminated_full_array = first_elimination(final_array, n, m)
    variables = back_substitution(eliminated_full_array, m)
    for i in range(m):
        print(variables[i], end=' ')

if __name__ == "__main__":
    main()