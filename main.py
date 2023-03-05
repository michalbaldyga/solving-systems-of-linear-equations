from solving_methods import *
from matplotlib import pyplot


# Zadanie A
N = 923
a1 = 10
a2 = a3 = -1
A = create_matrix(N, a1, a2, a3)
b = create_vector(N)

# Zadanie B
jacobi(A, b)
gauss_seidel(A, b)

# Zadanie C
a1 = 3
C = create_matrix(N, a1, a2, a3)
#jacobi(C, b)
#gauss_seidel(C, b)

# Zadanie D
lu_factorization(C, b)

# Zadanie E
a1 = 10
N = [100, 500, 1000, 2000, 3000]
jacobi_time = []
gauss_seidel_time = []
lu_factorization_time = []

for n in N:
    A = create_matrix(n, a1, a2, a3)
    b = create_vector(n)
    jacobi_time.append(jacobi(A, b))
    gauss_seidel_time.append(gauss_seidel(A, b))
    lu_factorization_time.append(lu_factorization(A, b))

pyplot.plot(N, jacobi_time, label="Jacobi", color="red")
pyplot.plot(N, gauss_seidel_time, label="Gauss-Seidel", color="green")
pyplot.plot(N, lu_factorization_time, label="LU_factorization", color="blue")
pyplot.legend()
pyplot.grid(True)
pyplot.ylabel('Czas [s]')
pyplot.xlabel('Liczba niewiadomych N')
pyplot.title('Zależność czasu od liczby niewiadomych')
pyplot.show()
