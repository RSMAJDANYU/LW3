import random

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f"{num:4}" for num in row))
    print()

def create_submatrix(n, value_func):
    sub_n = n // 2
    if n % 2 != 0:
        sub_n = (n + 1) // 2
    return [[value_func(i, j) for j in range(sub_n)] for i in range(sub_n)]

def count_zeros_in_odd_columns_in_region_4(E):
    count = 0
    rows = len(E)
    if rows == 0:
        return 0
    cols = len(E[0])
    for i in range(rows):
        for j in range(cols):
            if j % 2 == 0:
                if i >= j:
                    if E[i][j] == 0:
                        count += 1
    return count

def product_in_odd_rows_in_region_1(B):
    product = 1
    rows = len(B)
    if rows == 0:
        return 0
    cols = len(B[0])
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                if i <= j:
                    product *= B[i][j]
    return product

def swap_symmetrically_regions_1_and_2(C):
    n = len(C)
    if n == 0:
        return C
    for i in range(n // 2):
        for j in range(i, n - i):
            if j < n // 2:
                mirror_i = n - 1 - i
                mirror_j = n - 1 - j
                C[i][j], C[mirror_i][mirror_j] = C[mirror_i][mirror_j], C[i][j]
    return C

def swap_B_and_E(B, E):
    return E, B

def create_matrix_A(B, C, D, E, N):
    A = [[0 for _ in range(N)] for _ in range(N)]
    half = N // 2
    if N % 2 != 0:
        half = (N + 1) // 2
    
    for i in range(half):
        for j in range(half):
            A[i][j] = B[i][j]
    for i in range(half):
        for j in range(half, N):
            if j - half < len(D[0]):
                A[i][j] = D[i][j - half]
    for i in range(half, N):
        for j in range(half):
            if i - half < len(C[0]):
                A[i][j] = C[i - half][j]
    for i in range(half, N):
        for j in range(half, N):
            if i - half < len(E) and j - half < len(E[0]):
                A[i][j] = E[i - half][j - half]
    return A

def create_matrix_F(A, K, N):
    half = N // 2
    if N % 2 != 0:
        half = (N + 1) // 2
    
    B = [[A[i][j] for j in range(half)] for i in range(half)]
    D = [[A[i][j] for j in range(half, N)] for i in range(half)]
    C = [[A[i][j] for j in range(half)] for i in range(half, N)]
    E = [[A[i][j] for j in range(half, N)] for i in range(half, N)]
    
    zeros_in_E = count_zeros_in_odd_columns_in_region_4(E)
    product_in_B = product_in_odd_rows_in_region_1(B)
    
    if zeros_in_E * K > product_in_B:
        C = swap_symmetrically_regions_1_and_2(C)
    else:
        B, E = swap_B_and_E(B, E)
    
    F = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(half):
        for j in range(half):
            F[i][j] = B[i][j]
    for i in range(half):
        for j in range(half, N):
            if j - half < len(D[0]):
                F[i][j] = D[i][j - half]
    for i in range(half, N):
        for j in range(half):
            if i - half < len(C):
                F[i][j] = C[i - half][j]
    for i in range(half, N):
        for j in range(half, N):
            if i - half < len(E) and j - half < len(E[0]):
                F[i][j] = E[i - half][j - half]
    return F

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def multiply_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def add_matrices(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def scalar_multiply_matrix(K, matrix):
    return [[K * num for num in row] for row in matrix]

def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))
    
    B = create_submatrix(N, lambda i, j: i + j + 1)
    C = create_submatrix(N, lambda i, j: i - j - 1)
    D = create_submatrix(N, lambda i, j: i * j + 2)
    E = create_submatrix(N, lambda i, j: (i + 1) * (j + 1) - 3)
    
    A = create_matrix_A(B, C, D, E, N)
    print("Матрица A:")
    print_matrix(A)
    
    F = create_matrix_F(A, K, N)
    print("Матрица F:")
    print_matrix(F)
    
    AF = multiply_matrices(A, F)
    print("Результат A * F:")
    print_matrix(AF)
    
    F_T = transpose_matrix(F)
    KF_T = scalar_multiply_matrix(K, F_T)
    print("Результат K * F^T:")
    print_matrix(KF_T)
    
    result = add_matrices(AF, KF_T)
    print("Результат A*F + K*F^T:")
    print_matrix(result)

if __name__ == "__main__":
    main()