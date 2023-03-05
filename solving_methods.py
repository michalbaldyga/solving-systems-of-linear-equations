import time
from matrix import *
from vector import *


def residuum_vector(A, x, b):
    N = len(A)
    res = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[i] += A[i][j] * x[j]
    return subtract_vectors(res, b)


def jacobi(A, b):
    starting_time = time.time()
    N = len(A)
    residuum_value = pow(10, -9)
    x = [0 for _ in range(N)]
    x_tmp = [0 for _ in range(N)]
    k = 0

    while True:
        for i in range(N):
            result = b[i]
            for j in range(N):
                if i != j:
                    result -= A[i][j] * x[j]
            result /= A[i][i]
            x_tmp[i] = result
        x = copy_vector(x_tmp)
        res = residuum_vector(A, x, b)

        if norm(res) < residuum_value:
            break
        k += 1

    computation_time = time.time() - starting_time
    print("Jacobi's method")
    print('Time:', computation_time)
    print('Iterations:', k)
    print()
    return computation_time


def gauss_seidel(A, b):
    starting_time = time.time()
    N = len(A)
    x = [0 for _ in range(N)]
    residuum_value = pow(10, -9)
    k = 0

    while True:
        for i in range(N):
            result = b[i]
            for j in range(N):
                if i != j:
                    result -= A[i][j] * x[j]
            result /= A[i][i]
            x[i] = result
        res = residuum_vector(A, x, b)
        if norm(res) < residuum_value:
            break
        k += 1

    computation_time = time.time() - starting_time
    print("Gauss-Seidel's method")
    print("Time:", computation_time)
    print("Iterations:", k)
    print()
    return computation_time


def lu_factorization(A, b):
    starting_time = time.time()
    N = len(A)
    x = [1 for _ in range(N)]
    y = [0 for _ in range(N)]
    U = copy_matrix(A)             # Upper Triangular Matrix
    L = create_diagonal_matrix(x)  # Lower Triangular Matrix

    # creating matrices L and U; A = L * U
    for i in range(N):
        for j in range(i+1, N):
            L[j][i] = U[j][i] / U[i][i]
            for k in range(i, N):
                U[j][k] = U[j][k] - L[j][i]*U[i][k]

    # solving L * y = b
    for i in range(N):
        result = b[i]
        for j in range(i):
            result -= L[i][j] * y[j]
        y[i] = result / L[i][i]

    # solving U * x = y
    for i in range(N-1, -1, -1):
        result = y[i]
        for j in range(i+1, N):
            result -= U[i][j] * x[j]
        x[i] = result / U[i][i]

    res = residuum_vector(A, x, b)

    computation_time = time.time() - starting_time
    print("LU method")
    print("Time:", computation_time)
    print("Norm(res):", norm(res))
    print()
    return computation_time
