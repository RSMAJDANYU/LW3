#Формируется матрица F следующим образом: если в Е количество нулей в
# нечетных столбцах в области 4, умноженное на К больше, чем произведение чисел в нечетных строках в области 1,
# то поменять в С симметрично области 1 и 2 местами, иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: A*F+ K* F T.
# Выводятся по мере формирования А, F и все матричные операции последовательно.
import random


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{elem:5}' for elem in row))


def matrix_transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    return [[matrix[j][i] for j in range(n)] for i in range(m)]


def matrix_scalar_mul(matrix, scalar):
    return [[elem * scalar for elem in row] for row in matrix]


def matrix_mult(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            for j in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrix_add(A, B):
    n = len(A)
    m = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]


def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]
    print("\nМатрица A:")
    print_matrix(A)

    k = N // 2
    offset = 1 if N % 2 != 0 else 0

    F = [row[:] for row in A]
    E = [[F[i][j] for j in range(k)] for i in range(k)]
    B = [[F[i][j] for j in range(k + offset, N)] for i in range(k)]
    C = [[F[i][j] for j in range(k + offset, N)] for i in range(k + offset, N)]
    D = [[F[i][j] for j in range(k)] for i in range(k + offset, N)]

    count_zeros = 0
    for i in range(k):
        for j in range(k):
            if i > j and i + j < k - 1:
                if (j + 1) % 2 == 1:
                    if E[i][j] == 0:
                        count_zeros += 1

    product_ones = 1
    has_elements = False
    for i in range(k):
        for j in range(k):
            if i < j and i + j < k - 1:
                if (i + 1) % 2 == 1:
                    product_ones *= E[i][j]
                    has_elements = True

    if not has_elements:
        product_ones = 0

    print("\nПроверка условия для подматрицы E:")
    print(f"  - Количество нулей в нечетных столбцах (область 4): {count_zeros}")
    print(f"  - Произведение чисел в нечетных строках (область 1): {product_ones}")
    print(f"  - K * количество_нулей = {K} * {count_zeros} = {K * count_zeros}")
    condition_met = K * count_zeros > product_ones
    print(f"  - Условие (K * нули > произведение): {K * count_zeros} > {product_ones} -> {condition_met}")

    if condition_met:
        print("\nУсловие выполнилось: меняем области 1 и 2 в C симметрично")
        temp_C = [row[:] for row in C]
        for i in range(k):
            for j in range(k):
                if i < j and i + j < k - 1:
                    i1 = i
                    j1 = j
                    i2 = k - 1 - j
                    j2 = k - 1 - i
                    temp_C[i1][j1], temp_C[i2][j2] = temp_C[i2][j2], temp_C[i1][j1]

        for i in range(k):
            for j in range(k):
                F[k + offset + i][k + offset + j] = temp_C[i][j]
    else:
        print("\nУсловие не выполнилось: меняем B и E несимметрично")
        for i in range(k):
            for j in range(k):
                F[i][j], F[i][k + offset + j] = F[i][k + offset + j], F[i][j]

    print("\nМатрица F:")
    print_matrix(F)

    Ft = matrix_transpose(F)
    print("\nТранспонированная F (F^T):")
    print_matrix(Ft)

    AF = matrix_mult(A, F)
    print("\nРезультат A*F:")
    print_matrix(AF)

    KFt = matrix_scalar_mul(Ft, K)
    print("\nРезультат K*F^T:")
    print_matrix(KFt)

    R = matrix_add(AF, KFt)
    print("\nКонечный результат (A*F + K*F^T):")
    print_matrix(R)

if __name__ == "__main__":
    main()