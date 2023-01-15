import numpy as np

#Sistema de ecuaciones diagonalmente dominante CASO 1
A_caso1 = np.array([[2,1,1,1], [1,3,2,1], [1,1,4,1], [1,1,1,5]])
b_caso1 = np.array([2,3,4,5])

#Sistema de ecuaciones diagonalmente dominante CASO 2
A_caso2 = np.array([[12,-1,2,1], [-1,13,-1,3], [2,-1,11,-1], [1,3,-1,10]])
b_caso2 = np.array([1,2,3,4])

#Sistema de ecuaciones diagonalmente dominante CASO 3
A_caso3 = np.array([[1,1,1,1], [1,2,3,1], [1,3,6,1], [1,1,1,4]])
b_caso3 = np.array([1,2,3,4])

#Sistema de ecuaciones no diagonalmente dominante CASO 4
A_caso4 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
b_caso4 = np.array([1,2,3,4])

def matrix_validate(A, b):
    iter = 0
    n, m = A.shape
    aux = np.zeros(4)
    aux_X, iter = gauss_seidel(A, b, aux, 0.00001)
    if n != m:
        status = "Sistema no cuadrado"
        return False, status, iter
    diagonal_dominant = True
    for i in range(n):
        suma_no_diag = np.sum(np.abs(A[i, :i])) + np.sum(np.abs(A[i, i+1:]))
        if np.abs(A[i, i]) <= suma_no_diag and np.array_equal(aux, aux_X):
            diagonal_dominant = False
            status = "Sistema no diagonalmente dominante"
            break
    if not diagonal_dominant:
        return False, status, iter
    if np.linalg.det(A) == 0:
        status = "Sistema con determinante 0"
        return False, status, iter
    status = "Sistema válido"
    return True, status, iter

def gauss_seidel(A, b, x0, tol):
    n = len(b)
    x = x0.copy()
    iter = 0
    while True:
        x_prev = x.copy()
        for j in range(n):
            s1 = np.dot(A[j, :j], x[:j])
            s2 = np.dot(A[j, j+1:], x[j+1:])
            x[j] = (b[j] - s1 - s2)/A[j,j]
        iter += 1
        if np.linalg.norm(x - x_prev) < tol:
            return x, iter