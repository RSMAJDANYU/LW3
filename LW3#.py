import random

def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(' '.join(f"{num:4}" for num in row))
    print()

def create_matrix(rows, cols, random_fill=True):
    if random_fill:
        return [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]
    return [[0 for _ in range(cols)] for _ in range(rows)]

def get_submatrix(matrix, start_row, start_col, rows, cols):
    return [[matrix[start_row+i][start_col+j] for j in range(cols)] for i in range(rows)]

def place_submatrix(matrix, submatrix, start_row, start_col):
    for i in range(len(submatrix)):
        for j in range(len(submatrix[0])):
            matrix[start_row+i][start_col+j] = submatrix[i][j]

def count_zeros_in_odd_columns_region4(submatrix):
    count = 0
    rows = len(submatrix)
    cols = len(submatrix[0]) if rows > 0 else 0
    for j in range(1, cols, 2):
        for i in range(rows//2, rows):
            if submatrix[i][j] == 0:
                count += 1
    return count

def product_in_odd_rows_region1(submatrix):
    product = 1
    rows = len(submatrix)
    cols = len(submatrix[0]) if rows > 0 else 0
    for i in range(0, rows, 2):
        for j in range(0, cols//2):
            product *= submatrix[i][j]
    return product

def swap_regions_1_and_2(submatrix):
    rows = len(submatrix)
    cols = len(submatrix[0])
    half_cols = cols // 2
    for i in range(0, rows, 2):
        for j in range(half_cols):
            submatrix[i][j], submatrix[i][cols-1-j] = submatrix[i][cols-1-j], submatrix[i][j]

def swap_matrices_B_and_E(B, E):
    new_B = [row.copy() for row in E]
    new_E = [row.copy() for row in B]
    return new_B, new_E

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    return [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]

def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N (размер матрицы A): "))

    half = (N + 1) // 2
    A = create_matrix(N, N, random_fill=True)
    B = create_matrix(half, N-half, random_fill=True)
    C = create_matrix(N-half, N-half, random_fill=True)
    D = create_matrix(N-half, half, random_fill=True)
    E = create_matrix(half, half, random_fill=True)

    place_submatrix(A, E, 0, 0)
    place_submatrix(A, B, 0, half)
    place_submatrix(A, D, half, 0)
    place_submatrix(A, C, half, half)

    print_matrix(A, "Исходная матрица A")

    F = [row.copy() for row in A]
    E_F = get_submatrix(F, 0, 0, half, half)
    B_F = get_submatrix(F, 0, half, half, N-half)
    C_F = get_submatrix(F, half, half, N-half, N-half)

    zeros = count_zeros_in_odd_columns_region4(E_F)
    product = product_in_odd_rows_region1(E_F)

    print(f"Нулей в нечетных столбцах области 4 (E): {zeros}")
    print(f"Произведение в нечетных строках области 1 (E): {product}")

    if zeros * K > product:
        print("Меняем области 1 и 2 в C симметрично")
        swap_regions_1_and_2(C_F)
        place_submatrix(F, C_F, half, half)
    else:
        print("Меняем B и E местами несимметрично")
        new_B, new_E = swap_matrices_B_and_E(B_F, E_F)
        place_submatrix(F, new_E, 0, 0)
        place_submatrix(F, new_B, 0, half)

    print_matrix(F, "Матрица F после изменений")

    AF = matrix_multiply(A, F)
    print_matrix(AF, "A * F")

    FT = transpose(F)
    KFT = scalar_multiply(FT, K)
    print_matrix(KFT, "K * F^T")

    result = matrix_add(AF, KFT)
    print_matrix(result, "Результат: A*F + K*F^T")

if __name__ == "__main__":
    main()