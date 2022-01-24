# Multiplicar 2 matrices

import numpy as np

def check_square(matrix):
    rows = len(matrix)
    for row in matrix:
        if len(row) != rows:
            print('Error: La matriz no es cuadrada')
            exit(1)

    return True

# returns a list with the different types in a list
def list_type(list):
    return set(map(type, list))

def check_type(matrix):
    types = [] # list for the different types

    for row in matrix:
        row_type = list_type(row)
        # if a new type is found, add it
        if (not types.__contains__(row_type)):
            types.append(row_type)
    
    # if there are more than 1 type:
    if (len(types) > 1):
        print('Error: La matriz tiene más de un tipo')
        exit(1)

def check(matrix):
    check_square(matrix)
    check_type(matrix)

def mul_matrix(m1, m2):
    check(m1)
    check(m2)

    m1 = np.array(m1)
    m2 = np.array(m2)

    return np.dot(m1, m2)

def main():
    a = [[1, 2], [1, 1]]
    b = [[1, 2], [3, 1]]
    result = mul_matrix(a, b)
    print(result)

if __name__ == '__main__':
    main()